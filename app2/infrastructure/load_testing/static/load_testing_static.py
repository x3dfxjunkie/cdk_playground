"""Loadtesting Framework Stack"""
import logging
import os
import sys

from app.guest360_constructs.load_testing.static.load_testing_static import LoadTestingStatic
from app.infrastructure.workstream_stack import WorkstreamStack
from app.infrastructure.reliability.enable_stack import DeployFlag

from app.src.utils.feature_flag.feature_flag import FeatureFlag
from app.guest360_constructs.load_testing.kinesis.load_testing_kinesis_ingest import LoadTestingKinesisIngest
from app.guest360_constructs.load_testing.load_testing_dms import LoadTestingDmsRdsIngest

from app.src.reliability.Guest360ConfigInfra.assist import config_from_path
from aws_cdk import Stack, Tags
from cdk_nag import NagSuppressions
from app.src.reliability.utils import StackName

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Load_testing_static | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class LoadTestingStaticStack(WorkstreamStack):
    """Class for build LoadTestingStatic stack from LoadtestingStatic Construct
    guest360_constructs/load_testing/load_testing_static.py
    all the configurations are loaded from ./config/environment/*.yaml
    """

    def __init__(
        self,
        scope: Stack,
        construct_id: str,
        environment_config: dict,  # pylint: disable=unused-argument
        dms_stack_extension: list,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)
        environment = self.node.try_get_context("environment").lower()
        prefix = self.node.try_get_context("prefix")
        Tags.of(self).add("prefix", prefix)

        # pathing
        full_path = os.path.realpath(__file__)
        config_dir = f"{os.path.dirname(full_path)}/../config"

        loadtesting_config_path = f"{config_dir}/{environment}/static/*_static.yaml"

        # Load the configuration file(s)
        try:
            loaded_loadtesting_configs = config_from_path(loadtesting_config_path)
        except Exception as e:  # pylint: disable=broad-except
            print(f"Error loading the configuration file {loadtesting_config_path}, Error:{e}")

        # Deploy all Construct instances
        for loadtesting_config in loaded_loadtesting_configs:
            config = loadtesting_config["stack_config"]

            # log the current stack_extension for potential debugging...
            logger.debug(
                "Passing configuration to loadtesting stack: TYPE %s NAME %s",
                config["resources"],
                config["stack_extension"],
            )
            if (
                environment not in ["local", "prod"] and config["region"] == stack.region
            ):  # and prefix == "lst-use1-guest360":
                self.load_testing_static = LoadTestingStatic(  # pylint: disable=unused-variable
                    self,
                    construct_id=config["stack_extension"],
                    props=config["resources"],
                    environment_config=environment_config,
                )

                stack_path = self.node.try_get_context("stack_path")
                config_path = f"{stack_path}/app/configs/{environment}-infra-feature-flags.yaml"

                if DeployFlag.is_stack_enabled(self, "LoadTesting/KinesisIngest"):
                    # Deploy LoadTestKinesisIngestStack if is enabled
                    self.loadtest_deploy_k2k(environment_config, config_dir)

                with FeatureFlag(environment, "load_testing.dms_ingest", config_path) as dms_ingest_flag:
                    if dms_ingest_flag:
                        self.loadtest_deploy_dms(environment_config, config_dir, dms_stack_extension)

        # Nags

        NagSuppressions.add_stack_suppressions(
            self,
            [
                {"id": "AwsSolutions-IAM5", "reason": "CDK lambda BucketNotificationsHandler"},
                {"id": "AwsSolutions-IAM4", "reason": "Managed policies are ok for BucketNotificationsHandler"},
                {
                    "id": "AwsSolutions-L1",
                    "reason": "We need a specific runtime version",
                },
            ],
        )

    def loadtest_deploy_k2k(self, environment_config: dict, config_dir: str) -> None:
        """
            Method that deploys the resources of KinesisIngest construct
        Args:
            environment_config (dict): environment configuration
            config_dir (str): directory to load the kinesis ingest configuration file
        """
        load_testing_k2k_config = self.loadtest_get_kinesis_ingest_config(config_dir)
        # Deploy LoadTestKinesisIngest
        stack_extension = load_testing_k2k_config["stack_extension"]
        LoadTestingKinesisIngest(
            self,
            construct_id=stack_extension,
            props=load_testing_k2k_config["resources"],
            load_test_static=self.load_testing_static,
            environment_config=environment_config,
        )

        NagSuppressions.add_stack_suppressions(
            self,
            [
                {"id": "AwsSolutions-IAM5", "reason": "CDK lambda BucketNotificationsHandler"},
            ],
        )

    def loadtest_get_kinesis_ingest_config(self, config_dir: str) -> dict:
        """
            Method that returns the load test kinesis ingest configuration
        Args:
            config_dir (str): directory to load the kinesis ingest configuration file

        Returns:
            dict: Dictionary with the configuration of the load test kinesis ingest
        """
        k2k_config_file = f"{config_dir}/load_test_kinesis_ingest.yaml"
        k2k_config = config_from_path(k2k_config_file)
        return k2k_config[0]["stack_config"]

    def loadtest_deploy_dms(self, environment_config: dict, config_dir: str, dms_stack_extension: list) -> None:
        load_testing_dms_config = self.loadtest_get_dms_ingest_config(config_dir)

        stack_extension = load_testing_dms_config["stack_extension"]
        LoadTestingDmsRdsIngest(
            self,
            construct_id=stack_extension,
            props=load_testing_dms_config["resources"],
            load_test_static=self.load_testing_static,
            environment_config=environment_config,
            dms_stack_extension=dms_stack_extension,
        )

    def loadtest_get_dms_ingest_config(self, config_dir: str) -> dict:
        dms_config_file = f"{config_dir}/load_test_dms_ingest.yaml"
        dms_config = config_from_path(dms_config_file)
        return dms_config[0]["stack_config"]
