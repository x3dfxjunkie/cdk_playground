"""Source Data Contract Template for ACC_FARE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACC_FARE Data
    """

    FARE_NO: int = Field(
        ...,
        alias="FARE_NO",
        name="",
        description="""The system generated number for the daily fare""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NETT_RATE: str = Field(
        ...,
        alias="NETT_RATE",
        name="",
        description="""A flag indicating the fares defined for the board basis are costs ( value is 1 ) or prices ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEASON: int = Field(
        ...,
        alias="SEASON",
        name="",
        description="""The system generated number of the season for which the rates are defined""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DAYS: str = Field(
        ...,
        alias="DAYS",
        name="",
        description=""" The days of the week for which the allocations are defined_x000D_
  1 - Sunday_x000D_
  2 - Monday_x000D_
  3 - Tuesday_x000D_
  4 - Wednesday_x000D_
  5 - Thursday_x000D_
  6 - Friday_x000D_
  7 - Saturday_x000D_
  Example1 :- If allocations are for all days of the week in the defined period this value is 1234567_x000D_
  Example2 :- If allocations are for only weekends this value is 17""",
        example="""1234567""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NIGHTS: int = Field(
        ...,
        alias="NIGHTS",
        name="",
        description="""This is 1 since the rates are for a day.""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURRENCY: Optional[str] = Field(
        None,
        alias="CURRENCY",
        name="",
        description="""The TravelBox code of the currency in which the board basis fares are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SINGLE_FARE: float = Field(
        ...,
        alias="SINGLE_FARE",
        name="",
        description="""The single fare amount""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TWIN_FARE: float = Field(
        ...,
        alias="TWIN_FARE",
        name="",
        description="""The twin fare amount""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UNIT_FARE: float = Field(
        ...,
        alias="UNIT_FARE",
        name="",
        description="""The unit fare amount""",
        example=2272.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTRABED_FARE: float = Field(
        ...,
        alias="EXTRABED_FARE",
        name="",
        description="""The extrabed fare amount""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TEEN_FARE: float = Field(
        ...,
        alias="TEEN_FARE",
        name="",
        description="""The teen fare of the board basis""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD_FARE: float = Field(
        ...,
        alias="CHILD_FARE",
        name="",
        description="""The child fare of the board basis""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INFANT_FARE: float = Field(
        ...,
        alias="INFANT_FARE",
        name="",
        description="""The infant fare of the board basis""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FOC_CONTRACT: Optional[int] = Field(
        None,
        alias="FOC_CONTRACT",
        name="",
        description="""The system generated id of the contract""",
        example=4390,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FOC_NO: Optional[int] = Field(
        None,
        alias="FOC_NO",
        name="",
        description="""Deprecated""",
        example=2805,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD2_FARE: Optional[float] = Field(
        None,
        alias="CHILD2_FARE",
        name="",
        description="""The child2 fare of the board basis""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TEEN2_FARE: Optional[float] = Field(
        None,
        alias="TEEN2_FARE",
        name="",
        description="""The teen2 fare of the board basis""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD3_FARE: Optional[float] = Field(
        None,
        alias="CHILD3_FARE",
        name="",
        description="""The child3 fare of the board basis""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD4_FARE: Optional[float] = Field(
        None,
        alias="CHILD4_FARE",
        name="",
        description="""The child4 fare of the board basis""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHILD5_FARE: Optional[float] = Field(
        None,
        alias="CHILD5_FARE",
        name="",
        description="""The child5 fare of the board basis""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SINGLE2_FARE: Optional[float] = Field(
        None,
        alias="SINGLE2_FARE",
        name="",
        description="""The single2 fare amount""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TWIN2_FARE: Optional[float] = Field(
        None,
        alias="TWIN2_FARE",
        name="",
        description="""The twin2 fare amount""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTRABED2_FARE: Optional[float] = Field(
        None,
        alias="EXTRABED2_FARE",
        name="",
        description="""The extrabed2 fare amount""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_PAX: Optional[int] = Field(
        None,
        alias="MIN_PAX",
        name="",
        description="""If this is a group based contract, the minimum number of pax for which the rates are applied""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_PAX: Optional[int] = Field(
        None,
        alias="MAX_PAX",
        name="",
        description="""If this is a group based contract, the maximum number of pax for which the rates are applied""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1983-12-21 02:16:51""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=55491,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ROOM_APT_NO: int = Field(
        ...,
        alias="ROOM_APT_NO",
        name="",
        description="""The system generated number of the room/apartment of the contract""",
        example=35,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACC_FARE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:18.366303""",
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
        example="""ACC_FARE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=98098329518343,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestAccFareModel(BaseModel):
    """
    Payload class for TravelBox ACC_FARE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accommodation Fare"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store Room/Apartment fare information when Rate Type is 'Per Person'. The values are setup in 'Rooms' node in Accommodation Manager"""  # optional
        unique_identifier = ["data.CONTRACT_ID", "data.ROOM_APT_NO", "data.FARE_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ACC_FARE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
