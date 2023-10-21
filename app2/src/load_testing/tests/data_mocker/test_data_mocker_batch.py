import pytest
from unittest.mock import patch
from app.src.load_testing.app.data_mocker.data_mocker_batch import DataMockerBatch


def test_data_mocker_batch_init():
    data_contract_list = [
        {
            "data_contract": "app.src.data_structures.data_contracts.source.ea_wdw.v0.ea_wdw_lightning_lane_source_data_contract",
            "class_name": "EAWDWLightningLaneModel",
        },
        {
            "data_contract": "app/src/data_structures/data_contracts/source/dreams/charge_account/v0/dreams_charge_account_chrg_grp_source_data_contract.py",
            "class_name": "DREAMSChargeAccountChrgGrpModel",
        },
    ]

    batch = DataMockerBatch(data_contract_list)

    assert batch.data_contract_list == data_contract_list


@patch("app.src.load_testing.app.data_mocker.data_mocker.DataMocker.next", side_effect=["mock_data_1", "mock_data_2"])
def test_data_mocker_batch_next(mock_next_method):
    data_contract_list = [
        {
            "data_contract": "app.src.data_structures.data_contracts.source.ea_wdw.v0.ea_wdw_lightning_lane_source_data_contract",
            "class_name": "EAWDWLightningLaneModel",
        },
        {
            "data_contract": "app/src/data_structures/data_contracts/source/dreams/charge_account/v0/dreams_charge_account_chrg_grp_source_data_contract.py",
            "class_name": "DREAMSChargeAccountChrgGrpModel",
        },
    ]

    batch = DataMockerBatch(data_contract_list)
    result = batch.next()

    assert mock_next_method.call_count == 2
    assert result == ["mock_data_1", "mock_data_2"]
