"""
Logic for Guest360's base construct for S3 Buckets
"""
from typing import List, TypedDict, Union, cast

import aws_cdk
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.kms_key import Guest360KMSKey
from app.src.reliability.utils import S3BucketName
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired


@match_class_typing
class S3Props(TypedDict):
    """

    Properties class for strongtyping
    """

    bucket_name: str
    auto_delete_objects: NotRequired[
        bool
    ]  # Automatically delete objects before destroying the bucket. Defaults to True in latest.
    block_public_access: NotRequired[
        aws_cdk.aws_s3.BlockPublicAccess
    ]  # Specifies the policy regarding public access. Defaults to BLOCK_ALL.
    bucket_key_enabled: NotRequired[bool]  # Normal KMS or Bucket Key. Cost and security trade-offs. Defaults to True.
    encryption_key: NotRequired[
        Union[aws_cdk.aws_kms.Key, aws_cdk.aws_kms.IKey]
    ]  # KMS encryption key to use for SSE. If this is blank, a new one is created.
    lifecycle_rules: NotRequired[
        List[Union[dict, aws_cdk.aws_s3.LifecycleRule]]
    ]  # List of rules for object lifecycles.
    removal_policy: NotRequired[
        aws_cdk.RemovalPolicy
    ]  # Policy about retaining or destroying this bucket on stack destroy. Defaults to DESTROY in latest.
    versioned: NotRequired[bool]  # Enable/disable object versioning. Defaults to True.


class SsmImportProps(TypedDict):
    bucket_arn: str
    kms_arn: str


class Guest360S3Bucket(Construct360):
    """Guest360 Construct for S3 buckets.

    This includes some hard-coded values, as well as some overrideable defaults.
    Required props:
        {
            "bucket_name": string
        }

    Optional props:
        {
            "auto_delete_objects": bool  # Automatically delete objects before destroying the bucket. Defaults to True in latest.
            "block_public_access": aws_cdk.aws_s3.BlockPublicAccess # Specifies the policy regarding public access. Defaults to BLOCK_ALL.
            "bucket_key_enabled": bool  # Normal KMS or Bucket Key. Cost and security trade-offs. Defaults to True.
            "encryption_key": aws_cdk.aws_cdk.IKey  # KMS encryption key to use for SSE. If this is blank, a new one is created.
            "lifecycle_rules": list(dict) or list(aws_cdk.aws_s3.LifecycleRule)  # List of rules for object lifecycles.
            "removal_policy": aws_cdk.RemovalPolicy  # Policy about retaining or destroying this bucket on stack destroy. Defaults to DESTROY in latest.
            "versioned": bool  # Enable/disable object versioning. Defaults to True.
        }

    Usage:
        Guest360S3Bucket(self, f"{stack_name}-pipeline-bucket", current_region,
                        {
                            "bucket_name": f"{stack_name}-my-special-bucket",
                        })
    """

    @property
    def kms_key(self):
        return self._kms_key

    @property
    def bucket(self) -> aws_cdk.aws_s3.Bucket:
        return self._bucket

    @property
    def bucket_name(self) -> str:
        return self._bucket_name

    def __init__(self, scope: Construct360, construct_id: str, region: str, props: S3Props, **kwargs) -> None:
        super().__init__(scope, construct_id)

        self.ssm_export = None
        if kwargs.get("ssm_props", False):
            ssm_props: SsmImportProps = cast(SsmImportProps, kwargs.get("ssm_props"))
            aws_kms_key = aws_cdk.aws_kms.Key.from_key_arn(self, "kms_key", ssm_props["kms_arn"])
            bucket = aws_cdk.aws_s3.Bucket.from_bucket_attributes(
                self, "bucket", bucket_arn=ssm_props["bucket_arn"], encryption_key=aws_kms_key
            )
            self._bucket = bucket
            return

        # Check that props matches proper input structure
        S3Props(props)

        environment = self.node.try_get_context("environment")
        prefix = self.node.try_get_context("prefix")
        stack_name = self.node.try_get_context("stack_name")

        self.logging_bucket_map = {
            "local": f"wdpr-guest360-local-{region}-logging",
            "pra": "wdpr-ia-dev-us-east-1-logging",
            "latest": f"wdpr-guest360-dev-{region}-logging",
            "stage": f"wdpr-guest360-test-{region}-logging",
            "load": f"wdpr-guest360-test-{region}-logging",
            "prod": f"wdpr-guest360-prod-{region}-logging",
        }

        if environment == "local":
            logging_bucket = aws_cdk.aws_s3.Bucket(
                self,
                f"{stack_name}-logging-bucket",
                bucket_name=self.logging_bucket_map["local"],
                block_public_access=aws_cdk.aws_s3.BlockPublicAccess.BLOCK_ALL,
                enforce_ssl=True,
                encryption=aws_cdk.aws_s3.BucketEncryption.S3_MANAGED,
            )
            NagSuppressions.add_resource_suppressions(
                logging_bucket,
                [
                    {
                        "id": "AwsSolutions-S1",
                        "reason": "This is the logging bucket so will not have a logging bucket for a logging bucket",
                    }
                ],
            )
        else:
            logging_bucket = aws_cdk.aws_s3.Bucket.from_bucket_attributes(
                self,
                f"{stack_name}LoggingBucket-{props['bucket_name']}",
                bucket_arn=f"arn:aws:s3:::{self.logging_bucket_map[environment]}",
            )

        props_default = {
            "auto_delete_objects": environment == "latest",
            "block_public_access": aws_cdk.aws_s3.BlockPublicAccess.BLOCK_ALL,
            "bucket_key_enabled": True,
            "lifecycle_rules": [
                aws_cdk.aws_s3.LifecycleRule(
                    id="Default",
                    abort_incomplete_multipart_upload_after=aws_cdk.Duration.days(7),
                    expiration=aws_cdk.Duration.days(30),
                    noncurrent_version_expiration=aws_cdk.Duration.days(7),
                )
            ],
            "removal_policy": aws_cdk.RemovalPolicy.DESTROY
            if environment == "latest"
            else aws_cdk.RemovalPolicy.RETAIN,
            "versioned": True,
        }

        if "encryption_key" not in props:
            self._kms_key = Guest360KMSKey(
                self, f"{prefix}-{construct_id}-{props['bucket_name']}-kms", {"alias": props["bucket_name"]}
            ).key
        else:
            self._kms_key = props["encryption_key"]

        self.props_dict = {1: props_default, 2: props}
        self.props_merged = {**self.props_dict[1], **self.props_dict[2]}

        self._bucket_name = S3BucketName(prefix, props["bucket_name"]).name()
        self._bucket = aws_cdk.aws_s3.Bucket(
            self,
            f"{prefix}-{construct_id}-{props['bucket_name']}",
            bucket_name=self._bucket_name,
            auto_delete_objects=self.props_merged["auto_delete_objects"],
            block_public_access=self.props_merged["block_public_access"],
            bucket_key_enabled=self.props_merged["bucket_key_enabled"],
            encryption=aws_cdk.aws_s3.BucketEncryption.KMS,
            encryption_key=cast(aws_cdk.aws_kms.IKey, self._kms_key),
            enforce_ssl=True,
            event_bridge_enabled=True,
            lifecycle_rules=self.props_merged["lifecycle_rules"],
            object_ownership=aws_cdk.aws_s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
            removal_policy=self.props_merged["removal_policy"],
            server_access_logs_bucket=logging_bucket,
            server_access_logs_prefix="s3logs/",
            versioned=self.props_merged["versioned"],
        )

        default_alarms = [
            # Monitoring 5XX errors. This can help with measuring performace:
            # https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html#optimizing-performance-guidelines-measure
            {
                "metric": aws_cdk.aws_cloudwatch.Metric(
                    namespace="AWS/S3",
                    metric_name="5xxErrors",
                    statistic=aws_cdk.aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cdk.aws_cloudwatch.Unit.COUNT,
                    period=aws_cdk.Duration.minutes(1),
                ),
                "evaluation_periods": 2,
                "threshold": 5,
                "datapoints_to_alarm": 2,
                "comparison_operator": aws_cdk.aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            }
        ]

        for cw_alarm in default_alarms:
            Guest360Alarm(
                self,
                f"{self._bucket_name}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )

    @staticmethod
    def get_s3bucketname(prefix: str, bucket_name: str):
        return S3BucketName(prefix, bucket_name).name()

    def export_ssm(self, resource_name: str) -> str:
        prefix = self.node.try_get_context("prefix")
        stack_name = aws_cdk.Stack.of(self).stack_name
        construct_name = "Guest360S3Bucket"
        resource_prefix = f"/{prefix}/{stack_name}/{construct_name}/{resource_name}"

        def parameter_name(componenet_name: str):
            return f"{resource_prefix}/{componenet_name}"

        encryption_key_arn = self.bucket.encryption_key.key_arn if self.bucket.encryption_key else ""

        self.ssm_export = (
            [
                aws_cdk.aws_ssm.StringParameter(
                    self,
                    "bucket_arn_parameter",
                    parameter_name=parameter_name("bucket_arn"),
                    string_value=self.bucket.bucket_arn,
                ),
                aws_cdk.aws_ssm.StringParameter(
                    self, "kms_arn_parameter", parameter_name=parameter_name("kms_arn"), string_value=encryption_key_arn
                ),
            ]
            if self.ssm_export is None
            else self.ssm_export
        )

        return resource_prefix

    @classmethod
    def from_ssm(cls, scope: Construct360, construct_id: str, stack_name: str, resource: str):
        stack = aws_cdk.Stack.of(scope)
        prefix = stack.node.try_get_context("prefix")
        construct_name = "Guest360S3Bucket"

        def parameter_name(componenet_name):
            return f"/{prefix}/{stack_name}/{construct_name}/{resource}/{componenet_name}"

        bucket_arn = aws_cdk.aws_ssm.StringParameter.value_for_string_parameter(scope, parameter_name("bucket_arn"))
        kms_arn = aws_cdk.aws_ssm.StringParameter.value_for_string_parameter(scope, parameter_name("kms_arn"))
        return cls(scope, construct_id, "", {}, ssm_props={"bucket_arn": bucket_arn, "kms_arn": kms_arn})
