"""Testing module for lambda authorizer"""
import json
import logging
import os
import sys
from pathlib import Path

import aws_cdk
import pytest
from aws_cdk.assertions import Template

from app.guest360_constructs.data_service.lambda_authorizer.lambda_authorizer import LambdaAuthorizer

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

directory = os.path.dirname(os.path.realpath(__file__))

# use cop.deepcopy create new object so original is kept intact


SCOPE_MAP = """{
    "authorization": [
        {
            "authType": "pattern",
            "urlPattern": "/api/v1/experiences/*",
            "id": 1,
            "authToken": true,
            "gdsEnabled": false,
            "scopes": [
                {
                    "method": "GET",
                    "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-ia-roz-ccpa"
                    ]
                }
            ]
        }
    ]
}"""


class StackTest(aws_cdk.Stack):
    """
    create test stack in order to instantiate the aws construct
    """

    def __init__(self, scope, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, env=kwargs.get("env"))
        stack = aws_cdk.Stack.of(self)
        stack_path = str(Path(os.getcwd()).parents[0])
        region = stack.region.lower()
        self.node.set_context("environment", "local")
        LambdaAuthorizer(
            self,
            construct_id="authorizer-lambda-construct",
            stack_path=stack_path,
            stack_prefix="test",
            region=region,
            lambda_environment={},
            scope_map_json=SCOPE_MAP,
            authz_validate_url="https://stg.authorization.go.com/validate/",
        )


class TestLambdaAuthorizer:
    """Testing lambda authorizer"""

    stack_name = "TestStack"

    @pytest.fixture
    def stack_test(self):
        cdk_app = aws_cdk.App()

        # use cop.deepcopy create new object so original is kept intact
        stack_test = StackTest(
            cdk_app,
            self.stack_name,
            env=aws_cdk.Environment(account="0" * 12, region="us-east-1"),
        )
        yield stack_test

    def test_instantiate_construct(self, stack_test):
        """
        create dummy aws_cdk app and instantiate the StackTest with construct
        """
        # render template
        template = Template.from_stack(stack_test)
        logger.debug(json.dumps(template.to_json(), indent=2))
