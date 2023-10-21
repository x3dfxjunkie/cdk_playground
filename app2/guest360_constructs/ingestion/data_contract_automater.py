"""Data Contract Automater Construct"""

from typing import TypedDict, Sequence
from pathlib import Path
import os

import aws_cdk
from aws_cdk import aws_iam, aws_ec2, aws_apigateway, aws_logs, aws_lambda, CfnOutput, Stack
from cdk_nag import NagSuppressions
from constructs import Construct

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.ecr_repository import Guest360ECRRepository
from app.guest360_constructs.lambda_function import Guest360LambdaFunction
from app.src.reliability.utils import LogGroup, StackName


class DataContractAutomaterProps(TypedDict):
    """Data Contract Automater Construct Props"""

    vpc_endpoints: Sequence[aws_ec2.IVpcEndpoint]


class DataContractAutomater(Construct360):
    """Data Contract Automater Construct

    Args:
        vpc_endpoints (Sequence[aws_ec2.IVpcEndpoint]): VPC Endpoints for private api gateway
    """

    automater_role: aws_iam.IRole

    def __init__(self, scope: Construct, construct_id: str, props: DataContractAutomaterProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prefix = self.node.try_get_context("prefix")

        environment = self.node.try_get_context("environment")

        stack_path = str(Path(os.getcwd()).parents[0])

        log_group = aws_logs.LogGroup(
            self, LogGroup(prefix, "data_contract_automater_logs").name(), retention=aws_logs.RetentionDays.ONE_MONTH
        )

        principals_with_conditions = [
            aws_iam.PrincipalWithConditions(
                aws_iam.AnyPrincipal(), {"StringEquals": {"aws:SourceVpce": vpc_endpoint.vpc_endpoint_id}}
            )
            for vpc_endpoint in props["vpc_endpoints"]
        ]

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
                        principals=principals_with_conditions,
                    )
                ]
            )
            if environment != "local"
            else None
        )

        naming_prefix = f"{prefix}-{construct_id}"

        stack_name = self.node.try_get_context("stack_name")
        ecr_name = f"{stack_name}/ingestion/data_contract_automater"
        self.ecr_repository = Guest360ECRRepository.from_repository_name(
            Stack.of(self), StackName(naming_prefix, "ecr").name(), repository_name=ecr_name
        )

        automater_backend: Guest360LambdaFunction = Guest360LambdaFunction(
            self,
            "automater-backend",
            {
                "function_name": "data_contract_automater",
                "description": "Automater Flask Backend Lambda",
                "timeout": aws_cdk.Duration.seconds(900),
                "code": aws_lambda.DockerImageCode.from_ecr(repository=self.ecr_repository, tag="latest"),
            },
        )

        assert automater_backend.function.role is not None

        self.automater_role: aws_iam.IRole = automater_backend.function.role

        api_gateway = aws_apigateway.LambdaRestApi(
            self,
            "data-contract-automater-private-api-gateway",
            endpoint_configuration={
                "types": [aws_apigateway.EndpointType.PRIVATE],
                "vpc_endpoints": props.get("vpc_endpoints"),
            },
            cloud_watch_role=True,
            policy=policy,
            deploy_options={
                "description": "Data Contract Automater API",
                "stage_name": environment,
                "logging_level": aws_apigateway.MethodLoggingLevel.INFO,
                "metrics_enabled": True,
                "data_trace_enabled": True,
                "access_log_destination": aws_apigateway.LogGroupLogDestination(log_group),
            },
            handler=automater_backend.function,
        )

        aws_apigateway.RequestValidator(
            self,
            "data-contract-automater_validator",
            rest_api=api_gateway,
            validate_request_body=True,
            validate_request_parameters=True,
        )

        api_endpoints = [
            f"https://{api_gateway.rest_api_id}-{vpc_endpoint.vpc_endpoint_id}.execute-api.us-east-1.amazonaws.com/{api_gateway.deployment_stage.stage_name}/"
            for vpc_endpoint in props["vpc_endpoints"]
        ]

        CfnOutput(self, f"{construct_id}-api_gateway_endpoints", value=str(api_endpoints))

        NagSuppressions.add_resource_suppressions(
            api_gateway,
            [
                {
                    "id": "AwsSolutions-APIG4",
                    "reason": "Authentication is going to be tackled in a different issue",
                },
                {
                    "id": "AwsSolutions-COG4",
                    "reason": "User Pool is not a required authorizer for this application",
                },
            ],
            apply_to_children=True,
        )
