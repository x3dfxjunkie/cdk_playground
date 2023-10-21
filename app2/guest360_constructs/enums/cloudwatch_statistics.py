"""Cloudwatch statistics Enum for Percentiles"""
from enum import Enum


class CloudwatchPercentileStatistics(str, Enum):
    """Enum for Percentile options you can give
    for Cloudwatch Metrics, given that CDK does not have a set of enum
    values for Percentile statistics.

    These are all the available statistics that can be supplied:
    https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html

    And the Statistic enum that CDK offers:
    https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_cloudwatch/Statistic.html
    """

    P10: str = "p10"
    P20: str = "p20"
    P30: str = "p30"
    P40: str = "p40"
    P50: str = "p50"
    P60: str = "p60"
    P70: str = "p70"
    P80: str = "p80"
    P90: str = "p90"
    P95: str = "p95"
    P99: str = "p99"
