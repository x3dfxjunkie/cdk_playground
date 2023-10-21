"""Guest360DMSAlarm  Construct
"""
from typing import TypedDict
from aws_cdk import aws_cloudwatch, Duration
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.guest360_constructs.construct_360 import Construct360


@match_class_typing
class DMSDimensionMapProps(TypedDict):
    ReplicationInstanceIdentifier: str  # pylint: disable=C0103
    ReplicationTaskIdentifier: NotRequired[str]  # pylint: disable=C0103


class Guest360DMSAlarm(Construct360):
    """Guest360 Construct for DMS Alarms"""

    def __init__(
        self,
        scope: Construct360,
        construct_id: str,
        dimensions_map: DMSDimensionMapProps,
        dms_alarm_list: list,
        **kwargs,
    ) -> None:
        """__init__.
        Construct to create DMS Alarms
        Args:
            scope (Construct360)
            construct_id (str): Construct ID
            dimensions_map(dict) : Replication Instance and Task Identifiers
            dms_alarm_list(list) : List of alarms to create, composed for metrics and alarm params
        Returns:
            None
        """
        super().__init__(scope, construct_id, **kwargs)

        # Check that props matches proper input structure
        DMSDimensionMapProps(dimensions_map)

        # Convert from str to aws_cloudwatch.ComparisonOperator type
        alarm_comparison_operator = {
            "GREATER_THAN_OR_EQUAL_TO_THRESHOLD": aws_cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
            "GREATER_THAN_THRESHOLD": aws_cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
            "GREATER_THAN_UPPER_THRESHOLD": aws_cloudwatch.ComparisonOperator.GREATER_THAN_UPPER_THRESHOLD,
            "LESS_THAN_LOWER_OR_GREATER_THAN_UPPER_THRESHOLD": aws_cloudwatch.ComparisonOperator.LESS_THAN_LOWER_OR_GREATER_THAN_UPPER_THRESHOLD,
            "LESS_THAN_LOWER_THRESHOLD": aws_cloudwatch.ComparisonOperator.LESS_THAN_LOWER_THRESHOLD,
            "LESS_THAN_THRESHOLD": aws_cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
            "LESS_THAN_OR_EQUAL_TO_THRESHOLD": aws_cloudwatch.ComparisonOperator.LESS_THAN_OR_EQUAL_TO_THRESHOLD,
        }
        for dms_alarm in dms_alarm_list:
            # Create Metric
            dms_cw_metric = aws_cloudwatch.Metric(
                namespace="AWS/DMS",
                metric_name=dms_alarm["metric_name"],
                statistic=dms_alarm["metric"]["statistic"],
                period=Duration.seconds(dms_alarm["metric"]["period_in_seconds"]),
                dimensions_map=dimensions_map,
            )

            # Create alarm
            alarm_props = dms_alarm["alarm"].copy()
            alarm_props["metric"] = dms_cw_metric
            alarm_props["comparison_operator"] = alarm_comparison_operator[alarm_props["comparison_operator"]]

            Guest360Alarm(self, dms_alarm["metric_name"], props={**alarm_props})
