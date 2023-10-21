"""
Test event pipe utils
"""
import pytest
from app.src.ingestion.event_pipes.utils.data_contract_utils import generate_hash, DataContractNotFoundException


def test_generate_hash():
    assert isinstance(generate_hash("test"), str)


def test_data_contract_not_found_exception():
    with pytest.raises(DataContractNotFoundException):
        raise DataContractNotFoundException("Test not found data contract")
