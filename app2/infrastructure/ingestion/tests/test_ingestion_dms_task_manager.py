"""ingestion_dms_task_manager Stack tests
"""
import logging
import sys
import yaml
import pytest
from unittest.mock import patch
from aws_cdk import App, aws_lambda
from aws_cdk.assertions import Template
from app.infrastructure.ingestion.ingestion_dms_task_manager import DMSTaskManager

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

STACK_ID = "TestStack"

SHORT_ENV = {
    "ephemeral": "lst",
    "latest": "lst",
    "stage": "stg",
    "load": "lod",
    "prod": "prd",
}


@pytest.mark.timeout(30, method="signal")
@pytest.mark.parametrize("environment", ["latest", "load", "stage", "prod"])
def test_dms_task_manager(environment):
    short_env = SHORT_ENV[environment]
    test_context = {"environment": environment, "prefix": f"{short_env}-use1-guest360"}
    app = App(context=test_context)

    # Our goal here is validate the creation of the AWS resources.
    # The tests for the lambda code are executed at this location: app/src/ingestion/dms:dms_src_tests
    with patch(
        "app.infrastructure.ingestion.ingestion_dms_task_manager.aws_lambda.Code.from_asset",
        lambda *args: aws_lambda.Code.from_inline("""mytestcode"""),
    ):
        dms_manager_stack = DMSTaskManager(app, STACK_ID, config={})

    # render template
    template = Template.from_stack(dms_manager_stack)
    logger.debug(yaml.dump(template.to_json()))

    template.resource_count_is("AWS::StepFunctions::StateMachine", 1)
    template.resource_count_is("AWS::Lambda::Function", 2)
    template.resource_count_is("AWS::Events::Rule", 1)
    template.resource_count_is("AWS::DynamoDB::Table", 1)
