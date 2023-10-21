"""Module for Data Contract Unit testing"""

from typing import List

from pydantic import parse_obj_as


class TestModel:
    """Test Model"""

    def test_source_data_contract(self, contract_model, sample, logger):
        """Test that the data contract can be parsed."""
        contract_model.update_forward_refs()
        data_contract = parse_obj_as(List[contract_model], sample)
        logger.info(data_contract[0].json(indent=4, by_alias=True))

    def test_optional_fields_are_optional(self, contract_against_sample_tests):
        """Test that optional fields are optional."""
        contract_against_sample_tests.assert_optional_fields()

    def test_string_fields_are_datetime_or_date(self, contract_against_sample_tests):
        """Test that fields of type string are in fact a datetime based on sample values."""
        contract_against_sample_tests.assert_datetime_and_date_types()

    def test_assert_optional_default_is_none(self, field_syntax_tests):
        """Test that optional fields have a default of None."""
        field_syntax_tests.assert_optional_default_is_none()

    def test_assert_field_parameters_exist(self, field_syntax_tests):
        """Test that all fields have the required tags."""
        field_syntax_tests.assert_field_parameters_exist()

    def test_assert_example_type(self, field_syntax_tests):
        """Test example field types."""
        field_syntax_tests.assert_example_type()

    def test_root_model_config_tags(self, root_model_tests):
        """Test if the root model has the correct config tags."""
        root_model_tests.assert_root_model_config_tags()

    def test_root_unique_identifier_is_list_of_strings(self, root_model_tests):
        """Test if the unique identifier is of type list."""
        root_model_tests.assert_unique_identifier_is_list_of_strings()

    def test_unique_identifier_keys_exist(self, root_model_tests):
        """Test if unique identifier keys exist."""
        root_model_tests.assert_unique_identifier_keys_exist()
