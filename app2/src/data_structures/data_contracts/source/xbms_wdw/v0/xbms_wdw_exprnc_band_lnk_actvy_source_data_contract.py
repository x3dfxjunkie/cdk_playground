"""Source Data Contract Template for EXPRNC_BAND_LNK_ACTVY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):

    """
    Class for XBMS EXPRNC_BAND_LNK_ACTVY Data
    """

    EXPRNC_BAND_LNK_ACTVY_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_LNK_ACTVY_ID",
        name="",
        description="""""",
        example=1321461,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_LNK_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_LNK_ID",
        name="",
        description="""""",
        example=1328075,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_ID",
        name="",
        description="""""",
        example=2412434,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_TXN_ID: str = Field(
        ...,
        alias="EXPRNC_BAND_TXN_ID",
        name="",
        description="""""",
        example="""0x45B0BAA0751949F2B46D0D81DEF164FB""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_ASGN_DTS: datetime = Field(
        ...,
        alias="EXPRNC_BAND_ASGN_DTS",
        name="",
        description="""""",
        example="""2015-10-26 08:15:34.685000""",
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
        example="""2015-10-26 08:15:34.753000""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        name="",
        description="""""",
        alias="UPDT_USR_ID",
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
        example="""2015-10-26 08:15:34.753000""",
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

    EXPRNC_BAND_SRC_SYS_NATIVE_ID: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_SRC_SYS_NATIVE_ID",
        name="",
        description="""""",
        example="""452993446222""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_TXN_SRC_SYS_TX: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_TXN_SRC_SYS_TX",
        example="""travel-plan-id""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandLnkActvyModel(BaseModel):
    """Payload class for EXPRNC_BAND_LNK_ACTVY"""

    class Config:
        """Payload Level Metadata"""

        title = "ExprncBandLnkActvy"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Contains ExperienceBandLinkActivity for xband recipients"""
        unique_identifier = ["data.EXPRNC_BAND_LNK_ACTVY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_band_lnk_actvy"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
