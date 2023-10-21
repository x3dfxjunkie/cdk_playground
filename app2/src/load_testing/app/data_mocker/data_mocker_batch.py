"""
    The DataMockerBatch class is designed to generate synthetic data based on a provided
    list of data contracts. The data contract schema should be provided as a
    pydantic model, from which the data is generated.

    E.g
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
"""

from typing import List, Dict, Any
from app.src.load_testing.app.data_mocker.data_mocker_abc import DataMockerABC
from app.src.load_testing.app.data_mocker.data_mocker import DataMocker


DATA_CONTRACT_PATH = "data_contract"
DATA_CONTRACT_CLASS_NAME = "class_name"
ACTIVE_INJECTION = "active_injection"
DATA_CONTRACT_TEST_PATH = "data_contract_test_data_path"
ONLY_PAYLOAD_DATA = "only_payload_data"
CHANGE_FIELDS = "omit_fields"
OMIT_FIELDS = "change_fields"
USE_ALIAS = "use_alias"
ADD_DATA_CONTRACT = "add_data_contract"


class DataMockerBatch(DataMockerABC):
    """Data Mocker Batch class for generating synthetic data from a data contracts list."""

    def __init__(self, data_contract_list: List[Dict[str, Any]]):
        """Initialize the class with a data contracts list."""
        self.data_contract_list = data_contract_list

    def next(self) -> List[str]:
        """Generate synthetic data for each class in the data contract list."""
        data_mocker_list = []
        for item in self.data_contract_list:
            mocker = DataMocker(
                data_contract_path=item[DATA_CONTRACT_PATH],
                data_contract_class_name=item[DATA_CONTRACT_CLASS_NAME],
                active_injection=item.get(ACTIVE_INJECTION, True),
                data_contract_test_data_path=item.get(DATA_CONTRACT_TEST_PATH, ""),
                only_payload_data=item.get(ONLY_PAYLOAD_DATA, False),
                change_fields=item.get(CHANGE_FIELDS, 0.0),
                omit_fields=item.get(OMIT_FIELDS, 0.0),
                use_alias=item.get(USE_ALIAS, False),
                add_data_contract=item.get(ADD_DATA_CONTRACT, False),
            )
            data_mocker_list.append(mocker.next())
        return data_mocker_list
