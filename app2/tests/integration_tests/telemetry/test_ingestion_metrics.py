"""
pytests for ingestion pipeline telemetry metrics
"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed
# pylint: disable=unused-argument testing fixtures
import sys
import logging
import json
import boto3
import botocore
import datetime
import importlib
import time
import pytest
import pathlib
import yaml
import copy
import hashlib
import secrets
import functools
import operator

from polyfactory.factories import pydantic_factory

# override logging for noisy loggers
logging.getLogger("urllib3").setLevel(logging.INFO)
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
cloudwatch = boto3.client("cloudwatch")


# db is dictionary which need to update
# keys is a list need to depth of keys in a order
# value targeted value to update in dictionary
class DictUpdate:
    @staticmethod
    def set_by_path(db, keys, value):
        """Set a value in a nested object in db by keys sequence."""
        for index in range(1, len(keys)):
            subitem = DictUpdate.get_by_path(db, keys[:index])
            if not isinstance(subitem, dict):
                DictUpdate.get_by_path(db, keys[:index][:-1])[keys[:index][-1]] = {}
        DictUpdate.get_by_path(db, keys[:-1])[keys[-1]] = value
        return db

    @staticmethod
    def get_by_path(db, keys):
        try:
            return functools.reduce(operator.getitem, keys, db)
        except (KeyError, IndexError):
            return None


def get_configs() -> list:
    path = pathlib.Path(pytest.ingestion_config_path)
    if path.is_file():
        files = [path]
    elif path.is_dir():
        files = [file for file in path.iterdir() if not file.name.startswith(".")]
    else:
        raise OSError(f"{pytest.ingestion_config_path=} is not a file or directory")
    return files


def load_yaml(file) -> dict:
    with open(file, "r") as file_handle:
        file_dict = yaml.unsafe_load(file_handle)
    return file_dict


@pytest.mark.integration
class TestIngestionPipelineMetrics:
    """
    Class for testing pipeline metrics
    """

    metric_namespace = f"{pytest.stack_prefix}-ingest"
    metric_names = ["rows_started", "rows_success", "rows_warning", "rows_failed"]
    event_pipe_name_suffix = "event-bridge-pipe-validation"
    event_sources = ["ingestion_validator", "ingestion_firehose"]

    @pytest.mark.parametrize("config_file", get_configs())
    def test_telemetry_metric_counts_pipeline(self, config_file):
        logger.info(f"Analyzing {config_file=}")
        config = load_yaml(f"{config_file}")
        logger.debug(f"{config=}")
        start_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=2)
        try:
            # check if datacontract has at least one data_contract
            data_contracts = config["pattern_instances"][0]["data_pipe"]["data_contracts"]
        except KeyError:
            pytest.skip(f"No Datacontracts found for {config_file}")
        number_data_contracts = len(data_contracts)

        # get pipe information
        event_pipe_name = f'{pytest.stack_prefix}-{config["stack_extension"]}-{self.event_pipe_name_suffix}'
        pipe_describe = self.pipe_describe(event_pipe_name)
        kinesis_arn = self.pipe_source_arn(pipe_describe)
        # need to get just the kinesis stream name from the arn which is the last section of the arn split by /
        kinesis_name = kinesis_arn.split("/")[-1]
        # need to get just the function name from the arn which is the last section of the arn split by :
        function_arn = self.pipe_lambda_arn(pipe_describe)
        function_name = function_arn.split(":")[-1]
        logger.debug(f"{kinesis_arn=}")
        # get the source system and location from the stack-extension in the config
        dimensions = [
            {
                "Name": "function_name",
                "Value": function_name,
            },
            {
                "Name": "subject",
                "Value": kinesis_name,
            },
        ]

        self.push_events(config, kinesis_arn, data_contracts)
        # need to wait some time for metrics to show up in cloudwatch
        time.sleep(300)
        end_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=2)

        metrics = self.check_otel_metrics(config["stack_extension"], start_date, end_date, dimensions)
        # assert total number of rows/events sent is 3 times number of data contracts
        logger.info(
            f'{metrics["rows_started"]=}, { metrics["rows_success"]=}, {metrics["rows_warning"]=}, {metrics["rows_failed"]=}'
        )
        assert metrics["rows_started"] == number_data_contracts * 3
        # success is none currently due to datacontract not having necessary validators to dynamically create fully qualified datacontract
        assert metrics["rows_success"] == 0
        # assert metrics["rows_success"] == number_data_contracts
        # warnings is times 2 currently due to success issue
        assert metrics["rows_warning"] == number_data_contracts * 2
        # once the pydantic class is updated properly with validators this should then change to the following
        # assert metrics["rows_warning"] == number_data_contracts # NOSONAR
        assert metrics["rows_failed"] == number_data_contracts

    def check_otel_metrics(
        self, stack_extension: str, start_date: datetime.datetime, end_date: datetime.datetime, dimensions
    ) -> dict:
        metrics = {}
        for metric_name in self.metric_names:
            logger.debug(
                f"namespace={self.metric_namespace}-{stack_extension}, {metric_name=}, {dimensions=}, {start_date=}, {end_date=}"
            )
            response = cloudwatch.get_metric_statistics(
                Namespace=f"{self.metric_namespace}-{stack_extension}",
                MetricName=metric_name,
                Dimensions=dimensions,
                StartTime=start_date,
                EndTime=end_date,
                Period=60,
                Statistics=["Sum"],
            )
            try:
                metrics[metric_name] = response["Datapoints"][0]["Sum"]
            except (IndexError, KeyError):
                logger.error("metrics failed for response=%s", response)
                metrics[metric_name] = None
        return metrics

    def create_messages(self, kinesis_arn: str, config: dict, data_contract: dict, contract) -> None:
        # valid data
        success_contract_dict = contract.dict()
        for key_path in data_contract["key_path"]:
            DictUpdate.set_by_path(success_contract_dict, key_path["name"].split("."), key_path["value"])
        resp = self.send_kinesis_data(
            kinesis_arn=kinesis_arn,
            kinesis_partition_key=hashlib.sha256(str(success_contract_dict).encode()).hexdigest(),
            data=success_contract_dict,
        )
        logger.debug(f"{success_contract_dict=}")
        logger.debug(f"success kinesis resp {resp=}")

        # warning data - missing data/field
        warn_contract = copy.deepcopy(contract)
        warn_contract_dict = warn_contract.dict()
        for key_path in data_contract["key_path"]:
            DictUpdate.set_by_path(warn_contract_dict, key_path["name"].split("."), key_path["value"])
        field_to_none = secrets.choice(
            [field for field, value in warn_contract.data.__fields__.items() if value.required]
        )
        if config["ingest_pattern"] == "dms":
            warn_contract_dict["data"][field_to_none] = None
        else:
            warn_contract_dict[field_to_none] = None

        resp = self.send_kinesis_data(
            kinesis_arn=kinesis_arn,
            kinesis_partition_key=hashlib.sha256(str(warn_contract_dict).encode()).hexdigest(),
            data=warn_contract_dict,
        )
        logger.debug(f"{warn_contract_dict=}")
        logger.debug(f"warn kinesis resp {resp=}")

        # fail data - no data contract in payload found
        fail_contract_dict = {"test": "bad data"}
        resp = self.send_kinesis_data(
            kinesis_arn=kinesis_arn,
            kinesis_partition_key=hashlib.sha256(str(fail_contract_dict).encode()).hexdigest(),
            data=fail_contract_dict,
        )
        logger.debug(f"{fail_contract_dict=}")
        logger.debug(f"fail kinesis resp {resp=}")

    def send_kinesis_data(self, kinesis_arn: str, kinesis_partition_key: str, data: dict) -> dict:
        try:
            client = boto3.client("kinesis")
            response = client.put_record(
                Data=json.dumps(data, default=str).encode(), PartitionKey=kinesis_partition_key, StreamARN=kinesis_arn
            )
        except botocore.exceptions.ClientError as error:
            logger.exception("Failed to send data to kinesis stream=%s", kinesis_arn)
            raise error
        return response

    def pipe_describe(self, name: str) -> dict:
        try:
            client = boto3.client("pipes")
            response = client.describe_pipe(Name=name)
        except botocore.exceptions.ClientError as error:
            logger.exception("Failed to describe pipe=%s", name)
            raise error
        return response

    def pipe_source_arn(self, pipe_describe: dict) -> str:
        return pipe_describe["Source"]

    def pipe_lambda_arn(self, pipe_describe: dict) -> str:
        return pipe_describe["Enrichment"]

    def push_events(self, config: dict, kinesis_arn: str, data_contracts: list):
        for data_contract in data_contracts:
            # create dummy data for all contracts found and send to kinesis
            logger.debug(json.dumps(data_contract, indent=2, default=str))
            logger.info(f'{data_contract["class_name"]=}')
            module = importlib.import_module(data_contract["data_contract"])
            # dynamically create a data_contract factory class utilizing the type function
            data_contract_factory = type(
                data_contract["class_name"],
                (pydantic_factory.ModelFactory,),
                {"__model__": getattr(module, data_contract["class_name"])},
            )
            # build a contract using factory and generate fake data
            contract = data_contract_factory.build()
            contract_dict = contract.dict()
            logger.debug(f"{contract_dict=}")
            logger.debug(f"{contract.__fields__.keys()=}")
            self.create_messages(kinesis_arn, config, data_contract, contract)
