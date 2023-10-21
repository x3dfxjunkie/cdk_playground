"""Source Data Contract for XBMS  PO"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS PO Data
    """

    PO_ID: int = Field(
        ...,
        alias="PO_ID",
        name="",
        description="",
        example=26662,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_VNDR_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_VNDR_ID",
        name="",
        description="",
        example=10048,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_MFR_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_MFR_ID",
        name="",
        description="",
        example=502651,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PO_STS_ID: int = Field(
        ...,
        alias="PO_STS_ID",
        name="",
        description="",
        example=10004,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PO_NB: str = Field(
        ...,
        alias="PO_NB",
        name="",
        description="",
        example="""6505794398""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PO_PLACED_DT: datetime = Field(
        ...,
        alias="PO_PLACED_DT",
        name="",
        description="",
        example="""2021-10-16 03:18:26""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PO_EXPECT_SHIP_DT: Optional[datetime] = Field(
        None,
        alias="PO_EXPECT_SHIP_DT",
        name="",
        description="",
        example="""1980-04-11 01:40:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PO_EXPECT_DLVR_DT: Optional[datetime] = Field(
        None,
        alias="PO_EXPECT_DLVR_DT",
        name="",
        description="",
        example="""1975-09-28 00:49:15""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PO_ACTL_SHIP_DT: Optional[datetime] = Field(
        None,
        alias="PO_ACTL_SHIP_DT",
        name="",
        description="",
        example="""1978-01-17 12:43:34""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PO_ACTL_DLVR_DT: Optional[datetime] = Field(
        None,
        alias="PO_ACTL_DLVR_DT",
        name="",
        description="",
        example="""1975-11-20 17:46:06""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""XBANDAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1979-07-25 19:40:06""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""Nanda Venugopal""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1989-06-08 13:30:04""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOGICAL_DEL_IN: str = Field(
        ...,
        alias="LOGICAL_DEL_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SIMBA_SHIPMT_NB: Optional[str] = Field(
        None,
        alias="SIMBA_SHIPMT_NB",
        name="",
        description="",
        example="""quHIrcspfCIBybKAjIiM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTERNRECEIPTKEY: Optional[str] = Field(
        None,
        alias="EXTERNRECEIPTKEY",
        name="",
        description="",
        example="""rqwibQjuuqxaWCWsZkLG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS PO Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:44:12.083519""",
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
        example="""XBANDMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""PO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=19443099533903,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWPoModel(BaseModel):
    """
    Payload class for XBMS PO
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.PO_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PO"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
