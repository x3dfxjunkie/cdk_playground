""" Utils module for general use functions """
import json
import regex as re
import os
import faker

from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_DEFLATED
from typing import Generator, Union, Dict, List, Any
from pydantic.utils import deep_update
from werkzeug.datastructures import FileStorage


def save_files(requested_files: list[FileStorage], path: Path) -> list:
    """
    Saves files on workspace and returns a list of the filenames
    Args:
        requested_files: List of files.
        path: Path where files are going to be saved.

    Return:
        List of files names of requested files.
    """

    file_name_list = []
    for file in requested_files:
        temp_file_name = str(file.filename)
        file.save(Path.joinpath(path, temp_file_name))
        file_name_list.append(temp_file_name)
    return file_name_list


def write_file(file, path):
    """
    Writes a file in a given path. If file does not exist, it will be created.
    Args:
        file: Content of file.
        path: Path containing the name of the file.

    """
    with open(path, "w", encoding="utf-8") as output:
        json.dump(file, output)


def remove_files(file_names_list: list, path):
    """
    Removes a list of files from container.
    Args:
        file_names_list (list): List of file names to be removed.
        path (Path):
    """
    for file in set(file_names_list):
        os.remove(path.joinpath(file))


def keys_exists(nested_dict: dict, keys: list) -> bool:
    """
    Validates that a given key list exists progressively in a given nested dictionary.
    E.g.: If function is called like this:
        keys_exists(nested_dict, ['properties', 'items'])
    Function will check if keys exist in this way:
        nested_dict['properties']['items']
    Args:
        nested_dict (dict): Nested dictionary.
        keys (list): Keys to check progressively if exists.

    Returns:
        bool: Boolean to say that keys exists or not.
    """
    for key in keys:
        try:
            nested_dict = nested_dict[key]
        except KeyError:
            return False
    return True


def list_to_value_dict(data: Union[list, dict]) -> dict:
    """
    If attribute given is a lists, it converts it into a dictionary where unique value is the actual list.
    If it is a dictionary it returns the same dictionary.
    Args:
        data (Union[list, dict]): List or dictionary data to convert into a dictionary.

    Returns:
        dict: Result dictionary in case attribute given is a list.
    """
    if isinstance(data, list):
        return {"search_dict": data}
    return data


def encode_string(value: Union[str, int, float, list, dict, None]) -> Union[str, int, float, list, dict, None]:
    """
    It will process a given value:
        - If it's a string, escape special characters.
        - If it's a bool, set it as True to avoid None filter.
        - If it's something else, just return same value.
    Args:
        value (Union[str, int, float, list, dict, None]): Value to encode.

    Returns:
        Union[str, int, float, list, dict, None]: Value encoded.
    """
    if isinstance(value, str):
        return value.encode("unicode_escape").decode()
    if isinstance(value, bool):
        return True
    return value


def get_values_from_dict(key: str, search_dict: Union[dict, list], traceback_keys: list) -> Generator:
    """
    Yields all found values for a given key in a given dictionary accordingly to the corresponding traceback.
    Args:
        key (str): Key to search.
        search_dict (dict): Searching dictionary.
        traceback_keys (list): All keys that defines an attribute.
    Yields:
        generator: generator of found values.
    """
    if isinstance(search_dict, list):
        search_dict = {"search_dict": search_dict}
        traceback_keys.insert(0, "search_dict")

    if traceback_keys:
        if traceback_keys[0] in search_dict:
            search_dict = search_dict[traceback_keys[0]]
        else:
            # If key is not present in dict then stop generator
            # Example is not in the current payload example
            return
    else:
        # If key is empty then stop generator
        return

    # If our data is a list with dicts inside then iter over the dicts
    if search_dict and isinstance(search_dict, list) and isinstance(search_dict[0], dict):
        for d in search_dict:
            yield from get_values_from_dict(key, d, traceback_keys[1:])

    # If our data is a dict then return the value
    elif isinstance(search_dict, dict):
        yield from get_values_from_dict(key, search_dict, traceback_keys[1:])

    else:
        # If we are at the last traceback key then return the directly value
        if len(traceback_keys) == 1:
            if isinstance(search_dict, str):
                encoded = search_dict.encode("unicode_escape").decode()
                yield encoded
            elif isinstance(search_dict, bool):
                yield True
            else:
                yield search_dict


def create_update_tree_dict(key_list: list, updated_value: Union[str, int, float, list, dict, None]) -> Any:
    """
    Creates a tree dictionary with a given list of keys with last level of dictionary will be a given value.
    Args:
        key_list (list): List of keys to create tree dictionary.
        updated_value (Union[str, int, float, list, dict]): Value for last level.

    Returns:
        Any: Tree dictionary.
    """
    tree_dict = updated_value
    for k in reversed(key_list):
        tree_dict = {k: tree_dict}
    return tree_dict


def example_value_assign(
    json_schema: dict,
    data: Union[dict, list],
    key: str,
    field_data: dict,
    tree_keys: list,
    keys_to_add: Union[None, List[str]] = None,
    traceback_keys: list = [],
) -> dict:
    """
    Checks for an iterating item inside JSON Schema and starts the recursive process.
    If there is no iterating item, it assigns example value to JSON Schema.
    Args:
        json_schema (dict): JSON Schema dictionary to update.
        data (Union[dict, list]): Sample data dictionary
        key (str): Key to assign.
        field_data (dict): Value of key in JSON Schema dictionary.
        tree_keys (list): List of keys to create tree dictionary
        keys_to_add (Union[None, List[str]], optional): Keys to add to tree keys list. Defaults to None.

    Returns:
        dict: JSON Schema result with examples added.
    """

    tree_keys = tree_keys + [key] + (keys_to_add if keys_to_add else [])
    type_check = field_data["type"] in ["array", "object"]
    properties_check = keys_exists(field_data, ["properties"])
    items_check = keys_exists(field_data, ["items", "properties"])
    if type_check and (properties_check or items_check):
        example_value = example_generator(data, field_data, traceback_keys)
    else:
        tree_keys = tree_keys + ["example"]
        example_values = get_values_from_dict(key, data, traceback_keys)
        example_filtered = filter(lambda x: x is not None, example_values)
        example_value = next(example_filtered, None)

    return deep_update(json_schema, create_update_tree_dict(tree_keys, example_value))


def example_generator(data: Union[dict, list], json_schema: dict, traceback_keys: list = []) -> dict:
    """
    Function will add an example value in each on of the items that a json
    Args:
        data (Union[dict, list]): Data dictionary where function will look to get examples.
        json_schema (dict): JSON schema to be filled with examples.

    Returns:
        dict: JSON schema with example values.
    """
    new_json_schema = json_schema
    tree_keys = []

    if "items" in json_schema:
        json_schema = json_schema["items"]
        tree_keys.append("items")

    if "properties" in json_schema:
        json_schema = json_schema["properties"]
        tree_keys.append("properties")

    for key, field in json_schema.items():
        if "anyOf" in field:
            example_value = []
            for data_type in field["anyOf"]:
                if data_type["type"] != "null" and not example_value:
                    example_value.append(
                        example_value_assign(
                            {key: data_type}, data, key, data_type, [], traceback_keys=traceback_keys + [key]
                        )[key]
                    )
            new_json_schema = deep_update(
                new_json_schema, create_update_tree_dict(tree_keys + [key, "example"], example_value[0]["example"])
            )
        else:
            new_json_schema = example_value_assign(
                new_json_schema, data, key, field, tree_keys, traceback_keys=traceback_keys + [key]
            )
    return new_json_schema


def map_table_dets_with_example(table_dets_df, table_example_df):
    """
    Adds new column to dataframe using values from a dict
    Usage Example:
    --------------
    Sample dataframe :-
    U,L
    111,en
    112,en
    112,es
    113,es
    113,ja
    113,zh
    114,es

    d = {112: 'en', 113: 'es', 114: 'es', 111: 'en'}
    df['D'] = df['U'].map(d)
    df
    Out[248]:
        U   L   D
    0  111  en  en
    1  112  en  en
    2  112  es  en
    3  113  es  es
    4  113  ja  es
    5  113  zh  es
    6  114  es  es

    Merge two dataframes
    :param table_dets_df:
    :param table_example_df:
    :return:
    """
    if table_example_df.empty:
        table_dets_df["EXAMPLE"] = ""
    else:
        table_example_dict = table_example_df.to_dict("records")[0]
        table_dets_df["EXAMPLE"] = table_dets_df["COLUMN_NAME"].map(table_example_dict)
    return table_dets_df


def generate_mock_value(data_type: str) -> Union[str, int, float, list, dict]:
    """
    Generates mock value with a given data type from Faker.
    Args:
        data_type (str): Data type to be created.

    Returns:
        Union[str, int, float, list, dict]: Mocked value.
    """
    fkr = faker.Faker()
    if data_type == "string":
        return fkr.pystr(20)
    elif data_type == "integer":
        value = fkr.random_int()
    elif data_type == "float":
        value = fkr.random_number(digits=5)
    elif data_type == "number":
        value = fkr.random_number(digits=5)
    elif data_type == "datetime":
        value = str(fkr.date_time())
    elif data_type == "date-time":
        value = str(fkr.date_time())
    else:
        return fkr.pystr(20)
    return value


def get_mock_example(
    data_type: str, col_value: Union[str, int, float, list, dict, None]
) -> Union[str, int, float, list, dict]:
    """
    Generate mock data provided the datatype.
    Args:
        data_type (str): Data type.
        col_value (Union[str, int, float]): Column value.

    Returns:
        Union[str, int, float, list, dict]: Mocked value.
    """
    fkr = faker.Faker()
    if col_value is None or str(col_value).lower() in ["none", "nan"]:
        return generate_mock_value(data_type)
    elif data_type == "date-time":
        return str(fkr.date_time())
    else:
        return encode_string(col_value)


def create_zip_file(source: str, tables: List[str], contracts: List[str]) -> BytesIO:
    """
    Creates a Zip file with a given list a string values and file names.
    Args:
        source (str): Prefix in file names.
        tables (List[str]): List of file names.
        contracts (List[str]): List of file contents.

    Returns:
        BytesIO: Bytes object of the Zip file.
    """
    memory_file = BytesIO()
    with TemporaryDirectory() as temp_dir, ZipFile(memory_file, "w") as zipMe:
        for table_name, contract in zip(tables, contracts):
            file_name = f"{source}_{table_name}_source_data_contract.py"
            path = Path(Path(temp_dir) / file_name)
            with open(path, "w", encoding="utf-8") as file:
                file.write(contract)

            zipMe.write(path, file_name, compress_type=ZIP_DEFLATED)
    memory_file.seek(0)
    return memory_file


def get_datatype(datatype: str) -> str:
    """
    Returns the proper datatype given a data type from database table DDL.
    Args:
        datatype: Column name data type.

    Returns:
        Simpler datatype string.
    """
    str_list = ["char", "varchar", "nchar", "nvarchar", "string"]
    int_list = ["bigint", "number", "integer", "numeric"]
    float_list = ["float", "decimal", "double"]
    time_list = ["timestamp", "datetime"]
    if any(dtype in datatype for dtype in str_list):
        return "string"
    elif any(dtype in datatype for dtype in int_list):
        return "integer"
    elif any(dtype in datatype for dtype in float_list):
        return "float"
    elif any(dtype in datatype for dtype in time_list):
        return "date-time"
    else:
        return "string"


def get_custom_file_header(table_name: str) -> str:
    """
    Gets the custom file header for data contract with a given table name.
    Args:
        table_name (str): Table name.

    Returns:
        str: Custom data contract file header
    """

    return f'''"""Source Data Contract Template for {table_name}""" '''


def extract_json_objects(input_string: str) -> List[Dict[Any, Any]]:
    pattern = re.compile(r"\{(?:[^{}]|(?R))*\}")
    json_objects = pattern.findall(input_string)
    parsed_objects = [json.loads(obj) for obj in json_objects]
    return parsed_objects
