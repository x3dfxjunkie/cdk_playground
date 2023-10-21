"""Source Data Contract Template for UDA_APPLICABLE_VALUE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox UDA_APPLICABLE_VALUE Data
    """

    APPLICABLE_VALUE_CODE: Optional[str] = Field(
        None,
        alias="APPLICABLE_VALUE_CODE",
        name="",
        description="""NaN""",
        example="""T2""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPLICABLE_VALUE_ID: float = Field(
        ...,
        alias="APPLICABLE_VALUE_ID",
        name="",
        description="""user defined attribute value id""",
        example=107.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTRIBUTE_ID: float = Field(
        ...,
        alias="ATTRIBUTE_ID",
        name="",
        description="""User defined attribute id""",
        example=33.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    APPLICABLE_VALUES: Optional[str] = Field(
        None,
        alias="APPLICABLE_VALUES",
        name="",
        description="""Applicable values""",
        example="""T2""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT: Optional[str] = Field(
        None,
        alias="DEFAULT",
        name="",
        description="""An occupancy group can have multiple occupancies. This field marks whether this is the default occupancy of the occupancy group ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATTRIBUTE_TYPE: int = Field(
        ...,
        alias="ATTRIBUTE_TYPE",
        name="",
        description="""Attribute type of parent table : 0-free text,1-single select, 2-multi select""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACTIVE: Optional[str] = Field(
        None,
        alias="ACTIVE",
        name="",
        description="""Whether 3D secure filter is active or not""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1971-10-11 17:33:14""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox UDA_APPLICABLE_VALUE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:43:07.907485""",
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
        example="""UDA_APPLICABLE_VALUE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=60866423270884,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestUdaApplicableValueModel(BaseModel):
    """
    Payload class for TravelBox UDA_APPLICABLE_VALUE
    """

    class Config:
        """Payload Level Metadata"""

        title = "User Defined Attribute Applicable Value"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """User defined attribute values"""  # optional
        unique_identifier = ["data.APPLICABLE_VALUE_ID", "data.ATTRIBUTE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "UDA_APPLICABLE_VALUE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
