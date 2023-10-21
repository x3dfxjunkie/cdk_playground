"""
This module provides a locust user task class for testing using the DMS pattern.
"""

import os
from locust import User, constant_throughput, events, task
from app.src.load_testing.app.data_mocker.data_mocker_factory import DataMockerFactory
from app.src.load_testing.app.targets.target_factory import PatternType
from app.src.load_testing.app.targets.exceptions import LoadTestTargetException
from app.src.load_testing.app.targets.target_factory import TargetFactory
from app.src.load_testing.app.virtual_users.appconfig_utils.utils import AppConfigUtils
from app.src.load_testing.app.virtual_users.virtual_user_utils.utils import VirtualUserUtils


# environment variables names
ENV_VAR_SCENARIO_CONFIG = "scenario_config"
ENV_VAR_DATA_CONTRACTS_NAME = "app_config"
ENV_VAR_SEC_MAN_NAME = "secret_name"
ENV_VAR_EXECUTION_ID = "EXECUTION_ID"
ENV_VAR_LIMIT_RECORDS = "limit_records"
ENV_VAR_PREFIX_NAME = "prefix"
ENV_VAR_STACK_EXTENSION = "stack_extension"

ENV_VAR_LOCUST_RUN_TIME = "LOCUST_RUN_TIME"
CONFIG_REGION_NAME = "region"
CONFIG_ENVIRONMENT_NOT_FOUND_MSG = "data contract var is not provided"


class DMSVirtualUser(User):
    """
    Represents a virtual user locust task that sends data using the DMS pattern for load testing.

    Attributes:
        data_contracts (str): Data contracts environment variable.
        limit_records (int): Limit for records to be sent.
        secmanager (str): Name of the secret manager.
        app_config (AppConfigUtils): App configuration utility in order to get data contracts list.
        sec_manager (dict): Secret manager details.
        target (object): Target to which data is sent.
        data_mocker (object): Mocks data using the data contracts.
    """

    # locust variables
    abstract = False
    wait_time = constant_throughput(5)
    counter_task_runs = 0

    # pylint: disable=E1123
    def __init__(self, env):
        super().__init__(env)
        self.env = env
        self.data_contracts = os.getenv(ENV_VAR_DATA_CONTRACTS_NAME)
        if self.data_contracts is None:
            raise ValueError(CONFIG_ENVIRONMENT_NOT_FOUND_MSG)
        self.limit_records = int(os.getenv(ENV_VAR_LIMIT_RECORDS, "100"))
        self.prefix = os.getenv(ENV_VAR_PREFIX_NAME, "")
        self.stack_extension = os.getenv(ENV_VAR_STACK_EXTENSION, "")
        self.stack_ingestion_name = f"{self.prefix}-ingest-{self.stack_extension}"
        self.parameter_name = f"/{self.prefix}/{self.stack_ingestion_name}/rds-secret-parameter"
        self.secmanager = VirtualUserUtils.get_parameter(self.parameter_name)
        self.is_time_mode = len(os.getenv(ENV_VAR_LOCUST_RUN_TIME, "")) > 0

        self.app_config = AppConfigUtils(self.data_contracts)
        self.sec_manager = VirtualUserUtils.get_secret(
            self.secmanager,
            pattern_type=PatternType.PATTERN_TYPE_DMS,
        )
        self.config_data_mocker = VirtualUserUtils.get_config(
            pattern_type=PatternType.PATTERN_TYPE_DMS,
            key_config_name="data_mocker",
        )
        self.sql_config_transaction_generator = VirtualUserUtils.get_config(
            pattern_type=PatternType.PATTERN_TYPE_DMS,
            key_config_name="sql_transaction_generator",
        )
        self.get_target()
        self.get_data_mocker()

    def get_target(self) -> None:
        """
        Set the DMS pattern for the user locust task.
        """
        self.target = TargetFactory.get_target(
            endpoint_type=PatternType.PATTERN_TYPE_DMS,
            data_contract_batch=self.app_config.data_contract_list(),
            **self.sec_manager,
            **self.sql_config_transaction_generator,
        )
        self.target.create_sql_table()

    def get_data_mocker(self) -> None:
        """
        Set the data mocker for the user locust task.
        """
        self.data_mocker = DataMockerFactory.get_data_mocker(
            [{**item, **self.config_data_mocker} for item in self.app_config.data_contract_list()]
        )

    @task
    def send_event(self):
        """
        Send an event to the target. Stops sending after reaching the limit_records.
        """
        if not self.is_time_mode and self.__class__.counter_task_runs >= self.limit_records:
            self.env.runner.quit()
            return

        data = self.data_mocker.next()

        exception = None

        try:
            self.target.send_batch(data)
        except LoadTestTargetException as e:
            exception = str(e)
        finally:
            self.__class__.counter_task_runs += 1
            request_meta = {
                "name": self.target.target_type,
                "request_type": "send_event",
                "response_time": 0,
                "response_length": 0,
                "response": "",
                "exception": exception,
                "context": self,
            }
            events.request.fire(**request_meta)
