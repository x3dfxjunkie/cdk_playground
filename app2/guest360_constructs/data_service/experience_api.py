"""This construct is used to create the lambda to process API Gateway requests for Experiences.
The lambda is currently stored in /workspace/app/src/data_service/experience_api/experience_api/lambda_function.py .
"""
import os
import typing
from pathlib import Path

import aws_cdk
from aws_cdk import aws_iam, aws_lambda
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.lambda_function import Guest360LambdaFunction
from app.src.reliability.utils import LambdaFunctionName


class ExperienceRestAPILambdaEnvironment(typing.TypedDict):
    """Typed representation of expected AWS Lambda environment arguments passed into the lambda which will process the Experiences Rest API request."""

    EXPERIENCE_EVENT_TABLE_NAME: str
    IDENTITY_TABLE_NAME: str
    PROFILE_TABLENAME: str


class ExperienceApiLambda(Construct360):
    """This construct is used to create the lambda to process API Gateway requests for Experiences.
    The lambda is currently stored in /workspace/app/src/data_service/experience_api/experience_api/lambda_function.py .
    """

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        stack_prefix: str,
        lambda_environment: ExperienceRestAPILambdaEnvironment,
        lambda_timeout_seconds=aws_cdk.Duration.seconds(120),
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack_path = str(Path(os.getcwd()).parents[0])

        experience_api_lambda_name = LambdaFunctionName(
            prefix=stack_prefix,
            base_name="experience-api-lambda",
        ).name()

        self.experiences_api_lambda = Guest360LambdaFunction(
            self,
            experience_api_lambda_name,
            {
                "function_name": experience_api_lambda_name,
                "description": "Experiences API Lambda",
                "runtime": aws_lambda.Runtime.PYTHON_3_9,
                "timeout": lambda_timeout_seconds,
                "code": aws_lambda.Code.from_asset(
                    f"{stack_path}/bazel-bin/app/src/data_service/experience_api/lambda_archive.zip"
                ),
                "handler": "lambda_function.lambda_handler",
                "environment": typing.cast(typing.Dict[str, str], lambda_environment),
                "allow_public_subnet": False,
            },
        ).function

        NagSuppressions.add_resource_suppressions(
            self.experiences_api_lambda.role,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed policies are acceptable.",
                }
            ],
        )
        self.experiences_api_lambda.grant_invoke(aws_iam.ServicePrincipal("apigateway.amazonaws.com"))
