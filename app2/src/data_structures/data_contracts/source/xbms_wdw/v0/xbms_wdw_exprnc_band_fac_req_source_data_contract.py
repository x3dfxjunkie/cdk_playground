"""Source Data Contract for XBMS  EXPRNC_BAND_FAC_REQ"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_FAC_REQ Data
    """

    EXPRNC_BAND_REQ_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_ID",
        name="",
        description="",
        example=714000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_ID: int = Field(
        ...,
        alias="DSNY_FAC_ID",
        name="",
        description="",
        example=503300,
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

    EXPRNC_BAND_REQ_DS: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_REQ_DS",
        name="",
        description="",
        example="""1 M blue band""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PKG_CMPNT_ID: Optional[int] = Field(
        None,
        alias="PKG_CMPNT_ID",
        name="",
        description="",
        example=4373,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FAC_REQ_EXPECT_DLVR_DT: Optional[datetime] = Field(
        None,
        alias="FAC_REQ_EXPECT_DLVR_DT",
        name="",
        description="",
        example="""1993-09-05 10:23:07""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_CTR_ID: Optional[int] = Field(
        None,
        alias="COST_CTR_ID",
        name="",
        description="",
        example=8402,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WBS_ELMNT_ID: Optional[int] = Field(
        None,
        alias="WBS_ELMNT_ID",
        name="",
        description="",
        example=8504,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GNRL_LDGR_ID: Optional[int] = Field(
        None,
        alias="GNRL_LDGR_ID",
        name="",
        description="",
        example=6543,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OVRD_EXPRNC_BAND_STS_ID: Optional[int] = Field(
        None,
        alias="OVRD_EXPRNC_BAND_STS_ID",
        name="",
        description="",
        example=778,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AVAIL_GI_IN: str = Field(
        ...,
        alias="AVAIL_GI_IN",
        name="",
        description="",
        example="""Y""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_HLD_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_HLD_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURR_REQ_HLD_RSN_ID: Optional[int] = Field(
        None,
        alias="CURR_REQ_HLD_RSN_ID",
        name="",
        description="",
        example=3162,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MERCH_PO_NB: Optional[str] = Field(
        None,
        alias="MERCH_PO_NB",
        name="",
        description="",
        example="""gUkJluexrwaOEbEeYxvt""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_ON_DMND_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_ON_DMND_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BAB_SHIPMT_NB: Optional[str] = Field(
        None,
        alias="BAB_SHIPMT_NB",
        name="",
        description="",
        example="""EerJXSrnoGBQunAYXRQY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_FAC_REQ Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:46:44.991190""",
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
        example="""EXPRNC_BAND_FAC_REQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=24950018236503,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandFacReqModel(BaseModel):
    """
    Payload class for XBMS EXPRNC_BAND_FAC_REQ
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_REQ_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXPRNC_BAND_FAC_REQ"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
