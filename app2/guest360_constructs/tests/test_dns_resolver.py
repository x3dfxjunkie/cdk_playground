"""
DNS Resolver Construct
"""
import pytest
import logging
import sys
import os
import yaml
import strongtyping
from aws_cdk.aws_ec2 import Vpc
from app.guest360_constructs.security_group import Guest360SecurityGroup
from app.guest360_constructs.tests.utils import print_template_on_debug

from aws_cdk import App, Stack, assertions, Token

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {"prefix": "lst-test_sg_something", "environment": "latest"}
ENVIRONMENT = {"region": "us-east-1", "account": "123456789"}

@pytest.fixture(name="stack")
def fixture_stack():
    app = App(context=TEST_CONTEXT)
    stack = Stack(app, env=ENVIRONMENT)
    yield stack