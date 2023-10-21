"""
Tests for Guest360IamRole
"""
import hashlib
import yaml
import logging
import sys
import os
import yaml
from app.guest360_constructs.construct_360 import Construct360
from aws_cdk import App, Stack, assertions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
test_context = {
    "prefix_global": "lst-pytest",
}


def dump_template():
    app = App(context=test_context)
    stack = Stack(app)
    Construct360(scope=stack, construct_id="IAMRole")
    template = assertions.Template.from_stack(stack)
    return template


def test_construct_initialized():
    app = App(context=test_context)
    stack = Stack(app)
    Construct360(scope=stack, construct_id="IAMRole")
    template = assertions.Template.from_stack(stack)

    logger.debug(yaml.dump(template.to_json()))


def test_pass_id():
    app = App(context=test_context)
    stack = Stack(app)
    id_to_test = "SomeName"
    test_construct = Construct360(scope=stack, construct_id=id_to_test)
    pass_id = test_construct.pass_id
    assert isinstance(pass_id, str)
    assert pass_id.isalnum
    assert pass_id == "Construct360" + hashlib.sha1(id_to_test.encode()).hexdigest()[:5]

    template = assertions.Template.from_stack(stack)

    logger.debug(yaml.dump(template.to_json()))


def test_construct360_helpers(stack, constants):
    test_construct = Construct360(scope=stack, construct_id="foo")
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/../../configs/{test_construct._environment}-environment.yaml",
        mode="r",
        encoding="utf-8",
    ) as file:
        config = yaml.safe_load(file)
    assert test_construct._vpc_id == config["networking"][test_construct._region]["vpc"]["id"]
    assert test_construct._routable_subnets == config["networking"][test_construct._region]["subnets"]["private"]
    assert (
        test_construct._nonroutable_subnets == config["networking"][test_construct._region]["subnets"]["non-routable"]
    )
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/../../configs/constants.yaml",
        mode="r",
        encoding="utf-8",
    ) as file:
        constants = yaml.safe_load(file)
    assert test_construct._disney_internal_ipv4_cidr_blocks == constants["disney_internal_cidr_blocks"]["ipv4"]
    assert test_construct._account_numbers == constants["account_ids"][test_construct._environment]


if __name__ == "__main__":  # pragma: no cover
    _template = dump_template()
    print(yaml.dump(_template.to_json()))
