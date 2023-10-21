"""
This lambda function is triggered daily and on log group creation. It will subscribe all log groups that match the
environment variable filters to the configured Kinesis stream.
"""
import json
import os
import fnmatch

import boto3
import logging

from app.src.reliability.LogAggregator.lambda_function.env_keys import EnvKeys

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Get environment variables
stream_arn = os.environ[EnvKeys.STREAM_ARN.value]
subscription_filter_role_arn = os.environ[EnvKeys.SUBSCRIPTION_FILTER_ROLE_ARN.value]
include_group_patterns = os.getenv(EnvKeys.GROUP_PATTERNS.value, "*").split(",")
exclude_group_patterns = os.getenv(EnvKeys.NOT_GROUP_PATTERNS.value, "").split(",")
on_events = os.getenv(EnvKeys.EVENT_PATTERNS.value, "").split(",")
filter_pattern = " ".join([f"?{pattern}" for pattern in on_events]) if on_events else ""
region = os.getenv("AWS_REGION")


logs = boto3.client("logs", region_name=region)


def name_does_match_patterns(input_string, patterns_list) -> bool:
    return any(fnmatch.fnmatch(input_string.lower(), pattern.lower()) for pattern in patterns_list)


def log_group_is_matched(name: str) -> bool:
    if name_does_match_patterns(name, exclude_group_patterns):
        return False
    else:
        return name_does_match_patterns(name, include_group_patterns)


def get_filtered_log_groups() -> list:
    """Returns a list of cloudwatch log group names filtered using Lambda environment variables.

    Returns:
        list: log group names that pass the filter
    """
    log_groups = logs.describe_log_groups()["logGroups"]
    filtered_log_groups = []
    for log_group in log_groups:
        group_name = log_group["logGroupName"]
        if log_group_is_matched(group_name):
            filtered_log_groups.append(group_name)
    return filtered_log_groups


def group_not_subscribed_to_this_stream(subscription_filters: list) -> bool:
    return not any(subscription_filter["destinationArn"] == stream_arn for subscription_filter in subscription_filters)


def put_subscription_filter(log_group_name: str) -> None:
    logs.put_subscription_filter(
        logGroupName=log_group_name,
        filterName="LogEventsToKinesis",
        filterPattern=filter_pattern,
        destinationArn=stream_arn,
        roleArn=subscription_filter_role_arn,
        distribution="Random",
    )


def lambda_handler(event, _) -> None:
    # Cron Trigger
    if event.get("source") == "aws.events":
        # Loop through all log groups in the account, filtering by environment variables
        for name in get_filtered_log_groups():
            subscriptions = logs.describe_subscription_filters(logGroupName=name)["subscriptionFilters"]
            if group_not_subscribed_to_this_stream(subscriptions):
                put_subscription_filter(name)
    # LogGroup Creation Trigger
    elif event.get("source") == "aws.logs" and event["detail"]["eventName"] == "CreateLogGroup":
        name = event["detail"]["requestParameters"]["logGroupName"]
        if log_group_is_matched(name):
            put_subscription_filter(name)
    # Unknown event trigger
    else:
        logger.error(msg=json.dumps(event, indent=2, default=str))
        raise ValueError("Event is not from the daily trigger or log group creation")
