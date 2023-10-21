"""
Guest360 AWS Api Gateway construct library
"""
import json
import logging
import sys

import pytest
import yaml
from aws_cdk import App, Environment, Stack, aws_apigateway
from aws_cdk.assertions import Template

from app.guest360_constructs.api_gateway import Guest360APIGateway, Guest360APIGatewayProps

# ------------------------------------------------------------------------------------------------


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {
    "environment": "stage",
    "stack_name": "testStack",
    "prefix": "lst-TestApiGateway-use1",
}
CLOUDWATCH_ALARM_RESOURCE = "AWS::CloudWatch::Alarm"
COMPARISON_OPERATOR = "GreaterThanOrEqualToThreshold"
CLOUDWATCH_ALARM_NAMESPACE = "AWS/ApiGateway"


class TestApiGateway:
    """Guest360 TestApiGateway"""

    stack_id = "TestStack"
    api_gateway_id = "TestApiGatway"

    @pytest.mark.timeout(30, method="signal")
    def test_instantiate_construct_default_params(self):
        test_app = App(context=TEST_CONTEXT)
        environment = test_app.node.try_get_context("environment")
        test_stack = Stack(test_app, self.stack_id, env=Environment(account="123456789", region="us-east-1"))

        """
        ask for openapi path for each app
        """

        props: Guest360APIGatewayProps = {
            "method_props": [
                {
                    "path": "/api/v1/experiences",
                    "method": "get",
                    "api_lambda": "arn:aws:lambda:us-east-1:XXXXXXXXXXXX:function:YOUR_FUNCTION_NAME_ONE",
                    "credentials": {
                        "enabled": True,
                        "authorizer_lambda_arn": "arn:aws:lambda:us-east-1:XXXXXXXXXXXX:function:YOUR_FUNCTION_NAME_AUTH_ONE",
                    },
                }
            ],
            "api_log_level": aws_apigateway.MethodLoggingLevel.INFO,
            "swagger_path": "docs/workstreams/services/openapi.yaml",
        }

        """
        Ingest the environment file
        """

        with open(f"app/configs/{environment}-environment.yaml", "r", encoding="utf-8") as file:
            environment_config = yaml.safe_load(file)

        Guest360APIGateway(
            test_stack, construct_id=self.api_gateway_id, environment_config=environment_config, props=props
        )

        """ Render template"""
        template = Template.from_stack(test_stack)
        logger.debug(json.dumps(template.to_json(), indent=2))

        template.resource_count_is("AWS::IAM::Role", 2)
        template.resource_count_is("AWS::IAM::Policy", 1)
        template.resource_count_is("AWS::ApiGateway::RestApi", 1)
        template.resource_count_is(CLOUDWATCH_ALARM_RESOURCE, 4)
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": COMPARISON_OPERATOR,
                "EvaluationPeriods": 2,
                "DatapointsToAlarm": 2,
                "MetricName": "4XXError",
                "Namespace": CLOUDWATCH_ALARM_NAMESPACE,
                "Period": 60,
                "Statistic": "Sum",
                "Threshold": 5,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": COMPARISON_OPERATOR,
                "EvaluationPeriods": 2,
                "DatapointsToAlarm": 2,
                "MetricName": "5XXError",
                "Namespace": CLOUDWATCH_ALARM_NAMESPACE,
                "Period": 60,
                "Statistic": "Sum",
                "Threshold": 3,
                "Unit": "Count",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": COMPARISON_OPERATOR,
                "EvaluationPeriods": 2,
                "DatapointsToAlarm": 2,
                "MetricName": "IntegrationLatency",
                "Namespace": CLOUDWATCH_ALARM_NAMESPACE,
                "Period": 10,
                "Threshold": 3,
                "Unit": "Milliseconds",
            },
        )
        template.has_resource_properties(
            CLOUDWATCH_ALARM_RESOURCE,
            {
                "ComparisonOperator": COMPARISON_OPERATOR,
                "EvaluationPeriods": 2,
                "DatapointsToAlarm": 2,
                "MetricName": "Latency",
                "Namespace": CLOUDWATCH_ALARM_NAMESPACE,
                "Period": 10,
                "Threshold": 3,
                "Unit": "Milliseconds",
            },
        )
