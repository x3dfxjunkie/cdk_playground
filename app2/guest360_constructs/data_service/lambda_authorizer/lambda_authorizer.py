""" Module for the Lambda Authorizer """
from aws_cdk import aws_lambda
from cdk_nag import NagSuppressions
from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import LambdaFunctionName
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps


class LambdaAuthorizer(Construct360):
    """Construct of the Lambda Authorizer"""

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        stack_path: str,
        stack_prefix: str,
        lambda_environment: dict,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        authorizer_lambda_name = LambdaFunctionName(
            prefix=stack_prefix,
            base_name="authorizer-lambda",
        ).name()

        self.authorizer_lambda = Guest360LambdaFunction(
            self,
            authorizer_lambda_name,
            LambdaFunctionProps(
                function_name=authorizer_lambda_name,
                description="AuthZ authorizer Lambda",
                runtime=aws_lambda.Runtime.PYTHON_3_9,
                code=aws_lambda.Code.from_asset(
                    f"{stack_path}/bazel-bin/app/src/data_service/api_authorizers/lambda_archive.zip"
                ),
                handler="lambda_function.lambda_handler",
                allow_public_subnet=False,
                environment=lambda_environment,
            ),
        ).function

        NagSuppressions.add_resource_suppressions(
            self.authorizer_lambda.role,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed policies are acceptable.",
                }
            ],
        )

        # TODO - comment until wilcard can be resolved to specific resources:
        # lambda_execution_ssm_policy = aws_iam.PolicyStatement(
        #     **{
        #         "actions": [
        #             "ssm:GetParameter",
        #             "ssm:GetParametersByPath",
        #         ],
        #         "resources": ["*"],
        #     }
        # )

        # lambda_execution_s3_policy = aws_iam.PolicyStatement(
        #     **{
        #         "actions": [
        #             "s3:GetObject*",
        #         ],
        #         "resources": ["*"],
        #     }
        # )

        # self.authorizer_lambda.role.attach_inline_policy(
        #     aws_iam.Policy(
        #         self,
        #         id="lambda-authorizer-ssm-policy",
        #         statements=[lambda_execution_ssm_policy,
        #                     lambda_execution_s3_policy],
        #     )
        # )

        # api_principal = aws_iam.ServicePrincipal("apigateway.amazonaws.com")
        # self.authorizer_lambda.grant_invoke(api_principal)
