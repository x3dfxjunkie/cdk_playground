"""
# Case A - lists overwritten. Assumptions
# 1. Types in base will always be same type in incoming/new config (if exists in new)
# 2. Any new list will be over-written by new config
#
# def merge_dict(base: dict, new: dict):
# for thing in new dict:
# # if the thing is a dictionary also exists as dictionary in base:
# # # merge_dict(base_thing, new_thing) (recurse)
# # if the thing is a list:
# # # merge_dict(base_list, new_list)
# # else:
# # # base thing = new thing (not a dict)

# Case B - lists merged. Assumptions
# 1. Types in base will always be same type in incoming/new config (if exists in new)
# 2. Any new list will append to base if item is different, otherwise keep unique elements
# 3. We have identifiers for list elements (at least for dictionaries)
# def merge_dict_(base: dict, new: dict):
# for thing in new dict:
# # if the thing is a dictionary also exists as dictionary in base:
# # # merge_dict(base_thing, new_thing) (recurse)
# # if the thing is a list:
# # # merge_lists()
# # else:
# # # base thing = new thing (not a list or dict)

# def merge_lists(base: list, new: list):
# for element in new:
# # if element is dict:
"""
import copy
from jinja2 import Environment, FileSystemLoader
from functools import reduce
from pathlib import Path
from yaml import unsafe_load
from itertools import zip_longest


class BaseConfigurationNotFound(Exception):
    """Custom exception for base configuration file not being found"""


def merge_configurations(base: dict, custom: dict) -> dict:
    merged = copy.deepcopy(base)
    _merge_with_overwrite(merged, custom)
    return merged


def extend_dms_tasks(base: dict, custom: dict):
    """
    This function extends the template settings of DMS replication tasks
    and merges them with custom DMS task settings.

    Args:
        base (dict): Base configuration dictionary
        custom (dict): Custom configuration dictionary
    """
    base_dms_repl_task = base["pattern_instances"][0]["resources"]["dms_repl_task"]
    custom_dms_repl_tasks = custom["pattern_instances"][0]["resources"]["dms_repl_task"]

    # Merge the configurations, filling-in missing values and create the merged tasks list
    merged_tasks = []
    for base_task, custom_task in zip_longest(
        base_dms_repl_task, custom_dms_repl_tasks, fillvalue=base_dms_repl_task[0]
    ):
        merged_tasks.append(merge_configurations(base_task, custom_task))

    # Update the custom dictionary with the merged tasks
    custom["pattern_instances"][0]["resources"]["dms_repl_task"] = merged_tasks

    return custom


def _is_primitive(value) -> bool:
    return isinstance(value, (str, int, float, bool)) or value is None


def _is_list_of_primitives(l: list) -> bool:
    """
    is a list full of primitives?
    """
    return reduce(lambda x, y: x and y, map(_is_primitive, l))


def _merge_with_overwrite(base: dict, custom: dict) -> None:
    """
    Function for merging a base configuration dictionary and a custom configuration dictionary,
    where any key/value pairs in custom should overwrite the corresponding key/value pairs in base

    Args:
        base (dict): Base configuration dictionary
        custom (dict): Custom configuration dictionary
    """
    for key, custom_value in custom.items():
        if isinstance(base.get(key), dict) and isinstance(custom_value, dict):
            # with dictionaries, recurse
            _merge_with_overwrite(base[key], custom_value)
        elif isinstance(base.get(key), list) and isinstance(custom_value, list):
            if _is_list_of_primitives(base[key]) and _is_list_of_primitives(custom_value):
                base[key] = list(set(base[key] + custom_value))
            else:
                # Assumption: list of non-primitive elements have 1 element only
                # TODO: support multiple non-primitive types
                #
                base[key].extend(
                    [{} for _ in range(len(custom_value) - len(base[key]))]
                )  # Extend the existing list with empty dictionaries
                for i, sub_dict in enumerate(custom_value):
                    _merge_with_overwrite(base[key][i], sub_dict)
        else:
            # we're dealing with primitives or the case where base doesn't have key
            base[key] = custom_value


def load_and_render_base_template(
    config_dir: str, stack_extension: str = "dms_default", ingest_pattern: str = None
) -> dict:
    base_config_path = f"{config_dir}/pipelines/base/"
    environment = Environment(autoescape=True, loader=FileSystemLoader(base_config_path))
    base_template_file = f"{ingest_pattern}.yaml"

    if Path(f"{base_config_path}{base_template_file}").is_file():
        template = environment.get_template(base_template_file)
        content = template.render(stack_extension=stack_extension)
        base_config = unsafe_load(content)
        return base_config
    else:
        raise BaseConfigurationNotFound(
            f"Base configuration template file not found at {base_config_path}{base_template_file}"
        )
