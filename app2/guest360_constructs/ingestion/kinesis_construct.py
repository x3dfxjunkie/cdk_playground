"""Kinesis Guest360 Construct
"""
import logging
from copy import deepcopy
from typing import Dict, TypedDict, Union

from aws_cdk import Stack, aws_iam, aws_kinesis
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream, KinesisProps
from app.guest360_constructs.kinesis_firehose import Guest360KinesisFirehose, KinesisFirehoseProps
from app.src.reliability.utils import RoleName
from app.src.utils.feature_flag.feature_flag import FeatureFlag

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class StackCrossAccountProps(TypedDict):
    cross_account_type: Union[str, None]
    cross_account_id: Union[int, None]
    cross_account_role_name: Union[str, None]


@match_class_typing
class StackConfigProps(TypedDict):
    stack_extension: str
    kinesis: Dict  # this should be KinesisProps, just FYI. See Kinesis props for more info
    cross_account: StackCrossAccountProps
    kinesis_firehose: Dict


class Kinesis(Construct360):
    """Main Kinesis Construct to create the Kinesis Data Stream.
    Additional resources may be created based on the configuration for cross account IAM Roles, and Kinesis Firehose
    Args:
        Construct (Construct360): Defined as a re-usable Contruct object
    """

    @property
    def kinesis_stream(self) -> aws_kinesis.Stream:
        return self.kinesis_target_stream

    @property
    def kinesis_stream_name(self) -> str:
        return self.kinesis_target_stream_name

    @property
    def firehose_name(self) -> str:
        """Return the name of the firehose resource, if there is one."""
        if self._firehose is not None:
            return self._firehose.firehose_name
        else:
            return ""

    def __init__(self, scope: Construct360, construct_id: str, props: StackConfigProps, **kwargs) -> None:
        """
        Class for creating Kinesis Data Stream and Kinesis Firehose for logging raw messages.
        Supports creation of Cross-Account IAM Role if this is the target of a Cross-Account
        Lambda Function.
        """
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        # Imported props need to be checked apart
        KinesisProps(props["kinesis"])
        KinesisFirehoseProps(props["kinesis_firehose"])
        StackConfigProps(props)

        project_path = self.project_dir
        region = Stack.of(self).region.lower()
        prefix = self.node.try_get_context("prefix_global").lower()
        environment = self.node.try_get_context("environment").lower()
        stack_config = props
        stack_name = self.node.try_get_context("stack_name").lower()
        self._firehose = None

        # Retrieve configuration items for the stack being deployed
        # VAR_yaml_config_file = f"ingestion/kinesis/config/{stack_name}.yaml"

        def name_convention(short_resource_description: str) -> str:
            """Creates necessary naming convention
            Args:
                short_resource_description (str): Name of the resource.
            Returns:
                str: Formatted naming with desired conventions.
            """

            name = f"{stack_config['stack_extension']}-{short_resource_description}"
            return name

        ########################################################################################################
        # KINESIS
        ########################################################################################################

        # Kinesis Data Stream
        var_kinesis_stream_name = name_convention("stream")[:64]

        # If this is a cross_account source then we will take the Kinesis Data Stream name exactly how it is
        # to simulate the source test environment
        if "cross_account" in stack_config and "cross_account_type" in stack_config["cross_account"]:
            if stack_config["cross_account"]["cross_account_type"] == "source":
                var_kinesis_stream_name = stack_config["kinesis"]["kinesis_data_stream_name"]

        props = stack_config["kinesis"]
        props["stream_name"] = var_kinesis_stream_name

        # create kinesis datastream specific props
        datastream_props = deepcopy(props)

        g_kinesis_stream = Guest360KinesisDatastream(self, construct_id=var_kinesis_stream_name, props=datastream_props)

        self.kinesis_target_stream = g_kinesis_stream.kinesis_stream
        # Adding stream name explicitly since reference will return a Token to CDK, so downstream stacks cannot
        #  leverage "self.kinesis_target_stream.stream_name" directly.
        # stream_name is set with prefix internally in Guest360KinesisDatastream.
        self.kinesis_target_stream_name = g_kinesis_stream.kinesis_stream_name

        logger.debug("var_kinesis_stream_name: %s", self.kinesis_target_stream_name)

        self.streams: List[Dict[str, aws_kinesis.Stream]] = []
        self.streams.extend(ingest_pipe.streams)

        #######################################################################################################
        # IAM - Cross Account Role
        #######################################################################################################

        # We only create the IAM role in Guest360 if this is receiving events from a remote Lambda in another account
        if "cross_account" in stack_config and stack_config["cross_account"]["cross_account_type"] is not None:
            if stack_config["cross_account"]["cross_account_type"] == "target":
                var_principal_arn = "".join(
                    [
                        "arn:aws:iam::",
                        str(stack_config["cross_account"]["cross_account_id"]),
                        ":role/",
                        stack_config["cross_account"]["cross_account_role_name"],
                    ]
                )
                logger.debug("var_principal_arn: %s", var_principal_arn)

                # Create Kinesis IAM Role and Policy

                var_kinesis_role_name = RoleName(stack_config["stack_extension"], "ca-lambda-role").name()
                kinesis_stream_role_name = "ca-lambda"
                assume_principal = aws_iam.ArnPrincipal(var_principal_arn)

            elif stack_config["cross_account"]["cross_account_type"] == "gcp":
                var_web_principal = "accounts.google.com"
                var_web_audience = stack_config["cross_account"]["cross_account_role_name"]
                var_web_sub = str(stack_config["cross_account"]["cross_account_id"])
                var_web_conditional = {
                    "StringEquals": {
                        "accounts.google.com:aud": var_web_sub,
                        "accounts.google.com:sub": var_web_sub,
                        "accounts.google.com:oaud": var_web_audience,
                    }
                }
                logger.debug("var_web_conditional: %s", var_web_conditional)

                # Create Kinesis IAM Role and Policy

                var_kinesis_role_name = RoleName(stack_config["stack_extension"], "ca-gcp-role").name()
                kinesis_stream_role_name = "ca-gcp"
                assume_principal = aws_iam.WebIdentityPrincipal(var_web_principal, var_web_conditional)

            kinesis_stream_role_name_prefix = f"{construct_id}-{kinesis_stream_role_name}"

            if region == "us-east-1":
                # With roles being global Only create kinesis ca roles if region is us-east-1
                self.target_kinesis_access_role = Guest360IamRole(
                    self,
                    construct_id=var_kinesis_role_name,
                    props={
                        "role_name": f"{kinesis_stream_role_name_prefix}-role",
                        "assumed_by": assume_principal,
                        "description": "Cross Account IAM Role",
                    },
                ).role
            else:
                self.target_kinesis_access_role = aws_iam.Role.from_role_name(
                    self,
                    RoleName(prefix, f"{kinesis_stream_role_name_prefix}-role").name(),
                    role_name=RoleName(prefix, f"{kinesis_stream_role_name_prefix}-role").name(),
                    mutable=True,
                )

            self.kinesis_target_stream.grant_write(self.target_kinesis_access_role)

            NagSuppressions.add_resource_suppressions(
                self.target_kinesis_access_role,
                [
                    {
                        "id": "AwsSolutions-IAM5",
                        "reason": "Grant Write creates wildcard policy kms:GenerateDataKey* and kms:ReEncrypt*",
                    }
                ],
                True,
            )

        # The Kinesis Firehose will be deployed if the 'kinesis_firehose/enabled' is True.
        # The mandatory fields are 'kinesis_firehose/bucket_name' and
        # 'kinesis_firehose/kinesis_stream'

        kinesis_firehose = stack_config["kinesis_firehose"]
        kinesis_firehose["kinesis_stream"] = self.kinesis_target_stream
        kinesis_firehose["static_buckets"] = stack_config["static_buckets"]

        var_kinesis_firehose_name = f"{construct_id}-fhose"

        config_path = f"{project_path}/app/configs/{environment}-infra-feature-flags.yaml"

        # Call to Kinesis Firehose just if the global feature flag is enabled
        enabled_stack_name = kinesis_firehose.get("enabled_stack_name", "NOT_FOUND")
        with FeatureFlag(environment, "k2k_stream_global.kinesis_firehose_k2k", config_path) as kinesis_firehose_flag:
            if kinesis_firehose_flag and (
                environment not in ("local", "latest") or enabled_stack_name.lower() == stack_name.lower()
            ):
                self._firehose = Guest360KinesisFirehose(self, var_kinesis_firehose_name, props=kinesis_firehose)
