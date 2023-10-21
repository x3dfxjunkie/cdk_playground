""" Cloudwatch Alarm Construct """
import logging
import os
from pathlib import Path
from typing import Literal, TypedDict, Union

import jsii
import yaml
from aws_cdk import Stack, aws_cloudwatch, aws_cloudwatch_actions, aws_sns
from constructs import Construct
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

logger = logging.getLogger(__name__)


class AlarmPropError(Exception):
    pass


@match_class_typing
class AlarmProps(TypedDict):
    """
    Props for Guest360 Cloudwatch Alarm
    """

    evaluation_periods: Union[int, float]
    threshold: Union[int, float]
    alarm_name: NotRequired[str]
    comparison_operator: NotRequired[aws_cloudwatch.ComparisonOperator]  # Defaults to GreaterThanOrEqualToThreshold
    datapoints_to_alarm: NotRequired[jsii.Number]
    evaluate_low_sample_count_percentile: NotRequired[str]
    treat_missing_data: NotRequired[aws_cloudwatch.TreatMissingData]
    metric: NotRequired[aws_cloudwatch.Metric]
    # SNS/SNOW Related Props
    p_level_in_prod: NotRequired[Literal["p2", "p3", "P2", "P3"]]  # Default is "p3"
    custom_sns_alarm_topic_name: NotRequired[str]  # Not the arn, just the name. Defaults is None
    snow_integration_enabled: NotRequired[bool]  # Defaults to True if environment is static
    snow_assignment_group: NotRequired[str]  # Default to values in default config file
    alarm_actions_disabled: NotRequired[bool] = True  # Actions are enabled for static (not ephemeral) by default
    alarm_description: NotRequired[str]  # Maps to secondary description for SNOW. Primary description for non-SNOW


class Guest360Alarm(aws_cloudwatch.Alarm):
    """
    Guest360 Alarm that integrates with SNS and Service. It behaves exactly as a native cdk cloudwatch alarm with
    following notes:
    - This inherits from aws_cloudwatch.Alarm
    - This alarm processes SNS/SNOW actions with respect to environment (so that composing L2s don't have to).
    - Static environments are (by default) always pointed to the lowest severity SNS topic configured.
    - An instance of this alarm has only one action - the SNS action which can be linked to a Service Now topic.
    - Other L2s can compose themselves with multiple of these alarms if necessary (becoming their default alarm set).
    - Ephemeral environments can't enable SNS actions to SNOW topics but they can to other custom topics.

    Example: Setting a L2 construct alarm (environment agnostic). This will raise a P3 incident in production
    and a P4 incident in the other static environments. To elevate to P2 in prod, use `incident_severity_if_in_prod`.

        self.default_alarm = Guest360Alarm(
            self,
            f"{construct_id}-SQSQueue",
            props={
                "metric": self.default_metric,
                "evaluation_periods": 1,
                "threshold": 1,
            }
        )
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        props: Union[dict, AlarmProps],
        **kwargs,
    ):
        self._config = self._load_config()
        self._set_environment(scope)
        self._check_and_process_props(props)
        super().__init__(
            scope,
            construct_id,
            **props,
            **kwargs,
        )
        self._add_sns_alarm(construct_id)

    @staticmethod
    def _load_config():
        file_path = os.path.realpath(__file__)
        app_dir = Path(file_path).absolute().parents[1]
        config = app_dir / "infrastructure" / "reliability" / "configs" / "alarm_defaults.yaml"
        return yaml.safe_load(config.open(mode="r"))

    def _set_environment(self, scope: Construct) -> None:
        self._resource = scope.node.id
        self._stack = Stack.of(scope)
        self._environment = scope.node.try_get_context("environment")
        self._prefix = scope.node.try_get_context("prefix")
        self._is_static_environment = "guest360" in self._prefix
        self._sns_snow_env = self._config["sns_snow_settings"][self._environment]

    def _check_and_process_props(self, props: Union[dict, AlarmProps]) -> None:
        AlarmProps(props)

        # Get main props
        self._actions_disabled = props.pop(
            "alarm_actions_disabled",
            False,
        )
        self._snow_integration_enabled = props.pop(
            "snow_integration_enabled",
            False,
        )
        self._custom_topic_name = props.pop(
            "custom_sns_alarm_topic_name",
            "",
        )
        self._snow_assignment_group = props.pop(
            "snow_assignment_group",
            "",
        )

        # If user provides snow assignment group, assume they want SNOW integration enabled
        if self._snow_assignment_group and not self._snow_integration_enabled:
            self._snow_integration_enabled = self._is_static_environment

        # Parameter errors
        if self._snow_integration_enabled and self._actions_disabled:
            raise AlarmPropError("For SNOW integration you cannot disable alarm actions.")
        if self._custom_topic_name and self._snow_integration_enabled and not self._snow_assignment_group:
            raise AlarmPropError("For custom SNS-SNOW integration an assignment group must be provided")

        # Set default SNOW assignment group
        if not self._snow_assignment_group:
            self._snow_assignment_group = self._sns_snow_env["snow_assignment_group"]

        # Map environment to incdent p-level parameter
        self._p_level_in_prod: str = props.pop(
            "p_level_in_prod",
            "default_topic",
        ).lower()

        # Topic-SNOW-Alarm Logic
        if not self._custom_topic_name or self._custom_topic_name in self._sns_snow_env.values():
            # If no topic name provided or is a default topic name, then set default behavior
            props["actions_enabled"] = self._is_static_environment
            self._snow_integration_enabled = self._is_static_environment
            if self._p_level_in_prod == "default_topic":
                self._custom_topic_name = eval(self._sns_snow_env[self._p_level_in_prod])
            else:
                self._custom_topic_name = self._sns_snow_env[self._p_level_in_prod]
        elif self._snow_integration_enabled:
            # If a custom name is provided and snow integration enabled, then only static envs should alarm
            props["actions_enabled"] = self._is_static_environment
        else:
            # If custom topic name provided with no snow integration, alarm actions are always on (even ephemeral)
            props["actions_enabled"] = True

        # Explicitly disabling actions will override everything else
        props["actions_enabled"] &= not self._actions_disabled

        # Alarm message description
        self._build_and_set_alarm_description(props)

        # Attribute for debugging and inspection
        self._processed_props = props

        # Default Treat Missing Data to Ignore vs Missing
        props["treat_missing_data"] = aws_cloudwatch.TreatMissingData.IGNORE

    def _build_and_set_alarm_description(self, props) -> None:
        comparison_operator = props.get(
            "comparison_operator",
            aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,  # Cloudwatch default
        )
        metric = props["metric"]
        threshold = props["threshold"]
        description = f"{self._resource} failed on {metric.metric_name} {comparison_operator} {threshold}"
        secondary_description = props.pop(
            "alarm_description",
            description,  # Default
        )
        if self._snow_integration_enabled:
            props["alarm_description"] = (
                f"[SNOWAG:{self._sns_snow_env['snow_assignment_group']}]"
                f"[SNOWCI:{self._sns_snow_env['snow_configuration_items']}]"
                f"[SNOWDESC:{description}]"
                f"{secondary_description}"
            )
        else:
            props["alarm_description"] = f"{description}. {secondary_description}"

    def _add_sns_alarm(self, id_: str) -> None:
        topic_arn = f"arn:aws:sns:{self._stack.region}:{self._stack.account}:{self._custom_topic_name}"
        self._topic = aws_sns.Topic.from_topic_arn(
            self,
            id_,
            topic_arn=topic_arn,
        )
        self._action = aws_cloudwatch_actions.SnsAction(self._topic)
        self.add_alarm_action(self._action)  # aws_cloudwatch.Alarm method
        self.add_ok_action(self._action)  # aws_cloudwatch.Alarm method
