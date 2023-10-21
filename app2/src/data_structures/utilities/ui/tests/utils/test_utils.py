"""
Tests for Auto-Mater utilities functions
"""
import os
import pandas as pd

from pathlib import Path
from io import BytesIO
from werkzeug.datastructures import FileStorage
from app.src.data_structures.utilities.ui.tests.conftest import UPDATE_TREE_DICT, JSON_SCHEMA, DATA_DICT
from app.src.data_structures.utilities.ui.dataclass_generator.utils.utils import (
    save_files,
    write_file,
    remove_files,
    keys_exists,
    list_to_value_dict,
    encode_string,
    get_values_from_dict,
    create_update_tree_dict,
    example_value_assign,
    example_generator,
    map_table_dets_with_example,
    generate_mock_value,
    get_mock_example,
    create_zip_file,
    get_datatype,
    get_custom_file_header,
    extract_json_objects,
)


def test_save_files(tmp_path):
    source = BytesIO()
    file_name = "sample-data-test.json"
    file_object = FileStorage(stream=source, filename=file_name)
    files_list = [file_object]
    save_files(files_list, tmp_path)
    assert os.path.exists(tmp_path / file_name)


def test_write_file(tmp_path):
    file_content = {"test": "value"}
    path = tmp_path / "test_file.json"
    write_file(file_content, path)
    assert os.path.exists(path)


def test_remove_files(tmp_path):
    file_content = {"test": "value"}
    path = tmp_path / "test_file.json"
    write_file(file_content, path)
    assert os.path.exists(path)
    remove_files([path], Path("/"))
    assert not os.path.exists(path)


def test_keys_exists():
    assert keys_exists(JSON_SCHEMA, ["items", "properties", "arg_1"])
    assert not keys_exists(JSON_SCHEMA, ["items", "properties", "missing_arg"])


def test_list_to_value_dict():
    assert isinstance(list_to_value_dict(["test_1", "test_2"]), dict)
    assert list_to_value_dict(DATA_DICT) == DATA_DICT


def test_get_values_from_dict():
    found_values = get_values_from_dict("arg_1", DATA_DICT, ["lvl_1", "lvl_2", "lvl_3", "arg_1"])
    assert set(found_values) == {"value_1_1", "value_1_2", "value_1_3"}


def test_encode_string():
    assert "\\n" in str(encode_string("Test\nValue"))
    assert encode_string(False)
    int_value = 797879
    assert encode_string(int_value) == int_value


def test_create_update_tree_dict():
    key_list = ["lvl_1", "lvl_2"]
    value = "test_value"
    tree_dict = create_update_tree_dict(key_list, value)
    assert tree_dict == UPDATE_TREE_DICT


def test_example_value_assign():
    key_to_assign = "arg_1"
    schema_tree_keys = ["items", "properties"]
    updated_schema = example_value_assign(
        JSON_SCHEMA, DATA_DICT, key_to_assign, JSON_SCHEMA["items"]["properties"][key_to_assign], schema_tree_keys
    )
    assert "example" in updated_schema["items"]["properties"][key_to_assign]


def test_example_generator():
    example_json_schema = example_generator(DATA_DICT, JSON_SCHEMA)
    schema_arguments = example_json_schema["items"]["properties"]
    assert "example" in schema_arguments["arg_1"]
    assert "example" in schema_arguments["arg_2"]
    assert "example" in schema_arguments["arg_3"]


def test_map_table_dets_with_example():
    empty_df = pd.DataFrame()
    res_df = map_table_dets_with_example(empty_df, empty_df)
    assert "EXAMPLE" in res_df.columns
    assert len(res_df.EXAMPLE.value_counts()) == 0

    base_data = [
        {"arg_1": "val_1", "arg_2": "val_2", "COLUMN_NAME": 111},
        {"arg_1": "val_3", "arg_2": "val_4", "COLUMN_NAME": 222},
    ]
    base_df = pd.DataFrame(base_data)
    map_data = [{111: "map_1", 222: "map_2"}]
    map_df = pd.DataFrame(map_data)

    res_df = map_table_dets_with_example(base_df, map_df)
    assert "EXAMPLE" in res_df.columns
    assert len(res_df.EXAMPLE.value_counts()) > 0


def test_generate_mock_value():
    assert isinstance(generate_mock_value("string"), str)
    assert isinstance(generate_mock_value("integer"), int)
    assert isinstance(generate_mock_value("float"), int)
    assert isinstance(generate_mock_value("number"), int)
    assert isinstance(generate_mock_value("datetime"), str)
    assert isinstance(generate_mock_value("date-time"), str)
    assert isinstance(generate_mock_value("else"), str)


def test_get_mock_example():
    assert isinstance(get_mock_example(data_type="integer", col_value=None), int)
    assert isinstance(get_mock_example(data_type="date-time", col_value="12/31/9999"), str)
    assert isinstance(get_mock_example(data_type="string", col_value="else"), str)


def test_create_zip_file():
    source_name = "Test"
    tables = ["Table_1", "Table_2", "Table_3"]
    content = ["Content 1", "Content 2", "Content 3"]
    zip_file = create_zip_file(source_name, tables, content)
    assert isinstance(zip_file, BytesIO)


def test_get_datatype():
    assert get_datatype("char") == "string"
    assert get_datatype("bigint") == "integer"
    assert get_datatype("float") == "float"
    assert get_datatype("timestamp") == "date-time"
    assert get_datatype("else") == "string"


def test_get_custom_file_header():
    contract_header = get_custom_file_header("Test-table")
    assert isinstance(contract_header, str)
    assert "Source Data Contract Template for " in contract_header


def test_json_object():
    input_string1 = '{ "some" : "json" } , {"some2" : { "nested" : "json2" }}'
    input_string2 = 'some text { "some" : "json" } some more text'
    assert extract_json_objects(input_string1) == [{"some": "json"}, {"some2": {"nested": "json2"}}]
    assert extract_json_objects(input_string2) == [{"some": "json"}]
