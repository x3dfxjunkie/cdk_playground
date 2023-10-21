""""Pytest configuration file for data_contracts module."""

from datetime import datetime, date, time
from enum import Enum
from itertools import chain
from logging import Logger
from string import Template
from typing import List, TypeVar, Callable, Type, get_type_hints
import warnings
from dateutil.parser import parse
from pydantic import BaseModel, parse_obj_as
from pydantic.fields import ModelField
from pydantic.main import ModelMetaclass
from typing_inspect import is_optional_type


T = TypeVar("T", bound=ModelMetaclass)


def is_null(input_str: str) -> bool:
    """Returns if a field is '', 'null' or 'None'

    Args:
        input_str (str): any string representation.
    Returns:
        bool: True if the input_str is 'null' or 'None'
    """
    return input_str in {"", "null", "None"}


def is_datetime(input_str: str) -> bool:
    """Returns if a string is a representation of a datetime

    Args:
        input_str (str): any string representation.
    Returns:
        bool: True if the input_str is a datetime representation.
    """
    # Checks for the presence of a colon (typical in time components)
    if ":" in input_str:
        try:
            default_datetime = datetime.min
            parsed_datetime = parse(input_str, default=default_datetime)
            date_val = parsed_datetime.date()
            time_val = parsed_datetime.strftime("%H:%M:%S")
            # Validates that date and time part was present on original string, i.e, when not matching with the default date, which is autocompleted when not date is found or when checking that the time is present in the original string.
            return date_val != date.min and time_val in input_str
        except ValueError:
            pass
    return False


def is_date(input_str: str) -> bool:
    """Returns if a string is a representation of a date

    Args:
        input_str (str): any string representation.
    Returns:
        bool: True if the input_str is a date representation.
    """
    if input_str.count("-") == 2:
        try:
            # Converts to datetime and if it's a date always adds the default time (00:00:00).
            # It extracts the time portion without milliseconds to check if the value exists in the step ahead.
            parsed_time = parse(input_str).strftime("%H:%M:%S")
            # Validates that time portion was not present on the original string since 'dateutil.parse' adds the min time to dates.
            # For example, if the input string contains 00:00:00 it returns false.
            return parsed_time not in input_str
        except ValueError:
            pass
    return False


class ContractsAgainstSampleTests:
    """Test that the data contracts can be parsed against the sample data."""

    def __init__(self, dataclass: ModelMetaclass, sample_data: dict, logger: Logger):
        self.dataclass = dataclass
        self.sample_data = sample_data
        self.logger = logger
        self.data_instances = parse_obj_as(List[dataclass], sample_data)

    def _traverse_dataclass(self, assertion) -> None:
        """Traverse the dataclass and apply the assertion to each field.

        Args:
            assertion (callable): a function that executes an assertion.
        """
        # Start the traversal by calling _exec_traverse_fields with initial parameters
        self._exec_traverse_fields(self.dataclass, self.data_instances, assertion)

    def _exec_traverse_fields(self, dataclass, data_instances, assertion):
        """Recursively traverse the dataclass and apply the assertion to each field.

        Args:
            dataclass: The dataclass to traverse.
            data_instances: The data instances to process.
            assertion (callable): A function that executes an assertion.
        """
        for _, field in dataclass.__fields__.items():
            self._apply_assertion(dataclass, data_instances, field, assertion)

            if issubclass(field.type_, BaseModel):
                self._traverse_base_model_field(dataclass, field, data_instances, assertion)

    def _apply_assertion(self, dataclass, data_instances, field, assertion):
        """Apply the assertion function to a field."""
        assertion(dataclass, data_instances, field)

    def _traverse_base_model_field(self, dataclass, field, data_instances, assertion):
        """Traverse a field of type BaseModel."""
        field_name = field.name
        if "List" in str(get_type_hints(dataclass)[field_name]):
            data_instances = filter(lambda data_instance: data_instance, data_instances)
            # Get the value of the field for each data instance
            sub_instance_list = chain.from_iterable(
                map(
                    lambda data_instance, field_name=field_name: getattr(data_instance, field_name) or [],
                    data_instances,
                )
            )
            # Recursively call exec_traverse_dataclass for the sub-field type
            self._exec_traverse_fields(field.type_, sub_instance_list, assertion)
        else:
            data_instances = filter(lambda data_instance: data_instance is not None, data_instances)
            # Converted to list since the (lazy) content - data instances of this iterable will be used more than once by every field inside classes that inherit from BaseModel like Data, Metadata and other custom defined.
            # In this way, we avoid to get a empty iterable on the second time we call this variable during the next _exec_traverse_fields() execution (next step)
            sub_instance_list = self._get_sub_instance_list(data_instances, field_name)
            if not sub_instance_list:
                self.logger.warning(f"No data found for field '{field_name}' of dataclass {dataclass}")
            else:
                self._exec_traverse_fields(field.type_, sub_instance_list, assertion)

    def _get_sub_instance_list(self, data_instances, field_name):
        """Get the sub-instance list for a field."""
        return list(
            map(lambda data_instance, field_name=field_name: getattr(data_instance, field_name), data_instances)
        )

    @staticmethod
    def _assert_optional_fields(dataclass, data_instances, field) -> None:
        """Assert that optional fields are optional."""

        if not field.required:
            field_is_present = []
            field_is_none = []
            for data_instance in data_instances:
                if not data_instance:
                    field_is_present.append(False)
                    field_is_none.append(False)
                    continue
                rendered_instance = data_instance.dict(exclude_unset=True)
                if field.name in rendered_instance:
                    field_is_present.append(True)
                    field_is_none.append(rendered_instance[field.name] is None)
                else:
                    field_is_present.append(False)
                    field_is_none.append(False)
            assert set(field_is_present) != {
                True,
            } or set(field_is_none) != {
                False,
            }, f"Field '{field.name}' of dataclass {dataclass} is not optional"

    def assert_optional_fields(self):
        """Wrapper for _assert_optional_fields."""
        self._traverse_dataclass(self._assert_optional_fields)

    @staticmethod
    def _assert_datetime_and_date_types(dataclass, data_instances, field) -> None:
        """Assert that strings representing timestamps and date are correctly assigned to field types."""

        # This test applies to all str fields in a contract model.
        if field.type_ is str:
            # Filters just completely None instances of the dataclass, not for the field.
            data_instances = list(filter(lambda data_instance: data_instance is not None, data_instances))

            # It converts the instances to dic objects and excludes all None values for the field.  When a value is not present for a record or the value has is null in the payload, pydantic automatically autocompletes the value with None. So this shouldn't throw an exception.
            rendered_instances = filter(
                lambda data_instance: data_instance.get(field.name) is not None,
                map(lambda data_instance: data_instance.dict(), data_instances),
            )

            # Since 'field_values' variable will be used more than once is converted to list to not being exhausted when is_datetime_test is evaluated.
            field_values = list(
                map(lambda rendered_instance: str(rendered_instance.get(field.name)), rendered_instances)
            )
            is_null_text = map(is_null, field_values)
            is_datetime_test = map(is_datetime, field_values)
            is_date_test = map(is_date, field_values)
            # If after removing all the None values for the field the list is empty.
            if not field_values:
                warnings.warn(f"There are no examples for the field {field.name} to test date/datetime", UserWarning)
            elif all(is_null_text) or not is_null_text:
                warnings.warn(f"All the samples for the field {field.name} are null", UserWarning)
            else:
                assert not all(
                    is_datetime_test
                ), f"Field '{field.name}' of dataclass {dataclass} is of type {field.type_}, but all sample values are strings in datetime format."

                assert not all(
                    is_date_test
                ), f"Field '{field.name}' of dataclass {dataclass} is of type {field.type_}, but all sample values are strings in date format"

    def assert_datetime_and_date_types(self):
        """Wrapper for _assert_datetimes."""
        self._traverse_dataclass(self._assert_datetime_and_date_types)


class FieldSyntaxTests:
    """Test that all fields have the required parameters."""

    def __init__(self, dataclass, logger):
        self.dataclass = dataclass
        self.logger = logger

    def _traverse_dataclass(self, assertion: Callable[[Type[T], ModelField], None]) -> None:
        """Traverse the dataclass and apply the assertion to each field.

        Args:
            assertion (callable): a function that executes an assertion.
        """

        def exec_traverse_dataclass(dataclass, assertion, logger):
            for _, field in dataclass.__fields__.items():
                assertion(dataclass, field)
                field_type = field.type_
                if issubclass(field_type, BaseModel):
                    exec_traverse_dataclass(field_type, assertion, logger)

        exec_traverse_dataclass(self.dataclass, assertion, self.logger)

    @staticmethod
    def _assert_optional_default_is_none(dataclass: Type[T], field: ModelField) -> None:
        """Assert that optional fields have default value None."""

        if field.field_info.default is None:
            assert is_optional_type(
                field.annotation
            ), f"Field '{field.name}' from dataclass '{dataclass}' has default value None but is not optional."
        else:
            assert not is_optional_type(
                field.annotation
            ), f"Field '{field.name}' from dataclass '{dataclass}' has default value {field.field_info.default} but is optional."

    def assert_optional_default_is_none(self):
        """Wrapper for _assert_optional_default_is_none."""

        self._traverse_dataclass(self._assert_optional_default_is_none)

    @staticmethod
    def _assert_field_parameters_exist(dataclass: Type[T], field: ModelField) -> None:
        # if not issubclass(dataclass, Enum):

        assert field.field_info.alias, f"Field '{field.name}' from dataclass '{dataclass}' has no 'alias' parameter."
        if not issubclass(field.type_, BaseModel):
            assert (
                "example" in field.field_info.extra
            ), f"Field '{field.name}' from dataclass '{dataclass}' has no 'example' parameter."
            assert (
                "guest_identifier" in field.field_info.extra
            ), f"Field '{field.name}' from dataclass '{dataclass}' has no 'guest_identifier' parameter."
            assert (
                "transaction_identifier" in field.field_info.extra
            ), f"Field '{field.name}' from dataclass '{dataclass}' has no 'transaction_identifier' parameter."
            assert (
                "identifier_tag" in field.field_info.extra
            ), f"Field '{field.name}' from dataclass '{dataclass}' has no 'identifier_tag' parameter."

    def assert_field_parameters_exist(self):
        """Wrapper for _assert_field_parameters_exist."""

        self._traverse_dataclass(self._assert_field_parameters_exist)

    @staticmethod
    def _assert_example_type(dataclass: Type[T], field: ModelField) -> None:
        if not issubclass(field.type_, BaseModel):
            field_type = field.type_
            field_example = field.field_info.extra["example"]
            error_msg = Template(
                f"Field {field.name} from dataclass {dataclass} is of type {field_type} but has example of type $example_type"
            )
            error_msg_for_bad_list = Template(
                f"Field {field.name} from dataclass {dataclass} is of type $type but has an example with the following unexpected $issue: $values"
            )
            full_type = str(get_type_hints(dataclass)[field.name])
            if "List" in full_type:
                example_is_a_list = isinstance(field_example, list)
                if example_is_a_list:
                    not_expected_values = list(
                        filter(lambda v, field_type=field_type: not isinstance(v, field_type), field_example)
                    )
                    assert not not_expected_values, error_msg_for_bad_list.substitute(
                        type=full_type, issue="values", values=not_expected_values
                    )
                else:
                    raise AssertionError(
                        error_msg_for_bad_list.substitute(type=full_type, issue="type", values=type(field_example))
                    )
            elif issubclass(field_type, Enum):
                enum_types = [type(choice.value) for choice in field_type]
                assert {type(field.field_info.extra["example"])} == set(
                    enum_types
                ), f"Field '{field.name}' from dataclass {dataclass} has example {field.field_info.extra['example']} not matching the Enum values"
            elif isinstance(field_example, str) and is_datetime(field_example):
                assert field_type is datetime, error_msg.substitute(example_type=datetime)
            elif isinstance(field_example, str) and is_date(field_example):
                assert field_type is date, error_msg.substitute(example_type=date)
            else:
                assert isinstance(field_example, field_type), error_msg.substitute(example_type=type(field_example))

    def assert_example_type(self):
        """Wrapper for _assert_example_type."""

        self._traverse_dataclass(self._assert_example_type)


class RootModelTests:
    """Test root model."""

    def __init__(self, dataclass: Type[BaseModel], logger):
        self.dataclass = dataclass
        self.logger = logger
        self.root_class_config = self.dataclass.Config()

    def assert_root_model_config_tags(self):
        """Assert that the root model has the required config tags."""
        config = self.root_class_config

        optional_tags = ["description", "timezone", "pi_category", "isps", "financial_data"]
        for tag in optional_tags:
            if not hasattr(config, tag):
                self.logger.warning(f"Optional config tag {tag} not found.")

        mandatory_tags = ["stream_name", "unique_identifier", "key_path_name", "key_path_value"]
        for tag in mandatory_tags:
            assert hasattr(
                config, tag
            ), f"Mandatory attribute '{tag}' in root dataclass config {self.dataclass} not found"

    def assert_unique_identifier_is_list_of_strings(self):
        """Assert that the tag 'unique_identifier' is of type List"""

        unique_identifier = self.root_class_config.unique_identifier
        assert isinstance(
            unique_identifier, list
        ), f"Root dataclass config 'unique_identifier' from {self.dataclass} is not a List, but a {type(unique_identifier)}"
        assert all(
            isinstance(item, str) for item in unique_identifier
        ), f"Root dataclass config 'unique_identifier' from {self.dataclass} contains non-string elements"
        if not unique_identifier:
            warnings.warn(
                f"Root dataclass config 'unique_identifier' from {self.dataclass} is empty, suggesting this contract does not have a unique identifier. Is that right?",
                UserWarning,
            )

    def assert_unique_identifier_keys_exist(self):
        """Assert that all unique identifier keys exist in the contract"""

        assertion_msgs = {
            "inexistent_key": Template(
                "The unique identifier key '$key' does not exist in data contract $data_contract"
            ),
            "key_type_error": Template(
                "The provided unique identifier key '$key' for data contract $data_contract shouldn't be of type BaseModel"
            ),
        }

        def field_exists(dataclass: Type[BaseModel], path: str) -> tuple:
            field_names = path.split(".")
            field_name = field_names.pop(0)
            field = [field for _, field in dataclass.__fields__.items() if field.alias == field_name]
            if field:
                field_value = field[0].type_
                if issubclass(field_value, BaseModel):
                    path = ".".join(field_names)
                    if not path:
                        return False, assertion_msgs["key_type_error"]
                    return field_exists(field_value, path)
                else:
                    return True, ""
            return False, assertion_msgs["inexistent_key"]

        unique_identifier = self.root_class_config.unique_identifier
        for key in unique_identifier:
            result, message = field_exists(self.dataclass, key)
            assert result, message.substitute(key=key, data_contract=self.dataclass)
