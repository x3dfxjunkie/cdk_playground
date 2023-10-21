"""This file contains a construct that creates a datalake and can add multiple kinesis streams"""
import os
from pathlib import Path
from typing import List, Sequence, TypedDict, Union, cast

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.iam_role import Guest360IamRole, IAMProps
from app.guest360_constructs.lambda_function import Guest360LambdaFunction
from app.guest360_constructs.processing.processing_firehose import ProcessingFirehose, ProcessingFirehoseProps
from app.guest360_constructs.s3_bucket import Guest360S3Bucket, S3Props
from aws_cdk import Duration, Stack, aws_kinesis, aws_lambda, aws_iam
from cdk_nag import NagSuppressions


class Target(TypedDict):
    stream: Union[aws_kinesis.IStream, aws_kinesis.Stream]
    partitioning: str


class AnalyticsDatalakeProps(TypedDict):
    targets: Sequence[Target]


class AnalyticsDatalake(Construct360):
    """Abstracts the logic to create an s3 datalake. Currently only supports Kinesis, will expand when necessessary
    Args:
        props (_type_): AnalyticsDatalakeProps
    """

    bucket: Guest360S3Bucket
    targets: List[ProcessingFirehose]
    analysis_role: Guest360IamRole

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        props: AnalyticsDatalakeProps,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stack = Stack.of(self)
        stack_name = stack.stack_name
        current_region = stack.region

        bucket_props: S3Props = {
            "bucket_name": f"{stack_name}-datalake-bucket",
        }

        self.bucket = Guest360S3Bucket(self, "datalake_bucket", current_region, bucket_props)

        self.__implement_analytics_role()

        stack_path = str(Path(os.getcwd()).parents[0])

        self.__firehose_transformer = Guest360LambdaFunction(
            self,
            "firehose_transformer",
            {
                "code": aws_lambda.Code.from_asset(
                    f"{stack_path}/bazel-bin/app/src/processing/firehose_transformer/lambda_archive.zip"
                ),
                "description": "Processing Firehose Transformer",
                "handler": "lambda_function.lambda_handler",
                "runtime": aws_lambda.Runtime.PYTHON_3_9,
                "timeout": Duration.minutes(5),
            },
        )

        def kinesis_firehose_mapping(construct_id: str, target: Target) -> ProcessingFirehose:
            kinesis_firehose_props: ProcessingFirehoseProps = {
                "destination": {"bucket": self.bucket},
                "prefix": target["partitioning"],
                "kinesis_source": target["stream"],
                "lambda_transformer": cast(aws_lambda.IFunction, self.__firehose_transformer.function),
            }

            return ProcessingFirehose(
                self,
                construct_id,
                kinesis_firehose_props,  # type: ignore
            )

        self.targets = [
            kinesis_firehose_mapping(f'{props["targets"].index(target)}_datalake_firehose', target)
            for target in props["targets"]
        ]

        NagSuppressions.add_stack_suppressions(
            Stack.of(self),
            [
                {"id": "AwsSolutions-IAM5", "reason": "CDK lambda BucketNotificationsHandler"},
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok for BucketNotificationsHandler"},
            ],
        )

    def add_target(self, target: Target) -> ProcessingFirehose:
        kinesis_firehose_props: ProcessingFirehoseProps = {
            "destination": {"bucket": self.bucket},
            "prefix": target["partitioning"],
            "kinesis_source": target["stream"],
            "lambda_transformer": cast(aws_lambda.IFunction, self.__firehose_transformer.function),
        }

        processing_firehose = ProcessingFirehose(
            self,
            f'{len(self.targets)}"_datalake_firehose"',
            kinesis_firehose_props,  # type: ignore
        )

        self.targets.append(processing_firehose)
        return processing_firehose

    def __implement_analytics_role(self):
        account_id = Stack.of(self).account
        role_names = ["WDPR-PROVISIONER", "WDPR-DEVELOPER"]

        iam_props: IAMProps = {
            "assumed_by": aws_iam.CompositePrincipal(
                *[aws_iam.ArnPrincipal(f"arn:aws:iam::{account_id}:role/{role_name}") for role_name in role_names],
                aws_iam.ServicePrincipal("glue.amazonaws.com"),
            ),
            "description": "Used for Analysis",
        }

        self.analysis_role = Guest360IamRole(self, "analysis_role", iam_props)  # type: ignore

        self.bucket.bucket.grant_read_write(self.analysis_role.role)

        self.analysis_role.role.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceNotebookRole")
        )

        NagSuppressions.add_resource_suppressions(
            self.analysis_role.role,
            [
                {"id": "AwsSolutions-IAM5", "reason": "For analysis"},
                {"id": "AwsSolutions-IAM4", "reason": "Managed Policies are OK"},
            ],
            apply_to_children=True,
        )
