"""Snowflake External Stage Aws Resource Construct 
Creates roles, policies, sqs queue and policies for ExternalStage
"""
# pylint: disable=logging-fstring-interpolation lazy processing not needed in cdk

import logging
from typing import TypedDict

from aws_cdk import CfnOutput, Stack, aws_iam, aws_s3, aws_s3_notifications, aws_sqs
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.s3_bucket import Guest360S3Bucket

logger = logging.getLogger(__name__)


@match_class_typing
class ExternalStageProps(TypedDict):
    """ExternalStage properties"""

    external_stage_name: str
    s3_bucket: aws_s3.Bucket  # s3 bucket obj
    s3_bucket_name: str  # str bucket name
    s3_bucket_prefix: str  # s3 bucket prefix path
    iam_principal: NotRequired[str]  # principal
    snowflake_sqs_arn: NotRequired[str]  # sqs arn from snowflake snowpipe stage


class ExternalStage(Construct360):
    """AWS ExternalStage construct"""

    def __init__(self, scope: Construct360, construct_id: str, props: ExternalStageProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stack = Stack.of(self)
        prefix = self.node.try_get_context("prefix")
        self.prefix_cc = "".join([_.title() for _ in prefix.split("-")])
        is_static_env = self.node.try_get_context("is_static_env")

        # runtime typechecking
        ExternalStageProps(props)
        logger.debug(f"{props=}")

        external_stage_name = props["external_stage_name"]
        self._external_stage_name = "".join([_.title() for _ in external_stage_name.replace("_", "-").split("-")])
        props["s3_bucket_prefix"] = self.normalize_s3_prefix(props["s3_bucket_prefix"])

        self.bucket = props["s3_bucket"]
        self.bucket_name = Guest360S3Bucket.get_s3bucketname(prefix, props["s3_bucket_name"])
        self.bucket_prefix = props["s3_bucket_prefix"]

        #####
        # iam user get disney service now created user
        #####
        self._iam_principal = (
            aws_iam.User.from_user_attributes(
                self,
                f"{stack.region}-{self.pass_id}-{external_stage_name}",
                user_arn=f'arn:aws:iam::{stack.account}:user/{props["iam_principal"]}',
            )
            if props.get("iam_principal")
            else None
        )
        logger.debug(f"{self._iam_principal=}")

        #####
        # s3
        #####
        # create bucket name, path, kms key_id cloudformation outputs
        CfnOutput(
            self,
            f"{self.pass_id}-{self._external_stage_name}-s3_bucket_arn",
            description="ExternalStage S3 Bucket Name",
            value=self.bucket.bucket_arn,
        )
        CfnOutput(
            self,
            f"{self.pass_id}-{self._external_stage_name}-s3_prefix",
            description="ExternalStage S3 Bucket Prefix",
            value=self.bucket_prefix,
        )
        CfnOutput(
            self,
            f"{self.pass_id}-{self._external_stage_name}-s3_kms",
            description="ExternalStage S3 Bucket KMS Key",
            value=self.bucket.encryption_key.key_id,
        )

        # get encryption key and create alias`
        self._s3_encryption_key = self.bucket.encryption_key
        self._s3_encryption_key_alias = self._s3_encryption_key.add_alias(f"{self.bucket_name}-s3")
        if self._iam_principal:
            bucket_policies = [
                aws_iam.PolicyStatement(
                    **{
                        "actions": [
                            "s3:GetObject",
                            "s3:GetObjectVersion",
                        ],
                        "effect": aws_iam.Effect.ALLOW,
                        "principals": [self._iam_principal],
                        "resources": [
                            f"{self.bucket.bucket_arn}/{self.bucket_prefix}",
                        ],
                        "sid": f"{self._external_stage_name}ExternalStageS3RO",
                    },
                ),
                aws_iam.PolicyStatement(
                    **{
                        "actions": [
                            "s3:DeleteObject",
                            "s3:DeleteObjectVersion",
                            "s3:PutObject",
                        ],
                        "effect": aws_iam.Effect.ALLOW,
                        "principals": [self._iam_principal],
                        "resources": [f"{self.bucket.bucket_arn}/{self.bucket_prefix}"],
                        "sid": f"{self._external_stage_name}ExternalStageS3RW",
                    }
                ),
                aws_iam.PolicyStatement(
                    **{
                        "actions": [
                            "s3:ListBucket",
                            "s3:GetBucketLocation",
                        ],
                        "effect": aws_iam.Effect.ALLOW,
                        "principals": [self._iam_principal],
                        "resources": [f"{self.bucket.bucket_arn}"],
                        "sid": f"{self._external_stage_name}ExternalStageS3BucketInfo",
                    }
                ),
            ]
            #            bucket_policies = []
            for policy in bucket_policies:
                self.bucket.add_to_resource_policy(policy)

            kms_policies = [
                aws_iam.PolicyStatement(
                    **{
                        "actions": ["kms:Decrypt"],
                        "effect": aws_iam.Effect.ALLOW,
                        "principals": [self._iam_principal],
                        "resources": ["*"],
                        "sid": f"{self._external_stage_name}ExternalStageS3RO",
                    },
                ),
            ]
            for policy in kms_policies:
                self._s3_encryption_key.add_to_resource_policy(policy)

        # cdk event notification adds custom lambda for sqs events
        if props.get("snowflake_sqs_arn") and stack.region.lower() == "us-east-1" and is_static_env:
            snowflake_sqs = aws_sqs.Queue.from_queue_arn(
                self, f"{self.pass_id}-{self._external_stage_name}-snowflake_sqs", props["snowflake_sqs_arn"]
            )
            logger.debug("snowflake sqs url=%s", snowflake_sqs.queue_url)
            self.bucket.add_event_notification(
                aws_s3.EventType.OBJECT_CREATED,
                aws_s3_notifications.SqsDestination(snowflake_sqs),
            )

    @staticmethod
    def normalize_s3_prefix(string: str) -> str:
        """ensure prefix does not contain begin/end slashes"""
        string = string.removeprefix("/").removesuffix("/")
        string = "" if string == "" else f"{string}/*"
        return string
