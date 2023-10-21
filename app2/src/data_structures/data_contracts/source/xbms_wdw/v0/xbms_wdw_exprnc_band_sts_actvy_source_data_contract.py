"""Source Data Contract Template for EXPRNC_BAND_STS_ACTVY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_STS_ACTVY Data
    """

    EXPRNC_BAND_STS_ACTVY_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_STS_ACTVY_ID",
        name="",
        description="""""",
        example=6966856,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_STS_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_STS_ID",
        name="",
        description="""""",
        example=10028,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLD_EXPRNC_BAND_ID: int = Field(
        ...,
        alias="FFLD_EXPRNC_BAND_ID",
        name="",
        description="""""",
        example=4124156,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_TXN_ID: str = Field(
        ...,
        alias="EXPRNC_BAND_TXN_ID",
        name="",
        description="""""",
        example="""0xFABB98B8419749EEA9847782E82CDE4C""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_STS_CHNG_RSN_TX: Optional[str] = Field(
        None,
        alias="EXPRNC_BAND_STS_CHNG_RSN_TX",
        name="",
        description="""""",
        example="""Lost""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_STS_UPDT_DTS: datetime = Field(
        ...,
        alias="EXPRNC_BAND_STS_UPDT_DTS",
        name="",
        description="""""",
        example="""2015-10-26 15:07:12.221000""",
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
        example="""2015-10-26 15:07:12.221000""",
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
        example="""2015-10-26 15:07:12.221000""",
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

    EXPRNC_BAND_SUB_STS_ID: Optional[int] = Field(
        None,
        alias="EXPRNC_BAND_SUB_STS_ID",
        name="",
        description="""""",
        example=12000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandStsActvyModel(BaseModel):
    """Payload class for XBMSWDWExprncBandStsActvyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Experience Band Status Activity"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Contains the Users Experience Band Status Activity Details"""
        unique_identifier = ["data.EXPRNC_BAND_STS_ACTVY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "exprnc_band_sts_actvy"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
