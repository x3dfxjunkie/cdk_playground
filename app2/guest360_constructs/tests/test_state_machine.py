"""Modules required by the unit test of the StateMachine Constructor"""
import logging
import sys

import aws_cdk
import pytest
from aws_cdk import assertions
from app.guest360_constructs.tests.utils import print_template_on_debug
from app.guest360_constructs.state_machine import Guest360StateMachine

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

CLOUDWATCH_ALARM_RESOURCE = "AWS::CloudWatch::Alarm"


class TestStateMachine:
    """Class for test the state machine constructor"""

    stack_id = "TestStack"

    @pytest.mark.timeout(30, method="signal")
    def test_state_machine_creation(self):
        test_app = aws_cdk.App()
        stack = aws_cdk.Stack(test_app, self.stack_id, env=aws_cdk.Environment(account="123456789", region="us-east-1"))
        stack.node.set_context("environment", "local")
        stack.node.set_context("prefix", "test-prefix-use1")
        stack.node.set_context("prefix_global", "test-prefix")
        stack.node.set_context("region", "us-east-1")

        # Dummy dict

        state_machine_props = {
            "name": "test_name",
            "description": "test_description",
            "definition_file": "hello_world.yaml",
            "iam": {
                "assumed_by": aws_cdk.aws_iam.ServicePrincipal("states.amazonaws.com"),
                "role_name": "test_role",
                "description": "role description",
            },
            "state_function_parameters": {
                "cluster_arn": "var1",
                "locust_file": "",
                "run_time": "",
                "users": 100,
                "workers": 50,
                "cloudwatch_log_group_name": "",
                "cloudwatch_log_streeam_name": "",
                "cloudwatch_metrics_namespace": "",
                "target_stream": "",
            },
            "step_function_parameters": {
                "guest360_execution_status_table": "",
                "guest360_execute_load_test_scenario_arn": "",
            },
        }

        # Example State Machine Def from the AWS Docs: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html
        state_machine_definition = {
            "Comment": "Anz example of the Amazon States Language using a choice state.",
            "StartAt": "FirstState",
            "States": {
                "FirstState": {
                    "Type": "Task",
                    "Resource": "arn:aws:lambda:us-east-1:123456789012:function:FUNCTION_NAME",
                    "Next": "ChoiceState",
                },
                "ChoiceState": {
                    "Type": "Choice",
                    "Choices": [
                        {"Variable": "$.foo", "NumericEquals": 1, "Next": "FirstMatchState"},
                        {"Variable": "$.foo", "NumericEquals": 2, "Next": "SecondMatchState"},
                    ],
                    "Default": "DefaultState",
                },
                "FirstMatchState": {
                    "Type": "Task",
                    "Resource": "arn:aws:lambda:us-east-1:123456789012:function:OnFirstMatch",
                    "Next": "NextState",
                },
                "SecondMatchState": {
                    "Type": "Task",
                    "Resource": "arn:aws:lambda:us-east-1:123456789012:function:OnSecondMatch",
                    "Next": "NextState",
                },
                "DefaultState": {"Type": "Fail", "Error": "DefaultStateError", "Cause": "No Matches!"},
                "NextState": {
                    "Type": "Task",
                    "Resource": "arn:aws:lambda:us-east-1:123456789012:function:FUNCTION_NAME",
                    "End": True,
                },
            },
        }

        Guest360StateMachine(stack, "test_stepfunction", state_machine_definition, state_machine_props)
        template = assertions.Template.from_stack(stack)
        print_template_on_debug(template, logger)

        template.resource_count_is("AWS::IAM::Role", 1)
        template.resource_count_is("AWS::StepFunctions::StateMachine", 1)
        template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 9)
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 1,
                "DatapointsToAlarm": 1,
                "MetricName": "ExecutionsAborted",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 3,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 1,
                "DatapointsToAlarm": 1,
                "MetricName": "ExecutionsFailed",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 3,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "DatapointsToAlarm": 3,
                "MetricName": "ExecutionsTimedOut",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 5,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 1,
                "DatapointsToAlarm": 1,
                "MetricName": "ActivitiesFailed",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 3,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "DatapointsToAlarm": 3,
                "MetricName": "ActivitiesTimedOut",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 5,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 1,
                "DatapointsToAlarm": 1,
                "MetricName": "LambdaFunctionsFailed",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 3,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "DatapointsToAlarm": 3,
                "MetricName": "LambdaFunctionsTimedOut",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 5,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 1,
                "DatapointsToAlarm": 1,
                "MetricName": "ServiceIntegrationsFailed",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 3,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": "GreaterThanOrEqualToThreshold",
                "EvaluationPeriods": 3,
                "DatapointsToAlarm": 3,
                "MetricName": "ServiceIntegrationsTimedOut",
                "Namespace": "AWS/States",
                "Period": 180,
                "Statistic": "Sum",
                "Threshold": 5,
                "Unit": "Count",
            },
        )
