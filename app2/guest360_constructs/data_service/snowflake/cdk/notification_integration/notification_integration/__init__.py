""" Snowflake Notification Integration construct """
import logging
import re
from base64 import b64decode
import botocore.session
from typing import TypedDict
from aws_cdk import aws_iam, aws_sns, CfnOutput, Stack, aws_secretsmanager
from cdk_nag import NagSuppressions
from app.guest360_constructs.sns_topic import Guest360SNSTopic, Guest360SNSTopicProps
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.construct_360 import Construct360
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

logger = logging.getLogger(__name__)


@match_class_typing
class NotificationIntegrationProps(TypedDict):
    """aws notification integration props"""

    notification_name: str
    iam_user_arn: NotRequired[str]
    iam_external_id: NotRequired[str]


class NotificationIntegration(Construct360):
    """Snowflake Aws Notification Integration"""

    @property
    def sns_topic(self) -> aws_sns.Topic:
        return self.sni_sns_topic.topic

    @property
    def sns_topic_name(self) -> str:
        return self.sni_sns_topic.topic_name

    @property
    def sns_topic_role(self) -> aws_iam.Role:
        return self.sni_role.role

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        props: NotificationIntegrationProps,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)
        prefix = self.node.try_get_context("prefix")
        # is_static_env = self.node.try_get_context("is_static_env")

        # Check that props matches proper input structure
        NotificationIntegrationProps(props)

        self.notification_name = props["notification_name"]
        self._iam_user_arn = props.get("iam_user_arn")
        self._arn_secret_iam_external_id = props.get("arn_secret_iam_external_id")

        # if not us-east-1 do nothing
        # this is because notifications can only be sent to a single region from snowflake
        if stack.region != "us-east-1":
            return

        # Create Role
        assumed_by = aws_iam.CompositePrincipal(aws_iam.ServicePrincipal("sns.amazonaws.com"))
        role_props = {
            "role_name": "ingestion_raw_notifications-notification_integratio",
            "description": "Snowflake SNS access role for Snow Pipe Notifications",
        }
        if self._iam_user_arn:
            self._iam_external_id = self.get_aws_secret(secret_name=self._arn_secret_iam_external_id)
            if self._iam_external_id:
                assumed_by.add_principals(aws_iam.ArnPrincipal(self._iam_user_arn))
                role_props["external_ids"] = [self._iam_external_id]

        role_props["assumed_by"] = assumed_by

        self.sni_role = Guest360IamRole(
            self,
            construct_id=f"{self.notification_name}-notification_integration",
            props=role_props,
        )

        # Create the SNS Topic
        self.sni_sns_topic = Guest360SNSTopic(
            self,
            construct_id=f"{self.notification_name}-notification_integration-topic",
            props=Guest360SNSTopicProps(
                topic_name="ingestion_raw_notifications",
            ),
        )
        self.sni_sns_arn = str(self.sns_topic.topic_arn)
        self.sns_topic.grant_publish(self.sns_topic_role)

        # Output the SNS Topic ARN
        CfnOutput(
            self,
            f"{prefix}-{self.notification_name}-notification_integration-topic",
            description="SNS Topic ARN for the Snowflake Notification Integration",
            value=self.sni_sns_arn,
        )
        CfnOutput(
            self,
            f"{prefix}-{self.notification_name}-role",
            description="Snowflake Role to publish to SNS Topic for Notification Integration",
            value=self.sns_topic_role.role_arn,
        )

        # Nag Suppressions
        NagSuppressions.add_resource_suppressions(
            self.sns_topic, [{"id": "AwsSolutions-SNS2", "reason": "No sensitive data"}], True
        )

    def get_aws_secret(self, secret_name: str) -> str:
        """Returns the decoded secret value of a given secret name."""

        external_id = aws_secretsmanager.Secret.from_secret_complete_arn(self, "secret_external_id", secret_name)
        return external_id.secret_value_from_json("iam_external_id").unsafe_unwrap()
