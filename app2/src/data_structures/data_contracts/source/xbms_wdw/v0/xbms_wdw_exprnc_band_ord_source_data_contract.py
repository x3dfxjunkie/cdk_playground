"""Source Data Contract for XBMS EXPRNC_BAND_ORD"""

from __future__ import annotations

from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_ORD Data
    """

    EXPRNC_BAND_ORD_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_ORD_ID",
        name="",
        description="""""",
        example=577501,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_ID",
        name="",
        description="""""",
        example=857056,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_FFLMT_ORD_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_FFLMT_ORD_ID",
        name="",
        description="""""",
        example=567900,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ORD_UNIQ_ID: str = Field(
        ...,
        alias="EXPRNC_BAND_ORD_UNIQ_ID",
        name="",
        description="""""",
        example="""0x6B22C145F7DE43C2892011D5C43403E1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_ID: Optional[int] = Field(
        None,
        alias="ADDR_ID",
        name="",
        description="""""",
        example=811315,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ORD_EXPECT_SHIP_DT: Optional[date] = Field(
        None,
        alias="EXPRNC_BAND_ORD_EXPECT_SHIP_DT",
        name="",
        description="""""",
        example="""2015-08-16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ORD_ACTL_DLVR_DT: Optional[date] = Field(
        None,
        alias="EXPRNC_BAND_ORD_ACTL_DLVR_DT",
        name="",
        description="""""",
        example="""1977-06-06""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""XBANDAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""2015-08-14 02:07:15.860000""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""XBANDAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2015-08-14 02:07:15.860000""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOGICAL_DEL_IN: str = Field(
        ...,
        alias="LOGICAL_DEL_IN",
        name="",
        description="""""",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIP_SRVC_ID: int = Field(
        ...,
        alias="SHIP_SRVC_ID",
        name="",
        description="""""",
        example=10010,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ORD_EXPECT_DLVR_DT: Optional[date] = Field(
        None,
        alias="EXPRNC_BAND_ORD_EXPECT_DLVR_DT",
        name="",
        description="""""",
        example="""2015-08-21""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RSRT_SHIPMT_DSNY_FAC_ID: Optional[int] = Field(
        None,
        alias="RSRT_SHIPMT_DSNY_FAC_ID",
        name="",
        description="""""",
        example=504106,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURR_EXPRNC_BAND_ORD_STS_ID: int = Field(
        ...,
        alias="CURR_EXPRNC_BAND_ORD_STS_ID",
        name="",
        description="""""",
        example=10012,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REDIR_SHIPMT_TO_RSRT: str = Field(
        ...,
        alias="REDIR_SHIPMT_TO_RSRT",
        name="",
        description="""""",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLMT_LOC_ID: Optional[int] = Field(
        None,
        alias="FFLMT_LOC_ID",
        name="",
        description="""""",
        example=12345,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GRP_MSTR_REC_SORT_TYP_ID: Optional[int] = Field(
        None,
        alias="GRP_MSTR_REC_SORT_TYP_ID",
        name="",
        description="""""",
        example=12345,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandOrdModel(BaseModel):
    """Payload class for EXPRNC_BAND_ORD"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Band Order"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """"""
        unique_identifier = ["data.EXPRNC_BAND_ORD_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_band_ord"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
