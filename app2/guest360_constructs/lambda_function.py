"""Guest360LambdaFunction construct
"""
import logging
import re
from typing import Any, Dict, TypedDict, Union, cast, List
from aws_cdk import (
    aws_cloudwatch,
    # aws_codedeploy,
    aws_ec2,
    aws_iam,
    aws_lambda,
    aws_lambda_destinations,
    aws_logs,
    aws_sqs,
    Duration,
    Stack,
)

from cdk_nag import NagSuppressions
from constructs import Construct
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import LambdaFunctionName
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.guest360_constructs.enums.cloudwatch_statistics import CloudwatchPercentileStatistics

logger = logging.getLogger(__name__)


@match_class_typing
class LambdaFunctionProps(TypedDict):
    """lambda function properties"""

    code: Union[
        aws_lambda.Code,
        str,
    ]
    handler: str
    runtime: NotRequired[aws_lambda.Runtime]
    allow_public_subnet: NotRequired[bool]
    description: NotRequired[str]
    environment: NotRequired[Dict[str, Any]]
    function_name: NotRequired[str]
    on_failure: NotRequired[
        Union[
            aws_lambda_destinations.EventBridgeDestination,
            aws_lambda_destinations.LambdaDestination,
            aws_lambda_destinations.SnsDestination,
            aws_lambda_destinations.SqsDestination,
        ]
    ]
    timeout: NotRequired[Duration]
    vpc: NotRequired[Any]
    vpc_subnets: NotRequired[aws_ec2.SubnetSelection]
    enable_otel_tracing: NotRequired[bool]
    current_version_options: NotRequired[aws_lambda.VersionOptions]
    layers: NotRequired[List[Any]]
    memory_size: NotRequired[int]
    runtime_family: NotRequired[str]
    log_retention: NotRequired[aws_logs.RetentionDays]
    tracing: NotRequired[aws_lambda.Tracing]
    profiling: NotRequired[Any]
    dead_letter_queue_enabled: NotRequired[bool]
    dead_letter_queue: NotRequired[aws_sqs.Queue]
    initial_policy: NotRequired[List[aws_iam.PolicyStatement]]


@match_class_typing
class LambdaDockerProps(TypedDict):
    """lambda function docker properties"""

    code: aws_lambda.DockerImageCode
    function_name: NotRequired[str]
    description: NotRequired[str]


class Guest360LambdaFunction(Construct360):
    """Guest360 Construct for lambda function"""

    @property
    def function(self) -> Union[aws_lambda.Function, aws_lambda.DockerImageFunction]:
        return self.lambda_function

    @property
    def function_name(self) -> str | None:
        return self._function_name

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        props: Union[LambdaFunctionProps, LambdaDockerProps, dict],
        **kwargs,
    ) -> None:
        """__init__.
        Guest360LambdaFunction
        """
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack.of(self)

        prefix = self.node.try_get_context("prefix")

        # set function name if provided using the utils LambdaFunctionName class
        if "function_name" in props and props["function_name"] is not None:
            props["function_name"] = LambdaFunctionName(prefix, props["function_name"]).name()

        self._function_name = props.get("function_name", None)

        # Type check props
        if isinstance(props["code"], str):
            stack_path = self.node.try_get_context("stack_path")
            props["code"] = aws_lambda.Code.from_asset(f'{stack_path}/{props["code"]}')
        if isinstance(props["code"], aws_lambda.Code):
            LambdaFunctionProps(props)  # type: ignore
            props = cast(Union[LambdaFunctionProps, Dict[str, Any]], props)
            enable_otel_tracing = props.get("enable_otel_tracing", True)
            current_version_options = props.get("current_version_options", False)

            props["runtime"] = self.get_latest_version("PYTHON")

            if enable_otel_tracing:
                otel_lambda_env = {
                    "AWS_LAMBDA_EXEC_WRAPPER": "/opt/otel-instrument",
                    "OPENTELEMETRY_COLLECTOR_CONFIG_FILE": "/var/task/otel-config.yaml",
                    "OTEL_INSTRUMENTATION_AWS_LAMBDA_FLUSH_TIMEOUT": "900",
                    "OTEL_PROPAGATORS": "xray",
                    "OTEL_PYTHON_ID_GENERATOR": "xray",
                    "OTEL_NAMESPACE": stack.stack_name,
                    **props.get("environment", {}),
                }

                props["environment"] = otel_lambda_env

                assert "runtime" in props

                props["tracing"] = aws_lambda.Tracing.ACTIVE  # type: ignore
                adot_layer = aws_lambda.LayerVersion.from_layer_version_arn(
                    self, "AWSAdotLayer", self.get_adot_arn(stack, props["runtime"])
                )

                props["layers"] = [adot_layer, *props.get("layers", [])]

            props.pop("runtime_family", None)
            props.pop("enable_otel_tracing", None)

            self.lambda_function: Union[aws_lambda.Function, aws_lambda.DockerImageFunction] = aws_lambda.Function(
                self, self.pass_id, **props
            )

            if current_version_options:
                version = self.lambda_function.current_version
                aws_lambda.Alias(self, id=construct_id, alias_name="live", version=version)

            if enable_otel_tracing:
                self.lambda_function.add_to_role_policy(
                    aws_iam.PolicyStatement(
                        sid="OTELXrayCloudwatchRW",
                        actions=[
                            "xray:PutTraceSegments",
                            "xray:PutTelemetryRecords",
                            "cloudwatch:GetMetricStatistics",
                            "cloudwatch:GetMetricStream",
                            "cloudwatch:PutMetricStream",
                            "cloudwatch:StartMetricStreams",
                            "cloudwatch:GetMetricData",
                            "cloudwatch:GetMetricStatistics",
                            "cloudwatch:PutMetricData",
                        ],
                        resources=["*"],
                    ),
                )

                NagSuppressions.add_resource_suppressions(
                    self.lambda_function,
                    [
                        {
                            "id": "AwsSolutions-IAM5",
                            "reason": "allow lambda to perform cloudwatch and xray read/write ops for opentelem",
                        }
                    ],
                    True,
                )

        elif isinstance(props["code"], aws_lambda.DockerImageCode):
            LambdaDockerProps(props)  # type: ignore
            self.lambda_function: Union[
                aws_lambda.Function, aws_lambda.DockerImageFunction
            ] = aws_lambda.DockerImageFunction(self, f"{prefix}-LambdaDocker", **props)
        else:
            raise TypeError("Guest360LambdaFunction incorrect code type[aws_lambda.Code|aws_lambda.DockerImageCode]")

        # Errors - send an alarm if there are 5 or more errors in the span of 3, 1 minute periods
        # increasing the "Errors" alarm to have a larger threshold and evalutaion period
        # to account for the following:
        # Function errors include exceptions that your code throws and exceptions that the
        # Lambda runtime throws. https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html

        # DeadLetterErrors - send an alarm if there are 2 or more dead-letter queue event failures in the span of a minute
        # Throttles - send an alarm if there are 5 or more throttle errors in the span of a minute
        # Duration - send an alarm if a function runs for 10 or more minutes

        default_alarms = [
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/Lambda",
                    metric_name="Errors",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                    dimensions_map={"FunctionName": self.lambda_function.function_name},
                ),
                "evaluation_periods": 3,
                "threshold": 5,
                "datapoints_to_alarm": 2,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/Lambda",
                    metric_name="DeadLetterErrors",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                    dimensions_map={"FunctionName": self.lambda_function.function_name},
                ),
                "evaluation_periods": 1,
                "threshold": 2,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/Lambda",
                    metric_name="Throttles",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(1),
                    dimensions_map={"FunctionName": self.lambda_function.function_name},
                ),
                "evaluation_periods": 1,
                "threshold": 5,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/Lambda",
                    metric_name="Duration",
                    statistic=CloudwatchPercentileStatistics.P99,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(5),
                    dimensions_map={"FunctionName": self.lambda_function.function_name},
                ),
                "evaluation_periods": 3,
                "threshold": 10,
                "datapoints_to_alarm": 3,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
        ]

        for cw_alarm in default_alarms:
            Guest360Alarm(
                self,
                f"{self._function_name}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )

        NagSuppressions.add_resource_suppressions(
            self.lambda_function, [{"id": "AwsSolutions-IAM4", "reason": "using default policies allowed"}], True
        )

    def get_adot_arn(self, stack, runtime: aws_lambda.Runtime, arch="amd64") -> str:
        # Account that hosts the aws managed otel layer
        aws_account = "901920570463"
        runtime_family = runtime.family if runtime.family is not None else aws_lambda.RuntimeFamily.PYTHON
        layer_name = f"aws-otel-{runtime_family.value.lower()}"
        adot_version = "1-19-0"
        layer_version = "1"
        return (
            f"arn:aws:lambda:{stack.region}:{aws_account}:layer:{layer_name}-{arch}-ver-{adot_version}:{layer_version}"
        )

    @staticmethod
    def get_latest_version(family: str) -> aws_lambda.Runtime:
        family = family.upper()
        versions = [k for k in aws_lambda.Runtime.__dict__ if family in k]
        # each family has a different sort criteria due to versioning string differences
        if family == "PYTHON":
            # need to sort the python versions on the sub string version x_x to ensure proper order
            versions.sort(key=lambda test_str: list(map(int, re.findall(r"(\d+_\d+)+", test_str)))[0])
        elif family == "NODEJS":
            # replace X with 0 for sorting purposes
            logger.debug("versions=%s", versions)
            # remove the first element as no version string will be latest
            version_latest = versions.pop(0)
            version_latest = versions.pop(-1)
            versions.sort(key=lambda test_str: list(map(int, re.findall(r"(\d+)", test_str)))[0])
            versions.append(version_latest)

        logger.debug("versions.sort=%s", versions)
        latest_version = versions[-1]
        return getattr(aws_lambda.Runtime, latest_version)
