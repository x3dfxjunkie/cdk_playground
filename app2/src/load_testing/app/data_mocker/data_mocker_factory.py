"""
    This module defines two classes: 'AbstractDataMockerFactory' and 'DataMockerFactory'.
    'AbstractDataMockerFactory' is an abstract base class that sets the blueprint for its
    concrete child class 'DataMockerFactory'. 'DataMockerFactory' is used to instantiate
    the 'DataMocker' class with specific parameters.
"""
from app.src.load_testing.app.data_mocker.data_mocker_abc import DataMockerABC
from app.src.load_testing.app.data_mocker.data_mocker_batch import DataMockerBatch
from typing import List, Dict, Any


class DataMockerFactory:
    """
    The DataMockerFactory class is a concrete implementation of the AbstractDataMockerFactory.
    It implements the 'get_data_mocker' method and is responsible for creating and returning
    an instance of the 'DataMocker' class.
    """

    @staticmethod
    def get_data_mocker(data_contract_list: List[Dict[str, Any]]) -> DataMockerABC:
        """Create an instances of DataMocker with the given input data contract list.
        Args List:
        [
            {
                data_contract_path (str): Path to the Python module containing the data contract class.
                data_contract_class_name (str): Name of the data contract class.
                active_injection (bool): Determines if synthetic data should be generated. Default is True.
                data_contract_test_data_path (str, optional): Path to the JSON file containing test data.
                only_payload_data (bool, optional): Determines whether to return only payload data. Default is True.
                change_fields (float, optional): Probability to change the data type of a field. Default is 0.0.
                omit_fields (float, optional): Probability to omit a field. Default is 0.0.
                use_alias (bool, optional): Determines whether to use the field alias from the pydantic, Default is False.
            },
            ...
        ]
        """
        return DataMockerBatch(data_contract_list)
