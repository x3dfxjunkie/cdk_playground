""" DMS Ingestion Stack for DMS Ingest infrastructure."""
import logging
import sys
import os

import aws_cdk
from aws_cdk import Stack

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.ingestion.dms_ingest_event_pipe import Guest360DMSIngest
from app.guest360_constructs.ingestion.dms.dms_endpoint import DMSEngineType
from app.guest360_constructs.load_testing.load_testing_rds import LoadTestingRDS
from app.guest360_constructs.app_config_base import Guest360AppConfigBase
from app.infrastructure.workstream_stack import WorkstreamStack
from app.src.reliability.Guest360ConfigInfra.assist import config_from_path, static_config_from_path

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - DMS Ingestion | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class DMSIngestion(WorkstreamStack):
    """
    Stack definition for the dms ingestion pattern stack. Creates resources for data sourcing that use DMS pattern.
    """

    @property
    def kinesis_streams(self) -> list[aws_cdk.aws_kinesis.Stream]:
        """Property to return kinesis streams"""
        return self.target_kinesis_streams

    @property
    def stack_extension(self) -> str:
        return self._stack_extension

    def __init__(
        self, scope: Construct360, construct_id: str, config: dict, environment_config: dict, dms_certs: list, **kwargs
    ) -> None:
        """Initialization method for ingestion class
        Args:
            scope (Construct360): scope for stack
            construct_id (str): ID of construct for naming purposes
            environment_config (dict): environment configuration details
        """
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)
        environment = self.node.try_get_context("environment").lower()
        is_static_env = self.node.try_get_context("is_static_env")
        load_test_deploy = DMSIngestion.check_loadtest_env(environment, is_static_env)

        # pathing
        full_path = os.path.realpath(__file__)
        config_dir = f"{os.path.dirname(full_path)}/config"

        self.target_kinesis_streams = []
        self._stack_extension = ""

        # log the current stack_extension for potential debugging...
        logger.debug(
            "Passing configuration to pipeline stack: TYPE %s NAME %s",
            config["ingest_pattern"],
            config["stack_extension"],
        )
        app_config_base_props = {
            "deployment_strategy": {
                "deployment_duration_in_minutes": 0,
                "growth_factor": 100,
                "replicate_to": "NONE",
            },
        }
        app_config_base = Guest360AppConfigBase(
            self, construct_id=config["stack_extension"], props=app_config_base_props
        )

        # If load-testing enabled create a dummy RDS instance
        if "load_testing" in config and config["load_testing"] and load_test_deploy:
            self._stack_extension = config["stack_extension"]
            engine_type = config["load_testing_engine_type"]
            rds_config = DMSIngestion.loadtest_get_rds_config(config_dir, engine_type)
            self.loadtest_deploy_rds(config, environment_config, rds_config)
            rds_secret = self.load_testing_rds.rds_instance.rds_instance.secret.secret_arn
            config["pattern_instances"] = map(
                lambda config_dictionary: DMSIngestion.loadtest_update_dms(config_dictionary, rds_config, rds_secret),
                config["pattern_instances"],
            )
            self.ssm_export("rds-secret-parameter", rds_secret)

        for config_dictionary in config["pattern_instances"]:
            if config_dictionary["region"] == stack.region:
                config_dictionary["resources"].update(
                    {
                        "static_buckets": config["static_buckets"],
                        "dms_certificates": dms_certs,
                        "data_pipe": config_dictionary["data_pipe"],
                        "app_config_base": app_config_base,
                    }
                )
                dms_instance = Guest360DMSIngest(
                    self, construct_id=config["stack_extension"], props=config_dictionary["resources"]
                )
                self.target_kinesis_streams.extend(dms_instance.kinesis_streams)

    @staticmethod
    def loadtest_get_rds_config(config_dir: str, engine_type: str) -> dict:
        rds_config_path = f"{config_dir}/load_test/load_test_rds_{engine_type}.yaml"
        rds_configs = static_config_from_path(rds_config_path)
        for rds_config in rds_configs:
            if rds_config["engine_type"] == engine_type:
                return rds_config
            logger.info("No RDS config found for engine_type: %s - skipping loadtesting RDS creation", engine_type)

    def loadtest_deploy_rds(self, config: dict, environment_config: dict, rds_config: dict) -> None:
        self.load_testing_rds = LoadTestingRDS(
            self,
            construct_id=config["stack_extension"],
            props=rds_config["resources"],
            environment_config=environment_config,
        )

    @staticmethod
    def loadtest_update_dms(config_dictionary: dict, rds_config: dict, rds_secret: str) -> dict:
        config_dictionary["resources"]["source_endpoint"]["settings"]["secrets_manager_secret_id"] = rds_secret
        # ORACLE AWS RDS requires database name.  This value must be 1-8 characters
        if config_dictionary["resources"]["source_endpoint"]["engine_name"] == DMSEngineType.ORACLE:
            config_dictionary["resources"]["source_endpoint"]["database_name"] = rds_config["resources"]["rds"][
                "database_name"
            ]
        if "dms_table_mappings" in rds_config["resources"]:
            for task in config_dictionary["resources"]["dms_repl_task"]:
                task["table_mappings"] = rds_config["resources"]["dms_table_mappings"]
        return config_dictionary

    @staticmethod
    def check_loadtest_env(environment: str, is_static_env: bool) -> bool:
        if environment == "latest" and (not is_static_env):
            return True
        elif environment == "load":
            return True
        else:
            return False
