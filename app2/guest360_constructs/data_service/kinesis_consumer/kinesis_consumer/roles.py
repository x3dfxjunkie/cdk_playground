"""
File for the Data Service's kinesis consumer role base construct
"""
import aws_cdk
from aws_cdk import Stack, aws_iam
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs import iam_role


class KinesisConsumerRoles(Construct360):
    """
    Base Kinsesis Consumer Role Construct for Data Service
    """

    @property
    def roles(self):
        return self._roles

    def __init__(self, scope: Stack, construct_id: str, stream_name: str, role_configs: list, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ENVIRONMENT_NAME = self.node.try_get_context("environment")
        stack = Stack.of(self)
        prefix_global = self.node.try_get_context("prefix_global")

        # next step is to wrap this all up into a single construct for streams
        self._roles = []
        role_configs = role_configs if isinstance(role_configs, list) else []
        for role_config in role_configs:
            role_id = f'{stream_name}_{role_config["id"]}'

            composite_principal = aws_iam.CompositePrincipal(*[aws_iam.ArnPrincipal(i) for i in role_config["role_arns"]])
            iam_props = {"role_name": role_id, "description": "experience-events x-account IAM role for kinesis kcl consumer access", "assumed_by": composite_principal}
            role = iam_role.Guest360IamRole(
                self,
                construct_id=role_id,
                props=iam_props,
            ).role
            # Because allowing consumers to create their own consumer group's need to add additional read/write permissions to stream/<stream>/consumer/
            consumer_policy = aws_iam.Policy(
                self,
                f'{prefix_global}-{stream_name}_{role_config["id"]}-policy',
                statements=[
                    aws_iam.PolicyStatement(
                        **{
                            "actions": [
                                "kinesis:DeregisterStreamConsumer",
                                "kinesis:DescribeStreamConsumer",
                                "kinesis:RegisterStreamConsumer",
                                "kinesis:SubscribeToShard",
                            ],
                            "resources": [
                                f'arn:{stack.partition}:kinesis:*:{aws_cdk.Aws.ACCOUNT_ID}:stream/*-{stream_name}/consumer/{role_config["id"]}*',
                            ],
                        }
                    )
                ],
            )
            role.attach_inline_policy(consumer_policy)
            NagSuppressions.add_resource_suppressions(
                consumer_policy,
                [
                    {
                        "id": "AwsSolutions-IAM5",
                        "reason": "Allow Kinesis Consumers to create their own consumer groups based on a specific prefix",
                    }
                ],
                True,
            )
            self._roles.append(role)
