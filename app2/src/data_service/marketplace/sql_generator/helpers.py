"""
Guest360 Module with helper functions
"""
import os
import glob
import logging
import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from app.src.data_service.marketplace.sql_generator.generator_config import (
    DataContractConfig,
    SnowflakeConfig,
    SnowflakeConfigLoader,
    SchemaConfLoader,
    SchemaDataConf,
)

JINJA_ENV = Environment(loader=FileSystemLoader(Path(__file__).resolve().parent / "templates"), autoescape=True)
PARSER_CONFIG_PATH = Path(__file__).resolve().parent / "parser_config.yaml"
SCHEMA_NAME_DELIMITER = "_"


def to_snake_case(input_str: str) -> str:
    """Transforms a given dataclass name into snake_case format

    Args:
        s (str): dataclass name

    Returns:
        str: formatted dataclass name
    """
    if not any(map(lambda x: x.isupper(), input_str)):
        return input_str.replace("-", "_")
    fields = input_str.split("__")
    snake_cased_fields = []
    for i in range(len(fields)):
        matches = re.sub("([A-Z][a-z]+)", r" \1", re.sub("([A-Z]+)", r" \1", fields[i].replace("-", " "))).split()
        # We've seen some cases where the name of the column has an underscore as the last character.  If underscore is in last field, leave it:
        snake_cased_fields.append(
            "_".join(
                matches[j] if (matches[j][-1] == "_" and j == len(matches) - 1) else matches[j].replace("_", "")
                for j in range(len(matches))
            ).lower()
        )
    return "__".join(snake_cased_fields)


def default_managed_artifact_warehouse(
    environment: dict[str, str],
    managed_artifacts_database: str = "MA",
) -> str:
    return f'{managed_artifacts_database}_{environment["short_name"]}_WH'


def sql_section_header(header_value: str) -> str:
    return f"""

------------------------------------------------------------------------------
-- {header_value.upper()}
------------------------------------------------------------------------------
"""


def raw_schema_name(router_schema: str, name_delimiter: str = SCHEMA_NAME_DELIMITER) -> str:
    name_delimiter_index = router_schema.find(name_delimiter)
    if name_delimiter_index == -1:
        raise ValueError(f"The name delimiter {name_delimiter} was not found in the router_schema {router_schema}")

    # Return value past prefix + delimiter (e.g. LND_TEST -> TEST):
    return router_schema[(name_delimiter_index + len(name_delimiter)) :]


def unblobbing_schema_name(
    landing_schema_name: str,
    unblobbing_schema_prefix: str = "BRZ",
    name_delimiter: str = SCHEMA_NAME_DELIMITER,
) -> str:
    """Returns bronze / unblobbing schema name based on naming convention (i.e. replaces LND in landing schema with BRZ).

    Args:
        landing_schema_name (str)
        landing_schema_prefix (str, optional) Defaults to "LND".
        unblobbing_schema_prefix (str, optional) Defaults to "BRZ".

    Returns:
        str: Unblobbing schema name
    """
    return f"{unblobbing_schema_prefix}{name_delimiter}{raw_schema_name(landing_schema_name)}"


def render_sql_template(template_name: str, **kwargs) -> str:
    """Renders a jinja template given a filename and the context kwargs

    Args:
        template_name (str): name of the sql template

    Returns:
        str: rendered template
    """
    template = JINJA_ENV.get_template(template_name)
    return template.render(kwargs)


def get_logger(file: str) -> logging.Logger:
    """Returns logger for the specific given filename

    Args:
        file (str): filename

    Returns:
        logging.Logger: logger object
    """
    logger = logging.getLogger(file)
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def load_contracts(file_path: str) -> dict:
    """Loads contracts from a specific file
    The file must be in a YAML format

    Args:
        file_path (str): directory to find all the

    Returns:
        dict: loaded yaml file
    """
    with Path(file_path).open(encoding="utf8") as f:
        file = yaml.load(f, Loader=yaml.Loader)

        data_contracts = []

        try:
            # Configs are a bit inconsistent right now as files are getting ironed out.  Check two ways:
            if file["pattern_instances"][0]["resources"].get("data_pipe"):
                data_contracts = file["pattern_instances"][0]["resources"]["data_pipe"]["data_contracts"]
            else:
                data_contracts = file["pattern_instances"][0]["data_pipe"]["data_contracts"]
        except KeyError as ke:
            print(f"Could not find data_contracts section for file {file_path}")

    return data_contracts


def load_all_contracts(contracts_path: str) -> list[dict]:
    contracts_lst = []
    for file in glob.glob(contracts_path + "/*yaml"):
        with Path(file).open(encoding="utf8") as f:
            file_text = f.read()
            if "data_contracts" in file_text:
                contracts_lst.extend(load_contracts(file))

    return contracts_lst


def create_folders_tree(*folder_tree) -> None:
    os.makedirs(os.path.join(*folder_tree), exist_ok=True)


def write_sql_file(
    file_name: str,
    sql: str,
    generated_sql_directory: Path,
) -> None:
    with open(
        os.path.join(generated_sql_directory, file_name),
        "w",
        encoding="utf-8",
    ) as file:
        file.write(sql)


def load_data_contracts_config(environment_name: str) -> list[dict]:
    pipelines_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "../../../../infrastructure/ingestion/config/pipelines"
    )
    data_contracts_config_path = f"{pipelines_dir}/{environment_name.lower()}/"
    data_contracts_config = load_all_contracts(data_contracts_config_path)
    return data_contracts_config


def load_schema_gen_conf() -> SchemaDataConf:
    config_loader = SchemaConfLoader(PARSER_CONFIG_PATH)
    schema_config = config_loader.get_config()
    return schema_config


def load_snowflake_config() -> SnowflakeConfig:
    config_loader = SnowflakeConfigLoader(PARSER_CONFIG_PATH)
    snowflake_config = config_loader.get_config()
    return snowflake_config
