"""Module for utility functions relating to CloudWatch alarms"""
from typing import Any, Dict
from aws_cdk import aws_cloudwatch, Duration


def create_alarm_for_incoming_log_traffic(log_group_name: str, period_in_minutes: int) -> Dict[str, Any]:
    return {
        "metric": aws_cloudwatch.Metric(
            namespace="AWS/Logs",
            metric_name="IncomingLogEvents",
            statistic=aws_cloudwatch.Statistic.SUM.value,
            period=Duration.minutes(period_in_minutes),
            dimensions_map={"LogGroupName": log_group_name},
        ),
        "evaluation_periods": 1,
        "threshold": 1,
        "alarm_description": f"WARNING No logs received in {period_in_minutes} minutes. Possible error with container.",
        "datapoints_to_alarm": 1,
        "comparison_operator": aws_cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
        "alarm_actions_disabled": False,
    }
