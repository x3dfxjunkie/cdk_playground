"""
    Class locust user
"""
import json
import logging
import os
from uuid import uuid4


from app.src.load_testing.app.data_mocker.data_mocker_factory import DataMockerFactory
from app.src.load_testing.app.metrics_logger.cw_emf_metrics_logger import Guest360CloudwatchEmfMetricsLogger
from app.src.load_testing.app.sources.source_factory import SourceFactory
from app.src.load_testing.app.targets.exceptions import LoadTestTargetException
from app.src.load_testing.app.targets.target_factory import TargetFactory
from locust import User, constant_throughput, events, task


# Constants
# Need to move this to s config
CONFIG_METRICS_CWAGENT_IP = "0.0.0.0"
CONFIG_METRICS_CWAGENT_PORT = 25888

# environment variables names
ENV_VAR_SCENARIO_CONFIG = "scenario_config"
ENV_VAR_ENVIRONMENT_NAME = "environment"
ENV_VAR_PREFIX_NAME = "prefix"
ENV_VAR_EXECUTION_ID = "EXECUTION_ID"

# config name
CONFIG_INPUT_ENDPOINT_NAME = "endpoint"
CONFIG_INPUT_NAME = "input"
CONFIG_EVALUATION_METRICS_NAME = "metrics"
CONFIG_EVALUATION_TESTS_NAME = "tests"

CONFIG_INPUT_DATA_NAME = "data"
CONFIG_DATA_SCHEMA = "schema"
CONFIG_DATA_SCHEMA_NAME = "schema_name"
CONFIG_DATA_SCHEMA_RESOURCES = "schema_resources"
CONFIG_INPUT_DATA_ACTIVE_INJECTION_NAME = "active_injection"
CONFIG_DATA_LIMIT_RECORDS = "limit_records"
CONFIG_DATA_LIMIT_DURATION = "duration_seconds"
CONFIG_INPUT_DATA_SAMPLES_NAME = "samples"
CONFIG_SOURCE_NAME = "source"
CONFIG_SOURCE_PATH = "path"


CONFIG_DATA_RESOURCES = "schema_resources"
CONFIG_METRICS_NAME = "metrics"
CONFIG_METRICS_NAMESPACE_NAME = "namespace_name"
CONFIG_METRICS_DIMENSIONS_NAME = "dimensions"
CONFIG_METRICS_LOG_GROUP_NAME = "cw_log_group_name"
CONFIG_TYPE_NAME = "type"

CONFIG_OUTPUT_NAME = "output"
CONFIG_DESTINATION_NAME = "destination"
CONFIG_DESTINATION_DB_NAME = "database"
CONFIG_DESTINATION_SCHEMA_NAME = "schema"
CONFIG_DESTINATION_TABLE_NAME = "table"


# runners.HEARTBEAT_DEAD_INTERNAL = -180  # 3 minutes instead of 1 minute, which is the default
# runners.HEARTBEAT_LIVENESS = 10  # default is to make three attempts


CONFIG_TAG_NOT_FOUND_MSG = "Scenario config is not provided"


# pylint: disable=C0103,W0621,W0612
class Guest360VirtualUser(User):
    """
    Class that receives the scenario name and instance the objetcs necesary to run a load test
    """

    abstract = False
    wait_time = constant_throughput(5)
    counter_task_runs = 0

    def __init__(self, env):
        super().__init__(env)
        self.env = env
        self.environment = os.getenv(ENV_VAR_ENVIRONMENT_NAME, "latest")
        self.prefix = os.getenv(ENV_VAR_PREFIX_NAME, "")
        self.execution_id = os.getenv(ENV_VAR_EXECUTION_ID, "-")
        self.scenario_config = json.loads(json.loads(os.getenv(ENV_VAR_SCENARIO_CONFIG, "{}")))
        if self.scenario_config is None:
            raise ValueError(CONFIG_TAG_NOT_FOUND_MSG)

        self.get_metrics_logger()
        self.get_target_from_scenario()
        self.get_data_mocker()

    def get_target_from_scenario(self):
        endpoint_config = self.scenario_config[CONFIG_INPUT_NAME][CONFIG_INPUT_ENDPOINT_NAME]
        endpoint_type = endpoint_config[CONFIG_TYPE_NAME]
        self.target = TargetFactory.get_target(endpoint_type, config=endpoint_config, prefix=self.prefix)

    @property
    def limit_records(self):
        return self.scenario_config[CONFIG_INPUT_NAME][CONFIG_INPUT_DATA_NAME][CONFIG_DATA_LIMIT_RECORDS]

    def get_data_mocker(self):
        self.get_data_contracts_files()
        config_data = self.scenario_config[CONFIG_INPUT_NAME][CONFIG_INPUT_DATA_NAME]
        self.data_mocker = DataMockerFactory.get_data_mocker(**config_data)
        return config_data

    def get_data_contracts_files(self):
        source_config = self.scenario_config[CONFIG_INPUT_NAME][CONFIG_INPUT_DATA_NAME][CONFIG_INPUT_DATA_SAMPLES_NAME]
        source_type = source_config[CONFIG_SOURCE_NAME]
        source_path = source_config[CONFIG_SOURCE_PATH]
        schema_path = self.scenario_config[CONFIG_INPUT_NAME][CONFIG_INPUT_DATA_NAME][CONFIG_DATA_SCHEMA]
        schema_resources = self.scenario_config[CONFIG_INPUT_NAME][CONFIG_INPUT_DATA_NAME][CONFIG_DATA_RESOURCES]

        source = SourceFactory.get_source(source_type, config=source_config, prefix=self.prefix)

        paths_to_download = [source_path, schema_path, schema_resources]
        for path in paths_to_download:
            source.download_file(path)

    def get_destination_from_scenario(self):
        source_config = self.scenario_config[CONFIG_OUTPUT_NAME][CONFIG_DESTINATION_NAME]
        database_name = source_config[CONFIG_DESTINATION_DB_NAME]
        schema_name = source_config[CONFIG_DESTINATION_SCHEMA_NAME]
        table_name = source_config[CONFIG_DESTINATION_TABLE_NAME]
        return (database_name, schema_name, table_name)

    def get_metrics_logger(self):
        namespace = self.scenario_config[CONFIG_METRICS_NAME][CONFIG_METRICS_NAMESPACE_NAME]
        log_group_name = "-".join(
            [self.prefix, self.scenario_config[CONFIG_METRICS_NAME][CONFIG_METRICS_LOG_GROUP_NAME]]
        )
        self.dimensions = self.scenario_config[CONFIG_METRICS_NAME][CONFIG_METRICS_DIMENSIONS_NAME]
        self.dimensions.append({"name": "Execution_Id", "value": self.execution_id})

        self.metrics_logger = Guest360CloudwatchEmfMetricsLogger(
            CONFIG_METRICS_CWAGENT_IP, CONFIG_METRICS_CWAGENT_PORT, namespace, log_group_name
        )

    @task
    def send_event(self):
        if self.__class__.counter_task_runs >= self.limit_records:
            self.env.runner.stop()
            return

        data = self.data_mocker.next()
        database_name, schema_name, table_name = self.get_destination_from_scenario()
        wrapped_data = {
            "id": str(uuid4()),
            "data": data,
            "trace_id": self.execution_id,
            "database_name": database_name,
            "schema_name": schema_name,
            "table_name": table_name,
        }

        # inject trace_id , database, schema, table
        # TBD: this is where wrap the payload in cloudevent in the future
        exception = None

        try:
            # self.target.send_data(data)
            self.target.send_data(wrapped_data)
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
                "dimensions": self.dimensions,
                "metrics_logger": self.metrics_logger,
            }
            events.request.fire(**request_meta)


@events.request.add_listener
def on_request(
    request_type,
    name,
    response_time,
    response_length,
    response,
    exception,
    context,
    **kwargs,
):
    # pylint: disable=unused-argument
    """
    Event handler that get triggered on every request.
    """
    metrics = []
    metrics.append({"name": "event_all", "value": 1, "unit": "Count", "storage_resolution": 60})
    if not exception:
        metrics.append({"name": "events_success", "value": 1, "unit": "Count", "storage_resolution": 60})
    else:
        metrics.append({"name": "events_fail", "value": 1, "unit": "Count", "storage_resolution": 60})
    request_dimensions = [{"name": "target", "value": name}, {"name": "request_type", "value": request_type}]
    kwargs["metrics_logger"].publish(metrics, kwargs["dimensions"] + request_dimensions)
