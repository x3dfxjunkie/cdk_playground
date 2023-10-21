"""This file contains the ChatBot Stack"""
import yaml
from aws_cdk import aws_chatbot, aws_iam, aws_logs, aws_sns, Stack
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.sns_topic import Guest360SNSTopic
from app.infrastructure.workstream_stack import WorkstreamStack


class ChatBot(WorkstreamStack):
    """ChatBot Stack
    Contains resources to Maintain Chatbot. Chatbot is a "global" resource, so only deploy this in one region.

    The configuration file has the following schema:

        channel_defaults: &chan                # Account-level defaults that apply to each channel configuration
            slack_workspace_id: "[A-Z0-9]{9}"  # This part must be created manually in each account :(
            guardrail_policies:                # Guardrail policies further limit the scope of the channel IAM role
              - "ReadOnlyAccess"
        channels:                              # List of channel configurations
          dpp-guest360-latest-deployments:     # This is the name of the channel, also serves as construct ID
            <<: *chan                          # Import the account defaults
            slack_channel_id: "[A-Z0-9]{11}"   # Channel ID, found from channel properties in Slack
            notification_topics:               # List of SNS topics to subscribe to. These are written as an SNS
                                                "from_topic_arn" cdk call to convert to ITopic.
                                                - "arn:aws:sns:us-east-1:543276908693:lst-use1-guest360-cdk-pipeline-approval"
    """

    def __init__(self, scope: Construct360 | Stack, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._environment = self.deployment_environment
        self.stack_path = self.project_dir
        self._stack = Stack.of(self)

        self.environment_alarm_sns = self.alarm_sns()

        self.setup_channels()

    def setup_channels(self) -> None:
        """Loop through config file and associate slack channels to SNS topics"""
        with open(
            f"{self.stack_path}/app/infrastructure/reliability/configs/{self._environment}-chatbot.yaml",
            "r",
            encoding="UTF-8",
        ) as file:
            chatbot_config = yaml.safe_load(file)

        for channel in chatbot_config["channels"].keys():
            # Iterate over notification topics, if any are configured. Each must be converted to an ITopic.
            notification_topics = []
            if "notification_topics" in chatbot_config["channels"][channel]:
                for topic in chatbot_config["channels"][channel]["notification_topics"]:
                    if topic.startswith("self"):
                        topic = eval(topic, {}, {"self": self})
                    notification_topics.append(aws_sns.Topic.from_topic_arn(self, topic.split(":")[-1], topic))
            else:
                notification_topics = None

            # Iterate over guardrail policies and create IManagedPolicy from each.
            guardrail_policies = []
            for policy in chatbot_config["channels"][channel]["guardrail_policies"]:
                guardrail_policies.append(aws_iam.ManagedPolicy.from_aws_managed_policy_name(policy))

            # Create the actual channel configuration.
            slack_channel = aws_chatbot.SlackChannelConfiguration(
                self,
                channel,
                slack_channel_configuration_name=channel,
                slack_workspace_id=chatbot_config["channels"][channel]["slack_workspace_id"],
                slack_channel_id=chatbot_config["channels"][channel]["slack_channel_id"],
                guardrail_policies=guardrail_policies,
                log_retention=aws_logs.RetentionDays.THREE_MONTHS,
                logging_level=aws_chatbot.LoggingLevel.INFO,
                notification_topics=notification_topics,
            )

            # Add CloudWatchReadOnlyAccess to the channel role.
            slack_channel.role.add_managed_policy(
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchReadOnlyAccess")
            )

            # Export channel info to SSM.
            self.ssm_export(f"chatbot_{channel}", slack_channel.slack_channel_configuration_arn, channel)

            # This is for the log retention lambda.
            NagSuppressions.add_stack_suppressions(
                self,
                [
                    {
                        "id": "AwsSolutions-IAM4",
                        "reason": "Managed policies are ok.",
                    },
                    {"id": "AwsSolutions-IAM5", "reason": "Lambda needs wildcards for log retention."},
                ],
            )

    def alarm_sns(self) -> aws_sns.ITopic:
        """Create an SNS Topic for Alarms to ChatBot."""
        sns_topic = Guest360SNSTopic(
            self,
            "alarm-topic",
            {
                "topic_name": "alarm-notifications",
            },
        )
        sns_topic.topic.grant_publish(aws_iam.AccountRootPrincipal())
        sns_topic.topic.grant_publish(
            aws_iam.ServicePrincipal(
                "cloudwatch.amazonaws.com",
                conditions={
                    "ArnLike": {
                        "aws:SourceArn": f"arn:aws:cloudwatch:{self._stack.region}:{self._stack.account}:alarm:*"
                    },
                    "StringEquals": {"aws:SourceAccount": f"{self._stack.account}"},
                },
                region=self._stack.region,
            )
        )
        NagSuppressions().add_resource_suppressions(
            sns_topic,
            [
                {
                    "id": "AwsSolutions-SNS2",
                    "reason": "These are only for CW Alarms, no need for SSE.",
                }
            ],
            True,
        )
        return sns_topic.topic
