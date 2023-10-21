"""Source Data Contract Template for AIM_ACC_RESERVATION"""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox AIM_ACC_RESERVATION Data
    """

    ext_reservation_id: int = Field(
        ...,
        alias="EXT_RESERVATION_ID",
        name="",
        description="NA",
        example=740984,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    room_no: int = Field(
        ...,
        alias="ROOM_NO",
        name="",
        description="The system generated number for the room of the reservation",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    accom_code: Optional[str] = Field(
        None,
        alias="ACCOM_CODE",
        name="",
        description="Resort or Accoum Code",
        example="EGLPH",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    room_code: Optional[str] = Field(
        None,
        alias="ROOM_CODE",
        name="",
        description="Room code",
        example="PP5",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    block_code: Optional[str] = Field(
        None,
        alias="BLOCK_CODE",
        name="",
        description="NA",
        example="TTWDT19",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rate_code: Optional[str] = Field(
        None,
        alias="RATE_CODE",
        name="",
        description="rate_code",
        example="SP3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    service_date: Optional[datetime] = Field(
        None,
        alias="SERVICE_DATE",
        name="",
        description="service date",
        example="2020-12-24T06:30:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    freeze_id: Optional[str] = Field(
        None,
        alias="FREEZE_ID",
        name="",
        description="NA",
        example="OFF#694521",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    package_code: Optional[str] = Field(
        None,
        alias="PACKAGE_CODE",
        name="",
        description="NA",
        example="2020_WDTC_RST_CC_RT_BRD4_1_V1_B",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_modified_time: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="The time at which the last modification has done",
        example="2020-12-22T01:10:42.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox AIM_ACC_RESERVATION Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:30.613078""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    record_type: str = Field(
        ...,
        alias="record-type",
        name="",
        description="""Type of record""",
        example="""data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operation: str = Field(
        ...,
        alias="operation",
        name="",
        description="""Type of operation [insert, delete, update]""",
        example="""update""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="",
        description="""Partition key""",
        example="""schema-table""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schema_name: str = Field(
        ...,
        alias="schema-name",
        name="",
        description="""Name of schema""",
        example="""TBX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""AIM_ACC_RESERVATION""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=92646681613482,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestAimAccReservationModel(BaseModel):
    """
    Payload class for TravelBox AIM_ACC_RESERVATION
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Inventory Management Account Reservation"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = "NA"  # optional
        unique_identifier = ["data.EXT_RESERVATION_ID", "data.ROOM_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "AIM_ACC_RESERVATION"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
