"""Source Data Contract for XBMS EXPRNC_BAND"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):

    """
    Class for XBMS EXPRNC_BAND Data
    """

    EXPRNC_BAND_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_ID",
        name="",
        description="",
        example=1928813,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_DSNY_PROD_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_DSNY_PROD_ID",
        name="",
        description="",
        example=505302,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_UNIQ_ID: str = Field(
        ...,
        alias="EXPRNC_BAND_UNIQ_ID",
        name="",
        description="",
        example="""0xF7309EC4C7114A7AADCF1F1004CD71DD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_ID",
        name="",
        description="",
        example=714002,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ORD_ID: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_ORD_ID",
        name="",
        description="",
        example=549750,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLMT_SHIPMT_ID: Optional[int] = Field(
        None,
        alias="FFLMT_SHIPMT_ID",
        name="",
        description="",
        example=524650,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_PKG_ID: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_PKG_ID",
        name="",
        description="",
        example=12345,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_PRT_NM: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_PRT_NM",
        name="",
        description="",
        example="""Mickey""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_GST_CNFIRM_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_GST_CNFIRM_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_SEQ_NB: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_SEQ_NB",
        name="",
        description="",
        example=12345,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_CSTM_PRT_NM_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_CSTM_PRT_NM_IN",
        name="",
        description="",
        example="""N""",
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
        example="""2014-09-08 23:27:25.484000""",
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
        example="""2014-09-08 23:27:25.484000""",
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

    CURR_EXPRNC_BAND_LNK_ID: Optional[int] = Field(
        None,
        alias="CURR_EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=12345,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RTL_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_RTL_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_OVRD_PRT_NM: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_OVRD_PRT_NM",
        name="",
        description="",
        example="""Mouse""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ORIG_EXPRNC_BAND_LNK_ID: Optional[int] = Field(
        None,
        alias="ORIG_EXPRNC_BAND_LNK_ID",
        name="",
        description="",
        example=123456,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPT_OUT_IN: str = Field(
        ...,
        alias="OPT_OUT_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_OPT_OUT_RSN_ID: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_OPT_OUT_RSN_ID",
        name="",
        description="",
        example=12345,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_GST_SKU_OVRD_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_GST_SKU_OVRD_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCOG_REQ_ID: Optional[int] = Field(
        None,
        alias="INCOG_REQ_ID",
        name="",
        description="",
        example=123,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandModel(BaseModel):
    """Payload class for XBMSWDWExprncBandModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Band"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = "Contains Experience Band Details"  # optional
        unique_identifier = ["data.EXPRNC_BAND_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_band"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
