"""
AWS Cloud Map Construct
"""
import pytest
import logging
import sys
from app.guest360_constructs.service_discovery_namespace import Guest360ServiceDiscoveryNamespace
from app.guest360_constructs.tests.utils import print_template_on_debug

from aws_cdk import assertions, Token

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


def test_cloud_map_created(stack, constants):
    val = Guest360ServiceDiscoveryNamespace(stack, "TestCloudMap", {"name": "foo"})
    template = assertions.Template.from_stack(stack)
    print_template_on_debug(template, logger)
    template.resource_count_is(constants["AWSCLOUDMAP"], 1)
    assert Token.is_unresolved(val.namespace_hosted_zone_id)
