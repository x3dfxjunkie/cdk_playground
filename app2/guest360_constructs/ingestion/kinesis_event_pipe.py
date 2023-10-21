"""Kinesis Guest360 Construct
"""
import logging

from typing import Dict, TypedDict, Union
from copy import copy
from aws_cdk import Stack, aws_iam, aws_kinesis, aws_lambda
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired
from app.guest360_constructs.app_config import AppConfigProps, Guest360AppConfig
from app.guest360_constructs.ingestion.data_pipeline_dashboard import Guest360IngestionPipelineDashboard

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.event_bridge_pipes import Guest360EventBridgePipe, EventBridgePipeProps
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.ingestion import utils
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream, KinesisProps
from app.guest360_constructs.kinesis_firehose import Guest360KinesisFirehose, KinesisFirehoseProps
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.guest360_constructs.sqs_queue import Guest360SQSQueue, SQSQueueProps
from app.src.reliability.utils import RoleName, StackName
from app.src.utils.feature_flag.feature_flag import FeatureFlag

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class UnknownCrossAccountTypeException(Exception):
    """Custom exception for unknown cross account type specified in config"""


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


@match_class_typing
class KinesisStackConfigProps(TypedDict):
    """Props class to define typing for input props for Guest360DMSIngest construct"""

    stack_extension: str
    kinesis: Dict  # this should be KinesisProps
    kinesis_dmz: Dict  # this should be KinesisProps
    kinesis_firehose: Dict  # this should be KinesisFirehoseProps
    event_bridge_pipe_validation: Dict  # this should be EventBridgePipeProps
    event_bridge_pipe_dead_letter_queue: Dict  # this should be EventBridgePipeProps
    lambda_validator: Dict  # this should be LambdaFunctionProps
    lambda_dead_letter: Dict  # this should be LambdaFunctionProps
    sqs: Dict  # this should be SQSProps
    cross_account: StackCrossAccountProps
    app_config: Dict  # list of Guest360AppConfig resources, this should be AppConfigProps
    data_pipe: NotRequired[Dict]  # Datacontract info


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

    def __init__(self, scope: Construct360, construct_id: str, props: KinesisStackConfigProps, **kwargs) -> None:
        """
        Class for creating Kinesis Data Stream and Kinesis Firehose for logging raw messages.
        Supports creation of Cross-Account IAM Role if this is the target of a Cross-Account
        Lambda Function.
        """
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        # Imported props need to be checked apart
        KinesisProps(props["kinesis"])
        KinesisProps(props["kinesis_dmz"])
        KinesisFirehoseProps(props["kinesis_firehose"])
        LambdaFunctionProps(props["lambda_validator"])
        LambdaFunctionProps(props["lambda_dead_letter"])
        SQSQueueProps(props["sqs"])
        AppConfigProps(props["app_config"])

        KinesisStackConfigProps(props)

        project_path = self.project_dir

        region = Stack.of(self).region.lower()
        account = Stack.of(self).account
        prefix = self.node.try_get_context("prefix_global").lower()
        environment = self.node.try_get_context("environment").lower()
        stack_config = props
        stack = Stack.of(self)
        self._firehose = None

        kinesis_dmz_props = props["kinesis_dmz"]
        kinesis_validated_props = props["kinesis"]

        sqs_props = props["sqs"]

        event_bridge_pipe_validation_props = props["event_bridge_pipe_validation"]
        event_bridge_pipe_dlq_props = props["event_bridge_pipe_dead_letter_queue"]

        data_pipe_props = props.get("data_pipe", {})

        app_config_props = props["app_config"]
        app_config_base = props["app_config_base"]
        app_config_props["hosted_configuration"]["content"] = {**data_pipe_props, "source_type": "k2k"}
        app_config_props.update(
            {
                "application_id": app_config_base.application_id,
                "environment_id": app_config_base.environment_id,
                "deployment_strategy_id": app_config_base.deployment_strategy_id,
            }
        )

        self.streams: list[aws_kinesis.Stream] = []
        self.stream_names: list[str] = []

        if not kinesis_validated_props.get("stream_name"):
            # TODO: doing this because we don't have stream_name in the config right now like we do for DMS
            kinesis_validated_props["stream_name"] = f"{construct_id}-stream"[:64]

        dmz_stream_name = kinesis_dmz_props["stream_name"]
        validated_stream_name = f"{kinesis_validated_props['stream_name']}-validated"
        kinesis_dmz_service_props = copy(kinesis_dmz_props)
        kinesis_dmz_service_props["stream_name"] = dmz_stream_name
        lambda_validator_props = props["lambda_validator"]
        lambda_dead_letter_props = props["lambda_dead_letter"]
        kinesis_validated_service_props = copy(kinesis_validated_props)
        kinesis_validated_service_props["stream_name"] = validated_stream_name

        # Build out both DMZ and Validated kinesis stream
        kinesis_dmz_data_stream = Guest360KinesisDatastream(
            self, construct_id=dmz_stream_name, props=kinesis_dmz_service_props
        )

        kinesis_validated_data_stream = Guest360KinesisDatastream(
            self, construct_id=validated_stream_name, props=kinesis_validated_service_props
        )

        # Export references to SSM
        kinesis_dmz_data_stream.export_ssm(dmz_stream_name)
        kinesis_validated_data_stream.export_ssm(validated_stream_name)

        # Setup validator, add env variable
        lambda_validator_props["environment"] = {
            "eventSourceARN": kinesis_dmz_data_stream.kinesis_stream.stream_arn,
            **lambda_validator_props.get("environment", {}),
        }

        lambda_validator = Guest360LambdaFunction(
            self, construct_id=f"{lambda_validator_props['function_name']}", props=lambda_validator_props
        )

        # AppConfig layer extension
        layer_arn = utils.app_config_get_layer_arn(region)

        app_config_layer = aws_lambda.LayerVersion.from_layer_version_arn(self, "APPConfigLayer", layer_arn)
        lambda_validator.function.add_layers(app_config_layer)

        app_config = Guest360AppConfig(self, construct_id=f"{construct_id}-app-config", props=app_config_props)

        # Create AppConfig account iam role
        app_config_account_role_props = {
            "role_name": f"app-config-account-{props['stack_extension']}",
            "assumed_by": aws_iam.AccountPrincipal(account),
            "description": "IAM role to be used for granting account Lambda access to AppConfig",
        }

        if stack.is_primary_region:
            app_config_account_role = Guest360IamRole(
                self,
                StackName(prefix, app_config_account_role_props["role_name"]).name(),
                app_config_account_role_props,
            ).role

            utils.app_config_role_grants(
                app_config_role=app_config_account_role,
                app_config_key=app_config.key,
                region=region,
                account=account,
            )
        else:
            app_config_account_role = Guest360IamRole.from_role_name(
                self,
                StackName(prefix, app_config_account_role_props["role_name"]).name(),
                role_name=app_config_account_role_props["role_name"],
                mutable=True,
            )

        # Set AppConfig lambda environment
        utils.app_config_lambda_configuration(
            lambda_function=lambda_validator.function,
            app_config_base=app_config_base,
            app_config=app_config,
            app_config_role=app_config_account_role,
        )

        ## Add environment variables needed for the lambda DLQ to put the record
        lambda_dead_letter_props["environment"] = {
            "KINESIS_STREAM_NAME": kinesis_validated_data_stream.kinesis_stream_name,
            "eventSourceARN": kinesis_dmz_data_stream.kinesis_stream.stream_arn,
            **lambda_dead_letter_props.get("environment", {}),
        }

        # Create role and policies for event bridge pipes
        event_pipe_source_policy_statement = aws_iam.PolicyStatement(
            actions=[
                "kinesis:DescribeStream",
                "kinesis:DescribeStreamSummary",
                "kinesis:GetRecords",
                "kinesis:GetShardIterator",
                "kinesis:ListStreams",
                "kinesis:ListShards",
                "kinesis:SubscribeToShard",
            ],
            effect=aws_iam.Effect.ALLOW,
            resources=[
                kinesis_dmz_data_stream.kinesis_stream.stream_arn,
                kinesis_validated_data_stream.kinesis_stream.stream_arn,
            ],
            conditions={},
        )

        event_pipe_target_policy_statement = aws_iam.PolicyStatement(
            actions=["kinesis:PutRecord", "kinesis:PutRecords"],
            effect=aws_iam.Effect.ALLOW,
            resources=[kinesis_validated_data_stream.kinesis_stream.stream_arn],
            conditions={},
        )

        event_pipe_transform_policy_statement = aws_iam.PolicyStatement(
            actions=["lambda:InvokeFunction"],
            effect=aws_iam.Effect.ALLOW,
            resources=[lambda_validator.function.function_arn],
            conditions={},
        )

        event_pipe_role = aws_iam.Role(
            self,
            "Role",
            assumed_by=aws_iam.ServicePrincipal("pipes.amazonaws.com"),
        )

        event_pipe_kinesis_kms_encrypt_policy_statement = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "kms:Decrypt",
                "kms:DescribeKey",
                "kms:GenerateDataKey*",
                "kms:ReEncrypt*",
            ],
            resources=[kinesis_validated_data_stream.stream.encryption_key.key_arn],
        )

        # Policy statements of kms
        source_kms_policy_statement = aws_iam.PolicyStatement(
            actions=[
                "kms:Decrypt",
            ],
            principals=[event_pipe_role],
            resources=["*"],
        )

        encrypt_kms_policy_statement = aws_iam.PolicyStatement(
            actions=[
                "kms:Decrypt",
                "kms:DescribeKey",
                "kms:GenerateDataKey*",
                "kms:ReEncrypt*",
            ],
            principals=[event_pipe_role],
            resources=["*"],
        )

        # Update kms policy statements
        kinesis_validated_data_stream.stream.encryption_key.add_to_resource_policy(encrypt_kms_policy_statement)
        kinesis_dmz_data_stream.stream.encryption_key.add_to_resource_policy(source_kms_policy_statement)

        # Update event bridge pipe role
        event_pipe_role.add_to_policy(event_pipe_source_policy_statement)
        event_pipe_role.add_to_policy(event_pipe_target_policy_statement)
        event_pipe_role.add_to_policy(event_pipe_transform_policy_statement)
        event_pipe_role.add_to_policy(event_pipe_target_policy_statement)
        event_pipe_role.add_to_policy(event_pipe_kinesis_kms_encrypt_policy_statement)
        kinesis_dmz_data_stream.stream.encryption_key.grant_decrypt(event_pipe_role)

        # Set up event bridge pipes.
        if not event_bridge_pipe_validation_props.get("role_arn"):
            event_bridge_pipe_validation_props["role_arn"] = event_pipe_role.role_arn
        if not event_bridge_pipe_dlq_props.get("role_arn"):
            event_bridge_pipe_dlq_props["role_arn"] = event_pipe_role.role_arn
        event_bridge_pipe_validation_props["source_arn"] = kinesis_dmz_data_stream.kinesis_stream.stream_arn
        event_bridge_pipe_validation_props["target_arn"] = kinesis_validated_data_stream.kinesis_stream.stream_arn
        event_bridge_pipe_validation_props["enrichment"] = lambda_validator.lambda_function.function_arn

        config_path = f"{project_path}/app/configs/{environment}-infra-feature-flags.yaml"
        with FeatureFlag(
            environment, "k2k_stream_global.dead_letter_queue_pipe", config_path
        ) as dead_letter_queue_flag:
            if dead_letter_queue_flag:
                lambda_dead_letter = Guest360LambdaFunction(
                    self, construct_id=f"{lambda_dead_letter_props['function_name']}", props=lambda_dead_letter_props
                )

                # Grant invoke permissions lambda dlq to pipe dlq role
                lambda_dead_letter.function.grant_invoke(event_pipe_role)

                # Giving dead letter lambda access to dmz and validated kinesis stream
                kinesis_validated_data_stream.kinesis_stream.grant_write(lambda_dead_letter.function)
                kinesis_dmz_data_stream.kinesis_stream.grant_read(lambda_dead_letter.function)

                # Set up SQS queue
                dead_letter_queue = Guest360SQSQueue(
                    self, construct_id=f"{sqs_props['queue_name']}-sqs", props=sqs_props
                )

                # Define IAM statements for SQS and associated Kms Key policy statements permissions
                event_pipe_sqs_iam_policy_statement = aws_iam.PolicyStatement(
                    actions=["sqs:SendMessage", "sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueAttributes"],
                    effect=aws_iam.Effect.ALLOW,
                    resources=[dead_letter_queue.queue.queue_arn],
                    conditions={},
                )

                event_pipe_kinesis_kms_encrypt_policy_statement.add_resources(
                    dead_letter_queue.queue.encryption_master_key.key_arn
                )

                event_pipe_role.add_to_policy(event_pipe_sqs_iam_policy_statement)

                # Update kms policy dlq kinesis target
                dead_letter_queue.queue.encryption_master_key.add_to_resource_policy(encrypt_kms_policy_statement)

                # App Config Lambda extension
                lambda_dead_letter.function.add_layers(app_config_layer)

                # Set AppConfig lambda environment
                utils.app_config_lambda_configuration(
                    lambda_function=lambda_dead_letter.function,
                    app_config_base=app_config_base,
                    app_config=app_config,
                    app_config_role=app_config_account_role,
                )

                # Update properties
                event_bridge_pipe_validation_props["pipe_source_parameters"]["kinesis_stream_parameters"][
                    "deadLetterConfig"
                ]["arn"] = dead_letter_queue.queue.queue_arn

                event_bridge_pipe_dlq_props["source_arn"] = dead_letter_queue.queue.queue_arn
                event_bridge_pipe_dlq_props["target_arn"] = lambda_dead_letter.lambda_function.function_arn

                EventBridgePipeProps(event_bridge_pipe_dlq_props)  # type: ignore

                pipe_dlq = Guest360EventBridgePipe(
                    self, construct_id=f"{event_bridge_pipe_dlq_props['name']}", props=event_bridge_pipe_dlq_props
                )

                # Ensure the role is created before the pipes
                pipe_dlq.node.add_dependency(event_pipe_role)

                # Lambda dlq nag
                NagSuppressions.add_resource_suppressions(
                    lambda_dead_letter.function,
                    [
                        {
                            "id": "AwsSolutions-IAM5",
                            "reason": "Grant kms:ReEncrypt*",
                        }
                    ],
                    True,
                )

        EventBridgePipeProps(event_bridge_pipe_validation_props)  # type: ignore

        pipe_validation = Guest360EventBridgePipe(
            self, construct_id=f"{event_bridge_pipe_validation_props['name']}", props=event_bridge_pipe_validation_props
        )

        # Ensure the role is created before the pipes
        pipe_validation.node.add_dependency(event_pipe_role)

        # Stream name is edited by kinesis construct, need to get the name from the iStream object
        # This is needed to pass the streams on to other stacks
        stream_dmz_name = kinesis_dmz_data_stream.stream.stream_name
        stream_validated_name = kinesis_validated_data_stream.stream.stream_name

        self.streams.append({"stream_name": stream_dmz_name, "stream": kinesis_dmz_data_stream.stream})
        self.streams.append({"stream_name": stream_validated_name, "stream": kinesis_validated_data_stream.stream})

        # Retrieve configuration items for the stack being deployed
        # VAR_yaml_config_file = f"ingestion/kinesis/config/{stack_name}.yaml"

        ########################################################################################################
        # KINESIS
        ########################################################################################################

        # Kinesis Data Stream

        self.kinesis_target_stream = kinesis_dmz_data_stream.kinesis_stream
        # Adding stream name explicitly since reference will return a Token to CDK, so downstream stacks cannot
        #  leverage "self.kinesis_target_stream.stream_name" directly.
        # stream_name is set with prefix internally in Guest360KinesisDatastream.
        self.kinesis_target_stream_name = kinesis_dmz_data_stream.kinesis_stream_name

        logger.debug("var_kinesis_stream_name: %s", self.kinesis_target_stream_name)

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
                assume_principal = aws_iam.WebIdentityPrincipal(var_web_principal, var_web_conditional)
            else:
                raise UnknownCrossAccountTypeException(
                    f'Unknown cross account type: {stack_config["cross_account"]["cross_account_type"]}'
                )
            role_name = RoleName(construct_id, "ca-role").name()

            if stack.is_primary_region:
                # With roles being global Only create kinesis ca roles if region is us-east-1
                self.target_kinesis_access_role = Guest360IamRole(
                    self,
                    StackName(prefix, role_name).name(),
                    props={
                        "role_name": role_name,
                        "assumed_by": assume_principal,
                        "description": f"Cross Account IAM Role for {construct_id}",
                    },
                ).role
            else:
                self.target_kinesis_access_role = Guest360IamRole.from_role_name(
                    self,
                    StackName(prefix, role_name).name(),
                    role_name=role_name,
                    mutable=True,
                )

            # self.kinesis_target_stream.grant_write(self.target_kinesis_access_role)
            self.kinesis_target_stream.grant_write(self.target_kinesis_access_role)
            self.kinesis_target_stream.grant_read(self.target_kinesis_access_role)

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

        config_path = f"{project_path}/app/configs/{environment}-infra-feature-flags.yaml"

        # Call to Kinesis Firehose just if the global feature flag is enabled
        with FeatureFlag(environment, "k2k_stream_global.kinesis_firehose_k2k", config_path) as kinesis_firehose_flag:
            if kinesis_firehose_flag:
                kinesis_firehose = stack_config["kinesis_firehose"]
                kinesis_firehose["kinesis_stream"] = kinesis_validated_data_stream.stream
                kinesis_firehose["static_buckets"] = stack_config["static_buckets"]
                self._firehose = Guest360KinesisFirehose(self, construct_id, props=kinesis_firehose)
                # Nag Suppressions

        #####
        # Dashboard
        #####
        self._dashboard = Guest360IngestionPipelineDashboard(
            self, f"{stack.stack_name}-dashboard", name=stack.stack_name
        )

        # add dmz kinesis metrics
        self._dashboard.add_kinesis_stream(kinesis_dmz_data_stream.kinesis_stream_name)
        # add event pipe enrichment function to dashboard
        self._dashboard.add_function_enrichment(
            namespace=stack.stack_name,
            subject=kinesis_dmz_data_stream.kinesis_stream_name,
            function_name=lambda_validator.function_name,
        )
        # add lambda_dead_letter if exists
        self._dashboard.add_function_enrichment(
            namespace=stack.stack_name,
            subject=kinesis_dmz_data_stream.kinesis_stream_name,
            function_name=lambda_dead_letter.function_name,
        )
        # add validated kinesis metrics
        self._dashboard.add_kinesis_stream(kinesis_validated_data_stream.kinesis_stream_name)
        # add firehose metrics
        if self.firehose_name:
            self._dashboard.add_firehose(self.firehose_name)

        NagSuppressions.add_resource_suppressions(
            event_pipe_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Grant Write creates wildcard policy kms:GenerateDataKey* and kms:ReEncrypt*",
                }
            ],
            True,
        )
        NagSuppressions.add_resource_suppressions(
            app_config_account_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Resource wildcard due AppConfig uses ID's instead of names to build arns",
                }
            ],
            True,
        )
        # End Nag suppresions
