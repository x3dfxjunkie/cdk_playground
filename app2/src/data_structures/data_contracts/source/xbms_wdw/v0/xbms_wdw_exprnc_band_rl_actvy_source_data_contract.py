"""Source Data Contract for XBMS EXPRNC_BAND_RL_ACTVY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_RL_ACTVY Data
    """

    EXPRNC_BAND_RL_ACTVY_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_RL_ACTVY_ID",
        name="",
        description="",
        example=502450,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RL_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_RL_ID",
        name="",
        description="",
        example=500650,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLD_EXPRNC_BAND_ID: int = Field(
        ...,
        alias="FFLD_EXPRNC_BAND_ID",
        name="",
        description="",
        example=4107310,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_TXN_ID: str = Field(
        ...,
        alias="EXPRNC_BAND_TXN_ID",
        name="",
        description="",
        example="""0xC188B252F27542A88A5327CC4262D247""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_RL_UPDT_DTS: datetime = Field(
        ...,
        alias="EXPRNC_BAND_RL_UPDT_DTS",
        name="",
        description="",
        example="""2015-07-31 17:14:26.018000""",
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
        example="""2015-07-31 17:14:26.018000""",
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
        example="""2015-07-31 17:14:26.018000""",
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


class XBMSWDWExprncBandRlActvyModel(BaseModel):
    """Payload class for EXPRNC_BAND_RL_ACTVY"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Band RL Activity "
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Contains Experience Band RL Activity Details"""
        unique_identifier = ["data.EXPRNC_BAND_RL_ACTVY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_band_rl_actvy"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
