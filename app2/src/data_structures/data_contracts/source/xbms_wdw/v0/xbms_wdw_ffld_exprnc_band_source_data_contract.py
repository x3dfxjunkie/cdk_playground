"""Source Data Contract for XBMS  FFLD_EXPRNC_BAND"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS FFLD_EXPRNC_BAND Data
    """

    FFLD_EXPRNC_BAND_ID: int = Field(
        ...,
        alias="FFLD_EXPRNC_BAND_ID",
        name="",
        description="",
        example=3395160,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ID: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_ID",
        name="",
        description="",
        example=1854010,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_CONFIG_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_CONFIG_ID",
        name="",
        description="",
        example=502652,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIPMT_CASE_ID: int = Field(
        ...,
        alias="SHIPMT_CASE_ID",
        name="",
        description="",
        example=523300,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_PUBLIC_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_PUBLIC_ID",
        name="",
        description="",
        example=7641642,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_EXTNL_NB: str = Field(
        ...,
        alias="EXPRNC_BAND_EXTNL_NB",
        name="",
        description="",
        example="""107261352204""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_SECURE_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_SECURE_ID",
        name="",
        description="",
        example=1008012843302935,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_SHORT_RNGE_TAG_NB: int = Field(
        ...,
        alias="EXPRNC_BAND_SHORT_RNGE_TAG_NB",
        name="",
        description="",
        example=36076921229433860,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_LONG_RNGE_TAG_NB: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_LONG_RNGE_TAG_NB",
        name="",
        description="",
        example=7641642,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_LOT_NB: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_LOT_NB",
        name="",
        description="",
        example="""HctSxCIvGFMwaOiGVNCp""",
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
        example="""1993-09-23 16:15:55""",
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
        example="""2021-08-13 01:38:23""",
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

    CURR_EXPRNC_BAND_STS_ID: int = Field(
        ...,
        alias="CURR_EXPRNC_BAND_STS_ID",
        name="",
        description="",
        example=10031,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURR_DSNY_FAC_ID: Optional[int] = Field(
        None,
        alias="CURR_DSNY_FAC_ID",
        name="",
        description="",
        example=503300,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLMT_SHIPMT_CASE_ID: Optional[int] = Field(
        None,
        alias="FFLMT_SHIPMT_CASE_ID",
        name="",
        description="",
        example=506000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RTRN_DSNY_FAC_ID: Optional[int] = Field(
        None,
        alias="RTRN_DSNY_FAC_ID",
        name="",
        description="",
        example=5631,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RTRN_DT: Optional[datetime] = Field(
        None,
        alias="EXPRNC_BAND_RTRN_DT",
        name="",
        description="",
        example="""2016-12-06 21:46:18""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_CTR_ID: Optional[int] = Field(
        None,
        alias="COST_CTR_ID",
        name="",
        description="",
        example=9249,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WBS_ELMNT_ID: Optional[int] = Field(
        None,
        alias="WBS_ELMNT_ID",
        name="",
        description="",
        example=5822,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GNRL_LDGR_ID: Optional[int] = Field(
        None,
        alias="GNRL_LDGR_ID",
        name="",
        description="",
        example=3825,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLMT_PROCURMT_RSN_ID: Optional[int] = Field(
        None,
        alias="FFLMT_PROCURMT_RSN_ID",
        name="",
        description="",
        example=7998,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_DSNY_PROD_SFX_ID: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_DSNY_PROD_SFX_ID",
        name="",
        description="",
        example=8755,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURR_EXPRNC_BAND_SUB_STS_ID: Optional[int] = Field(
        None,
        alias="CURR_EXPRNC_BAND_SUB_STS_ID",
        name="",
        description="",
        example=56,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLMT_SHIPMT_ID: Optional[int] = Field(
        None,
        alias="FFLMT_SHIPMT_ID",
        name="",
        description="",
        example=7929,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BUILD_BAND_IN: str = Field(
        ...,
        alias="BUILD_BAND_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PUBLIC_KEY: Optional[str] = Field(
        None,
        alias="PUBLIC_KEY",
        name="",
        description="",
        example="""BTGEYwHLKszOlnKKCill""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for XBMS FFLD_EXPRNC_BAND Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:47:03.328790""",
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
        example="""FFLD_EXPRNC_BAND""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=50884567603806,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWFfldExprncBandModel(BaseModel):
    """
    Payload class for XBMS FFLD_EXPRNC_BAND
    """

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""  # optional
        unique_identifier = ["data.FFLD_EXPRNC_BAND_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "FFLD_EXPRNC_BAND"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
