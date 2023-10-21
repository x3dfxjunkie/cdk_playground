import json

import pytest

from io import BytesIO
from werkzeug.datastructures import FileStorage
from unittest.mock import patch
from pathlib import Path
from tempfile import TemporaryDirectory
from datamodel_code_generator import InputFileType
from app.src.data_structures.utilities.ui.tests.conftest import (
    PATCH_DATACLASS_GEN_DIR,
    DATA_DICT,
    JSON_SCHEMA,
    XML_DATA,
)
from app.src.data_structures.utilities.ui.dataclass_generator.utils.utils import write_file
from app.src.data_structures.utilities.ui.dataclass_generator.utils.multiple_file_handler import (
    InvalidDataContractFileFormatException,
    DataContractFileFormat,
    validate_files,
    consolidate_jsons,
    get_file_format,
    equal_format_validation,
    files_handler,
    build_json_schema,
)


def test_validate_files():
    source = BytesIO()
    file = "sample-data-test.json"
    file_object = FileStorage(stream=source, filename=file)
    files_list = [file_object]
    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        input_file_names, file_name, file_format = validate_files(files_list, temp_path)
        assert file_name == file
        assert file_format == DataContractFileFormat.JSON


def test_consolidate_jsons():
    file_names = ["json_1.json", "json_2.json", "json_3.json"]
    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        for file in file_names:
            write_file(DATA_DICT, Path(temp_path / file))

        consolidated_json = consolidate_jsons(file_names, temp_path)
        assert isinstance(consolidated_json, str)
        with open(Path(temp_path / consolidated_json), "r", encoding="utf-8") as json_file:
            assert "lvl_1" in json_file.read()


def test_get_file_format():
    file_name = "test.json"
    file_format = get_file_format(file_name)
    assert file_format == file_name[5:]


def test_equal_format_validation():
    is_equal, file_format = equal_format_validation(["json_1.json", "json_2.json", "json_3.json"])
    assert is_equal
    assert file_format == DataContractFileFormat.JSON


def test_files_handler():
    file_names = ["json_1.json", "json_2.json", "json_3.json"]
    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        for file in file_names:
            write_file(DATA_DICT, Path(temp_path / file))

        file_name, file_format = files_handler(["json_1.json", "json_2.json", "json_3.json"], temp_path)
        assert file_name
        assert file_format == DataContractFileFormat.JSON
        with pytest.raises(InvalidDataContractFileFormatException):
            files_handler(["csv_1.csv", "json_2.json", "json_3.json"], temp_path)
        uniq_file = ["json_2.json"]
        files_handler(uniq_file, temp_path)
        assert file_name
        assert file_format == DataContractFileFormat.JSON


class TestSchemaBuilder:
    """Tests for JsonSchemaBuilder"""

    # test data for test_build_json_schema_output
    TEST_DATA = [
        {
            "id": 1,
            "register_timestamp": "2023-09-29 11:49:00",
            "name": "Zé Carioca",
            "email": "zé.carioca@disney.com",
            "birth_date": "1942-08-24",
            "address": {"city": "Rio de Janeiro"},
            "checkin_timestamp": "2023-09-29 11:49:01",
            "checkout_timestamp": "2023-09-29 18:00:00",
        },
        {
            "id": 2,
            "register_timestamp": "2023-09-29 11:49:02",
            "name": "Panchito Pistoles",
            "email": "panchito.pistoles@disney.com",
            "birth_date": "1945-01-01",
            "address": {"city": "Ciudad de Mexico"},
            "checkin_timestamp": None,
            "checkout_timestamp": "",
        },
        {
            "id": 3,
            "register_timestamp": "2023-09-29 11:49:03",
            "name": "Donald Duck",
            "email": "donald.duck@disney.com",
            "birth_date": "1934-06-09",
            "address": {"city": "Orlando"},
            "checkin_timestamp": "2023-09-29 11:49:04",
            "checkout_timestamp": "2023-09-29 18:00:01",
        },
    ]

    @patch(f"{PATCH_DATACLASS_GEN_DIR}.utils.multiple_file_handler.example_generator")
    def test_build_json_schema_read_file(self, example_generator):
        example_generator.return_value = str(JSON_SCHEMA)
        with TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            file_formats = ["yaml", "csv", "json", "xml", "else"]
            for file_format in file_formats:
                file_name = "test." + file_format

                if file_format == "else":
                    write_file(DATA_DICT, Path(temp_path / file_name))
                    with pytest.raises(InvalidDataContractFileFormatException):
                        build_json_schema(file_name, file_format, temp_path)
                    continue
                elif file_format == DataContractFileFormat.XML:
                    with open(Path(temp_path / file_name), "w", encoding="utf-8") as f:
                        f.write(XML_DATA)
                else:
                    write_file(DATA_DICT, Path(temp_path / file_name))

                input_file, input_file_type = build_json_schema(
                    file_name, DataContractFileFormat[file_format.upper()].value, temp_path
                )

                if file_format == DataContractFileFormat.YAML:
                    assert input_file
                    assert input_file_type == InputFileType.OpenAPI
                else:
                    assert input_file_type == InputFileType.JsonSchema

    def test_build_json_schema_output(self):
        with TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            file_name = "test.json"
            write_file(self.TEST_DATA, Path(temp_path / file_name))
            input_file, _ = build_json_schema(file_name, DataContractFileFormat.JSON, temp_path)
            json_schema_rep = json.loads(input_file)
            test_fields = json_schema_rep["items"]["properties"]

        assert test_fields["register_timestamp"]["format"] == "date-time"
        assert test_fields["birth_date"]["format"] == "date"
        assert test_fields["checkin_timestamp"]["anyOf"][1]["format"] == "date-time"
        assert "format" not in test_fields["checkout_timestamp"]
