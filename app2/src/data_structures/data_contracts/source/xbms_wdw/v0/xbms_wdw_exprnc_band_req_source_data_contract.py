"""Source Data Contract for XBMS EXPRNC_BAND_REQ"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):

    """
    Class for XBMS EXPRNC_BAND_REQ Data
    """

    EXPRNC_BAND_REQ_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_ID",
        name="",
        description="",
        example=734422,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_UNIQ_ID: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_UNIQ_ID",
        name="",
        description="",
        example="""0x80C605E012B4441F9901B82F16914425""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHIP_SRVC_ID: Optional[int] = Field(
        None,
        alias="SHIP_SRVC_ID",
        name="",
        description="",
        example=10010,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_TYP_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_TYP_ID",
        name="",
        description="",
        example=10004,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDR_ID: Optional[int] = Field(
        None,
        alias="ADDR_ID",
        name="",
        description="",
        example=747516,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_RSN_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_REQ_RSN_ID",
        name="",
        description="",
        example=10003,
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
        example="""2014-11-05 11:58:27.445000""",
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
        example="""2015-01-06 06:10:09.683000""",
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

    EXPRNC_BAND_ADDR_CONFIRMED_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_ADDR_CONFIRMED_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURR_EXPRNC_BAND_REQ_STS_ID: int = Field(
        ...,
        alias="CURR_EXPRNC_BAND_REQ_STS_ID",
        name="",
        description="",
        example=10024,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REQ_STS_OVRD_IN: str = Field(
        ...,
        alias="EXPRNC_BAND_REQ_STS_OVRD_IN",
        name="",
        description="",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandReqModel(BaseModel):

    """
    Payload class for XBMS EXPRNC_BAND_REQ
    """

    class Config:
        """Payload Level Metadata"""

        title = "Experience Band Request"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Experience Band Req Details"""  # optional
        unique_identifier = ["data.EXPRNC_BAND_REQ_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_band_req"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
