"""
Module with functions to consolidate multiple files into one.
The initial scope includes: JSON, YAML, CSV, XML.
"""

from csv import DictReader
from datetime import datetime, date
from dateutil.parser import parse
from enum import Enum
import json
from pathlib import Path
from typing import Union
import xmltodict

from datamodel_code_generator import InputFileType
from genson import SchemaBuilder
from genson.schema.strategies import String

from app.src.data_structures.utilities.ui.dataclass_generator.utils.utils import (
    save_files,
    example_generator,
)


class InvalidDataContractFileFormatException(Exception):
    ...


class DataContractFileFormat(str, Enum):
    JSON = "json"
    YAML = "yaml"
    CSV = "csv"
    XML = "xml"


def validate_files(requested_files: list, save_file_path: Path = None) -> tuple[list, str, str]:
    """
    Validates that a given list of files exists, have a correct extension and
    if list has more than one, all of them should be JSONs.
    Args:
        requested_files (list): List of loaded files on Auto-Mater app.
        save_file_path (Path): Path where files are going to be stored.

    Returns:
        tuple[list, str, str]:
            - List of loaded file names.
            - Consolidated file name.
            - File format.
    """
    input_file_names = save_files(requested_files, save_file_path)
    file_name, file_format = files_handler(input_file_names, save_file_path)

    supported_formats = {data_contract_file_format.value for data_contract_file_format in DataContractFileFormat}
    if file_format not in supported_formats:
        raise InvalidDataContractFileFormatException(
            f"File format doesn't match with the supported ones. {supported_formats}"
        )

    return input_file_names, file_name, file_format


def consolidate_jsons(file_name_list: list, path: Path) -> str:
    """
    Consolidates JSONs given a list of file names and stores it in workspace.
    Args:
        file_name_list (list): List of file names.
        path (Path): Path where consolidate JSON file will be stored.

    Returns:
        str: File name of the consolidated JSON file.
    """
    file_name = "temp_file.json"
    with open(path.joinpath(file_name_list[0]), encoding="utf-8") as f:
        json_file = f.read()
        json_object = json.loads(json_file)

    for file in file_name_list[1:]:
        with open(path.joinpath(file), encoding="utf-8") as f:
            temp_json_file = f.read()
            json_object.update(json.loads(temp_json_file))

    with open(path.joinpath(file_name), "w", encoding="utf-8") as f:
        json.dump(json_object, f, ensure_ascii=False)

    return file_name


def get_file_format(file_name: str) -> str:
    """
    Gets file extension in a file name.
    Args:
        file_name (str): file name

    Returns:
        str: _description_
    """
    return file_name.split(".")[-1].lower()


def equal_format_validation(file_name_list: list) -> tuple[bool, str]:
    """
    Validates that all file formats are the same in a given list of file names.
    Args:
        file_name_list (list): List of file names.

    Returns:
        tuple[bool, str]: Boolean if formats are equal, first checked format.
    """
    file_format = get_file_format(file_name_list[0])
    is_equal = all(get_file_format(file_name) == file_format for file_name in file_name_list)
    return is_equal, file_format


def files_handler(file_name_list: list, path: Path) -> tuple[str, str]:
    """
    Handles a given list of file names to validate that file formats are the same,
    and consolidates JSONs files in an only temporary file.
    Args:
        file_name_list (list): List of file names.
        path (Path): Path where consolidate JSON file will be stored.

    Returns:
        tuple[str, str]: File name, file format.
    """
    if len(file_name_list) > 1:
        equal_format, file_format = equal_format_validation(file_name_list)

        if not equal_format or file_format != DataContractFileFormat.JSON:
            raise InvalidDataContractFileFormatException(f"File format JSON is not the same for all files.")

        file_name = consolidate_jsons(file_name_list, path)
    else:
        file_name = file_name_list[0]
        file_format = get_file_format(file_name)

    return file_name, file_format


class StringFormat(String):
    """
    Class to add the schema property 'format' to strings representing date or datetime formats.
    This class extends the genSON SchemaBuilder behavior. For more information, please
    refer to the following docs: https://github.com/wolverdude/genson/#customizing-schemabuilder
    """

    KEYWORDS = (*String.KEYWORDS, "format")

    def __init__(self, node_class):
        super().__init__(node_class)
        self.format = None
        self.non_date_encountered = False

    def add_schema(self, schema):
        super().add_schema(schema)
        if self.format is None:
            self.format = schema.get("format")

    def add_object(self, obj):
        super().add_object(obj)
        if not self.non_date_encountered:
            if self.is_date(obj):
                self.format = "date"
            elif self.is_datetime(obj):
                self.format = "date-time"
            else:
                self.format = None
                self.non_date_encountered = True

    def to_schema(self):
        schema = super().to_schema()
        if self.format is not None:
            schema["format"] = self.format
        return schema

    @staticmethod
    def is_datetime(input_str: str) -> bool:
        """Returns if a string is a representation of a datetime

        Args:
            input_str (str): any string representation.
        Returns:
            bool: True if the input_str is a datetime representation.
        """
        # Checks for the presence of a colon (typical in time components)
        if ":" in input_str:
            try:
                default_datetime = datetime.min
                parsed_datetime = parse(input_str, default=default_datetime)
                date_val = parsed_datetime.date()
                time_val = parsed_datetime.strftime("%H:%M:%S")
                # Validates that date and time part was present on original string, i.e, when not matching with the default date, which is autocompleted when not date is found or when checking that the time is present in the original string.
                return date_val != date.min and time_val in input_str
            except ValueError:
                pass
        return False

    @staticmethod
    def is_date(input_str: str) -> bool:
        """Returns if a string is a representation of a date

        Args:
            input_str (str): any string representation.
        Returns:
            bool: True if the input_str is a date representation.
        """
        if input_str.count("-") == 2:
            try:
                # Converts to datetime and if it's a date always adds the default time (00:00:00).
                # It extracts the time portion without milliseconds to check if the value exists in the step ahead.
                parsed_time = parse(input_str).strftime("%H:%M:%S")
                # Validates that time portion was not present on the original string since 'dateutil.parse' adds the min time to dates.
                # For example, if the input string contains 00:00:00 it returns false.
                return parsed_time not in input_str
            except ValueError:
                pass
        return False


class CustomSchemaBuilder(SchemaBuilder):
    """
    Extends the SchemaBuilder behavior to use extra strategies. For more information, please
    relate to the following docs: https://github.com/wolverdude/genson/#customizing-schemabuilder
    """

    EXTRA_STRATEGIES = (StringFormat,)


class JsonSchemaBuilder:
    """Wraps the logic that creates a json schema from a given data structure"""

    def build_json_schema(self, file_name: str, file_format: str, path: Path) -> tuple[Union[Path, str], InputFileType]:
        """
        Builds a JSON schema string for a given file name and format.
            - If it is a YAML, it wil only return a Path object with the file name and OpenAPI file format.
            - If it is a CSV or JSON, it will build the JSON schema using SchemaBuilder library.
            - If it is an XML parse it into a dictionary.
        Args:
            file_name (str): File name to read and turn into a JSON schema.
            file_format (str): File format of file to process.
            path (Path): Path where consolidate JSON file will be stored.
        Returns:
            tuple[Union[Path, str], InputFileType]: File input to generate dataclass Path object or string, file type object to generate dataclass.
        """
        if file_format == DataContractFileFormat.YAML:
            input_file = Path(file_name)
            input_file_type = InputFileType.OpenAPI
        else:
            loaded_json = self._read_file(file_name, file_format, path)
            builder = CustomSchemaBuilder()
            builder.add_object(loaded_json)
            json_schema = builder.to_schema()
            input_file = json.dumps(example_generator(loaded_json, json_schema))
            input_file_type = InputFileType.JsonSchema
        return input_file, input_file_type

    def _read_file(self, file_name: str, file_format: str, path: Path) -> dict:
        """
        Reads the sample imputed in auto-mater and outputs a dict representation of the contents.

        Args:
            file_name (str): File name to read and turn into a JSON schema.
            file_format (str): File format of file to process.
            path (Path): Path where consolidate JSON file will be stored.

        Returns:
            dict: dictionary representation of the file contents.
        """
        with open(path.joinpath(file_name), "r", encoding="utf8") as loaded_file:
            match file_format:
                case DataContractFileFormat.CSV:
                    csv_reader = DictReader(loaded_file)
                    loaded_json = list(row for row in csv_reader)
                case DataContractFileFormat.JSON:
                    loaded_json = json.load(loaded_file)
                case DataContractFileFormat.XML:
                    loaded_json = xmltodict.parse(loaded_file.read())
                case _:
                    raise InvalidDataContractFileFormatException(f"Invalid file format {file_format} supplied.")
        return loaded_json


def build_json_schema(file_name: str, file_format: str, path: Path) -> tuple[Union[Path, str], InputFileType]:
    return JsonSchemaBuilder().build_json_schema(file_name, file_format, path)
