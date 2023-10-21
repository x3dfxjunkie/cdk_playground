""" Messaging ingest construct for ecs listener infrastructure."""

import os
from copy import copy
from typing import Dict, TypedDict

import aws_cdk
from aws_cdk import Stack, aws_iam
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.ecs_consumer import ECSConsumerProps, Guest360ECS
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream, KinesisProps
from app.guest360_constructs.kinesis_firehose import Guest360KinesisFirehose, KinesisFirehoseProps
from app.guest360_constructs.ingestion.data_pipeline_dashboard import Guest360IngestionPipelineDashboard

from app.guest360_constructs.ingestion import utils
from app.guest360_constructs.event_bridge_pipes import Guest360EventBridgePipe, EventBridgePipeProps
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.guest360_constructs.sqs_queue import Guest360SQSQueue, SQSQueueProps
from app.src.utils.feature_flag.feature_flag import FeatureFlag
from app.src.reliability.utils import StackName

from app.guest360_constructs.app_config import Guest360AppConfig, AppConfigProps


@match_class_typing
class MessagingProps(TypedDict):
    """Props class to define typing for input props for Guest360MessagingIngest construct"""

    cluster_name: str  # Name of the ECS Cluster
    ecs: Dict  # this should be ECSConsumerProps, just FYI. See ECSConsumer props for more info
    kinesis: Dict  # this should be KinesisProps, just FYI. See Kinesis props for more info
    kinesis_dmz: Dict  # this should be KinesisProps
    kinesis_firehose: Dict  # this should be KinesisFirehoseProps, just FYI. See KinesisFirehose props for more info
    # source_kms_key: str  # kms-key id for SM for source
    event_bridge_pipe_validation: Dict  # this should be EventBridgePipeProps
    event_bridge_pipe_dead_letter_queue: Dict  # this should be EventBridgePipeProps
    lambda_validator: Dict  # this should be LambdaFunctionProps
    lambda_dead_letter: Dict  # this should be LambdaFunctionProps
    sqs: Dict  # this should be SQSProps
    data_pipe: Dict  # Datacontract info
    app_config: Dict  # list of Guest360AppConfig resources, this should be AppConfigProps


class Guest360MessagingIngest(Construct360):
    """Construct for messaging ingest pattern.
    Creates an ECS cluster and kinesis streams for each queue being listened to.
    """

    @property
    def kinesis_streams(self) -> list[aws_cdk.aws_kinesis.Stream]:
        """Property to return kinesis streams"""
        return self.streams

    @property
    def dashboard(self) -> aws_cdk.aws_cloudwatch.Dashboard:
        return self._dashboard

    @property
    def firehose_name(self) -> str:
        """Return the name of the firehose resource, if there is one."""
        if self._firehose is not None:
            return self._firehose.firehose_name
        else:
            return ""

    def __init__(self, scope: Construct360, construct_id: str, props: MessagingProps, **kwargs) -> None:
        """Construct to create resources for messaging (rabbitmq, pubsub, etc) ingestion

        Args:
            scope (Construct360):
            construct_id (str): Construct ID
            props (dict): Configurations for Messaging ECS Cluster - see MessagingProps TypedDict
        """

        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        # Imported props need to be checked apart
        ECSConsumerProps(props["ecs"])
        KinesisProps(props["kinesis"])
        KinesisProps(props["kinesis_dmz"])
        KinesisFirehoseProps(props["kinesis_firehose"])
        LambdaFunctionProps(props["lambda_validator"])
        LambdaFunctionProps(props["lambda_dead_letter"])
        SQSQueueProps(props["sqs"])
        AppConfigProps(props["app_config"])

        MessagingProps(props)

        stack = Stack.of(self)
        environment = self.node.try_get_context("environment").lower()
        prefix = self.node.try_get_context("prefix")
        region_name = Stack.of(self).region.lower()
        account = Stack.of(self).account
        global_prefix = self.node.try_get_context("prefix_global")

        # Props section
        kinesis_dmz_props = props["kinesis_dmz"]
        kinesis_validated_props = props["kinesis"]
        sqs_props = props["sqs"]
        event_bridge_pipe_validation_props = props["event_bridge_pipe_validation"]
        event_bridge_pipe_dlq_props = props["event_bridge_pipe_dead_letter_queue"]
        data_pipe_props = props["data_pipe"]
        lambda_validator_props = props["lambda_validator"]
        lambda_dead_letter_props = props["lambda_dead_letter"]
        app_config_props = props["app_config"]
        app_config_base = props["app_config_base"]
        app_config_props["hosted_configuration"]["content"] = {**data_pipe_props, "source_type": "messaging"}
        app_config_props.update(
            {
                "application_id": app_config_base.application_id,
                "environment_id": app_config_base.environment_id,
                "deployment_strategy_id": app_config_base.deployment_strategy_id,
            }
        )

        self.streams: list[aws_cdk.aws_kinesis.Stream] = []
        self.stream_names: list[str] = []
        self.stream_dict: dict[str, aws_cdk.aws_kinesis.Stream] = {}

        config_path = (
            f"{os.path.dirname(os.path.realpath(__file__))}/../../configs/{environment}-infra-feature-flags.yaml"
        )

        # Create target kinesis stream - will be the target endpoints for Messaging
        target_name = props["stack_extension"]
        naming_prefix = f"{prefix}-{target_name}"
        kinesis_dmz_stream_name = kinesis_dmz_props["stream_name"]
        kinesis_validated_stream_name = f"{kinesis_validated_props['stream_name']}-validated"
        kinesis_dmz_service_props = copy(kinesis_dmz_props)
        kinesis_dmz_service_props["stream_name"] = kinesis_dmz_stream_name
        kinesis_validated_service_props = copy(kinesis_validated_props)
        kinesis_validated_service_props["stream_name"] = kinesis_validated_stream_name

        # Build out both DMZ and Validated kinesis stream
        kinesis_dmz_data_stream = Guest360KinesisDatastream(
            self, construct_id=kinesis_dmz_stream_name, props=kinesis_dmz_service_props
        )

        kinesis_validated_data_stream = Guest360KinesisDatastream(
            self, construct_id=kinesis_validated_stream_name, props=kinesis_validated_service_props
        )

        # Export kinesis references to SSM
        kinesis_validated_data_stream.export_ssm(kinesis_validated_stream_name)
        kinesis_dmz_data_stream.export_ssm(kinesis_dmz_stream_name)

        # Setup validator, add env variable for ssm
        lambda_validator_props["environment"] = {
            "eventSourceARN": kinesis_dmz_data_stream.kinesis_stream.stream_arn,
            **lambda_validator_props.get("environment", {}),
        }

        lambda_validator = Guest360LambdaFunction(
            self, construct_id=f"{lambda_validator_props['function_name']}", props=lambda_validator_props
        )

        # AppConfig layer extension
        layer_arn = utils.app_config_get_layer_arn(region_name)

        app_config_layer = aws_cdk.aws_lambda.LayerVersion.from_layer_version_arn(self, "APPConfigLayer", layer_arn)
        lambda_validator.function.add_layers(app_config_layer)

        # Add AppConfig resources
        app_config = Guest360AppConfig(self, construct_id=f"{construct_id}-app-config", props=app_config_props)

        # Create AppConfig account iam role
        app_config_account_role_props = {
            "role_name": f"app-config-account-{props['stack_extension']}",
            "assumed_by": aws_iam.AccountPrincipal(account),
            "description": "IAM role to be used for granting account Lambda access to AppConfig",
        }

        app_config_account_role = Guest360IamRole(
            self,
            StackName(global_prefix, app_config_account_role_props["role_name"]).name(),
            app_config_account_role_props,
        ).role

        utils.app_config_role_grants(
            app_config_role=app_config_account_role,
            app_config_key=app_config.key,
            region=region_name,
            account=account,
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
        KMS_DECRYPT = "kms:Decrypt"
        event_pipe_kinesis_kms_encrypt_policy_statement = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                KMS_DECRYPT,
                "kms:DescribeKey",
                "kms:GenerateDataKey*",
                "kms:ReEncrypt*",
            ],
            resources=[kinesis_validated_data_stream.stream.encryption_key.key_arn],
        )

        # Policy statements of kms
        source_kms_policy_statement = aws_iam.PolicyStatement(
            actions=[
                KMS_DECRYPT,
            ],
            principals=[event_pipe_role],
            resources=["*"],
        )

        encrypt_kms_policy_statement = aws_iam.PolicyStatement(
            actions=[
                KMS_DECRYPT,
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

        # Creates Event Bridge Pipe Dead Letter Queue just if the global feature flag is enabled
        with FeatureFlag(
            environment, "messaging_stream_global.dead_letter_queue_pipe", config_path
        ) as dead_letter_queue_flag:
            if dead_letter_queue_flag:
                # Dead Letter Queue Lambda definition
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

        # Call to Kinesis Firehose just if the global feature flag is enabled
        var_kinesis_firehose_name = target_name
        with FeatureFlag(
            environment, "messaging_stream_global.kinesis_firehose_messaging", config_path
        ) as kinesis_firehose_flag:
            if kinesis_firehose_flag:
                firehose_props = props["kinesis_firehose"]
                firehose_props["static_buckets"] = props["static_buckets"]
                firehose_props["kinesis_stream"] = kinesis_validated_data_stream.stream
                self._firehose = Guest360KinesisFirehose(self, var_kinesis_firehose_name, props=firehose_props)

        for service in props["ecs"]["services"]:
            service["environment"]["KINESIS_STREAM"] = stream_dmz_name
            self.stream_dict[service["service_name"]] = kinesis_dmz_data_stream.stream

        # Ensure stream name to publish to is updated in each set of environment variables to pass to containers

        props["ecs"]["stack_extension"] = construct_id
        ecs_cluster = Guest360ECS(self, props["cluster_name"], props["ecs"])
        for service_name, stream in self.stream_dict.items():
            # Granting write access for messaging ecs target role for target kinesis streams
            stream.grant_write(ecs_cluster.task_roles[service_name].role)
            # Is it necessary to grant read?
            stream.grant_read(ecs_cluster.task_roles[service_name].role)

            NagSuppressions.add_resource_suppressions(
                ecs_cluster.task_roles[service_name].role,
                [
                    {
                        "id": "AwsSolutions-IAM5",
                        "reason": "Grant Write creates wildcard policy kms:GenerateDataKey* and kms:ReEncrypt*",
                    }
                ],
                True,
            )

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

        # Nag Suppressions
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
        # End Nag suppressions
