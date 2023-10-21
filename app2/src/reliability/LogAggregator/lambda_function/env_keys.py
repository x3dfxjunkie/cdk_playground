"""
Environment variables shared between Lambda construct and Lambda code.
"""
from enum import Enum


class EnvKeys(Enum):
    """
    Keys for environment variable for the Lambda function
    """

    STREAM_ARN = "STREAM_ARN"
    SUBSCRIPTION_FILTER_ROLE_ARN = "SUBSCRIPTION_FILTER_ROLE_ARN"
    GROUP_PATTERNS = "GROUP_PATTERNS"
    NOT_GROUP_PATTERNS = "NOT_GROUP_PATTERNS"
    EVENT_PATTERNS = "EVENT_PATTERNS"
