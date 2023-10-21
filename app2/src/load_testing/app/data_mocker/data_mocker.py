"""
    The DataMocker class is designed to generate synthetic data based on a provided
    data contracts model schema. The data contract schema should be provided as a
    pydantic model, from which the data is generated.
"""
import importlib
import json
import secrets
import uuid
from pydantic import create_model, BaseModel
from polyfactory.factories import pydantic_factory
from datetime import datetime
from typing import Type, Dict, Any
from app.src.load_testing.app.data_mocker.data_mocker_abc import DataMockerABC


class DataMocker(DataMockerABC):
    """
    class that produces synthetic data based on Data Contracts.

        Args:
            data_contract_path (str): Path to the Python module containing the data contract class.
            data_contract_class_name (str): Name of the data contract class.
            active_injection (bool): Determines if synthetic data should be generated. Default is True.
            data_contract_test_data_path (str, optional): Path to the JSON file containing test data.
            only_payload_data (bool, optional): Determines whether to return only payload data. Default is True.
            change_fields (float, optional): Probability to change the data type of a field. Default is 0.0.
            omit_fields (float, optional): Probability to omit a field. Default is 0.0.
            use_alias (bool, optional): Determines whether to use the field alias from the pydantic, Default is False.
            add_data_contract (bool, optional): Determines whether to add the info from the pydantic, Default is False.
    """

    def __init__(
        self,
        data_contract_path: str,
        data_contract_class_name: str,
        active_injection: bool = True,
        data_contract_test_data_path: str = None,
        only_payload_data: bool = False,
        change_fields: float = 0.0,
        omit_fields: float = 0.0,
        use_alias: bool = False,
        add_data_contract: bool = False,
    ):
        self.data_contract_path = data_contract_path
        self.data_contract_class_name = data_contract_class_name
        self.change_fields = change_fields
        self.omit_fields = omit_fields
        self.only_payload_data = only_payload_data
        self.active_injection = active_injection
        self.use_alias = use_alias
        self.add_data_contract = add_data_contract

        if not (0.0 <= self.change_fields <= 1.0) or not (0.0 <= self.omit_fields <= 1.0):
            raise ValueError("change_fields and omit_fields must be values between 0.0 and 1.0 inclusive.")

        module = importlib.import_module(data_contract_path.replace(".py", "").replace("/", "."))
        self.original_model = getattr(module, data_contract_class_name)
        self.data_contract_factory = self._create_factory(self.original_model)

        if not self.active_injection:
            if not data_contract_test_data_path:
                raise ValueError("data_contract_test_data_path must be provided when active_injection is False.")

            with open(data_contract_test_data_path, "r", encoding="utf-8") as json_file:
                self.json_data_list = json.load(json_file)
                self.json_data = iter(self.json_data_list)

        self.initialized = True

    def _create_factory(self, model) -> type:
        """Create a factory to produce instances of the provided Pydantic model."""

        return type(model.__name__, (pydantic_factory.ModelFactory,), {"__model__": model})

    def _change_type_field(self, type_field: Type[Any]) -> Type[Any]:
        """
        Change the data type of the field based on a mapping, if active_injection is True.

        Args:
            type_field (Type[Any]): Original data type of the field.

        Returns:
            Type[Any]: New or original data type of the field.
        """
        if not self.active_injection:
            return type_field
        type_mappings = {int: str, str: int, datetime: str, bool: int, uuid.UUID: str}
        return type_mappings.get(type_field, type_field)

    def _modify_model_fields(self, model: Type[BaseModel]) -> Dict[str, Any]:
        """
        Modify the fields of a Pydantic model.

        Args:
            model (Type[BaseModel]): Original Pydantic model.

        Returns:
            Dict[str, Any]: Dictionary representing the modified fields of the model.
        """
        fields = {}
        for name, field in model.__fields__.items():
            if issubclass(field.type_, BaseModel):
                nested_model = create_model(f"nested_model_{name}", **self._modify_model_fields(field.type_))
                fields[name] = (nested_model, ...)
            else:
                if secrets.SystemRandom().random() > self.omit_fields:  # NOSONAR
                    #  https://rules.sonarsource.com/python/RSPEC-2245/
                    new_type = (
                        self._change_type_field(field.type_)
                        if secrets.SystemRandom().random() < self.change_fields  # NOSONAR
                        #  https://rules.sonarsource.com/python/RSPEC-2245/
                        else field.type_
                    )
                    fields[name] = (new_type, ...)
        return fields

    def modify(self):
        """Modify the original model's fields and recreate the factory."""
        modified_fields = self._modify_model_fields(self.original_model)
        new_model = create_model("new_model", **modified_fields)
        self.data_contract_factory = self._create_factory(new_model)

    def next(self) -> str | dict:
        """
        Generate the next piece of synthetic or test data based on the data contract model.

        Returns:
            str: JSON string representing the synthetic or test data.
        """
        if self.active_injection:
            if self.change_fields > 0.0 or self.omit_fields > 0.0:
                self.modify()

            new_model_instance = self.data_contract_factory.build()
            result = json.loads(new_model_instance.json(by_alias=self.use_alias))
        else:
            result = next(self.json_data, None)
            if result is None:
                self.json_data = iter(self.json_data_list)
                result = next(self.json_data)

        if self.add_data_contract:
            if self.only_payload_data:
                return {
                    "data_contract": self.data_contract_path,
                    "class_name": self.data_contract_class_name,
                    "payload": result.get("data", {}),
                }
            else:
                return {
                    "data_contract": self.data_contract_path,
                    "class_name": self.data_contract_class_name,
                    "payload": result,
                }

        if self.only_payload_data:
            return json.dumps(result.get("data", {}))
        return json.dumps(result)
