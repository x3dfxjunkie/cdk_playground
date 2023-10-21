"""Source Data Contract for XBMS  EXPRNC_BAND_VNDR_INVTRY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_VNDR_INVTRY Data
    """

    EXPRNC_BAND_VNDR_INVTRY_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_VNDR_INVTRY_ID",
        name="",
        description="",
        example=500050,
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

    VNDR_INVTRY_ITEM_ID: int = Field(
        ...,
        alias="VNDR_INVTRY_ITEM_ID",
        name="",
        description="",
        example=505400,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VNDR_BAND_REORD_NTFCTN_DT: Optional[datetime] = Field(
        None,
        alias="VNDR_BAND_REORD_NTFCTN_DT",
        name="",
        description="",
        example="""2019-06-01 15:59:06""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INVTRY_ON_HND_CN: int = Field(
        ...,
        alias="INVTRY_ON_HND_CN",
        name="",
        description="",
        example=250,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INVTRY_COMTD_CN: int = Field(
        ...,
        alias="INVTRY_COMTD_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INVTRY_AVAIL_CN: int = Field(
        ...,
        alias="INVTRY_AVAIL_CN",
        name="",
        description="",
        example=300,
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
        example="""2019-03-12 00:31:59""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""XBANDAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""2012-12-02 23:50:34""",
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


class Metadata(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_VNDR_INVTRY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:50:17.245302""",
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
        example="""EXPRNC_BAND_VNDR_INVTRY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=64699767150049,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandVndrInvtryModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_VNDR_INVTRY
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_VNDR_INVTRY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_VNDR_INVTRY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
