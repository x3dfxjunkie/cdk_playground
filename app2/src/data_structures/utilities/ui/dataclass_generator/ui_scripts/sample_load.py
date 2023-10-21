from tempfile import TemporaryDirectory
from pathlib import Path
from app.src.data_structures.utilities.ui.dataclass_generator.utils.multiple_file_handler import (
    validate_files,
    build_json_schema,
)
from app.src.data_structures.utilities.ui.dataclass_generator.utils.s3_downloader import s3_file_downloader
from app.src.data_structures.utilities.ui.dataclass_generator.utils.data_contract_generator import (
    generate_data_contract,
)
import json
from polyfactory.factories import pydantic_factory
import types
from typing import Tuple


def data_contract_model_rename(model_name: str, data_contract: str) -> str:
    words_to_replace = {
        'title = ""': f'title = "{model_name}"',
        'description = ""': f'description = "{model_name}"',
        "class Model(BaseModel)": f"class {model_name}Model(BaseModel)",
        "class ModelItem(BaseModel)": f"class {model_name}Model(BaseModel)",
        "date:": "date_:",
        """None = Field(
        ...""": """None = Field(
        None""",
        'unique_identifier = [""]': "unique_identifier = []",
    }

    for search, replace in words_to_replace.items():
        data_contract = data_contract.replace(search, replace)

    return data_contract


def get_data_contract(requested_files: list) -> Tuple[str, str]:
    with TemporaryDirectory() as temporary_dir_name:
        input_file_names, file_name, file_format = validate_files(requested_files, Path(temporary_dir_name))
        input_file, input_file_type = build_json_schema(file_name, file_format, Path(temporary_dir_name))

        file_name_wo_ext = file_name.split(".")[0]
        model_name = "".join(
            map(lambda s: s.capitalize(), file_name_wo_ext.split("_" if "_" in file_name_wo_ext else "-"))
        )

        output_data_contract = generate_data_contract(model_name, input_file, input_file_type, {"example"})
        input_file_names.append(file_name)

    return data_contract_model_rename(model_name, output_data_contract), f"{model_name}Model"


def get_synthetic_data(data_contract: str, model_name: str, quantity: int) -> str:
    # Convert the code to a module named "my_dynamic_module"
    module_name = "my_dynamic_module"
    dynamic_module = data_contract_in_str_to_module_in_memory(module_name, data_contract)

    # Get the Model class from the dynamically created module
    model_class = getattr(dynamic_module, model_name)

    class ModelFactory(pydantic_factory.ModelFactory):
        __model__ = model_class

    model_instances = ModelFactory.batch(quantity)

    jsons = []
    for i in model_instances:
        json_result = json.loads(i.json(by_alias=True))
        jsons.append(json_result)

    return json.dumps(jsons)


def data_contract_in_str_to_module_in_memory(module_name, code_string):
    """
    Convert a Python code string to a Python module.

    Args:
        module_name (str): The name for the new module.
        code_string (str): The Python code in string format.

    Returns:
        module: The dynamically created Python module.
    """
    code_string = code_string.replace("from __future__ import annotations", "")

    # Create an empty module
    new_module = types.ModuleType(module_name)

    # Execute the code within the module's namespace
    exec(code_string, new_module.__dict__)

    return new_module


def handle_s3_request(s3_location: str):
    with s3_file_downloader(s3_location=s3_location) as s3_downloaded_files:
        data_contract, _ = get_data_contract(s3_downloaded_files)
        return data_contract
