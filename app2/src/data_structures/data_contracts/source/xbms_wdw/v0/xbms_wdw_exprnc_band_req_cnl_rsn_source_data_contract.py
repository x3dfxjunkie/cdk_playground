"""Source Data Contract for XBMS  EXPRNC_BAND_REQ_CNL_RSN"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_REQ_CNL_RSN Data
    """

    EXPRNC_BAND_REQ_CNL_RSN_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_CNL_RSN_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_CNL_RSN_CD: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_CNL_RSN_CD",
        name="",
        description="",
        example="""BABC01""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_CNL_RSN_CD_NM_STERLING: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_CNL_RSN_CD_NM_STERLING",
        name="",
        description="",
        example="""Reservation Cancelled""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_CNL_RSN_DS: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_CNL_RSN_DS",
        name="",
        description="",
        example="""Guest has completed the order but guest cancelled reservation before MB order has been sent to XPO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="",
        example="""reference_data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="""1995-05-06 02:08:53""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="",
        example="""reference_data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="""1971-08-23 00:05:08""",
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

    REQ_CNL_RSN_CST_DSPL_IN: str = Field(
        ...,
        alias="REQ_CNL_RSN_CST_DSPL_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_HLD_RSN_ID: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_REQ_HLD_RSN_ID",
        name="",
        description="",
        example=5049,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_REQ_CNL_RSN Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:49:51.825558""",
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
        example="""EXPRNC_BAND_REQ_CNL_RSN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=89801190951430,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandReqCnlRsnModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_REQ_CNL_RSN
    """

    class Config:
        """Payload Level Metadata"""

        title = "Experience Band Request Cancel Reason"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Table containing RAPI cancel codes for cancellation events."""  # optional
        unique_identifier = ["data.EXPRNC_BAND_REQ_CNL_RSN_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_REQ_CNL_RSN"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
