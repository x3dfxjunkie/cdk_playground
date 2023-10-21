import json
import boto3

from io import BytesIO
from moto import mock_s3
from werkzeug.datastructures import FileStorage
from app.src.data_structures.utilities.ui.tests.conftest import DATA_DICT, DATA_CONTRACT
from app.src.data_structures.utilities.ui.dataclass_generator.ui_scripts.sample_load import (
    data_contract_model_rename,
    get_data_contract,
    handle_s3_request,
    data_contract_in_str_to_module_in_memory,
    get_synthetic_data,
)


def test_data_contract_model_rename():
    data_contract = """
    title = ""
    description = ""
    class Model(BaselModel)
    """
    output_data_contract = data_contract_model_rename("TestModelName", data_contract)
    assert "TestModelName" in output_data_contract


def test_get_data_contract():
    file_1 = BytesIO(json.dumps(DATA_DICT).encode("utf-8"))
    data_contract, model_name = get_data_contract(
        [FileStorage(file_1, filename="test_data_contract.json", content_type="json")]
    )
    assert data_contract
    assert "TestDataContract" in data_contract and "TestDataContract" in model_name


def test_data_contract_in_str_to_module_in_memory():
    module_name = "test_module"
    module_code_in_str = DATA_CONTRACT
    module_code_in_memory = data_contract_in_str_to_module_in_memory(module_name, module_code_in_str)
    assert module_name in str(module_code_in_memory)


def test_get_synthetic_data():
    model_name = "SnappEntitlementSourceDataContractSampleModel"
    quantity = 1
    synthetic_data = get_synthetic_data(DATA_CONTRACT, model_name, quantity)
    assert synthetic_data


@mock_s3
def test_handle_s3_request():
    file_content = json.dumps(DATA_DICT)
    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="sample-bucket")
    s3_client.put_object(Bucket="sample-bucket", Key="folder1/folder2/file1.json", Body=file_content)
    contract = handle_s3_request("s3://sample-bucket/folder1/folder2/file1.json")
    assert "Source Data Contract" in contract
