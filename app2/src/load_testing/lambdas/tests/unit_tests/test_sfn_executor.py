"""
Test Lambda to execute the sfn 
"""
import pytest
import boto3
import os

from moto import mock_stepfunctions
from app.src.load_testing.lambdas.sfn_executor import lambda_function


# pylint: disable=W0613, W0621
@pytest.fixture
def mock_os_environment(monkeypatch):
    monkeypatch.setenv("SFN_ARN", "arn:aws:states:us-east-1:123456789012:stateMachine:test_state_machine")


@mock_stepfunctions
def test_lambda_handler(mock_os_environment):
    # Create a Step Functions client
    client = boto3.client("stepfunctions", region_name="us-east-1")

    # Mock the creation of the state machine
    client.create_state_machine(
        name="test_state_machine",
        definition='{"Comment": "Test State Machine", "StartAt": "State1", "States": {"State1": {"Type": "Pass", "End": True}}}',
        roleArn="arn:aws:iam::123456789012:role/test_state_machine",
    )

    # Invoke the lambda_handler
    event = {"bucket_path": "/local", "test_type": "load"}
    handler = {}
    lambda_function.lambda_handler(event, handler)

    executions = client.list_executions(stateMachineArn=os.getenv("SFN_ARN"))["executions"]
    print(executions)
    assert len(executions) == 1
    assert executions[0]["stateMachineArn"] == os.getenv("SFN_ARN")
