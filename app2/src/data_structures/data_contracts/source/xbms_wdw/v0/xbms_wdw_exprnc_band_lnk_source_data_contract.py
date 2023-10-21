"""Source Data Contract Template for EXPRNC_BAND_LNK"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for XBMS EXPRNC_BAND_LNK Data
    """

    EXPRNC_BAND_LNK_ID: int = Field(
        ...,
        alias="EXPRNC_BAND_LNK_ID",
        name="",
        description="""""",
        example=965042,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPRNC_BAND_LNK_UNIQ_ID: str = Field(
        ...,
        alias="EXPRNC_BAND_LNK_UNIQ_ID",
        name="",
        description="""""",
        example="""0x664FC454BE7642DF9096C43BC909542A""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_SRC_SYS_NATIVE_ID: Optional[str] = Field(
        None,
        alias="GST_SRC_SYS_NATIVE_ID",
        name="",
        description="""""",
        example="""177209519""",
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
        example="""2014-09-08 21:27:22.759000""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="f-xbandapp",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2019-02-12 23:47:25""",
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

    SRC_SYS_TX: Optional[str] = Field(
        None,
        alias="SRC_SYS_TX",
        name="",
        description="""""",
        example="""transactional-guest-id""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_PRFL_FRST_NM: Optional[str] = Field(
        None,
        alias="GST_PRFL_FRST_NM",
        name="",
        description="""""",
        example="""Mickey""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GST_PRFL_LST_NM: Optional[str] = Field(
        None,
        alias="GST_PRFL_LST_NM",
        name="",
        description="""""",
        example="""Mouse""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCOG_REQ_ID: Optional[int] = Field(
        None,
        alias="INCOG_REQ_ID",
        name="",
        description="""""",
        example=1234,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class XBMSWDWExprncBandLnkModel(BaseModel):
    """Payload class for EXPRNC_BAND_LNK"""

    class Config:
        """Payload Level Metadata"""

        title = "ExperienceBandLink"
        stream_name = "prd-use1-guest360-xbms-wdw-stream"
        description = """Contains ExperienceBandLink for xband recipients."""
        unique_identifier = ["data.EXPRNC_BAND_LNK_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "exprnc_band_lnk"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
