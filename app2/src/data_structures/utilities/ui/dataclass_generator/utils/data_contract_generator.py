""" Data Contract Generator Script """
import json
import os
import sys

from pathlib import Path
from typing import Union
from pandas import DataFrame
from tempfile import TemporaryDirectory
from datamodel_code_generator import generate, InputFileType
from app.src.data_structures.utilities.ui.dataclass_generator.utils.constants import init_json_schema, get_constraints
from app.src.data_structures.utilities.ui.dataclass_generator.config.database import MainDatabase
from app.src.data_structures.utilities.ui.dataclass_generator.utils.utils import (
    get_mock_example,
    get_datatype,
    get_custom_file_header,
)


class DataContractGenerator:
    """Data Contract Generator class"""

    def __init__(self, db_config: dict, working_dir: str = os.getcwd()):
        """
        Data Contract Generator constructor.
        Args:
            db_config (dict[str, str  |  int]): Database configuration dictionary.
            working_dir (str, optional): Working directory. Defaults to os.getcwd().
        """
        self.model_name = None
        self.data_contract_file_name = None
        self.config_dict = db_config
        self.working_dir = working_dir
        self.db = MainDatabase.get_database(db_config["db_type"])(db_config)

    def get_source_name(self) -> str:
        """
        Gets data source name.
        Returns:
            str: Data source name.
        """
        return self.config_dict["source_name"]

    def get_schema_name(self) -> str:
        """
        Gets schema name if exists. If not return database name.
        Returns:
            str: Schema or Database name.
        """
        return self.config_dict.get("schema_name", self.config_dict.get("database"))

    def generate_class_name(self, table_name: str):
        """
        Generates Data Contract name which matches format {sourcename}{tablename}Model
        Example: TravelboxeastAccroomModel
        Args:
            table_name (str): Table name.
        """

        source_name = self.get_source_name().replace("_", "")
        table_name = table_name.replace("_", "").lower()
        model_suffix = "_".join((table_name, "Model"))
        self.model_name = source_name + "".join(word.title() for word in model_suffix.split("_"))

    def get_list_of_tables(self) -> list:
        """
        Gets list of tables from database connection.
        Returns:
            list: List of tables.
        """
        return self.db.get_list_of_tables()

    def get_json_schema(self, df: DataFrame, pk_df: DataFrame) -> str:
        """
        Creates JSON Schema to feed data contract generator function.
        Args:
            df (DataFrame): Dataframe of data to create data contract.
            pk_df (DataFrame): Primary key dataframe.

        Returns:
            str: JSON Schema string
        """
        j_schema = init_json_schema()
        constraints_dict = get_constraints()

        def create_property(row):
            data_type = get_datatype(row["DATA_TYPE"].lower())
            col_dets = {
                "description": "",
                "type": data_type,
                "example": get_mock_example(data_type, row["EXAMPLE"]),
            }
            return {row["COLUMN_NAME"]: col_dets}

        properties = df.apply(create_property, axis=1).to_dict()
        j_schema["properties"]["data"]["properties"] = properties
        j_schema["properties"]["data"]["required"] = df["COLUMN_NAME"].values.tolist()

        constraints_dict["properties"]["CONSTRAINT"]["primary_key"] = pk_df["PRIMARY_KEY"].values.tolist()
        j_schema["properties"][self.model_name] = constraints_dict

        return json.dumps(j_schema, ensure_ascii=True, default=str)

    def generate_data_contract_file_name(self, table_name: str):
        """
        Generates data contract file name.
        Args:
            table_name (str): Table name
        """
        schema_name = self.get_schema_name()
        source_name = self.get_source_name()
        suffix = "source_data_contract"
        self.data_contract_file_name = "_".join((source_name, schema_name, table_name, suffix)).lower()

    def init_contract_details(self, table_name: str):
        """
        Initializes class variables for data contract generator:
            - Data contract class name.
            - Data contract file name.
        Args:
            table_name (str): Data contract table name.
        """
        self.generate_class_name(table_name)
        self.generate_data_contract_file_name(table_name)

    def get_data_contracts(self, table_list: list) -> list:
        """
        Generates data contracts in a list.
        Args:
            table_list (list): Table names list.

        Returns:
            list: Data contracts list.
        """
        with self.db.db_connection() as conn:
            contracts = []
            for table_name in table_list:
                self.init_contract_details(table_name)
                df, pk_df = self.db.get_table_details_from_db(conn, table_name)
                json_schema = self.get_json_schema(df, pk_df)

                data_contract = generate_data_contract(
                    table_name, json_schema, InputFileType.JsonSchema, {"example", "primary_key"}
                )
                contracts.append(data_contract)

            return contracts


def get_custom_template_path() -> Path:
    """
    Gets the Data Contract generator custom templates' path.
    Returns:
        Path: Custom templates path.
    """
    return Path(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "custom_templates"))


def generate_data_contract(
    contract_name: str,
    input_file: Union[Path, str],
    input_file_type: InputFileType,
    extra_keys: set,
) -> str:
    """
    Generates Data Contract script for a given loaded file.
    Args:
        contract_name (str): Name of the data contract.
        input_file (Union[Path, str]): Input file to be processed. Could be Path if YAML or string if JSON or CSV.
        extra_keys: Extra keys set to place on each field.
        input_file_type (InputFileType): Input file type to be processed. (JSON, CSV, OpenAPI, YAML)

    Returns:
        str: Data Contract string.
    """
    with TemporaryDirectory() as temp_dir:
        output = Path(Path(temp_dir) / "temp_file.py")
        generate(
            input_file,
            input_file_type=input_file_type,
            custom_template_dir=get_custom_template_path(),
            output=output,
            custom_file_header=get_custom_file_header(contract_name),
            snake_case_field=True,
            use_schema_description=True,
            use_double_quotes=True,
            capitalise_enum_members=True,
            field_extra_keys=extra_keys,
        )

        with open(output, "r", encoding="utf8") as output_file:
            return output_file.read()
