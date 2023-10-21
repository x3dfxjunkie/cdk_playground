"""
Guest360 sql generator configuration classes
"""
from abc import ABC, abstractmethod
import yaml, os, json
from pathlib import Path
from datetime import datetime
import boto3
from typing import Union, List, Dict
import argparse
from typing import Any


class DataContractConfig:
    """Config Class for data contracts. YAML files"""

    def __init__(
        self,
        ingestion_config: dict,
    ):
        self.class_name = ingestion_config.get("class_name")
        self.data_contract = ingestion_config.get("data_contract")
        self.data_contract_version = ingestion_config.get("data_contract_version")

        self.router_database = ingestion_config.get("router_database")
        self.router_schema = ingestion_config.get("router_schema")
        self.router_table = ingestion_config.get("router_table")
        self.recursive_depth = ingestion_config.get("recursive_depth", 3)

    def to_dict(self):
        return self.__dict__.copy()


# TODO - we'll need this back once most of the config is merged with ingestion config:
# class TableParserConfig:
#     """Config Class for the table parser. YAML files"""

#     def __init__(
#         self,
#         parser_config: dict,
#     ):
#         self.environment = parser_config.get("environment")

#         self.unblobbing_database = parser_config.get("unblobbing_database")
#         self.unblobbing_schema_prefix = parser_config.get("unblobbing_schema_prefix")

#         self.managed_artifacts_database = parser_config.get("managed_artifacts_database")
#         self.managed_artifacts_schema = parser_config.get("managed_artifacts_schema")

#         self.data_warehouse = parser_config.get("data_warehouse")
#         self.external_stage = parser_config.get("external_stage")

#         self.data_contracts = parser_config.get("data_contracts")


class ConfigLoader(ABC):
    def load_config(self):
        with self.config_path.open(encoding="utf8") as file:
            self.config_data = yaml.safe_load(file)

    @abstractmethod
    def get_config(
        self,
    ):
        pass


class SnowflakeConfig:
    """Config Class for the table parser. YAML files"""

    def __init__(
        self,
        snowflake_config: dict,
    ):
        self.snowflake_config = snowflake_config

        self.type = snowflake_config.get("type")

        self.default_router_database = snowflake_config.get("default_router_database")
        self.unblobbing_database = snowflake_config.get("bronze_database")
        self.unblobbing_schema_prefix = snowflake_config.get("bronze_schema_prefix")

        self.managed_artifacts_database = snowflake_config.get("managed_artifacts_database")
        self.managed_artifacts_schema = snowflake_config.get("managed_artifacts_schema")

        self.data_warehouse = snowflake_config.get("data_warehouse")
        self.external_stage = snowflake_config.get("external_stage")

        self.recreate_if_exists: dict[str, bool] = snowflake_config.get("recreate_if_exists", [])

        self.environments: list[dict[str, Union[str, bool]]] = snowflake_config.get("environments", [])

        self.timestamp_validation: dict[str, Any] = snowflake_config.get("timestamp_validation", [])

    @property
    def environments_to_process_s3(self) -> list:
        """Returns the list of environments to be processed."""
        return [env for env in self.environments if env.get("is_uploaded_to_s3", False)]

    @property
    def data_contracts(self) -> list[str]:
        contracts = self.snowflake_config.get("data_contracts", [])
        return [contract.get("name", "") for contract in contracts if "name" in contract]

    @property
    def contracts2skip(self) -> list[str]:
        contracts = self.snowflake_config.get("contracts2skip", [])
        return [contract.get("name", "") for contract in contracts if "name" in contract]


class SchemaDataConf:
    def __init__(
        self,
        snowflake_config: dict,
    ):
        for schema_val in snowflake_config["values"]:
            val = list(schema_val.values())[0]
            if not val:
                val = ""
            setattr(self, *schema_val.keys(), val)


class SnowflakeConfigLoader(ConfigLoader):
    """Config Class for Snowflake loader"""

    def __init__(self, config_path):
        self.config_path = config_path
        self.snowflake_config = None

    def load_config(self):
        super().load_config()
        self.snowflake_config = SnowflakeConfig(self.config_data["pattern_instances"][0]["data_pipe"]["target"][0])

    def get_config(self):
        if self.snowflake_config is None:
            self.load_config()
        return self.snowflake_config


class ContractTrackerBase(ABC):
    """Abstract Base Class for contract tracker"""

    def __init__(self, contract_tracker_directory: str):
        self.contract_tracker_directory = contract_tracker_directory

    @abstractmethod
    def load_existing_contracts(self) -> dict:
        """Load existing contracts from the tracker file"""
        pass

    @abstractmethod
    def save_contracts(self, contracts: dict) -> None:
        """Save updated contracts to the tracker file"""
        pass


class ContractTrackerS3Handler(ContractTrackerBase):
    """
    Handles loading and saving of contracts using S3.

    Attributes:
        environment_name (str): Name of the environment.
        s3_bucket (str): The S3 bucket path.
        s3_client: Boto3 S3 client.
        s3_key (str): Object key in the S3 bucket.
    """

    def __init__(self, base_directory: Path, environment_name: str):
        """
        Initializes the ContractTrackerS3Handler.

        Args:
            environment_name (str): Name of the environment.
        """
        self.environment_name = environment_name.lower()
        self.s3_bucket = "lst-use1-guest360-build-pipeline-bucket"
        self.s3_key = f"CodeBuild/GeneratedSQL/{self.environment_name}.yaml"
        self.session = boto3.Session()
        self.s3_client = self.session.client("s3")

    def load_existing_contracts(self) -> dict:
        """
        Loads existing contracts from S3.

        Returns:
            dict: A dictionary containing the contracts.
        """
        try:
            response = self.s3_client.get_object(Bucket=self.s3_bucket, Key=self.s3_key)
            file_content = response["Body"].read().decode("utf-8")
            existing_contracts = yaml.safe_load(file_content)
            if existing_contracts is None or "contracts" not in existing_contracts:
                existing_contracts = {"contracts": []}
            return existing_contracts
        except self.s3_client.exceptions.NoSuchKey:
            return {"contracts": []}

    def save_contracts(self, contracts: dict) -> None:
        """
        Saves contracts to S3.

        Args:
            contracts (dict): A dictionary containing the contracts to save.
        """
        contracts_str = yaml.dump(contracts)
        self.s3_client.put_object(Bucket=self.s3_bucket, Key=self.s3_key, Body=contracts_str)


class ContractTrackerFileHandler(ContractTrackerBase):
    """
    Handles loading and saving of contracts using a yaml file.

    Attributes:
        environment_name (str): Name of the environment.
        base_directory (Path): Base directory for the contracts.
        file_path (Path): Path to the yaml file for a specific environment.
    """

    def __init__(self, base_directory: Path, environment_name: str):
        """
        Initializes the ContractTrackerFileHandler.

        Args:
            base_directory (Path): Base directory for the contracts.
            environment_name (str): Name of the environment.
        """

        self.environment_name = environment_name.lower()  # Ensure environment_name is lowercase
        self.base_directory = Path(base_directory)
        self.file_path = self.base_directory / f"{self.environment_name}.yaml"  # Use lowercase filename
        super().__init__(str(self.file_path))

    def load_existing_contracts(self) -> dict:
        """
        Loads existing contracts from a yaml file.

        Returns:
            dict: A dictionary containing the contracts.
        """

        if not self.file_path.exists():
            return {"contracts": []}
        with open(self.contract_tracker_directory, "r") as file:
            existing_contracts = yaml.safe_load(file)
        if existing_contracts is None or "contracts" not in existing_contracts:
            existing_contracts = {"contracts": []}
        return existing_contracts

    def save_contracts(self, contracts: dict) -> None:
        """
        Saves contracts to a yaml file.

        Args:
            contracts (dict): A dictionary containing the contracts to save.

        Returns:
            None: This function doesn't return any value but saves the contracts to a yaml file.
        """

        with open(self.contract_tracker_directory, "w") as file:
            yaml.dump(contracts, file)


class CustomJSONEncoder(json.JSONEncoder):
    """
    Custom JSON Encoder to handle specific object types like datetime and sets.
    """

    def default(self, obj):
        """
        Overrides the default JSON encoding behavior for certain object types.

        Args:
            obj: The object to encode.

        Returns:
            Encoded object suitable for JSON serialization.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, set):
            return list(obj)
        return super().default(obj)


class SchemaConfLoader(ConfigLoader):
    def __init__(self, config_path):
        self.config_path = config_path
        self.schema_config = None

    def load_config(self):
        super().load_config()
        self.schema_config = SchemaDataConf(
            self.config_data["pattern_instances"][0]["data_schema_generation"]["static_info"]
        )

    def get_config(self):
        if self.schema_config is None:
            self.load_config()
        return self.schema_config
