"""Step Machine Construct
State Machine construct allow deploy State Machine using
definition in YAML or JSON files
"""
from typing import TypedDict, Dict, Any
from typing_extensions import NotRequired
from aws_cdk import aws_stepfunctions as sfn, aws_cloudwatch, Duration

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.iam_role import Guest360IamRole, IAMProps
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.src.reliability.utils import RoleName
from strongtyping.strong_typing import match_class_typing


@match_class_typing
class StateMachineProps(TypedDict):
    """StateMachineProps."""

    name: str  # State Machine name
    description: str  # State Machine description
    definition_file: str  # Name of definition file
    iam: NotRequired[
        Dict
    ]  # Props for IAM construct - this should be IamPops, just FYI. See Guest360IAM Construct for more details.
    state_function_parameters: NotRequired[Dict[str, any]]  # State Function execution parameters

class Guest360StateMachine(Construct360):
    """Guest360StateMachine."""

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        state_machine_definition: dict,
        state_machine_props: StateMachineProps,
        **kwargs,
    ) -> None:
        """Construct to create Step Function
        :param scope:
        :param construct_id:
        :param state_machine_definition : Configuration file that defines the StateMachine
        :param state_machine_props: Configurations for StateMachine - see StateMachineProps TypedDict
        """
        super().__init__(scope, construct_id)

        prefix = self.node.try_get_context("prefix_global")

        service_name = state_machine_props["name"]
        definition_substitutions = {**state_machine_props["step_function_parameters"], **kwargs}

        if "role_arn" in kwargs:
            self.state_machine_role = kwargs["role_arn"]
        else:
            IAMProps(state_machine_props["iam"])  # test if props["iam"] is of type IAMProps
            iam_role = state_machine_props["iam"]
            self.state_machine_role = self.create_role(self, service_name, iam_role).role.role_arn

        self.state_machine = sfn.CfnStateMachine(
            self,
            f"{prefix}{service_name}",
            state_machine_name=f"{prefix}-{service_name}",
            definition=state_machine_definition,
            role_arn=self.state_machine_role,
            definition_substitutions=definition_substitutions,
        )

        # ExecutionsAborted - throw an alarm if 1 data point is over 3 in the span of 3 minutes
        # ExecutionsFailed - throw an alarm if 1 data point is over 3 in the span of 3 minutes
        # ExecutionsTimedOut - throw an alarm if 3 data points are over 5 in the span of 3 minutes
        # ActivitiesFailed - throw an alarm if 1 data point is over 3 in the span of 3 minutes
        # ActivitiesTimedOut - throw an alarm if 3 data points are over 5 in the span of 3 minutes
        # LambdaFunctionsFailed - throw an alarm if 1 data point is over 3 in the span of 3 minutes
        # LambdaFunctionsTimedOut - throw an alarm if 3 data points are over 5 in the span of 3 minutes
        # ServiceIntegrationsFailed - throw an alarm if 1 data point is over 3 in the span of 3 minutes
        # ServiceIntegrationsTimedOut - throw an alarm if 3 data points are over 5 in the span of 3 minutes
        default_alarms = [
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="ExecutionsAborted",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 1,
                "threshold": 3,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="ExecutionsFailed",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 1,
                "threshold": 3,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="ExecutionsTimedOut",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 3,
                "threshold": 5,
                "datapoints_to_alarm": 3,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="ActivitiesFailed",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 1,
                "threshold": 3,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="ActivitiesTimedOut",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 3,
                "threshold": 5,
                "datapoints_to_alarm": 3,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="LambdaFunctionsFailed",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 1,
                "threshold": 3,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="LambdaFunctionsTimedOut",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 3,
                "threshold": 5,
                "datapoints_to_alarm": 3,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="ServiceIntegrationsFailed",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 1,
                "threshold": 3,
                "datapoints_to_alarm": 1,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
            {
                "metric": aws_cloudwatch.Metric(
                    namespace="AWS/States",
                    metric_name="ServiceIntegrationsTimedOut",
                    statistic=aws_cloudwatch.Statistic.SUM.value,
                    unit=aws_cloudwatch.Unit.COUNT,
                    period=Duration.minutes(3),
                ),
                "evaluation_periods": 3,
                "threshold": 5,
                "datapoints_to_alarm": 3,
                "comparison_operator": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            },
        ]

        for cw_alarm in default_alarms:
            Guest360Alarm(
                self,
                f"{prefix}-{service_name}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )

    @classmethod
    def create_role(cls, scope, service_name, iam_props):
        prefix = scope.node.try_get_context("prefix_global")
        return Guest360IamRole(scope, RoleName(prefix, service_name).name(), iam_props)
