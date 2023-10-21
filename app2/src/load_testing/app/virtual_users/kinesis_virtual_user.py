"""
    Class locust user
"""
import os
import json
from app.src.load_testing.app.data_mocker.data_mocker_factory import DataMockerFactory
from app.src.load_testing.app.targets.target_factory import PatternType
from app.src.load_testing.app.targets.exceptions import LoadTestTargetException
from app.src.load_testing.app.targets.target_factory import TargetFactory
from app.src.load_testing.app.virtual_users.appconfig_utils.utils import AppConfigUtils
from app.src.load_testing.app.virtual_users.virtual_user_utils.utils import VirtualUserUtils
from locust import User, constant_throughput, events, task


# environment variables names
ENV_VAR_SCENARIO_CONFIG = "scenario_config"
ENV_VAR_ENVIRONMENT_NAME = "environment"
ENV_VAR_PREFIX_NAME = "prefix"
ENV_VAR_EXECUTION_ID = "EXECUTION_ID"
ENV_VAR_LOCUST_RUN_TIME = "LOCUST_RUN_TIME"
ENV_VAR_LIMIT_RECORDS = "limit_records"
ENV_VAR_APP_CONFIG = "app_config"
ENV_VAR_SUFFIX_NAME = "suffix"
ENV_VAR_ENDPOINT_TYPE = "endpoint_type"

CONFIG_REGION_NAME = "region"
CONFIG_STREAM_NAME = "stream_name"
ENV_VAR_REGION_NAME = "region"
CONFIG_ENVIRONMENT_NOT_FOUND_MSG = "Environment is not provided"


# pylint: disable=C0103,W0621,W0612,E1121
class KinesisVirtualUser(User):
    """
    Class that receives the scenario name and instance the objects necessary to run a load test
    """

    abstract = False
    wait_time = constant_throughput(5)
    counter_task_runs = 0

    def __init__(self, env):
        super().__init__(env)
        self.env = env
        self.environment = os.getenv(ENV_VAR_ENVIRONMENT_NAME)
        if self.environment is None:
            self.env.runner.quit()
            raise ValueError(CONFIG_ENVIRONMENT_NOT_FOUND_MSG)
        self.prefix = os.getenv(ENV_VAR_PREFIX_NAME, "")
        self.is_time_mode = len(os.getenv(ENV_VAR_LOCUST_RUN_TIME, "")) > 0
        self.suffix = os.getenv(ENV_VAR_SUFFIX_NAME, "kinesis-dmz")
        self.limit_records = int(os.getenv(ENV_VAR_LIMIT_RECORDS, "100"))
        self.execution_id = os.getenv(ENV_VAR_EXECUTION_ID, "-")
        self.appconfig = os.getenv(ENV_VAR_APP_CONFIG, "-")
        self.region = os.getenv(ENV_VAR_REGION_NAME, "us-east-1")
        self.config_data_mocker = VirtualUserUtils.get_config(
            pattern_type=PatternType.PATTERN_TYPE_KINESIS,
            key_config_name="data_mocker",
        )

        self.app_config = AppConfigUtils(self.appconfig)
        self.get_target()
        self.get_data_mocker()

    def get_target(self) -> None:
        endpoint_config = {
            CONFIG_REGION_NAME: self.region,
            CONFIG_STREAM_NAME: self.app_config.kinesis_target_name(self.suffix),
        }
        self.target = TargetFactory.get_target(
            PatternType.PATTERN_TYPE_KINESIS,
            config=endpoint_config,
            prefix=self.prefix,
        )

    def get_data_mocker(self) -> None:
        self.data_mocker = DataMockerFactory.get_data_mocker(
            [{**item, **self.config_data_mocker} for item in self.app_config.data_contract_list()]
        )

    @task
    def send_event(self):
        if not self.is_time_mode and self.__class__.counter_task_runs >= self.limit_records:
            self.env.runner.quit()
            return

        data = self.data_mocker.next()

        exception = None

        try:
            [self.target.send_data(json.loads(item)) for item in data]
        except LoadTestTargetException as e:
            exception = str(e)
        finally:
            self.__class__.counter_task_runs += 1
            request_meta = {
                "name": self.target.target_type,
                "request_type": "send_event",
                "response_time": 0,  # not used
                "response_length": 0,  # not used
                "response": "",  # not used
                "exception": exception,
                "context": self,
                # "dimensions": self.dimensions,
                # "metrics_logger": self.metrics_logger,
            }
            events.request.fire(**request_meta)
