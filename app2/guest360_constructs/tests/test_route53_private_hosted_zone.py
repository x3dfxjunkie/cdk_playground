"""
Security Group Construct
"""
import pytest
import logging
import sys
import os
import yaml
from aws_cdk.aws_route53 import PrivateHostedZone
from app.guest360_constructs.route53_private_hosted_zone import Guest360PrivateHostedZone
from app.guest360_constructs.tests.utils import print_template_on_debug

from aws_cdk import App, Stack, assertions, Token

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_DOMAIN = "privatelink.snowflakecomputing.com"


def test_private_hosted_zone_created(stack, constants):
    Guest360PrivateHostedZone(stack, "TestPHZ", {"zone_name": TEST_DOMAIN})
    test = {"Name": f"{TEST_DOMAIN}."}
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
    template.has_resource_properties(constants["AWSHOSTEDZONE"], test)


def test_private_hosted_zone_created_no_dot(stack, constants):
    Guest360PrivateHostedZone(stack, "TestPHZA", {"zone_name": TEST_DOMAIN, "add_trailing_dot": False})
    test = {"Name": f"{TEST_DOMAIN}"}
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
    template.has_resource_properties(constants["AWSHOSTEDZONE"], test)


def test_private_hosted_zone_get_hosted_zone_arn(stack):
    val = Guest360PrivateHostedZone(stack, "TestPHZ", {"zone_name": TEST_DOMAIN})
    assert Token.is_unresolved(val.get_hosted_zone_arn)
    assert type(val.get_hosted_zone) == PrivateHostedZone


def test_private_hosted_zone_get_hosted_zone_id(stack):
    val = Guest360PrivateHostedZone(stack, "TestPHZ", {"zone_name": TEST_DOMAIN})
    assert Token.is_unresolved(val.get_hosted_zone_id)


def test_private_hosted_zone_get_from_lookup(stack):
    from_lookup = Guest360PrivateHostedZone.get_from_lookup(stack, "test", "foo.com")
    assert from_lookup.hosted_zone_id == "foo.com"


def test_private_hosted_zone_get_from_hosted_zone_id(stack):
    from_private_hosted_zone_id = Guest360PrivateHostedZone.get_from_hosted_zone_id(
        stack, "test", **{"hosted_zone_id": "foo"}
    )
    assert from_private_hosted_zone_id.hosted_zone_id == "foo"


def test_private_hosted_zone_get_from_hosted_zone_attribrutes(stack):
    from_private_hosted_zone_attributes = Guest360PrivateHostedZone.get_from_hosted_zone_attributes(
        stack, "test", **{"hosted_zone_id": "foo", "zone_name": "foo"}
    )
    assert from_private_hosted_zone_attributes.hosted_zone_id == "foo"


def test_private_hosted_zone_add_vpc(stack, constants):
    Guest360PrivateHostedZone(stack, "TestPHZ5", {"zone_name": TEST_DOMAIN, "extra_vpcs": ["vpc-54321"]})
    test = {"Name": f"{TEST_DOMAIN}."}
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
    template.has_resource_properties(constants["AWSHOSTEDZONE"], test)


def test_private_hosted_zone_bad_props(stack):
    with pytest.raises(TypeError):
        Guest360PrivateHostedZone(stack, "TestPHZ", {"zone_name": TEST_DOMAIN, "foo": "bar"})


def test_private_hosted_zone_bad_domain_count(stack):
    with pytest.raises(RuntimeError) as ex:
        Guest360PrivateHostedZone(stack, "TestPHZ", {"zone_name": TEST_DOMAIN * 13})
    assert "zone name cannot be more than 255 bytes long" in str(ex.value)


def test_private_hosted_zone_bad_domain_first_character(stack):
    Guest360PrivateHostedZone(stack, "TestPHZ", {"zone_name": "#.com"})


def test_private_hosted_zone_bad_domain_section_count(stack):
    with pytest.raises(RuntimeError) as ex:
        Guest360PrivateHostedZone(stack, "TestPHZ", {"zone_name": f"{'b'*63}.{'a'*64}.com"})
    assert "zone name labels cannot be more than 63 bytes long" in str(ex.value)
    Guest360PrivateHostedZone(stack, "TestPHZ1", {"zone_name": ".com"})


def test_private_hosted_zone_correct_domain_section_count(stack, constants):
    Guest360PrivateHostedZone(stack, "TestPHZ", {"zone_name": f"{'b'*63}.{'a'*63}.com"})
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSHOSTEDZONE"], 1)
