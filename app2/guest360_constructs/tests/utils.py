import json
import yaml
from typing import Literal, Union
import logging

from aws_cdk import assertions


def print_template_on_debug(
    template: assertions.Template,
    logger: logging.Logger,
    print_type: Literal["both", "yaml", "json"] = "both",
    print_sections: Union[tuple, list, Literal["*"]] = ("Resources",),  # Resources, Conditions, Mappings, Outputs, etc.
    include_resource_types: Union[tuple, list] = ("*",),
    exclude_resource_types: Union[tuple, list] = (),
    json_indent: int = 2,
) -> None:
    """
    Helper for test debugging.
    Run with `pytest [file name] --log-cli-level=DEBUG`

    Set print_sections to ["*"] to print whole template
    """

    template = template.to_json()

    # Cull sections
    if print_sections != ["*"] and print_sections != "*":
        template = {k: v for k, v in template.items() if k in print_sections}

    # Can include only resource types if desired
    if include_resource_types != ("*",) and include_resource_types != ["*"]:
        template["Resources"] = {k: v for k, v in template["Resources"].items() if v["Type"] in include_resource_types}

    # Can ignore resource types if desired
    if exclude_resource_types:
        template["Resources"] = {
            k: v for k, v in template["Resources"].items() if v["Type"] not in exclude_resource_types
        }

    # Print
    if print_type.lower() in ["yaml", "yml", "both"]:
        logger.debug(f"\n{yaml.dump(template)}")
    if print_type.lower() in ["json", "both"]:
        logger.debug(f"\n{json.dumps(template, indent=json_indent)}")
