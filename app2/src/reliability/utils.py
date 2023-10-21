#!/usr/bin/env python
"""Utils library for Guest360"""

import re


# function to shorten prefixes for resources that have very low name length limits
def shorten_prefix(prefix: str) -> str:
    if "guest360" in prefix:
        short_prefix = prefix.replace("guest360", "g360")
    else:
        short_prefix = prefix.replace("-pr", "")
    return short_prefix


def clean_resource_name(base_name: str) -> str:
    valid_pattern = r"^[\.\-_A-Za-z0-9]+$"
    if not re.match(valid_pattern, base_name):
        base_name = re.sub("_", "-", re.sub(r"[\W]", "", base_name.lower()))
    return base_name


class BuildName:
    """BuildName

    This class will build a resource name based on inputs

    Args:
        prefix (str): prefix for the build name
        base_name (str): base_name for the build name
        max_length (int): the max length of the resource name

    Returns:
        string
    """

    def __init__(self, prefix: str, base_name: str, max_length: int, min_length: int = 0) -> None:
        """Init method for BuildName class

        Args:
            prefix (str): Prefix for name
            base_name (str): Base name for name
            max_length (int): Max length of name (will cut off at the end)
            min_length (int, optional): Minimum length of name. Defaults to 0.

        Raises:
            ValueError: max_length Cannot be Negative
            ValueError: min_length Cannot be Negative
            ValueError: min_length cannot be greater than, or equal to max_length.
        """
        self.prefix = prefix
        self.base_name = base_name

        if max_length < 0:
            raise ValueError("max_length Cannot be Negative")

        if min_length < 0:
            raise ValueError("min_length Cannot be Negative")

        if min_length >= max_length:
            raise ValueError("min_length cannot be greater than, or equal to max_length.")

        self.max_length = max_length
        self.min_length = min_length

    def name(self) -> str:
        """Returns the name based on provided values in initialization method

        Returns:
            str: Name
        """
        invalid_ending_chars = "-."
        return (
            "-".join([self.prefix, self.base_name])
            .lower()[self.min_length : self.max_length]
            .strip(invalid_ending_chars)
        )


class ContainerName(BuildName):
    """
    Naming convention for docker containers
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for ContainerName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=255)


class DashboardName(BuildName):
    """CloudWatch DashboardName

    Dashboard Name contains 255 characters alphanumeric characters
    including hyphens and underscores.

    More info:

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#aws-resource-cloudwatch-dashboard-properties

    Args:
        prefix (str): prefix for stack name
        base_name (str): base name for dashboard name
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for DashboardName

        Args:
            prefix (str): prefix for stack name
            base_name (str): base name for Dashboard name
        """
        super().__init__(
            re.sub("[^A-Za-z0-9._-]", "-", prefix.lower()),
            re.sub("[^A-Za-z0-9._-]", "-", base_name.lower()),
            max_length=255,
        )


class DynamoDBTableName(BuildName):
    """
    Naming Convention for DynamoDB Tables
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for DynamoDBTableName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=255)


class ECRRepoName(BuildName):
    """
    Naming convention for ECR Repositories
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for ECRRepoName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=256, min_length=2)


class ECSClusterName(BuildName):
    """
    Naming convention for ECR Clusters
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for ECSClusterName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=255)


class FargateServiceName(BuildName):
    """
    Naming convention for Fargate Services
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for FargateServiceName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=255)


class KinesisStreamName(BuildName):
    """
    Naming convention for Kinesis Streams
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for KinesisStreamName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=128)


class KmsKeyAliasName(BuildName):
    """
    Naming convention for KMS Key Aliases
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for KmsKeyAliasName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(
            re.sub("[^A-Za-z0-9_-]", "", prefix),
            re.sub("[^A-Za-z0-9_-]", "", base_name),
            max_length=256,
        )


class LambdaFunctionName(BuildName):
    """
    Naming convention for Lambda Functions
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for LambdaFunctionName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(
            re.sub("[^A-Za-z0-9._-]", "", prefix),
            re.sub("[^A-Za-z0-9._-]", "", base_name),
            max_length=64,
        )


class QueueName(BuildName):
    """
    Naming convention for Queues
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for QueueName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=80)


class RoleName(BuildName):
    """
    Naming convention for IAM Roles
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for RoleName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=64)


class LogGroup(BuildName):
    """
    Naming convention for Log Groups
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for LogGroup

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=512)


class StateMachine(BuildName):
    """
    Naming convention for State Machines
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for StateMachine

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=80)


class S3BucketName(BuildName):
    """S3BucketName

    Reference:
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html

    Args:
        prefix (str): prefix for bucket name
        base_name (str): base name for bucket name

    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """S3BucketName

        Reference:
        https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html

        Args:
            prefix (str): prefix for bucket name
            base_name (str): base name for bucket name

        """
        super().__init__(
            # Substitute any characters NOT matching a-z, 0-9 or - with a -.
            # Substitute all trailing non alphanumeric characters with empty space
            re.sub("[^a-z0-9-]", "-", prefix.lower()),
            re.sub("[^a-z0-9]*$", "", re.sub("[^a-z0-9-]", "-", base_name.lower())),
            max_length=63,
        )


class SecurityGroupName(BuildName):
    """
    Naming convention for Security Groups
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for SecurityGroupName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=255)


class StackName(BuildName):
    """StackName

    Stack Name contains 128 characters alphanumeric characters
    including hyphens.

    More info:

    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console-create-stack-parameters.html

    Args:
        prefix (str): prefix for stack name
        base_name (str): base name for stack name
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for SecurityGroupName

        Args:
            prefix (str): prefix for stack name
            base_name (str): base name for stack name
        """
        super().__init__(
            re.sub("[^A-Za-z0-9.-]", "-", prefix.lower()),
            re.sub("[^A-Za-z0-9.-]", "-", base_name.lower()),
            max_length=128,
        )


class KinesisFirehoseName(BuildName):
    """
    Naming convention for Kinesis Firehoses
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for KinesisFirehoseName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=64)


class GlueJobName(BuildName):
    """
    Naming convention for Glue
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for GlueJobName
        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=64)


class EventBridgePipeName(BuildName):
    """
    Naming convention for Event Bridge Pipes
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for EventBridgePipeName
        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        # regex supplied from docs: https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_CreatePipe.html
        super().__init__(prefix, clean_resource_name(base_name), max_length=64)


class DMSResourceName(BuildName):
    """
    Naming convention for DMS resource names
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for DmsEndpointName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        prefix = shorten_prefix(prefix)
        # more info on names https://docs.aws.amazon.com/cli/latest/reference/dms/create-replication-task.html
        # https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Creating.html
        super().__init__(prefix, clean_resource_name(base_name), max_length=31)


class AppConfigName(BuildName):
    """
    Naming convention for App Config
    """

    def __init__(self, prefix: str, base_name: str) -> None:
        """init method for AppConfigName

        Args:
            prefix (str): Prefix of name
            base_name (str): Base name
        """
        super().__init__(prefix, base_name, max_length=64)
        # more info: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-name
