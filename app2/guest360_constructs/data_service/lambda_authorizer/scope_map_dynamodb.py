""" Module of the Scope Map in DynamoDB """
import aws_cdk
from aws_cdk import aws_dynamodb, aws_lambda, aws_logs
from aws_cdk import custom_resources as aws_cr
from cdk_nag import NagSuppressions

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.dynamodb_globaltable import Guest360DynamodbGlobaltable
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.src.reliability.utils import LambdaFunctionName


class ScopeMapDynamoDB(Construct360):
    """Construct of the Scope Map DynamoDB Table"""

    # pylint: disable=unused-argument
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

        self.scopes_map_dynamodb = Guest360DynamodbGlobaltable(
            self,
            construct_id=construct_id,
            table_name="scope_map_dynamodb",
            partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.NUMBER),
        )

        lambda_environment["SCOPE_MAP_TABLE_NAME"] = self.scopes_map_dynamodb.table.table_name

        # Custom Resource to populate the table of Scope Map from AuthZ
        cr_dynamodb_lambda_name = LambdaFunctionName(
            prefix=stack_prefix,
            base_name="cr-dynamodb-lambda",
        ).name()

        self.cr_dynamodb_lambda = Guest360LambdaFunction(
            self,
            cr_dynamodb_lambda_name,
            LambdaFunctionProps(
                function_name=cr_dynamodb_lambda_name,
                description="Custom Resource Lambda to populate the Scope Map DynamoDB Table",
                runtime=aws_lambda.Runtime.PYTHON_3_9,
                code=aws_lambda.Code.from_asset(
                    f"{stack_path}/bazel-bin/app/src/data_service/api_authorizers/scope_map/cr_lambda_archive.zip"
                ),
                handler="lambda_function.lambda_handler",
                allow_public_subnet=False,
                environment=lambda_environment,
                timeout=aws_cdk.Duration.seconds(15),
            ),
        ).function

        self.custom_resource_provider = aws_cr.Provider(
            self,
            "custom-resource-provider",
            on_event_handler=self.cr_dynamodb_lambda,
            log_retention=aws_logs.RetentionDays.ONE_DAY,
        )

        NagSuppressions.add_resource_suppressions(
            self.cr_dynamodb_lambda.role,
            [
                {
                    "id": "AwsSolutions-IAM5",
                    "reason": "Managed policies are acceptable.",
                },
            ],
        )

        self._custom_resource = aws_cdk.CustomResource(
            self, "custom-resource", service_token=self.custom_resource_provider.service_token
        )

        self.scopes_map_dynamodb.table.grant_read_write_data(self.cr_dynamodb_lambda)
