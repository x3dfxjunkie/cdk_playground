"""Unit testing for the configuration merge logic"""
import os
import pytest
import yaml

from functools import reduce
from app.src.ingestion.event_pipes.utils.merge_config import merge_configurations, load_and_render_base_template


def configuration_updates_have_been_applied(merged: dict, custom: dict) -> bool:
    dicts_match = True
    for k, v in custom.items():
        if isinstance(v, dict):
            dicts_match &= configuration_updates_have_been_applied(merged[k], v)
        elif isinstance(v, list):
            dicts_match &= all(x in merged[k] for x in v)
        else:
            dicts_match &= merged[k] == v
    return dicts_match


# TODO: make these parameters variables
@pytest.mark.parametrize(
    "base_configuration,custom_configuration",
    [
        ({"a": 1, "b": "x", "c": 3.5}, {"a": 2, "c": 4.2}),
        ({"a": [1, 2], "b": 3}, {"a": [1, 2, 3, 4]}),
        ({"a": [{"a": 2}], "b": 3}, {"a": [{"a": 5}]}),
        # TODO: Support this case
        # ({"a": [{"b": "c"}, {"d": "e"}]}, {"a": [{"d": "f"}]}),
        (
            {"a": 1, "b": "something", "c": ["this", "is", "a", "list"], "d": {"1": {"e": 3, "f": 4}, "2": 2}},
            {"d": {"1": {"e": 5, "f": 6}}},
        ),
    ],
)
def test_merge_with_overwrite(base_configuration, custom_configuration):
    merged = merge_configurations(base_configuration, custom_configuration)
    print(merged, "\n", custom_configuration)
    assert configuration_updates_have_been_applied(merged, custom_configuration)


def test_merge_list_of_dicts_inexact_match():
    # in this case, the custom config tries to override one entry in the list but because we're checking for the presence of all keys,
    # the custom configuration fails to apply
    base_config_yaml = """
    testing:
        endpoint_type: test
        engine_name: test
        settings:
            - timeout: 5
              some_other_config: temp
            - poll_interval: 10
              timeout: 10
              delay: 25
        data_list:
            - data: data1
              name: john
              age: 34
              address: 
                - test: something
                  name: data_value
                  street: test
    """
    custom_config_yaml = """
    testing:
        settings:
            - poll_interval: 10
              timeout: 20
        data_list:
            - data: data
              name: john
              address: 
                - test: something_data
                  name: data_value
                - test: something_data1
                  name: data_value1
            - data: data2
              name: john
              age: 34
              address: 
                - test: something_data
                  name: data_value
                - test: something_data1
                  name: data_value1
    """
    base_config = yaml.safe_load(base_config_yaml)
    custom_config = yaml.safe_load(custom_config_yaml)
    merged = merge_configurations(base_config, custom_config)
    assert not configuration_updates_have_been_applied(merged, custom_config)


@pytest.mark.parametrize(
    "custom_config, output",
    [
        ({"stack_extension": "dms_test", "ingest_pattern": "dms"}, "dms_test"),
        ({"stack_extension": "messaging_test", "ingest_pattern": "messaging"}, "messaging_test"),
        ({"stack_extension": "k2k_test", "ingest_pattern": "kinesis2kinesis"}, "k2k_test"),
    ],
)
def test_load_and_render_base_template(custom_config, output):
    stack_path = os.path.dirname(os.path.abspath(__file__)).split("/")
    while stack_path[-1] != "app":
        stack_path.pop()
    stack_path = "/".join(stack_path) + "/infrastructure/ingestion/config"
    base_config = load_and_render_base_template(
        stack_path, custom_config.get("stack_extension"), custom_config.get("ingest_pattern")
    )
    # Validates stack extension is properly render from Jinja
    assert base_config["stack_extension"] == output


def test_multi_element_configuration():
    base_config_yaml = """
    testing:
        endpoint_type: test
        engine_name: test
        data_list:
            - data: data1
              name: john
              age: 34
  """
    custom_config_yaml = """
  testing:
      data_list:
          - data: custom
            name: john
            age: 34
          - data: another_custom
            name: john
            age: 33
          - data: yet_another_custom
            name: john
            age: 34
          - data: super_custom
            name: john
            age: 31
  """
    base_config = yaml.safe_load(base_config_yaml)
    custom_config = yaml.safe_load(custom_config_yaml)
    merged = merge_configurations(base_config, custom_config)
    merged_list = merged["testing"]["data_list"]
    assert len(merged_list) == 4
    merged_values_from_dicts = reduce(lambda x, y: x | y, map(lambda x: set(x.values()), merged_list))
    assert all(
        x in merged_values_from_dicts for x in ("custom", "another_custom", "yet_another_custom", "super_custom")
    )
