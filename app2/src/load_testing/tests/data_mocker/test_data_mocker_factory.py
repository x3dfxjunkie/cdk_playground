"""Unit Test for DataMocker Factory Class"""

import pytest
from unittest.mock import patch, MagicMock
from app.src.load_testing.app.data_mocker.data_mocker_factory import DataMockerFactory
from app.src.load_testing.app.data_mocker.data_mocker_batch import DataMockerBatch


@patch("app.src.load_testing.app.data_mocker.data_mocker_batch.DataMockerBatch.__new__", return_value=MagicMock())
def test_get_data_mocker(mock_new_batch_method):
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

    result = DataMockerFactory.get_data_mocker(data_contract_list)

    mock_new_batch_method.assert_called_once_with(DataMockerBatch, data_contract_list)
    assert isinstance(result, MagicMock)
