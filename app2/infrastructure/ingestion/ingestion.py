"""
File containing code for the guest360 ingestion pipeline stack
"""

import logging
import sys
from pathlib import Path
from typing import List, Dict

import aws_cdk
from aws_cdk import Stack, Tags, aws_kinesis
from cdk_nag import NagSuppressions
from enum import Enum

from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.guest360_constructs.lambda_layer_construct import Guest360LambdaLayer
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from app.infrastructure.ingestion.ingestion_dms import DMSIngestion
from app.infrastructure.ingestion.dms_certs import DMSIngestionCerts
from app.infrastructure.ingestion.messaging import IngestionMessaging
from app.infrastructure.ingestion.kinesis import IngestionKinesis
from app.infrastructure.ingestion.ingestion_dms_task_manager import DMSTaskManager
from app.infrastructure.workstream_stack import WorkstreamStack
from app.infrastructure.reliability.enable_stack import DeployFlag
from app.src.reliability.Guest360ConfigInfra.assist import config_from_path, static_config_from_path
from app.src.ingestion.event_pipes.utils.merge_config import (
    merge_configurations,
    load_and_render_base_template,
    extend_dms_tasks,
)
from app.src.utils.feature_flag.feature_flag import FeatureFlag
from app.src.reliability.utils import StackName


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Ingestion | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class IngestionPattern(str, Enum):
    MESSAGING: str = "messaging"
    K2K: str = "kinesis2kinesis"
    DMS: str = "dms"


class Ingestion(WorkstreamStack):
    """
    Stack definition for the ingestion stack. Creates resources for data sourcing.
    """

    @property
    def s3_buckets(self) -> List[aws_cdk.aws_s3.Bucket]:
        """Property to return s3 buckets created by this stack.
        Returns:
            List: list of buckets
        """
        return self._buckets

    @property
    def streams(self) -> List[Dict[str, aws_kinesis.Stream]]:
        """Property to return kinesis streams created by this stack.
        Returns:
            List: List of Kinesis Streams
        """
        return self._kinesis_streams

    @property
    def stack_extension_dms(self) -> list[str]:
        return self.dms_stack_extensions

    def __init__(self, scope: Stack, construct_id: str, environment_config: dict, **kwargs) -> None:
        """Initialization method for ingestion class
        Args:
            scope (Construct360): scope for stack
            construct_id (str): ID of construct for naming purposes
            environment_config (dict): environment configuration details
        """
        super().__init__(scope, construct_id, **kwargs)

        self.construct_id = construct_id
        self._environment = self.node.try_get_context("environment").lower()
        self._stack = Stack.of(self)
        self._project_path = self.project_dir
        this_file_path = Path(__file__)
        self._config_dir = f"{this_file_path.parent}/config"

        # List to store the buckets / kms keys for reference
        self._buckets = []

        # Ingest pattern kinesis streams list
        self._kinesis_streams = []

        # DMS stack extensions
        self.dms_stack_extensions = []

        # DMS certificates list
        self._certificates = []

        # Using environment config to quiet pylint
        environment_config["unused"] = "unused"

        # Tags update
        Tags.of(self).add("prefix", self.prefix)

        # Create Appflow lambda
        self._appflow_lambda()

        # Deploy DMS certificates stack
        self._dms_certificates()

        # Deploy DMS task manager stack
        self._deploy_dms_task_manager()

        # Create ingestion static objects
        self._create_ingestion_static_objects()

        """
        Pipelines
        """

        # You can make <my-file-name>.yaml to just test your specific stack, but * gives everything underneath that path
        pipeline_config_path = f"{self._config_dir}/pipelines/{self._environment}/*.yaml"

        # Load the configuration file(s)
        loaded_pipeline_configs = config_from_path(pipeline_config_path)

        # Deploy all Construct instances
        logger.debug("BEGIN loading configuration into DATA PIPELINES...")
        for pipeline_config in loaded_pipeline_configs:
            config = pipeline_config["stack_config"]
            if (ingest_pattern := config.get("ingest_pattern")) not in (e.value for e in IngestionPattern):
                logger.debug(
                    "Unknown pattern %s - skipping configuration merge logic and stack creation", ingest_pattern
                )
                continue

            # Load base config template
            base_config = load_and_render_base_template(self._config_dir, config.get("stack_extension"), ingest_pattern)

            # Add static objects to the config data
            config["static_buckets"] = self._buckets

            # Merging template
            config = merge_configurations(base_config, config)

            match ingest_pattern:
                case IngestionPattern.MESSAGING:
                    if DeployFlag.is_stack_enabled(self, "Ingestion/Messaging"):
                        self._messaging_pattern(config=config)
                case IngestionPattern.K2K:
                    if (
                        DeployFlag.is_stack_enabled(self, "Ingestion/Kinesis2Kinesis")
                        or config["stack_extension"] == "dlr-lightning-lane"
                    ):
                        self._kinesis2kinesis(config=config)
                case IngestionPattern.DMS:
                    if DeployFlag.is_stack_enabled(self, "Ingestion/DMS"):
                        config = extend_dms_tasks(base_config, config)
                        self._dms_pattern(config=config, environment_config=environment_config)

        # Nags
        NagSuppressions.add_stack_suppressions(
            self,
            [
                {"id": "AwsSolutions-IAM5", "reason": "CDK lambda BucketNotificationsHandler"},
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok for BucketNotificationsHandler"},
            ],
        )

    def _kinesis2kinesis(self, config: dict) -> None:
        """
        Cross account kinesis work

        Args:
            config (dict): Kinesis2Kinesis config
        """

        if config["active"]:
            kinesis_stack = IngestionKinesis(
                self,
                config["stack_extension"],
                stack_name=StackName(self.prefix, f"ingest-{config['stack_extension']}").name(),
                config=config,
                termination_protection=self._environment == "prod",
                tags=self._stack.tags.tag_values(),
            )
            self._kinesis_streams.extend(kinesis_stack.kinesis_streams)

    def _messaging_pattern(self, config: dict) -> None:
        """
        Load the messaging construct (RabbitMQ, Google Pub/Sub, etc.), but not in local

        NOTE:
        Messaging should be turned off locally because
        a number of our ECS configurations are not supported by local stack.
        we also only want to deploy listeners in an environment once, due to there
        only being one queue

        Args:
            config (dict): Messaging config
        """

        termination_protection = self.node.try_get_context("termination_protection")
        if isinstance(config["active"], str):
            if config["active"].lower() == "true":
                config["active"] = True
            else:
                config["active"] = False

        if self.deployment_environment != self.EnvNames.LOCAL and config["active"]:
            for config_dictionary in config["pattern_instances"]:
                if config_dictionary["region"] == self._stack.region:
                    config_dictionary["resources"].update({"static_buckets": config["static_buckets"]})

                    # Stack per messaging config
                    messaging_stack = IngestionMessaging(
                        self,
                        config["stack_extension"],
                        stack_name=StackName(self.prefix, f"ingest-{config['stack_extension']}").name(),
                        config=config,
                        config_dictionary=config_dictionary,
                        tags=self._stack.tags.tag_values(),
                        termination_protection=termination_protection,
                    )

                    self._kinesis_streams.extend(messaging_stack.kinesis_streams)

    def _dms_pattern(self, config: dict, environment_config: dict, **kwargs) -> None:
        """
        Deploy DMS pattern workstream stacks

        Args:
            config (dict): DMS config
            environment_config (dict): Environment config details
        """

        is_static_env = self.node.try_get_context("is_static_env")

        # DMS only for us-east-1 initially, only load active, data pipelines
        if self.is_primary_region and config["active"] and (config["feature_branch"] or is_static_env):
            dms_stack = DMSIngestion(
                self,
                config["stack_extension"],
                config=config,
                environment_config=environment_config,
                dms_certs=self._certificates,
                stack_name=StackName(self.prefix, f"ingest-{config['stack_extension']}").name(),
                tags=self._stack.tags.tag_values(),
                termination_protection=self._environment == "prod",
            )
            self.dms_stack_extensions.append(dms_stack.stack_extension)
            self._kinesis_streams.extend(dms_stack.kinesis_streams)
            if dms_cert_stack := getattr(self, "dms_cert_stack"):
                dms_stack.add_dependency(dms_cert_stack)

    def _dms_certificates(self) -> None:
        """
        Load DMS certificates configuration and deploy DMS Ingestion Certs stack

        """

        dms_certificates_path = f"{self._config_dir}/static_objects/{self._environment}/certificates/*.yaml"
        loaded_dms_certificates_configs = static_config_from_path(dms_certificates_path)

        if DeployFlag.is_stack_enabled(self, "Ingestion/DMS/Certificates"):
            for config in loaded_dms_certificates_configs:
                # DMS only for us-east-1 initially
                if self.is_primary_region and config["active"]:
                    self.dms_cert_stack = DMSIngestionCerts(
                        self,
                        "dms-certificates",
                        config=config,
                        stack_name=StackName(self.prefix, "dms-certificates").name(),
                        tags=self._stack.tags.tag_values(),
                        termination_protection=self._environment == "prod",
                    )
                    self._certificates.extend(self.dms_cert_stack.certificates)

    def _appflow_lambda(self) -> None:
        """
        Function to deploy Appflow code based Lambda function

        """

        ctam_appflow_lambda_props: LambdaFunctionProps = {
            "code": aws_cdk.aws_lambda.Code.from_asset(
                f"{self._project_path}/bazel-bin/app/src/ingestion/appflow/custom_connector_ctam/custom_connector_guest360_ctam/ctam_appflow_ingest_api_lambda.zip"
            ),
            "description": "ctam lambda handler",
            "function_name": "ctam-appflow",
            "handler": "app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam.handlers.lambda_handler.ctam_lambda_handler",
            "runtime": aws_cdk.aws_lambda.Runtime.PYTHON_3_9,
        }

        ctam_appflow_lambda = Guest360LambdaFunction(
            self._stack, construct_id="ctam_appflow_lambda", props=ctam_appflow_lambda_props
        )

        principal = aws_cdk.aws_iam.ServicePrincipal("appflow.amazonaws.com")

        ctam_appflow_lambda.function.grant_invoke(principal)

    def _create_ingestion_static_objects(self) -> None:
        """
        Load and deploy static resource definitions for the Ingestion stack

        """

        # Load the configuration file(s)
        static_objects_path = f"{self._config_dir}/static_objects/{self._environment}/*.yaml"
        loaded_static_object_configs = static_config_from_path(static_objects_path)

        logger.debug("BEGIN loading configuration into STATIC OBJECTS...")

        # Filter active configs
        active_static_object_configs = filter(lambda obj: obj["active"], loaded_static_object_configs)

        for obj in active_static_object_configs:
            # only load active, static_objects
            for instance in obj["instances"]:
                self._create_static_resource(instance)

    def _create_static_resource(self, instance: dict):
        """
        Creates an instance of ingestion static resource

        Args:
            instance (dict): Loaded instance of static ingestion resource
        """

        static_object_name = f"{self.construct_id}-{instance['name']}"

        logger.debug("Passing configuration for static object: TYPE %s NAME %s", instance["type"], static_object_name)
        if instance["type"] == "bucket":
            instance["bucket_props"]["bucket_name"] = static_object_name
            var_bucket: Guest360S3Bucket = Guest360S3Bucket(
                self, static_object_name, region=self._stack.region, props=instance["bucket_props"]
            )
            self._buckets.append(
                {
                    "bucket": var_bucket.bucket,
                    "kms_key": var_bucket.kms_key,
                    "bucket_name": static_object_name,
                    "bucket_full_name": var_bucket.bucket_name,
                }
            )
            if static_object_name == f"{self.construct_id}-raw":
                var_bucket.export_ssm(static_object_name)
                self._grant_access_to_specific_dpms(var_bucket)

        # lambda layer for k2k cross-account app code
        elif instance["type"] == "k2klayer":
            props = instance["resources"]
            Guest360LambdaLayer(self, construct_id=static_object_name, props=props)

    def _grant_access_to_specific_dpms(self, var_bucket: Guest360S3Bucket):
        """
        Grant access to specific Data Product Managers (DPMs) who are working on
        the data contract effort and need access to view the
        raw data in s3 for testing purposes

        This also grants the developer role access to read S3 data in lower environments.

        Args:
            var_bucket (Guest360S3Bucket): S3 Bucket static resource
        """

        policy = aws_cdk.aws_iam.PolicyStatement(
            actions=["kms:Decrypt"],
            principals=[aws_cdk.aws_iam.ArnPrincipal(f"arn:aws:iam::{self._stack.account}:role/WDPR-GUEST360_DPM_ROLE")]
            + [aws_cdk.aws_iam.ArnPrincipal(f"arn:aws:iam::{self._stack.account}:role/WDPR-GUEST360_DEVELOPER")]
            if self._environment != self.EnvNames.PROD
            else [aws_cdk.aws_iam.ArnPrincipal(f"arn:aws:iam::{self._stack.account}:role/WDPR-GUEST360_DPM_ROLE")],
            resources=["*"],
        )
        var_bucket.kms_key.add_to_resource_policy(policy)

    def _deploy_dms_task_manager(self) -> None:
        """
        Deploy DMS Task Manager stack
        """

        feature_flag_path = f"{self._project_path}/app/configs/{self._environment}-infra-feature-flags.yaml"

        with FeatureFlag(
            self._environment, "dms_stacks.ingestion_dms_task_manager", feature_flag_path
        ) as dms_taskmanager_flag:
            if dms_taskmanager_flag or self.is_static_env:
                DMSTaskManager(
                    self,
                    "ingest-dms-task-manager",
                    config={},
                    stack_name=StackName(self.prefix, "ingest-dms-task-manager").name(),
                    tags=self._stack.tags.tag_values(),
                    termination_protection=self._environment == "prod",
                )
