"""Source Data Contract Template for DREAMS Price - Seasons data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - SEAS_T Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2020-10-07T11:13:38Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrt_tier_grp_nm: str = Field(
        ...,
        alias="RSRT_TIER_GRP_NM",
        name="",
        description="",
        example="Deluxe Villas",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seas_cd: str = Field(
        ...,
        alias="SEAS_CD",
        name="",
        description="",
        example="S1019",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seas_id: int = Field(
        ...,
        alias="SEAS_ID",
        name="",
        description="",
        example=234896,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    seas_nm: str = Field(
        ...,
        alias="SEAS_NM",
        name="",
        description="",
        example="Season 4 B",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2020-10-07T11:13:38Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceSeasTModel(BaseModel):
    """Payload class for DREAMSPriceSeasTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """This table is used to store Seasons information."""
        unique_identifier = ["data.SEAS_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SEAS_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
