"""
    Tests for AppConfigUtils Class
"""

import pytest
import json
import io
from app.src.load_testing.app.virtual_users.appconfig_utils.utils import AppConfigUtils
from unittest.mock import patch
from botocore.response import StreamingBody


@pytest.fixture
def mock_appconfig_client():
    with patch("boto3.client") as mock_client:
        yield mock_client("appconfig")


MOCK_DATA_CONTRACT_WDW = (
    "app.src.data_structures.data_contracts.source.ea_wdw.v0.ea_wdw_lightning_lane_source_data_contract"
)
MOCK_DATA_CONTRACT_DREAM = "app.src.data_structures.data_contracts.source.dreams.charge_account.v0.dreams_charge_account_chrg_grp_source_data_contract"
sample_json_content = b'{"data_contracts":["test_data"]}'
sample_json_content = b'{"data_contracts":[{"data_contract":"app.src.data_structures.data_contracts.source.ea_wdw.v0.ea_wdw_lightning_lane_source_data_contract","class_name":"EAWDWLightningLaneModel"},{"data_contract":"app.src.data_structures.data_contracts.source.dreams.charge_account.v0.dreams_charge_account_chrg_grp_source_data_contract","class_name":"DREAMSChargeAccountChrgGrpModel"}]}'
content_length = len(sample_json_content)
hosted_config_response = {"Content": StreamingBody(io.BytesIO(sample_json_content), content_length=content_length)}

appconfig_data = {
    "name": "lst-use1-pr-4268-wdw-venuenext-arrivalwin-app",
    "stack_extension": "wdw-venuenext-arrivalwin",
    "data": {"application_id": "agn1s57", "configuration_profile_id": "sb1odfs", "version_number": 1},
}


@pytest.fixture
def mock_app_config_utils(mock_appconfig_client):
    def side_effect_hosted(*args, **kwargs):
        return {"Content": StreamingBody(io.BytesIO(sample_json_content), content_length=content_length)}

    mock_appconfig_client.get_hosted_configuration_version.return_value = hosted_config_response
    mock_appconfig_client.get_hosted_configuration_version.side_effect = side_effect_hosted

    return AppConfigUtils(appconfig_data)


def test_data_contract_list(mock_app_config_utils):
    expected_result = [
        {
            "data_contract": MOCK_DATA_CONTRACT_WDW,
            "class_name": "EAWDWLightningLaneModel",
        },
        {
            "data_contract": MOCK_DATA_CONTRACT_DREAM,
            "class_name": "DREAMSChargeAccountChrgGrpModel",
        },
    ]

    assert mock_app_config_utils.data_contract_list() == expected_result


def test_kinesis_target_name(mock_app_config_utils):
    assert mock_app_config_utils.kinesis_target_name("suffix") == "wdw-venuenext-arrivalwin-suffix"
