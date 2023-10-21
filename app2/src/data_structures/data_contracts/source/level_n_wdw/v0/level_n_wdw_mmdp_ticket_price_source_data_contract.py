"""Source Data Contract for Level-N MMDP_TICKET_PRICE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N MMDP_TICKET_PRICE Data
    """

    ID: int = Field(
        ...,
        alias="ID",
        name="",
        description="""""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TICKET_CODE: Optional[str] = Field(
        None,
        alias="TICKET_CODE",
        name="",
        description="""""",
        example="""AJFMM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TIKCET_PRICE: Optional[float] = Field(
        None,
        alias="TIKCET_PRICE",
        name="",
        description="""""",
        example=39.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TIKCET_DESC: Optional[str] = Field(
        None,
        alias="TIKCET_DESC",
        name="",
        description="""""",
        example="""Resident 1-Day Magic Your Way EPCOT�� or Disney���s Hollywood Studios�� or Disney���s Animal Kingdom��Ticket 10+ with 1-Day Memory Maker""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""LNS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""1978-01-29 03:53:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""LNS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2020-10-27 13:44:47""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LGCL_DEL_IN: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="""""",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_SLS_TAX: Optional[float] = Field(
        None,
        alias="LVL_N_ENTTL_SLS_TAX",
        name="",
        description="""""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N MMDP_TICKET_PRICE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:35.735443""",
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
        example="""SFLNSMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""MMDP_TICKET_PRICE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=25091216458942,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWMmdpTicketPriceModel(BaseModel):
    """
    Payload class for Level N MMDP_TICKET_PRICE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Memory Maker Day Pass Ticket Price"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Reference table containing memory maker day pass codes and their ticket price and description."""  # optional
        unique_identifier = ["data.ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "MMDP_TICKET_PRICE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
