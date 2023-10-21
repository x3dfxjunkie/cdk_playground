"""Unit Test for DataMocker Class"""
import pytest
import json
from pydantic import BaseModel
from app.src.load_testing.app.data_mocker.data_mocker import DataMocker
from app.src.data_structures.data_contracts.source.dreams.charge_account.v0.dreams_charge_account_chrg_grp_source_data_contract import (
    DREAMSChargeAccountChrgGrpModel,
)

DATA_CONTRACTS_PATH = "app/src/data_structures/data_contracts/source/dreams/charge_account/v0/dreams_charge_account_chrg_grp_source_data_contract.py"
DATA_CONTRACT_CLASS_NAME = "DREAMSChargeAccountChrgGrpModel"
DATA_CONTRACT_TEST_DATA_PATH = "app/src/data_structures/data_contracts/tests/test_data/dreams/charge_account/v0/dreams_charge_account_chrg_grp_source_data_contract_sample.json"


def test_data_mocker_change_fields_boundary():
    with pytest.raises(ValueError):
        DataMocker(
            data_contract_path=DATA_CONTRACTS_PATH,
            data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
            active_injection=True,
            change_fields=1.1,
        )


def test_data_mocker_omit_fields_boundary():
    with pytest.raises(ValueError):
        DataMocker(
            data_contract_path=DATA_CONTRACTS_PATH,
            data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
            active_injection=True,
            omit_fields=1.1,
        )


def test_data_mocker_invalid_module_path():
    with pytest.raises(ValueError):
        DataMocker(
            data_contract_path=DATA_CONTRACTS_PATH,
            data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
            active_injection=False,
        )


def test_data_mocker_invalid_json_path():
    with pytest.raises(FileNotFoundError):
        DataMocker(
            data_contract_path=DATA_CONTRACTS_PATH,
            data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
            active_injection=False,
            data_contract_test_data_path="invalid/path.json",
        )


def test_data_mocker_without_injection():
    data_mocker = DataMocker(
        data_contract_path=DATA_CONTRACTS_PATH,
        data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
        active_injection=False,
        data_contract_test_data_path=DATA_CONTRACT_TEST_DATA_PATH,
        only_payload_data=False,
    )
    data = data_mocker.next()
    data_dict = json.loads(data)
    print(json.dumps(data_dict, indent=2))
    try:
        DREAMSChargeAccountChrgGrpModel.parse_obj(data_dict)
    # pylint: disable=broad-except
    # This is a test we want to catch all exceptions that may occur.
    except Exception as e:
        pytest.fail(f"Validation failed with error {e}")


def test_data_generation():
    mocker_instance = DataMocker(
        data_contract_path=DATA_CONTRACTS_PATH,
        data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
        active_injection=True,
    )
    data = mocker_instance.next()
    assert isinstance(data, str)


def test_modify_model_fields():
    class NestedModel(BaseModel):
        attr: int

    class TestModel(BaseModel):
        nested: NestedModel
        value: int

    data_mocker = DataMocker(
        data_contract_path=DATA_CONTRACTS_PATH,
        data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
        active_injection=True,
        change_fields=0.5,
        omit_fields=0.5,
    )
    modified_fields = data_mocker._modify_model_fields(TestModel)
    assert isinstance(modified_fields, dict)
    if "nested" in modified_fields:
        assert issubclass(modified_fields["nested"][0], BaseModel)
    if "value" in modified_fields:
        assert modified_fields["value"][0] in [int, str]


def test_modify_method():
    data_mocker = DataMocker(
        data_contract_path=DATA_CONTRACTS_PATH,
        data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
        active_injection=True,
    )
    original_factory = data_mocker.data_contract_factory
    data_mocker.modify()
    assert original_factory != data_mocker.data_contract_factory


def test_active_injection_true():
    data_mocker = DataMocker(
        data_contract_path=DATA_CONTRACTS_PATH,
        data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
        active_injection=True,
        change_fields=0.5,
        omit_fields=0.5,
    )
    data = data_mocker.next()
    data_dict = json.loads(data)
    assert isinstance(data_dict, dict)


def test_active_injection_true_no_changes():
    data_mocker = DataMocker(
        data_contract_path=DATA_CONTRACTS_PATH,
        data_contract_class_name=DATA_CONTRACT_CLASS_NAME,
        active_injection=True,
        change_fields=0.0,
        omit_fields=0.0,
    )
    data = data_mocker.next()
    data_dict = json.loads(data)
    assert isinstance(data_dict, dict)
