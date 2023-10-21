""" DMS ingest construct"""

from copy import copy
from itertools import product
from typing import Dict, List, TypedDict, Union

import aws_cdk
import yaml
from aws_cdk import Stack, aws_iam, aws_ssm
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.ingestion import utils
from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.ingestion.dms.dms_endpoint import DMSEndpointProps, Guest360DMSEndpoint
from app.guest360_constructs.ingestion.dms.dms_replication_instance import DMSReplicationProps, Guest360DMSReplication
from app.guest360_constructs.ingestion.dms.dms_replication_task import (
    DMSReplicationTasksProps,
    Guest360DMSReplicationTask,
)
from app.guest360_constructs.ingestion.data_pipeline_dashboard import Guest360IngestionPipelineDashboard

from app.guest360_constructs.iam_role import Guest360IamRole, IAMProps
from app.guest360_constructs.kinesis_datastream import Guest360KinesisDatastream, KinesisProps
from app.guest360_constructs.kinesis_firehose import Guest360KinesisFirehose, KinesisFirehoseProps
from app.guest360_constructs.event_bridge_pipes import Guest360EventBridgePipe, EventBridgePipeProps
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.guest360_constructs.sqs_queue import Guest360SQSQueue, SQSQueueProps
from app.src.reliability.utils import SecurityGroupName, StackName, DMSResourceName
from app.src.utils.feature_flag.feature_flag import FeatureFlag
from app.guest360_constructs.app_config import Guest360AppConfig, AppConfigProps


class FetchCertificateError(Exception):
    "Failed to get the requested certificate"


class DMSNetworkingProps(TypedDict):
    allowlist: Dict[str, Dict]  # List of SG ingress and egress rules (all outbound allowed)
    blocklist: NotRequired[Dict[str, Dict]]  # List of Network ACL rules (for potential explicit denies)


@match_class_typing
class DMSProps(TypedDict):
    """Props class to define typing for input props for Guest360DMSIngest construct"""

    source_endpoint: Dict  # this should be DMSEndpointProps
    dms_repl_instance: Dict  # this should be DMSReplicationProps
    dms_repl_task: list[Dict]  # this should be DMSReplicationTasksProps
    kinesis: Dict  # this should be KinesisProps
    kinesis_dmz: Dict  # this should be KinesisProps
    kinesis_firehose: Dict  # this should be KinesisFirehoseProps
    target_iam: Dict  # this should be IAMProps
    source_iam: Dict  # this should be IAMProps
    source_kms_key: str  # kms-key id for SM for source
    target_endpoint: Dict  # this should be DMSEndpointProps
    networking: Dict  # this should be DMSNetworkingProps
    event_bridge_pipe_validation: Dict  # this should be EventBridgePipeProps
    event_bridge_pipe_dead_letter_queue: Dict  # this should be EventBridgePipeProps
    lambda_validator: Dict  # this should be LambdaFunctionProps
    lambda_dead_letter: Dict  # this should be LambdaFunctionProps
    sqs: Dict  # this should be SQSProps
    data_pipe: Dict  # Datacontract info
    app_config: Dict  # list of Guest360AppConfig resources, this should be AppConfigProps
    source_ssl_cert: NotRequired[str]  # ssl cert name for source


class Guest360DMSIngest(Construct360):
    """Construct for DMS RDBS ingestion pattern.
    Creates an DMS instance, replication task, kinesis streams, and endpoints for each RDBS table we are ingesting
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

    def __init__(self, scope: Construct360, construct_id: str, props: DMSProps, **kwargs) -> None:
        """Construct to create resources for messaging (rabbitmq, pubsub, etc) ingestion

        Args:
            scope (Construct360):
            construct_id (str): Construct ID
            props (dict): Configurations for DMS DMS Ingestion pipeline - see DMSProps TypedDict
        """

        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        # Imported props need to be checked apart
        DMSEndpointProps(props["source_endpoint"])
        DMSReplicationProps(props["dms_repl_instance"])
        for task in props["dms_repl_task"]:
            DMSReplicationTasksProps(task)
        KinesisProps(props["kinesis"])
        KinesisProps(props["kinesis_dmz"])
        KinesisFirehoseProps(props["kinesis_firehose"])
        IAMProps(props["target_iam"])
        DMSEndpointProps(props["target_endpoint"])
        LambdaFunctionProps(props["lambda_validator"])
        LambdaFunctionProps(props["lambda_dead_letter"])
        SQSQueueProps(props["sqs"])
        AppConfigProps(props["app_config"])
        DMSProps(props)

        project_path = self.project_dir
        stack = Stack.of(self)
        environment = self.node.try_get_context("environment").lower()
        self.region_name = aws_cdk.Stack.of(self).region.lower()
        self.account = Stack.of(self).account
        prefix = self.node.try_get_context("prefix")
        self.global_prefix = self.node.try_get_context("prefix_global")

        kinesis_dmz_props = props["kinesis_dmz"]
        kinesis_validated_props = props["kinesis"]

        sqs_props = props["sqs"]

        event_bridge_pipe_validation_props = props["event_bridge_pipe_validation"]
        event_bridge_pipe_dlq_props = props["event_bridge_pipe_dead_letter_queue"]

        data_pipe_props = props["data_pipe"]

        app_config_props = props["app_config"]
        app_config_base = props["app_config_base"]
        app_config_props["hosted_configuration"]["content"] = {**data_pipe_props, "source_type": "dms"}
        app_config_props.update(
            {
                "application_id": app_config_base.application_id,
                "environment_id": app_config_base.environment_id,
                "deployment_strategy_id": app_config_base.deployment_strategy_id,
            }
        )

        self.streams: list[aws_cdk.aws_kinesis.Stream] = []
        self.stream_names: list[str] = []

        # create target kinesis stream - will be the target endpoints for DMS
        target_name = props["stack_extension"]
        naming_prefix = f"{prefix}-{target_name}"
        source_naming_prefix = DMSResourceName(naming_prefix, "src").name()
        target_naming_prefix = DMSResourceName(naming_prefix, "tgt").name()
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

        # Setup validator, add env variable
        lambda_validator_props["environment"] = {
            "eventSourceARN": kinesis_dmz_data_stream.kinesis_stream.stream_arn,
            **lambda_validator_props.get("environment", {}),
        }

        lambda_validator = Guest360LambdaFunction(
            self, construct_id=f"{lambda_validator_props['function_name']}", props=lambda_validator_props
        )

        # AppConfig layer extension
        layer_arn = utils.app_config_get_layer_arn(self.region_name)

        app_config_layer = aws_cdk.aws_lambda.LayerVersion.from_layer_version_arn(self, "APPConfigLayer", layer_arn)
        lambda_validator.function.add_layers(app_config_layer)

        # Add AppConfig resources
        app_config = Guest360AppConfig(self, construct_id=f"{construct_id}-app-config", props=app_config_props)

        # Create AppConfig account iam role
        app_config_account_role_props = {
            "role_name": f"app-config-account-{props['stack_extension']}",
            "assumed_by": aws_iam.AccountPrincipal(self.account),
            "description": "IAM role to be used for granting account Lambda access to AppConfig",
        }

        app_config_account_role = Guest360IamRole(
            self,
            StackName(self.global_prefix, app_config_account_role_props["role_name"]).name(),
            app_config_account_role_props,
        ).role

        utils.app_config_role_grants(
            app_config_role=app_config_account_role,
            app_config_key=app_config.key,
            region=self.region_name,
            account=self.account,
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

        # Creates Event Bridge Pipe Dead Letter Queue just if the global feature flag is enabled
        config_path = f"{project_path}/app/configs/{environment}-infra-feature-flags.yaml"
        with FeatureFlag(
            environment, "dms_stream_global.dead_letter_queue_pipe", config_path
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
        with FeatureFlag(environment, "dms_stream_global.kinesis_firehose_dms", config_path) as kinesis_firehose_flag:
            if kinesis_firehose_flag:
                # The Kinesis Firehose will be deployed if the 'kinesis_firehose/enabled' is True.
                var_kinesis_firehose_name = target_name
                firehose_props = props["kinesis_firehose"]
                firehose_props["static_buckets"] = props["static_buckets"]
                firehose_props["kinesis_stream"] = kinesis_validated_data_stream.stream
                self._firehose = Guest360KinesisFirehose(self, var_kinesis_firehose_name, props=firehose_props)

        # TODO create iam service roles for kinesis target streams
        source_iam_props = props["source_iam"]
        target_iam_props = props["target_iam"]
        secrets_arn = props["source_endpoint"]["settings"]["secrets_manager_secret_id"]
        kms_arn = f"arn:aws:kms:{self.region_name}:{self.account}:key/{props['source_kms_key']}"

        if self.region_name == "us-east-1":
            # The role is used by DMS for the Kinesis target streams
            self.dms_target_role = Guest360IamRole(
                self, StackName(self.global_prefix, target_iam_props["role_name"]).name(), target_iam_props
            ).role

            self.secrets_manager_role = Guest360IamRole(
                self, StackName(self.global_prefix, source_iam_props["role_name"]).name(), source_iam_props
            ).role

        # Since IAM is global if region is us-west-2 assume the roles have already been created and avoid creating them again.
        else:
            self.dms_target_role = Guest360IamRole.from_role_name(
                self,
                StackName(self.global_prefix, f"{target_iam_props['role_name']}").name(),
                role_name=target_iam_props["role_name"],
                mutable=True,
            )
            self.secrets_manager_role = Guest360IamRole.from_role_name(
                self,
                StackName(self.global_prefix, f"{source_iam_props['role_name']}").name(),
                role_name=source_iam_props["role_name"],
                mutable=True,
            )

        # granting write access for dms target role for target kinesis streams
        kinesis_dmz_data_stream.kinesis_stream.grant_write(self.dms_target_role)
        kinesis_dmz_data_stream.kinesis_stream.grant_read(self.dms_target_role)

        # grant secrets manager access
        secrets_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"],
            resources=[secrets_arn],
        )

        self.secrets_manager_role.add_to_policy(secrets_policy)

        # grant kms key access
        kms_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["kms:Decrypt", "kms:DescribeKey"],
            resources=[kms_arn],
        )

        self.secrets_manager_role.add_to_policy(kms_policy)

        # Grab networking information from global environment config
        env_config_path = f"{project_path}/app/configs/{environment}-environment.yaml"
        with open(
            env_config_path,
            mode="r",
            encoding="utf-8",
        ) as file:
            environment_config = yaml.safe_load(file)
            subnets_config = environment_config["networking"][self.region_name]["subnets"]["non-routable"]
            vpc_config = environment_config["networking"][self.region_name]["vpc"]["id"]

            subnet_id_list = [subnet["id"] for subnet in subnets_config]

        vpc = aws_cdk.aws_ec2.Vpc.from_lookup(
            self, StackName(f"{prefix}-{construct_id}", "vpc").name(), vpc_id=vpc_config
        )

        sg_group = aws_cdk.aws_ec2.SecurityGroup(
            self,
            StackName(f"{prefix}-{construct_id}", "dms-sg").name(),
            security_group_name=SecurityGroupName(f"{prefix}-{construct_id}", "dms-sg").name(),
            vpc=vpc,
            allow_all_outbound=False,
        )

        networking_props = props["networking"]

        egress: Dict[str, List[Union[int, str]]] = networking_props["allowlist"]["egress"]

        all_cidrs_and_ports = product(egress["cidrs"], egress["ports"])
        for cidr, port in all_cidrs_and_ports:
            sg_group.add_egress_rule(
                peer=aws_cdk.aws_ec2.Peer.ipv4(cidr),
                connection=aws_cdk.aws_ec2.Port.tcp(port),
                description=f"egress-{cidr}-{port}",
            )

        # add rule to allow all local traffic
        sg_group.add_egress_rule(
            peer=aws_cdk.aws_ec2.Peer.ipv4(networking_props["allowlist"]["local_egress"]["cidr"]),
            connection=aws_cdk.aws_ec2.Port.all_traffic(),
            description="all local traffic",
        )

        sg_group_id = sg_group.security_group_id
        sg_group_id_list = [sg_group_id]

        # create replication instance
        instance_props = props["dms_repl_instance"]
        sg_ids = instance_props["security_group_ids"]

        if sg_ids:
            sg_group_id_list.extend(sg_ids)

        dms_instance_props = copy(instance_props)
        dms_instance_props["subnet_props"]["subnet_list"] = subnet_id_list
        dms_instance_props["security_group_ids"] = sg_group_id_list
        self.dms_repl_instance = Guest360DMSReplication(
            self, StackName(prefix, f"{construct_id}-instance").name(), dms_instance_props
        )

        # Create src endpoint
        source_props = props["source_endpoint"]
        dms_source_props = self.add_endpoint_identifier(source_naming_prefix, source_props)
        if "source_ssl_cert" in props:
            certificate_name = StackName(prefix, props["source_ssl_cert"]).name()
            dms_source_props = self.add_ssl_cert(props, dms_source_props, certificate_name)
        dms_source_props["settings"]["secrets_manager_access_role_arn"] = self.secrets_manager_role.role_arn
        self.dms_source_endpoint = Guest360DMSEndpoint(
            self, StackName(prefix, f"{construct_id}-source").name(), dms_source_props
        )

        # Create DMZ kinesis target endpoint
        kinesis_target_props = props["target_endpoint"]
        kinesis_endpoint_props = self.add_endpoint_identifier(target_naming_prefix, kinesis_target_props)
        kinesis_endpoint_props["settings"]["service_access_role_arn"] = self.dms_target_role.role_arn
        kinesis_endpoint_props["settings"]["stream_arn"] = kinesis_dmz_data_stream.kinesis_stream.stream_arn
        # add schema table to partition
        kinesis_endpoint_props["settings"]["partition_include_schema_table"] = True
        self.dms_target_endpoint = Guest360DMSEndpoint(
            self, StackName(prefix, f"{construct_id}-target").name(), kinesis_endpoint_props
        )

        self._dashboard = Guest360IngestionPipelineDashboard(
            self, f"{stack.stack_name}-dashboard", name=stack.stack_name
        )

        # Create replication task
        tasks_props = props["dms_repl_task"]
        self.dms_repl_tasks_list = []
        for task_prop in tasks_props:
            instance_identifier = self.dms_repl_instance.dms_replication_instance.resource_identifier
            arn_prefix = f"arn:aws:dms:{self.region_name}:{self.account}"
            dms_task_props = self.create_task_config(arn_prefix, prefix, target_name, instance_identifier, task_prop)
            self.dms_repl_task = Guest360DMSReplicationTask(
                self,
                StackName(prefix, f"{construct_id}-{task_prop['replication_task_identifier']}").name(),
                dms_task_props,
            )
            self.dms_repl_task.node.add_dependency(
                self.dms_target_endpoint, self.dms_source_endpoint, self.dms_repl_instance
            )
            self.dms_repl_tasks_list.append(self.dms_repl_task)
            self._dashboard.add_dms(
                stack.stack_name,
                task_prop["replication_task_identifier"],
                self.dms_repl_instance.dms_replication_instance_name,
                self.dms_repl_task.dms_replication_name,
            )

        #####
        # Dashboard
        #####

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
            self.dms_target_role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Grant Write creates wildcard policy kms:GenerateDataKey* and kms:ReEncrypt*",
                }
            ],
            True,
        )

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

    @staticmethod
    def add_endpoint_identifier(naming_prefix: str, props: DMSEndpointProps) -> DMSEndpointProps:
        """adds identifiers to the endpoint config

        Args:
            naming_prefix (str): identifier for the endpoint arn and resource name
            props (DMSEndpointProps): default props from yaml config

        Returns:
            DMSEndpointProps: endpoint props including newly created identifier
        """
        dms_endpoint_props = copy(props)
        dms_endpoint_props["endpoint_identifier"] = naming_prefix
        dms_endpoint_props["resource_identifier"] = naming_prefix
        return dms_endpoint_props

    @staticmethod
    def create_task_config(
        arn_prefix: str, prefix: str, target_name: str, instance_identifier: str, props: DMSReplicationTasksProps
    ) -> DMSReplicationTasksProps:
        """updates the task config

        Args:
            arn_prefix (str): arn with region and account
            prefix (str): stack prefix
            target_name (str): data source for naming purposes
            instance_identifier (str): replication instance name
            props (DMSReplicationTasksProps): default props from yaml config

        Returns:
            DMSReplicationTasksProps: task configs to include needed identifiers for instance, endpoints, tasks
        """
        dms_task_props = copy(props)
        replication_task_id = dms_task_props["replication_task_identifier"]
        naming_prefix = f"{prefix}-{target_name}"
        source_identifier = DMSResourceName(naming_prefix, "src").name()
        target_identifier = DMSResourceName(naming_prefix, "tgt").name()
        dms_task_props["source_endpoint_arn"] = f"{arn_prefix}:endpoint:{source_identifier}"
        dms_task_props["target_endpoint_arn"] = f"{arn_prefix}:endpoint:{target_identifier}"
        dms_task_props["replication_instance_arn"] = f"{arn_prefix}:rep:{instance_identifier}"
        dms_task_props["replication_task_identifier"] = f"{target_name}-{replication_task_id}"
        dms_task_props["resource_identifier"] = DMSResourceName(naming_prefix, replication_task_id).name()
        return dms_task_props

    def add_ssl_cert(
        self, dms_props: DMSProps, endpoint_props: DMSEndpointProps, certificate_name: str
    ) -> DMSEndpointProps:
        """_summary_
        Args:
            props (DMSProps): dms props loaded from the config file with static resources added
            endpoint_props (DMSEndpointProps): dictionary of endpoint props for DMS endpoint CFN
            certificate_name (str): certificate name so that arn may be identified and imported
        Returns:
            DMSEndpointProps: endpoint props with additional ssl_cert arn added to the props
        """
        if endpoint_props["ssl_mode"] in ["verify-ca", "verify-full"]:
            certificates = dms_props["dms_certificates"]
            cert = next(filter(lambda x: certificate_name in x["certificate_name"], certificates))
            cert_parameter = cert["parameter_name"]
            endpoint_props["certificate_arn"] = aws_ssm.StringParameter.value_for_string_parameter(self, cert_parameter)
        return endpoint_props
