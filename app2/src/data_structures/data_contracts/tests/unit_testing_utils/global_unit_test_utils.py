"""Module for Data Contract Unit Testing Utils"""

import json
import importlib
import os

from functools import lru_cache


def get_contracts_root_path(level_up_string):
    root_path = os.path.abspath(os.path.join(__file__, level_up_string))
    return root_path


def read_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        json_object = json.load(f)
    return json_object


@lru_cache(None)
def get_data_contracts_info():
    all_sources = {}
    contracts_root_path = get_contracts_root_path("../")
    mapping_json_dir = f"{contracts_root_path}/mapping_jsons"
    for source_file in os.listdir(mapping_json_dir):
        if source_file.endswith("data_contract_mapping.json"):
            source_data_contracts_info = f"{mapping_json_dir}/{source_file}"
            source_file_content = read_json(source_data_contracts_info)
            all_sources.update(source_file_content)
    return all_sources


def get_data_contracts_model_names():
    data_contracts_models = get_data_contracts_info().keys()
    return data_contracts_models


def get_contract_name(model_name):
    data_contracts_info = get_data_contracts_info()
    contract_name_value = data_contracts_info[model_name]["data-contract-name"]
    return contract_name_value


def folder_location_cleaner(folder_location):
    if folder_location.endswith("/"):
        folder_location = folder_location[:-1]
    if folder_location.startswith("/"):
        folder_location = folder_location[1:]
    return folder_location


def get_contract_data_source_folder(model_name):
    data_contracts_info = get_data_contracts_info()
    data_contract_folder = data_contracts_info[model_name]["data-source-folder"]
    clean_data_contract_folder = folder_location_cleaner(data_contract_folder)
    return clean_data_contract_folder


def convert_slash_to_dot(folder_location):
    location_with_dots = folder_location.replace("/", ".")
    return location_with_dots


def get_data_contract_import_location(model_name):
    contract_name = get_contract_name(model_name)
    contract_data_source_folder = get_contract_data_source_folder(model_name)
    contract_data_source_folder_dots = convert_slash_to_dot(contract_data_source_folder)
    location = f"app.src.data_structures.data_contracts.source.{contract_data_source_folder_dots}.{contract_name}"
    return location


def get_model_class(model_name):
    module_name = get_data_contract_import_location(model_name)
    module = importlib.import_module(module_name)
    model_class = getattr(module, model_name)
    return model_class


def clean_sample_path(sample_folder):
    folders = sample_folder.split("/")
    total_folders = len(folders)
    last_folder = folders[-1].lower()
    if (total_folders > 1) and (last_folder[0] == "v") and (last_folder[1:].isdigit()):
        sample_folder = "/".join(sample_folder.split("/")[:-1])
    return sample_folder


def get_sample_dir(model_name):
    contracts_root_path = get_contracts_root_path("../../")
    sample_data_source_folder = get_contract_data_source_folder(model_name)
    sample_dir = f"{contracts_root_path}/test_data/{sample_data_source_folder}"
    return sample_dir


def get_samples_path(model_name):
    sample_dir = get_sample_dir(model_name)
    contract_name = get_contract_name(model_name)
    sample_path = f"{sample_dir}/{contract_name}_sample.json"
    return sample_path


def get_model_sample(model_name):
    sample_path = get_samples_path(model_name)
    sample_object = read_json(sample_path)
    return sample_object


def camel_to_snake(s):
    return "".join(["_" + c.lower() if c.isupper() else c for c in s]).lstrip("_")


def get_test_dev_path(model_name):
    data_contract_file_name = get_contract_name(model_name)
    common_path = "app/src/data_structures/data_contracts"
    test_name = f"{data_contract_file_name}_test"
    test_dir = f"/workspace/{common_path}/tests/unit_tests/"
    test_full_name = f"{test_dir}{test_name}.py"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    if not os.path.exists(f"{test_dir}__init__.py"):
        with open(f"{test_dir}__init__.py", "w", encoding="utf-8") as f:
            f.write("")
    return test_full_name, test_name


def write_sample_file(model_name, samples):
    """Function to write the sample file"""
    sample_dir = get_sample_dir(model_name)
    sample_path = get_samples_path(model_name)
    if not os.path.exists(sample_dir):
        os.makedirs(sample_dir)
    with open(sample_path, "w", encoding="utf-8") as outfile:
        json.dump(samples, outfile)
