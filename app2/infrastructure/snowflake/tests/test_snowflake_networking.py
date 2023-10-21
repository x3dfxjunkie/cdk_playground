"""
Snowflake L3 Construct
"""
import logging
import sys
import os
import yaml
from app.infrastructure.snowflake.snowflake_networking import Guest360SnowflakeNetworking
from app.guest360_constructs.tests.utils import print_template_on_debug

from aws_cdk import assertions, Token

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


def get_config(env):
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/../configs/{env}-snowflake.yaml",
        mode="r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)


def get_environment_config(env):
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/../../../configs/{env}-environment.yaml",
        mode="r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)


def test_snowflake_networking_created(stack, constants):
    val = Guest360SnowflakeNetworking(stack, "teststack")
    config = get_config(stack.node.get_context("environment"))["networking"]
    test_subnets = [
        subnet["id"]
        for subnet in get_environment_config(stack.node.get_context("environment"))["networking"][stack.region][
            "subnets"
        ]["private"]
    ]
    if config["feature_flag_enabled"]:
        assert val.get_feature_flag == True
        for item in config["accounts"]:
            if item["enabled"]:
                template = assertions.Template.from_stack(stack)
                print_template_on_debug(template, logger)
                template.resource_count_is(constants["AWSSECURITYGROUP"], 2)
                template.resource_count_is(constants["AWSVPCENDPOINT"], 1)
                template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
                template.resource_count_is(constants["AWSRECORDSET"], len(item["snowflake_urls"]))
                template.resource_count_is(constants["AWSRESOLVER"], 1)
                template.has_resource_properties(constants["AWSVPCENDPOINT"], {"SubnetIds": test_subnets})
    else:
        assert val.get_feature_flag == False


def test_mock_snowflake_networking_created(teststack, constants):
    val = Guest360SnowflakeNetworking(teststack, "mockstack")
    config = get_config(teststack.node.get_context("environment"))["networking"]
    if config["feature_flag_enabled"]:
        assert val.get_feature_flag == True
        for item in config["accounts"]:
            template = assertions.Template.from_stack(teststack)
            print_template_on_debug(template, logger)
            if item["enabled"]:
                template.resource_count_is(constants["AWSSECURITYGROUP"], 2)
                template.resource_count_is(constants["AWSVPCENDPOINT"], 1)
                template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
                template.resource_count_is(constants["AWSRECORDSET"], len(item["snowflake_urls"]))
                template.resource_count_is(constants["AWSRESOLVER"], 1)
            else:
                template.resource_count_is(constants["AWSRESOLVER"], 0)
                template.resource_count_is(constants["AWSSECURITYGROUP"], 0)
                template.resource_count_is(constants["AWSVPCENDPOINT"], 0)
                template.resource_count_is(constants["AWSHOSTEDZONE"], 0)
                template.resource_count_is(constants["AWSRECORDSET"], 0)
    else:
        assert val.get_feature_flag == False
