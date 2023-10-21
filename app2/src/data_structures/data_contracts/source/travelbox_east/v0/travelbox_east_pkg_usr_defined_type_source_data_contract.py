"""Source Data Contract Template for PKG_USR_DEFINED_TYPE"""

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox PKG_USR_DEFINED_TYPE Data
    """

    user_defined_type_id: int = Field(
        ...,
        alias="USER_DEFINED_TYPE_ID",
        name="",
        description="Auto generated number",
        example=2321,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    package_id: int = Field(
        ...,
        alias="PACKAGE_ID",
        name="",
        description="Package foreign key",
        example=14013,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_modified_time: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="The time at which the last modification has done",
        example="2016-05-31T06:08:45.448Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    element_id: Optional[int] = Field(
        None,
        alias="ELEMENT_ID",
        name="",
        description="Element foreign key",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    attribute_id: Optional[int] = Field(
        None,
        alias="ATTRIBUTE_ID",
        name="",
        description="Attribute foreign key",
        example=112,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    free_text_value: Optional[str] = Field(
        None,
        alias="FREE_TEXT_VALUE",
        name="",
        description="Free text value",
        example="FAOLFW1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    attribute_type: Optional[int] = Field(
        None,
        alias="ATTRIBUTE_TYPE",
        name="",
        description="Attribute type of parent table : 0-free text,1-single select, 2-multi select",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    date_value: Optional[datetime] = Field(
        None,
        alias="DATE_VALUE",
        name="",
        description="NA",
        example="2021-10-22 12:00:00.000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    element_history_id: Optional[int] = Field(
        None,
        alias="ELEMENT_HISTORY_ID",
        name="",
        description="NA",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox PKG_USR_DEFINED_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:49:31.731692""",
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
        example="""PKG_USR_DEFINED_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=78869253490039,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastPkgUsrDefinedTypeModel(BaseModel):
    """
    Payload class for TravelBox PKG_USR_DEFINED_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Package User Defined Type"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = "NA"  # optional
        unique_identifier = ["data.USER_DEFINED_TYPE_ID", "data.PACKAGE_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PKG_USR_DEFINED_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
