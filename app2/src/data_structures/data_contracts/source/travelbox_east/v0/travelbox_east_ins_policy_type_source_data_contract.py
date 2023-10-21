"""Source Data Contract Template for INS_POLICY_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox INS_POLICY_TYPE Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""TI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Travel Insurance""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INS_GROUP: Optional[str] = Field(
        None,
        alias="INS_GROUP",
        name="",
        description="""The associated insurance group as defined in 'INS_POLICY_GROUP' configuration""",
        example="""Family""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INS_LEVEL: Optional[str] = Field(
        None,
        alias="INS_LEVEL",
        name="",
        description="""The associated insurance level as defined in 'INS_POLICY_GROUP' configuration""",
        example="""Standard""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TYPE: Optional[str] = Field(
        None,
        alias="TYPE",
        name="",
        description="""The availbility type (1 = Available 2 = Free Sell)""",
        example="""lTapkZGAAXvMGyhRzHdn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox INS_POLICY_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:52:49.698650""",
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
        example="""INS_POLICY_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=38093406341424,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastInsPolicyTypeModel(BaseModel):
    """
    Payload class for TravelBox INS_POLICY_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Insurance Policy Type"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """Contains insurance policy types which can be created using insurance module -> setup menu -> policy types"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "INS_POLICY_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
