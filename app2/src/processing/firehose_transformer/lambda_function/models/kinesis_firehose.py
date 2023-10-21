"""
    Kinesis Firehose Models
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class KinesisFirehoseRecord(BaseModel):
    """
    This dataclass contains an Kinesis Firehose Record to promote strong typing
    """

    record_id: Optional[str] = Field(alias="recordId")
    approximate_arrival_timestamp: int = Field(alias="approximateArrivalTimestamp")
    data: str

    class Config:
        allow_population_by_field_name = True


class KinesisFirehoseResponseRecord(BaseModel):
    """
    This dataclass contains an Kinesis Firehose Record to promote strong typing
    """

    record_id: Optional[str] = Field(alias="recordId")
    approximate_arrival_timestamp: int = Field(alias="approximateArrivalTimestamp")
    data: str
    result: str
    metadata: Optional[Dict[str, Any]] = None

    class Config:
        allow_population_by_field_name = True


class KinesisFirehoseEvent(BaseModel):
    """
    This dataclass contains an Kinesis Firehose Event to promote strong typing
    """

    invocation_id: Optional[str] = Field(alias="invocationId")
    delivery_stream_arn: Optional[str] = Field(alias="deliveryStreamArn")
    region: Optional[str] = None
    records: List[KinesisFirehoseRecord]


class KinesisFirehoseResponse(BaseModel):
    """
    This dataclass contains an Kinesis Firehose Response to promote strong typing
    """

    records: List[KinesisFirehoseResponseRecord]
