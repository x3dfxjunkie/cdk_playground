"""Source Data Contract Template for DSNY_FAC_BAND_INVTRY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):

    """
    Class for XBMS DSNY_FAC_BAND_INVTRY Data
    """

    DSNY_FAC_BAND_INVTRY_ID: int = Field(
        ...,
        alias="DSNY_FAC_BAND_INVTRY_ID",
        name="",
        description="""""",
        example=16073805,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DSNY_FAC_ID: int = Field(
        ...,
        alias="DSNY_FAC_ID",
        name="",
        description="""""",
        example=503300,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FFLD_EXPRNC_BAND_ID: int = Field(
        ...,
        alias="FFLD_EXPRNC_BAND_ID",
        name="",
        description="""""",
        example=30480995,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_TXN_ID: str = Field(
        ...,
        alias="EXPRNC_BAND_TXN_ID",
        name="",
        description="""""",
        example="""0x11EDBF4E5DFD5847AEFF040300000000""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_FRST_REC_FAC_DTS: datetime = Field(
        ...,
        alias="EXPRNC_BAND_FRST_REC_FAC_DTS",
        name="",
        description="""""",
        example="""2023-03-10 14:18:02""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_REC_LVG_FAC_DTS: Optional[datetime] = Field(
        None,
        alias="EXPRNC_BAND_REC_LVG_FAC_DTS",
        name="",
        description="""""",
        example="""2023-08-24 01:24:17.981000""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""f-xbandapp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""2023-03-10 14:18:02""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""f-xbandapp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2023-08-24 01:24:17.988000""",
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

    FAC_SHIPMT_CASE_NB: str = Field(
        ...,
        alias="FAC_SHIPMT_CASE_NB",
        name="",
        description="""""",
        example="""CD52464400""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWDsnyFacBandInvtryModel(BaseModel):
    """Payload class for DSNY_FAC_BAND_INVTRY"""

    class Config:
        """Payload Level Metadata"""

        title = "Disney Facility Band Inventory"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Table for the facility band inventory and the mapping disney facility ID and experience band transaction ID."""
        unique_identifier = ["data.DSNY_FAC_BAND_INVTRY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "dsny_fac_band_invtry"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
