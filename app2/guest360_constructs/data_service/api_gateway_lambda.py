import json
import os
from email import policy
from pathlib import Path

import yaml
from aws_cdk import Duration
from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda

from app.guest360_constructs.construct_360 import Construct360


class ApiGatewayLambdas(Construct360):
    def __init__(self, scope: Construct360, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack_name = self.node.try_get_context("stack_name")
        stack_path = str(Path(os.getcwd()).parents[0])

        profile_lambda_environment = {
            "ssm_config_path": f"/{stack_name}/data-services/api-authorizer-lambda/api-config",
        }

        lightinglane_lambda_environment = {
            "ssm_config_path": f"/{stack_name}/data-services/profile-lambda/config",
        }

        _lambda_execution_policy_statement = iam.PolicyStatement(
            **{
                "actions": [
                    "ssm:GetParameter",
                    "ssm:GetParametersByPath",
                ],
                "resources": ["*"],
            }
        )

        _lambda_execution_policy = iam.Policy(
            self,
            id="lambda-authorizer-ssm-policy",
            statements=[_lambda_execution_policy_statement],
        )

        _api_principal = iam.ServicePrincipal("apigateway.amazonaws.com")

        _profile_api_lambda = _lambda.Function(
            self,
            "profile-api",
            function_name="-".join((stack_name, "profile", "api")),
            description="Profile API Lambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            timeout=Duration.seconds(10),
            code=_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/data_service/profile_api/lambda_archive.zip"),
            handler="profile_api.lambda_handler",
            environment=profile_lambda_environment,
        )
        _profile_api_lambda.grant_invoke(_api_principal)
        _profile_api_lambda.role.attach_inline_policy(_lambda_execution_policy)

        _lightinglane_api_lambda = _lambda.Function(
            self,
            "lightinglane_api_lambda",
            function_name="-".join((stack_name, "lightinglane", "api")),
            description="Lightinglane API Lambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/data_service/profile_api/lambda_archive.zip"),
            handler="profile_api.lambda_handler",
            environment=lightinglane_lambda_environment,
            # role=_lambda_execution_role,
        )
        _lightinglane_api_lambda.role.attach_inline_policy(_lambda_execution_policy)
        _lightinglane_api_lambda.grant_invoke(_api_principal)
