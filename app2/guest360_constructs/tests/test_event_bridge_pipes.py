"""
unit tests for event bridge pipes
"""
import pytest
from aws_cdk import App, Stack, Aspects
from aws_cdk.assertions import Template

from cdk_nag import AwsSolutionsChecks

from app.guest360_constructs.event_bridge_pipes import Guest360EventBridgePipe, InvalidPipePropertyParameterError
from app.guest360_constructs.enums.event_bridge_pipe_states import EventBridgePipeState

TEST_CONTEXT = {"prefix_global": "lst-teststack", "prefix": "lst-teststack-use1", "environment": "local"}
CLOUDWATCH_ALARM_RESOURCE = "AWS::CloudWatch::Alarm"
SOURCE_ARN = "arn:aws:kinesis:us-east-1:123456789:test:TestSourceKinesis"
TARGET_ARN = "arn:aws:kinesis:us-east-1:123456789:test:TestTargetKinesis"
ROLE_ARN = "arn:aws:eventbridgepipes:us-east-1:123456789:secret:TestSecret"


@pytest.fixture(scope="module")
def app_stack():
    app = App(context=TEST_CONTEXT)
    aspects = Aspects.of(app)
    aspects.add(AwsSolutionsChecks(verbose=True))
    stack = Stack(app)
    yield stack


def test_event_bridge_pipe_create_success(app_stack):  # pylint: disable=W0621
    props = {
        "name": "test",
        "pipe_source_parameters": {},
        "pipe_target_parameters": {},
        "role_arn": ROLE_ARN,
        "source_arn": SOURCE_ARN,
        "target_arn": TARGET_ARN,
    }
    Guest360EventBridgePipe(app_stack, construct_id="test_event_bridge_pipe_id", props=props)
    template = Template.from_stack(app_stack)

    template.has_resource_properties(
        "AWS::Pipes::Pipe",
        {
            "DesiredState": EventBridgePipeState.RUNNING,
            "Name": "lst-teststack-use1-test",
            "RoleArn": ROLE_ARN,
            "Source": SOURCE_ARN,
            "SourceParameters": {},
            "Target": TARGET_ARN,
            "TargetParameters": {},
        },
    )
    template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 0)


def test_event_bridge_pipe_create_failure(app_stack):  # pylint: disable=W0621
    props = {
        "name": "test",
        "pipe_source_parameters": {"something_invalid": "something_else_invalid"},
        "pipe_target_parameters": {},
        "role_arn": ROLE_ARN,
        "source_arn": SOURCE_ARN,
        "target_arn": TARGET_ARN,
    }

    with pytest.raises(InvalidPipePropertyParameterError):
        Guest360EventBridgePipe(app_stack, construct_id="test_event_bridge_pipe_id_2", props=props)
