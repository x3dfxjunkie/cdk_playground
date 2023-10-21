""" GithubRunner Construct Runner Stack
"""
import os
from pathlib import Path
from typing import Sequence, TypedDict

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.lambda_function import Guest360LambdaFunction, LambdaFunctionProps
from app.src.reliability.utils import LambdaFunctionName, LogGroup, QueueName
from aws_cdk import Duration, aws_apigateway, aws_ec2, aws_iam, aws_lambda, aws_lambda_destinations, aws_logs, aws_sqs
from cdk_nag import NagSuppressions


class GithubRunnerProps(TypedDict):
    vpc_endpoints: Sequence[aws_ec2.IVpcEndpoint]


class GithubRunner(Construct360):
    """Construct class that creates a Github Runner Resource"""

    def __init__(self, scope: Construct360, construct_id: str, props: GithubRunnerProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prefix = self.node.try_get_context("prefix")

        environment = self.node.try_get_context("environment")

        github_runner_webhook_handler_name = LambdaFunctionName(prefix, "webhook").name()

        stack_path = str(Path(os.getcwd()).parents[0])

        github_webhook_dlq = aws_sqs.Queue(self, f"{prefix}-webhook-dlq", queue_name=QueueName(prefix, "github-webhook-dlq").name(), enforce_ssl=True)

        github_webhook_sqs_queue = aws_sqs.Queue(self, f"{prefix}-github-webhook-queue", queue_name=QueueName(prefix, "github-webhook-queue").name(), enforce_ssl=True)

        github_runner_webhook_handler = Guest360LambdaFunction(self, github_runner_webhook_handler_name, LambdaFunctionProps(code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/reliability/GithubRunner/lambda_archive.zip"), description="GitHub Runner Webhook handler", function_name=github_runner_webhook_handler_name, handler="lambda_function.webhook_handler", runtime=aws_lambda.Runtime.PYTHON_3_9, timeout=Duration.minutes(1), environment={"SQS_QUEUE_URL": github_webhook_sqs_queue.queue_url}, on_failure=aws_lambda_destinations.SqsDestination(github_webhook_dlq)))

        github_webhook_sqs_queue.grant_send_messages(github_runner_webhook_handler.function)

        github_webhook_dlq.grant_send_messages(github_runner_webhook_handler.function)

        log_group = aws_logs.LogGroup(self, LogGroup(prefix, "github_webhook_logs").name())

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
                            aws_iam.AccountRootPrincipal(),  # Loosen Principal after Authentication
                        ],
                    )
                ]
            )
            if environment != "local"
            else None
        )

        github_webhook_api = aws_apigateway.RestApi(
            self,
            f"{prefix}-github_webhook",
            rest_api_name=f"{prefix}-github_webhook",
            endpoint_configuration=aws_apigateway.EndpointConfiguration(types=[aws_apigateway.EndpointType.PRIVATE], vpc_endpoints=props.get("vpc_endpoints")),
            cloud_watch_role=True,
            deploy_options={
                "description": "OpenAPI gateway",
                "stage_name": environment,
                "logging_level": aws_apigateway.MethodLoggingLevel.INFO,
                "metrics_enabled": True,
                "data_trace_enabled": True,
                "access_log_destination": aws_apigateway.LogGroupLogDestination(log_group),
            },
            policy=policy,
        )

        github_webhook_resource = github_webhook_api.root.add_resource("github-webhook")

        github_webhook_method = github_webhook_resource.add_method("POST", aws_apigateway.LambdaIntegration(github_runner_webhook_handler.function))

        resource_policy_document = aws_iam.PolicyDocument(statements=[aws_iam.PolicyStatement(effect=aws_iam.Effect.ALLOW, actions=["execute-api:Invoke"], resources=[github_webhook_method.method_arn, github_webhook_api.arn_for_execute_api()])])

        github_runner_scaler = LambdaFunctionName(prefix, "scaler").name()

        Guest360LambdaFunction(self, github_runner_scaler, LambdaFunctionProps(function_name=github_runner_scaler, description="GitHub Runner Scaler", runtime=aws_lambda.Runtime.PYTHON_3_9, timeout=Duration.minutes(2), code=aws_lambda.Code.from_asset(f"{stack_path}/bazel-bin/app/src/reliability/GithubRunner/lambda_archive.zip"), handler="lambda_function.scaler_handler", allow_public_subnet=False))

        aws_iam.Policy(self, f"{prefix}-github_webhook_policy", document=resource_policy_document)

        aws_apigateway.RequestValidator(self, f"{prefix}-github_webhook_validator", rest_api=github_webhook_api, validate_request_body=True, validate_request_parameters=True)

        NagSuppressions.add_resource_suppressions(
            self,
            [
                {
                    "id": "AwsSolutions-IAM4",
                    "reason": "Managed Policies are OK",
                }
            ],
            apply_to_children=True,
        )

        NagSuppressions.add_resource_suppressions(
            github_webhook_method,
            [
                {
                    "id": "AwsSolutions-APIG4",
                    "reason": "HMAC Authentication is for a different Issue",
                },
                {
                    "id": "AwsSolutions-COG4",
                    "reason": "User Pool is not a required authorizer for this application",
                },
            ],
        )

        NagSuppressions.add_resource_suppressions(
            github_webhook_sqs_queue,
            [
                {
                    "id": "AwsSolutions-SQS3",
                    "reason": "DLQ Associated to a lambda",
                }
            ],
        )

        NagSuppressions.add_resource_suppressions(github_runner_webhook_handler.function.role.node.try_find_child("DefaultPolicy"), [{"id": "AwsSolutions-IAM5", "reason": "kms:GenerateDataKey* and kms:ReEncrypt* are ok"}])

        NagSuppressions.add_resource_suppressions(
            github_webhook_dlq,
            [
                {
                    "id": "AwsSolutions-SQS3",
                    "reason": "SQS Queue is actually a DLQ itself (for Kinesis stream).",
                }
            ],
        )
