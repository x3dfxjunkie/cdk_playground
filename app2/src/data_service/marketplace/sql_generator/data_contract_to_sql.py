"""
Guest360 sql generator main file
"""
import os
import yaml
import json
from typing import List, Dict
from functools import partial
from pathlib import Path
from datetime import datetime
import shutil
from typing import Union
import hashlib
import importlib
import logging, sys
import argparse


import re
from app.src.data_service.marketplace.sql_generator.schema_generator import generate_schema_sql_files
from app.src.data_service.marketplace.sql_generator.function_generator import generate_sql_function
from app.src.data_service.marketplace.sql_generator.generator_config import (
    DataContractConfig,
    SnowflakeConfig,
    SnowflakeConfigLoader,
    ContractTrackerFileHandler,
    ContractTrackerS3Handler,
    CustomJSONEncoder,
)
from app.src.data_service.marketplace.sql_generator.helpers import (
    render_sql_template,
    to_snake_case,
    write_sql_file,
    load_data_contracts_config,
    load_snowflake_config,
    create_folders_tree,
    unblobbing_schema_name,
    raw_schema_name,
    default_managed_artifact_warehouse,
    sql_section_header,
)
from app.src.data_service.marketplace.sql_generator.table_field import LANDING_TABLE_FIELDS
from app.src.data_service.marketplace.sql_generator.table import UnblobbedTable
from app.src.data_service.marketplace.sql_generator.table_parser import (
    TableParser,
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def contract_to_sql(
    table_parser_config: SnowflakeConfig,
    data_contract_config: DataContractConfig,
    environment: dict[str, str],
    parser: TableParser,
    create_landing: bool = False,
) -> str:
    """
    Generates DDL for bronze level artifacts (unblob table, streams, tasks, tags) given a data contract.

    Args:
        config_parser (ConfigTableParser): Configuration for the parser.  Contains DB, schema, and table details for resources being generated.
        data_contract_config (ConfigDataContract): Ingestion level config which contains information about DB table name to use for both landing and bronze.
        parser: The table parser instance.
        create_landing: Passing argument for landing table.
    """
    table_parser_config.table_name = to_snake_case(data_contract_config.router_table)
    external_stage = table_parser_config.external_stage
    timestamp_validation = table_parser_config.timestamp_validation
    out_str = ""
    suspend_tasks = ""
    resume_tasks = ""

    notification_integration_config = get_notification_integration(environment["name"].lower())

    error_integration_name = notification_integration_config["notification_name"]

    cloud_event_fields = [field for field in LANDING_TABLE_FIELDS if field["cloudevent"] == True]

    for table in parser.get_tables():
        table_database = table_parser_config.unblobbing_database
        table_schema = unblobbing_schema_name(data_contract_config.router_schema)
        landing_database = data_contract_config.router_database
        landing_schema = data_contract_config.router_schema
        managed_artifacts_database = table_parser_config.managed_artifacts_database
        managed_artifacts_schema = table_parser_config.managed_artifacts_schema
        managed_artifacts_prefix = raw_schema_name(data_contract_config.router_schema)
        warehouse = default_managed_artifact_warehouse(
            environment=environment, managed_artifacts_database=managed_artifacts_database
        )

        p_render_sql_template = partial(
            render_sql_template,
            table=table,
            environment=environment["name"],
            landing_database=landing_database,
            landing_schema=landing_schema,
            external_stage=external_stage,
            schedule="1 minute",
            error_integration_name=error_integration_name,
            timestamp_validation=timestamp_validation,
        )

        if isinstance(table, UnblobbedTable):
            create_template = "create_table.sql"
            stream_template = "create_stream.sql"
            task_template = "create_task.sql"
            if create_landing:
                out_str += sql_section_header("LANDING TABLE")
                out_str += p_render_sql_template(
                    template_name="create_landing_table.sql",
                    table_database=landing_database,
                    table_schema=landing_schema,
                    cloud_event_fields=cloud_event_fields,
                    recreate_if_exists=table_parser_config.recreate_if_exists["landing_table"],
                )

                out_str += sql_section_header("LANDING PIPE")
                out_str += p_render_sql_template(
                    template_name="create_landing_pipe.sql",
                    pipe_database=managed_artifacts_database,
                    pipe_schema=managed_artifacts_schema,
                    pipe_prefix=managed_artifacts_prefix,
                    cloud_event_fields=cloud_event_fields,
                    recreate_if_exists=table_parser_config.recreate_if_exists["landing_table_pipe"],
                )

        else:
            create_template = "create_child_table.sql"
            stream_template = "create_child_stream.sql"
            task_template = "create_child_task.sql"

        out_str += sql_section_header("BRONZE TABLE")
        out_str += p_render_sql_template(
            template_name=create_template,
            table_database=table_database,
            table_schema=table_schema,
        )
        out_str += p_render_sql_template(
            template_name="pk_notnull_constraint.sql",
            table_database=table_database,
            table_schema=table_schema,
        )

        # TODO - disable tags until Einav's team finalizes requirements to save processing time:
        # out_str += sql_section_header("BRONZE TABLE TAGS")
        # out_str += p_render_sql_template(
        #     template_name="create_tags.sql",
        #     tag_database=managed_artifacts_database,
        #     tag_schema=managed_artifacts_schema,
        # )

        # out_str += p_render_sql_template(
        #     template_name="setup_tags.sql",
        #     table_database=table_database,
        #     table_schema=table_schema,
        #     tag_database=managed_artifacts_database,
        #     tag_schema=managed_artifacts_schema,
        # )

        out_str += sql_section_header("BRONZE TABLE COMMENTS")
        out_str += p_render_sql_template(
            template_name="setup_column_comments.sql",
            table_database=table_database,
            table_schema=table_schema,
            tag_database=managed_artifacts_database,
            tag_schema=managed_artifacts_schema,
        )

        out_str += sql_section_header("BRONZE STREAM")
        out_str += p_render_sql_template(
            template_name=stream_template,
            stream_database=managed_artifacts_database,
            stream_schema=managed_artifacts_schema,
            stream_prefix=managed_artifacts_prefix,
        )

        out_str += sql_section_header("BRONZE TASK")
        out_str += p_render_sql_template(
            template_name=task_template,
            stream_database=managed_artifacts_database,
            stream_schema=managed_artifacts_schema,
            stream_prefix=managed_artifacts_prefix,
            managed_artifacts_prefix=managed_artifacts_prefix,
            task_database=managed_artifacts_database,
            task_schema=managed_artifacts_schema,
            table_database=table_database,
            table_schema=table_schema,
            warehouse=warehouse,
        )

        # Suspend running tasks before running script:
        suspend_tasks += p_render_sql_template(
            template_name="alter_task.sql",
            task_database=managed_artifacts_database,
            managed_artifacts_prefix=managed_artifacts_prefix,
            task_schema=managed_artifacts_schema,
            table_database=table_database,
            table_schema=table_schema,
            task_action="SUSPEND",
        )
        resume_tasks += p_render_sql_template(
            template_name="alter_task.sql",
            task_database=managed_artifacts_database,
            managed_artifacts_prefix=managed_artifacts_prefix,
            task_schema=managed_artifacts_schema,
            table_database=table_database,
            table_schema=table_schema,
            task_action="RESUME",
        )

    out_str = (
        sql_section_header("SUSPEND ANY RUNNING TASKS")
        + suspend_tasks.strip()
        + "\n\n"
        + out_str.strip()
        + sql_section_header("RESUME TASKS")
        + resume_tasks.strip()
    )
    return out_str


def generate_environment_sql_files(
    environment: dict,
    environment_path: Union[Path, str],
    table_parser_config: SnowflakeConfig,
    unique_schemas: set,
    data_contracts_config: dict,
    contract_tracker_directory: Path,
    s3_upload: bool = False,
    recursive_depth: int = 3,
    create_landing: bool = False,
) -> None:
    """
    Generates SQL files for a specific environment based on data contracts.

    Args:
        environment (dict): The environment details.
        environment_path (Union[Path, str]): The path to the environment.
        table_parser_config (SnowflakeConfig): Snowflake configuration for table parsing.
        unique_schemas (set): A set of unique schemas.
        data_contracts_config (dict): Configuration details for the data contracts.
        contract_tracker_directory (Path): The directory for contract trackers.
        s3_upload: Passing argument for local/S3 execution.
        recursive_depth (int): Indicates how many recursive calls are made when parsing the data contracts.
        create_landing: Passing argument for landing table.
    """

    all_ddls = ""

    tracker_class = ContractTrackerS3Handler if s3_upload else ContractTrackerFileHandler
    tracker = tracker_class(contract_tracker_directory, environment["name"])

    existing_contracts = tracker.load_existing_contracts()

    contracts_dict = {contract["name"]: contract for contract in existing_contracts["contracts"]}

    generated_pipelines_directory = os.path.join(environment_path, "pipelines")
    create_folders_tree(generated_pipelines_directory)

    for contract_config in data_contracts_config:
        data_contract_config = DataContractConfig(contract_config)
        data_contract_config.recursive_depth = recursive_depth

        if should_skip_contract(data_contract_config, table_parser_config):
            continue

        try:
            unique_schemas.add(data_contract_config.router_schema)
            parser = TableParser(
                data_contract_config=data_contract_config,
                table_parser_config=table_parser_config,
            )
            parser.parse_tables(
                data_contract_config.data_contract,
                data_contract_config.class_name,
            )

            ddl = generate_sql_for_contract(
                data_contract_config, table_parser_config, environment, parser, create_landing
            )
            ddl_hash = sql_to_hash(ddl)
            generate_sql = check_and_update_contracts_version(data_contract_config, contracts_dict, parser, ddl_hash)
            if generate_sql:
                write_sql_file(
                    generated_sql_directory=generated_pipelines_directory,
                    file_name=data_contract_config.class_name + ".sql",
                    sql=ddl,
                )
                all_ddls += ddl

        except Exception as e:
            logger.exception(f"Could not process contract {data_contract_config.class_name}: {str(e)}")

    existing_contracts["contracts"] = list(contracts_dict.values())
    tracker.save_contracts(existing_contracts)
    write_sql_file(
        file_name="_AllContracts.sql",
        generated_sql_directory=generated_pipelines_directory,
        sql=all_ddls,
    )


def should_skip_contract(data_contract_config, table_parser_config):
    """
    Determines if a contract should be skipped based on its configuration and the table parser configuration.

    Args:
        data_contract_config: The data contract configuration.
        table_parser_config: Snowflake configuration for table parsing.

    Returns:
        bool: True if the contract should be skipped, False otherwise.
    """

    return data_contract_config.class_name in table_parser_config.contracts2skip or (
        table_parser_config.data_contracts and data_contract_config.class_name not in table_parser_config.data_contracts
    )


def check_and_update_contracts_version(data_contract_config, contracts_dict, parser, ddl_hash):
    """
    Checks and updates the version of a contract.

    Args:
        data_contract_config: Configuration details for the data contract.
        contracts_dict: Dictionary containing contracts information.
        parser: The table parser instance.

    Returns:
        bool: True if a new version is generated, False otherwise.
    """

    contract_info = contracts_dict.get(data_contract_config.class_name)

    if contract_info:
        current_version = next(
            (version for version in contract_info["version_history"] if version["state"] == "current"), None
        )

        # Check if the current version is different from the stored version
        if current_version and (
            current_version["version"] != data_contract_config.data_contract_version
            or current_version["contract_config_hash"] != contract_config_to_hash(data_contract_config)
            or current_version["contract_dictionary_hash"] != contract_dictionary_to_hash(parser)
            or current_version["ddl_hash"] != ddl_hash
        ):
            current_version["state"] = "previous"
            contract_info["version_history"].insert(
                0,
                new_version_dict(
                    data_contract_config.data_contract_version,
                    contract_config_to_hash(data_contract_config),
                    contract_dictionary_to_hash(parser),
                    ddl_hash,
                ),
            )
            return True
    else:
        contracts_dict[data_contract_config.class_name] = {
            "name": data_contract_config.class_name,
            "version_history": [
                new_version_dict(
                    data_contract_config.data_contract_version,
                    contract_config_to_hash(data_contract_config),
                    contract_dictionary_to_hash(parser),
                    ddl_hash,
                )
            ],
        }
        return True
    return False


def contract_config_to_hash(data_contract_config):
    """
    Converts the data contract configuration to its hash representation.

    Args:
        data_contract_config: Configuration details for the data contract.

    Returns:
        str: MD5 hash of the contract configuration.
    """

    contract_dict = data_contract_config.to_dict()
    contract_string = json.dumps(contract_dict, sort_keys=True)
    contract_hash = hashlib.md5(contract_string.encode()).hexdigest()  # NOSONAR
    return contract_hash


def contract_dictionary_to_hash(parser):
    """
    Converts the parsed schema of a contract to its hash representation.

    Args:
        parser: The table parser instance with the parsed schema.

    Returns:
        str: MD5 hash of the parsed schema.
    """

    contract_dict = parser.parsed_schema
    contract_string = str(contract_dict)
    contract_hash = hashlib.md5(contract_string.encode()).hexdigest()  # NOSONAR
    return contract_hash


def sql_to_hash(ddl: str) -> str:
    """Generate a hash from the DDL."""
    # Generate the hash
    ddl_hash = hashlib.md5(ddl.encode()).hexdigest()  # NOSONAR

    return ddl_hash


def new_version_dict(data_contract_version, data_contract_config_hash, data_contract_dictionary_hash, ddl_hash):
    """
    Creates a dictionary representation for a new version of a contract.

    Args:
        data_contract_version: Version details of the data contract.
        data_contract_config_hash: Hash of the contract configuration.
        data_contract_dictionary_hash: Hash of the parsed schema.

    Returns:
        dict: Dictionary with details of the new contract version.
    """

    return {
        "version": data_contract_version,
        "state": "current",
        "timestamp": datetime.now(),
        "contract_config_hash": data_contract_config_hash,
        "contract_dictionary_hash": data_contract_dictionary_hash,
        "ddl_hash": ddl_hash,
    }


def generate_sql_for_contract(data_contract_config, table_parser_config, environment, parser, create_landing):
    """
    Generates SQL for a given data contract.

    Args:
        data_contract_config: Configuration details for the data contract.
        table_parser_config: Snowflake configuration for table parsing.
        environment: The environment details.
        parser: The table parser instance.
        create_landing: Passing argument for landing table.

    Returns:
        str: SQL string for the given contract.
    """

    ddl = sql_section_header(f"DATA CONTRACT: {data_contract_config.class_name}")
    ddl += (
        contract_to_sql(
            table_parser_config=table_parser_config,
            data_contract_config=data_contract_config,
            environment=environment,
            parser=parser,
            create_landing=create_landing,
        )
        + "\n\n"
    )
    return ddl


def generate_sql_files(
    table_parser_config: SnowflakeConfig,
    generated_sql_directory: Path,
    contract_tracker_directory: Path,
    s3_upload: bool,
    recursive_depth: int,
    create_landing: bool = False,
):
    """
    Generates SQL files based on the table parser configuration.

    Args:
        table_parser_config (SnowflakeConfig): Snowflake configuration for table parsing.
        generated_sql_directory (Path): Directory path to store generated SQL files.
        contract_tracker_directory (Path): Directory path for contract tracking.
        s3_upload: Passing argument for local/S3 execution.
        recursive_depth (int): Indicates how many recursive calls are made when parsing the data contracts.
        create_landing: Passing argument for landing table.

    Returns:
        None: This function doesn't return any value but generates SQL files in the specified directory.
    """

    unique_schemas = set()
    environments_to_process = (
        table_parser_config.environments_to_process_s3 if s3_upload else table_parser_config.environments
    )

    for environment in environments_to_process:
        # creates folder for each defined enviroment
        environment_name = environment["name"].lower()
        enviroment_folder_path = os.path.join(generated_sql_directory, environment_name)
        create_folders_tree(generated_sql_directory, environment_name)

        # Creates pipeline sql files
        data_contracts_config = load_data_contracts_config(environment_name)
        generate_environment_sql_files(
            environment=environment,
            environment_path=enviroment_folder_path,
            table_parser_config=table_parser_config,
            unique_schemas=unique_schemas,
            data_contracts_config=data_contracts_config,
            contract_tracker_directory=contract_tracker_directory,
            s3_upload=s3_upload,
            recursive_depth=recursive_depth,
            create_landing=create_landing,
        )

        # Creates schema creation sql files
        generate_schema_sql_files(
            unique_schemas=unique_schemas, enviroment_path=enviroment_folder_path, environment_name=environment_name
        )

        # timestamp validation function
        generate_sql_function(
            template_name="validation_dts_function.sql",
            enviroment_path=enviroment_folder_path,
            file_name=table_parser_config.timestamp_validation["function_definitions"]["function_name"],
            timestamp_validation=table_parser_config.timestamp_validation,
        )


def get_notification_integration(
    environment: str,
):
    """
    Retrieves the notification integration for a given environment.

    Args:
        environment (str): The name of the environment.

    Returns:
        The notification integration configuration or None if not found.
    """

    # import here due to dynamic environment from context
    snowflake_static_resources_configs = importlib.import_module(
        f"app.infrastructure.data_service.configs.snowflake_static_resources.{environment}"
    )
    config = snowflake_static_resources_configs.get_configs()
    if len(config):
        return config[0]["notification_integration"]
    else:
        return None


def main():
    """
    Entry point of the script. Processes command line arguments and triggers the generation of SQL files.
    """
    parser = argparse.ArgumentParser(description="Environment Processing Options.")
    parser.add_argument("--s3_upload", action="store_true", help="Generate to S3 bucket for one environment.")
    parser.add_argument("--create_landing", action="store_true", help="Create table and pipe in SQL.")
    parser.add_argument(
        "-rd", "--recursive_depth", default=3, type=int, help="Number of recursive calls when parsing data contracts"
    )
    args = parser.parse_args()

    prepare_and_generate_files(
        s3_upload=args.s3_upload, create_landing=args.create_landing, recursive_depth=args.recursive_depth
    )


def prepare_and_generate_files(s3_upload, create_landing, recursive_depth):
    """
    Prepares the necessary directories and triggers the generation of SQL files based on the given arguments.

    Args:
        s3_upload (bool): A flag indicating whether to generate files locally.
        create_landing (bool): A flag indicating whether to create table and pipe in SQL.
        recursive_depth (int): Indicates how many recursive calls are made when parsing the data contracts.

    Returns:
        None
    """
    # Set directory "generated_sql" and create if not exist
    generated_sql_directory = os.path.join(Path(__file__).resolve().parent, "generated_sql")
    contract_tracker_directory = os.path.join(Path(__file__).resolve().parent, "contract_trackers")

    os.makedirs(contract_tracker_directory, exist_ok=True)

    # Remove existing files before every execution:
    if os.path.exists(generated_sql_directory):
        shutil.rmtree(generated_sql_directory)

    generate_sql_files(
        table_parser_config=load_snowflake_config(),
        generated_sql_directory=generated_sql_directory,
        contract_tracker_directory=contract_tracker_directory,
        s3_upload=s3_upload,  # Passing the argparse for local/S3 value here
        recursive_depth=recursive_depth,
        create_landing=create_landing,  # Passing the argparse for landing table value here
    )


if __name__ == "__main__":
    main()
