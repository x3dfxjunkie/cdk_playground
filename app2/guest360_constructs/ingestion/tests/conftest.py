import pytest
import aws_cdk
import os
from pathlib import Path

STACK_PATH = str(Path(os.getcwd()))
ENVIRONMENTS = ["load", "stage", "prod"]
ENV_SHORT = {"local": "lcl", "latest": "lst", "stage": "stg", "prod": "prd", "load": "lod"}


@pytest.fixture(params=ENVIRONMENTS)
def test_stack(request):
    environment = request.param
    test_app = aws_cdk.App()
    stack = aws_cdk.Stack(test_app, "TestStack", env=aws_cdk.Environment(account="123456789", region="us-east-1"))
    stack.node.set_context("region", "us-east-1")
    stack.node.set_context("stack_name", "test")
    stack.node.set_context("is_static_env", True)
    stack.node.set_context("stack_path", STACK_PATH)
    stack.node.set_context("environment", environment)
    stack.node.set_context("prefix", f"{ENV_SHORT[environment]}-use1-guest360")
    stack.node.set_context("prefix_global", f"{ENV_SHORT[environment]}-guest360")
    stack.is_primary_region = lambda: True
    yield stack
