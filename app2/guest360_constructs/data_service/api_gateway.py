"""
Guest360 AWS Api Gateway construct library
"""
import os

import aws_cdk
import yaml
from aws_cdk import aws_apigateway, aws_iam, aws_lambda, aws_logs
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360


class APIGateway(Construct360):
    """
    Guest360 AWS api gateway construct specific to dataservice
    """

    @property
    def rest_api(self):
        return self._rest_api

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        environment_config: dict,
        authorizer_lambda: aws_lambda.Function,
        experience_api_lambda: aws_lambda.Function,
        stack_path: str,
        api_log_level=aws_apigateway.MethodLoggingLevel.INFO,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = aws_cdk.Stack.of(self)
        stack_name = self.node.try_get_context("stack_name")
        environment = self.node.try_get_context("environment")
        region = stack.region
        # account_id = environment_config["account"]

        swagger = self.load_swagger(stack_path)

        # Inject lambda arns into swagger
        swagger["paths"]["/api/v1/experiences"]["get"]["x-amazon-apigateway-integration"]["uri"] = f"arn:aws:apigateway:{region}" f":lambda:path/2015-03-31/functions/" f"{experience_api_lambda.function_arn}/invocations"

        # Add API authorizer:
        swagger["components"]["securitySchemes"]["authz-authorizer"]["x-amazon-apigateway-authorizer"]["authorizerUri"] = f"arn:aws:apigateway:{region}:lambda:path/2015-03-31/functions/{authorizer_lambda.function_arn}/invocations"

        # print(json.dumps(swagger, indent=2))

        rest_api_log_group = aws_logs.LogGroup(
            self,
            f"{stack_name}-restapi-log-group",
        )

        rest_api_role = aws_iam.Role(self, id="rest-api-authorizer-role", assumed_by=aws_iam.ServicePrincipal("apigateway.amazonaws.com"))

        rest_api_role.add_to_policy(
            aws_iam.PolicyStatement(
                actions=["lambda:InvokeFunction", "lambda:GetFunctionConfiguration"],
                effect=aws_iam.Effect.ALLOW,
                resources=[
                    authorizer_lambda.function_arn,
                    experience_api_lambda.function_arn,
                ],
            )
        )

        swagger["paths"]["/api/v1/experiences"]["get"]["x-amazon-apigateway-integration"]["credentials"] = f"{rest_api_role.role_arn}"

        swagger["components"]["securitySchemes"]["authz-authorizer"]["x-amazon-apigateway-authorizer"]["authorizerCredentials"] = f"{rest_api_role.role_arn}"

        # PRIVATE endpoint type also requires a policy be assigned to the API:
        policy = (
            aws_iam.PolicyDocument(
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
            if environment != "local"
            else None
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
                "logging_level": api_log_level,
                "metrics_enabled": True,
                "data_trace_enabled": True,
                "access_log_destination": aws_apigateway.LogGroupLogDestination(rest_api_log_group),
            },
        )

        # Set the VPC Endpoint IDs for the private api gateway endpoint.
        # Endpoint IDs are not present in LocalStack however.
        if environment != "local":
            cfn_rest_api: aws_apigateway.CfnRestApi = self._rest_api.node.default_child
            vpc_endpoint_ids = [endpoint["id"] for endpoint in environment_config["networking"][region]["endpoints"] if endpoint["service_name"] == "execute-api"]

            cfn_rest_api.endpoint_configuration = aws_apigateway.CfnRestApi.EndpointConfigurationProperty(
                types=[
                    aws_apigateway.EndpointType.PRIVATE.name,
                ],
                vpc_endpoint_ids=vpc_endpoint_ids,
            )

        # TODO - add resource level for cloud watch role, but can't get reference:
        NagSuppressions.add_stack_suppressions(
            stack,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed policies are acceptable.",
                    "applies_to": ("[Policy::arn:<AWS::Partition>:iam::aws:" "policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs]"),
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
    def load_swagger(stack_path: str) -> dict:
        with open(os.path.join(stack_path, "docs", "workstreams", "services", "openapi.yaml"), "r", encoding="UTF-8") as file:
            return yaml.safe_load(file)
