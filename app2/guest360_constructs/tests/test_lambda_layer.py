"""test for lambda layer construct
"""
import json
import logging
import sys

import aws_cdk
import pytest
from aws_cdk import assertions

from app.guest360_constructs.lambda_layer_construct import Guest360LambdaLayer

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


class TestLambdaLayer:
    """Test class for Lambda Layer Construct"""

    stack_id = "TestStack"

    @pytest.mark.timeout(90, method="signal")
    def test_lambda_layer_created(self):
        test_app = aws_cdk.App()
        stack = aws_cdk.Stack(test_app, self.stack_id, env=aws_cdk.Environment(account="123456789", region="us-east-1"))
        stack.node.set_context("environment", "local")
        stack.node.set_context("prefix", "test-prefix-use1")
        stack.node.set_context("prefix_global", "test-prefix")
        stack.node.set_context("region", "us-east-1")

        # 'pragma: allowlist secret'
        props = {
            "lambda_layer": {
                "layer_name": "local-test",
                "cross_account_access": True,
                "cross_account_id": ["1234567789"],
                "description": "lambda layer test",
                "code": "",
                "compatible_runtimes": aws_cdk.aws_lambda.Runtime.PYTHON_3_9,
            }
        }

        Guest360LambdaLayer(stack, "test-layer", props)

        template = assertions.Template.from_stack(stack)

        logger.debug(json.dumps(template.to_json(), indent=2))

        template.resource_count_is("AWS::Lambda::LayerVersion", 1)
