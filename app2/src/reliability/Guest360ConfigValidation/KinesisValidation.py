
from typing import Union

import aws_cdk.aws_kinesis as kinesis
from aws_cdk import Duration


class Guest360ConfigKinesisValidation():
    """Validation method for Kinesis
    """

    def getKinesisShardCount(shard_count: int) -> Union[int, None]:
        """Check if the number of shards is an integer and also > 0

        Args:
            shard_count (int): Number of shards to provision

        Returns:
            int | None: returns the number of shards or None
        """
        # Check if integer
        if isinstance(shard_count, int) and shard_count > 0:
            return shard_count
        else:
            return None

    def getKinesisRetentionPeriod(retention_period: int) -> Union[Duration, None]:
        """Returns the number of days of retention for the Kinesis Stream. Check if the retention_period is an integration and >0 and <=365

        Args:
            retention_period (int): Check if an integration and >0 and <=365

        Returns:
            Duration | None: valid retention_period in Duration.days or None
        """
        # Check if integer and <= 365 days
        if isinstance(retention_period, int) and retention_period > 0 and retention_period <= 365:
            return Duration.days(retention_period)
        else:
            return None

    def getKinesisStreamMode(stream_mode: str) -> Union[kinesis.StreamMode, None]:
        """Checks if the Kinesis Stream Mode is "ON_DEMAND" or "PROVISIONED"

        Args:
            stream_mode (str): validate the stream mode string provided

        Returns:
            kinesis.StreamMode | None: Literal value of the stream mode - kinesis.StreamMode.ON_DEMAND or kinesis.StreamMode.PROVISIONED, or None if it is incorrect
        """
        if stream_mode == "ON_DEMAND":
            return kinesis.StreamMode.ON_DEMAND
        elif stream_mode == "PROVISIONED":
            return kinesis.StreamMode.PROVISIONED
        else:
            return None
