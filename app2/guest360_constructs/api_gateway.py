"""
Guest360 AWS Api Gateway construct library
"""

from typing import List, TypedDict

import aws_cdk
import yaml
from aws_cdk import Duration, aws_apigateway, aws_iam, aws_logs, aws_cloudwatch
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.guest360_constructs.construct_360 import Construct360
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing


class Guest360APIGatewayCredentialsProps(TypedDict):
    enabled: bool
    authorizer_lambda_arn: str


class Guest360APIGatewayMethodProps(TypedDict):
    method: str  # enum option is pending
    path: str
    api_lambda: str
    credentials: Guest360APIGatewayCredentialsProps


@match_class_typing
class Guest360APIGatewayProps(TypedDict):
    method_props: List[Guest360APIGatewayMethodProps]
    api_log_level: aws_apigateway.MethodLoggingLevel
    swagger_path: str


class Guest360APIGateway(Construct360):
    """
    Guest360 AWS api gateway construct
    """

    @property
    def rest_api(self):
        return self._rest_api

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        environment_config: dict,
        props: Guest360APIGatewayProps,
        **kwargs,
    ) -> None:
        """Guest360 Construct for API Gateway.

        Each time this method is called, need to be prepared openapi.yaml definition updated with paths and methods desired to perform with lambda arn
        If credentials are needed, set True/False and add the lambda auth arn
        Note: ***Lambdas arn are not necessary in plain text, you can add a variables loaded with methods or similar.

        Required props example:
            props: Guest360APIGatewayProps = {
                "method_props": [{
                        "path": "/api/v1/first_path",
                        "method": "get",
                        "api_lambda": "AddLambdaARN",
                        "credentials": {
                            "enabled": True,
                            "authorizer_lambda_arn": "AddLambdaAuthorizerARN"
                            }
                     },
                     {
                        "path": "/api/v1/second_path",
                        "method": "get",
                        "api_lambda": "AddLambdaARN",
                        "credentials": {
                            "enabled": False,
                            "authorizer_lambda_arn": ""
                      }
                        ...
                        you can add more if it was needed
                        ...
                ],
                "api_log_level": aws_apigateway.MethodLoggingLevel.INFO,
                "swagger_path": "app/docs/workstreams/services/openapi.yaml"
            }


        Usage:
            Guest360APIGateway(self,
                construct_id="api-gateway-guest360construct",
                environment_config=environment_config,
                props,
            )
        """

        super().__init__(scope, construct_id, **kwargs)
        stack = aws_cdk.Stack.of(self)
        stack_name = self.node.try_get_context("stack_name")
        environment = self.node.try_get_context("environment")
        region = stack.region
        Guest360APIGatewayProps(props)
        if props.get("api_log_level") is None:
            props["api_log_level"] = aws_apigateway.MethodLoggingLevel.INFO
        # account_id = environment_config["account"]
        # laod openapi file
        swagger = self.load_swagger(props["swagger_path"])
        for index in props["method_props"]:
            # when credentials in required
            if index["credentials"]["enabled"]:
                # Inject lambda arns into swagger
                swagger["paths"][index["path"]][index["method"]]["x-amazon-apigateway-integration"]["uri"] = (
                    f"arn:aws:apigateway:{region}"
                    f":lambda:path/2015-03-31/functions/"
                    f"{index['api_lambda']}/invocations"
                )

                # Add API authorizer:
                swagger["components"]["securitySchemes"]["authz-authorizer"]["x-amazon-apigateway-authorizer"][
                    "authorizerUri"
                ] = f"arn:aws:apigateway:{region}:lambda:path/2015-03-31/functions/{index['credentials']['authorizer_lambda_arn']}/invocations"

                # Creating the iam role
                rest_api_role = aws_iam.Role(
                    self, id="rest-api-authorizer-role", assumed_by=aws_iam.ServicePrincipal("apigateway.amazonaws.com")
                )

                # Creating the iam policy
                rest_api_role.add_to_policy(
                    aws_iam.PolicyStatement(
                        actions=["lambda:InvokeFunction", "lambda:GetFunctionConfiguration"],
                        effect=aws_iam.Effect.ALLOW,
                        resources=[
                            f"{index['api_lambda']}",
                            f"{index['credentials']['authorizer_lambda_arn']}",
                        ],
                    )
                )

                # Inject role in credentials dection
                swagger["paths"][index["path"]][index["method"]]["x-amazon-apigateway-integration"][
                    "credentials"
                ] = rest_api_role.role_arn

                swagger["components"]["securitySchemes"]["authz-authorizer"]["x-amazon-apigateway-authorizer"][
                    "authorizerCredentials"
                ] = rest_api_role.role_arn

            # when credentials in not required
            else:
                swagger["paths"][index["path"]][index["method"]]["x-amazon-apigateway-integration"]["uri"] = (
                    f"arn:aws:apigateway:{region}"
                    f":lambda:path/2015-03-31/functions/"
                    f"{index['api_lambda']}/invocations"
                )

        # Creating the cloudwatch logGroup
        rest_api_log_group = aws_logs.LogGroup(
            self,
            f"{stack_name}-restapi-log-group",
        )

        # PRIVATE endpoint type also requires a policy be assigned to the API:
        policy = aws_iam.PolicyDocument(
            statements=[
                aws_iam.PolicyStatement(
                    effect=aws_iam.Effect.ALLOW,
                    actions=[
                        "execute-api:Invoke",
                    ],
                    resources=[
                        "*",
                    ],
                    principals=[
                        aws_iam.AccountRootPrincipal(),
                    ],
                )
            ]
        )

        self._rest_api = aws_apigateway.SpecRestApi(
            self,
            f"{stack_name}-restapi",
            api_definition=aws_apigateway.ApiDefinition.from_inline(swagger),
            cloud_watch_role=True,
            endpoint_types=[
                aws_apigateway.EndpointType.PRIVATE,
            ],
            policy=policy,
            deploy_options={
                "description": "OpenAPI gateway",
                "stage_name": environment,
                "logging_level": props["api_log_level"],
                "metrics_enabled": True,
                "data_trace_enabled": True,
                "access_log_destination": aws_apigateway.LogGroupLogDestination(rest_api_log_group),
            },
        )

        # Set the VPC Endpoint IDs for the private api gateway endpoint.
        # Endpoint IDs are not present in LocalStack however.
        if environment != "local":
            cfn_rest_api = self._rest_api.node.default_child
            vpc_endpoint_ids = [
                endpoint["id"]
                for endpoint in environment_config["networking"][region]["endpoints"]
                if endpoint["service_name"] == "execute-api"
            ]

            cfn_rest_api.endpoint_configuration = aws_apigateway.CfnRestApi.EndpointConfigurationProperty(
                types=[
                    aws_apigateway.EndpointType.PRIVATE.name,
                ],
                vpc_endpoint_ids=vpc_endpoint_ids,
            )

        # 4XXError - Alarm if there are 2 or more client side errors in the given threshold
        # 5XXError - Alarm if there are 2 or more server side errors in the given threshold
        # IntegrationLatency - Alarm if the latency from the backend to the front end is longer than 10 seconds
        # Latency - Alarm if the latency from API Gateway to the client is over 10 seconds

        default_alarms = [
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/ApiGateway",
                    metric_name="4XXError",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 2,
                "threshold": 5,
                "datapoints_to_alarm": 2,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/ApiGateway",
                    metric_name="5XXError",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                ),
                "evaluation_periods": 2,
                "threshold": 3,
                "datapoints_to_alarm": 2,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/ApiGateway",
                    metric_name="IntegrationLatency",
                    unit=aws_cloudwatch.Unit.MILLISECONDS,
                    period=Duration.seconds(10),
                ),
                "evaluation_periods": 2,
                "threshold": 3,
                "datapoints_to_alarm": 2,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/ApiGateway",
                    metric_name="Latency",
                    unit=aws_cloudwatch.Unit.MILLISECONDS,
                    period=Duration.seconds(10),
                ),
                "evaluation_periods": 2,
                "threshold": 3,
                "datapoints_to_alarm": 2,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
        ]

        for cw_alarm in default_alarms:
            Guest360Alarm(
                self,
                f"{stack_name}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )

        # TODO - add resource level for cloud watch role, but can't get reference:
        NagSuppressions.add_stack_suppressions(
            stack,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed policies are acceptable.",
                    "applies_to": (
                        "[Policy::arn:<AWS::Partition>:iam::aws:"
                        "policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs]"
                    ),
                }
            ],
        )
        NagSuppressions.add_resource_suppressions(
            self._rest_api,
            [
                {
                    "id": "AwsSolutions-APIG2",
                    "reason": "validation done within swagger",
                }
            ],
        )

    @staticmethod
    def load_swagger(swagger_path: str) -> dict:
        with open(swagger_path, "r", encoding="UTF-8") as file:
            return yaml.safe_load(file)
