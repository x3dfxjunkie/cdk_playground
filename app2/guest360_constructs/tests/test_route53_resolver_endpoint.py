"""
Route53 DNS Resolver Construct
"""
import pytest
import logging
import sys
import os
import yaml
from app.guest360_constructs.route53_resolver_endpoint import Guest360Route53ResolverEndpoint
from app.guest360_constructs.tests.utils import print_template_on_debug

from aws_cdk import assertions, Token

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

ENVIRONMENT_VARIABLES = {"region": "us-east-1", "account": "123456789"}
AWSROUTE53RESOLVER = "AWS::Route53Resolver::ResolverEndpoint"

def get_config(env):
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/../../configs/{env}-environment.yaml",
        mode="r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)


def test_resolver_created(stack):
    Guest360Route53ResolverEndpoint(
        stack, "TestResolver", {"name": "TestResolver", "security_group_ids": ["sg-123456"]}
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(AWSROUTE53RESOLVER, 1)
    template.has_resource_properties(AWSROUTE53RESOLVER, {"Direction": "INBOUND"})


def test_resolver_created_static_ip(teststack):
    if teststack.node.get_context("environment") == "test-local":
        with pytest.raises(ValueError) as exc:
            Guest360Route53ResolverEndpoint(
                teststack,
                "TestResolver",
                {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo1"},
            )
        assert "Resolver information is not set up in the environment configuration file" in str(exc.value)
    else:
        val = get_config(teststack.node.get_context("environment"))
        Guest360Route53ResolverEndpoint(
            teststack,
            "TestResolver",
            {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo"},
        )
        template = assertions.Template.from_stack(teststack)
        print_template_on_debug(template, logger)
        template.resource_count_is(AWSROUTE53RESOLVER, 1)
        template.has_resource_properties(AWSROUTE53RESOLVER, {"Direction": "INBOUND"})
        template.has_resource_properties(
            AWSROUTE53RESOLVER, {"IpAddresses": val["networking"][teststack.region]["resolvers"]["foo"]}
        )


def test_resolver_created_static_ip_no_resolver(teststack):
    if teststack.node.get_context("environment") == "test-local":
        with pytest.raises(ValueError) as exc:
            Guest360Route53ResolverEndpoint(
                teststack,
                "TestResolver",
                {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo1"},
            )
        assert "Resolver information is not set up in the environment configuration file" in str(exc.value)
    else:
        with pytest.raises(ValueError) as exc:
            Guest360Route53ResolverEndpoint(
                teststack,
                "TestResolver",
                {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo-bar"},
            )
        assert "resolver_config_tag not found" in str(exc.value)


def test_resolver_get_arn(teststack):
    if teststack.node.get_context("environment") == "test-local":
        with pytest.raises(ValueError) as exc:
            Guest360Route53ResolverEndpoint(
                teststack,
                "TestResolver",
                {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo1"},
            )
        assert "Resolver information is not set up in the environment configuration file" in str(exc.value)
    else:
        val = Guest360Route53ResolverEndpoint(
            teststack,
            "TestResolver",
            {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo"},
        )
        assert Token.is_unresolved(val.resolver_endpoint_arn)


def test_resolver_incorrect_entries(teststack):
    if teststack.node.get_context("environment") == "test-prod":
        with pytest.raises(ValueError) as exc:
            Guest360Route53ResolverEndpoint(
                teststack,
                "TestResolver",
                {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo1"},
            )
        assert "resolver_config_tag not found" in str(exc.value)
    elif teststack.node.get_context("environment") == "test-local":
        with pytest.raises(ValueError) as exc:
            Guest360Route53ResolverEndpoint(
                teststack,
                "TestResolver",
                {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo1"},
            )
        assert "Resolver information is not set up in the environment configuration file" in str(exc.value)
    else:
        with pytest.raises(KeyError) as exc:
            Guest360Route53ResolverEndpoint(
                teststack,
                "TestResolver",
                {"name": "TestResolver", "security_group_ids": ["sg-123456"], "resolver_config_tag": "foo1"},
            )
        assert "Ip" in str(exc.value)


def test_add_tags_to_resolver(stack):
    tags = [{"key": "foo", "value": "bar"}, {"key": "bar", "value": "foo"}]
    tags_aws = [{"Key": "bar", "Value": "foo"}, {"Key": "foo", "Value": "bar"}]  # sorted and caps
    Guest360Route53ResolverEndpoint(
        stack,
        "TestResolver",
        {"name": "TestResolver", "security_group_ids": ["sg-123456"], "tags": tags},
    )
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(AWSROUTE53RESOLVER, 1)
    template.has_resource_properties(AWSROUTE53RESOLVER, {"Direction": "INBOUND"})
    template.has_resource_properties(AWSROUTE53RESOLVER, {"Tags": tags_aws})
