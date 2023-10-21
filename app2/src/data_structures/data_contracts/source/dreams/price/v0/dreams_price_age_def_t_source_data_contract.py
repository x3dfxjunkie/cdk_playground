"""Source Data Contract Template for AGE_DEF"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - AGE_DEF Data"""

    age_def_id: int = Field(
        ...,
        alias="AGE_DEF_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_typ_nm: str = Field(
        ...,
        alias="AGE_TYP_NM",
        name="",
        description="",
        example="Child",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entrprs_age_typ_id: int = Field(
        ...,
        alias="ENTRPRS_AGE_TYP_ID",
        name="",
        description="",
        example=202326,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_def_min_age_nb: int = Field(
        ...,
        alias="AGE_DEF_MIN_AGE_NB",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    age_def_max_age_nb: int = Field(
        ...,
        alias="AGE_DEF_MAX_AGE_NB",
        name="",
        description="",
        example=12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    entrprs_age_typ_nm: str = Field(
        ...,
        alias="ENTRPRS_AGE_TYP_NM",
        name="",
        description="",
        example="Spa & Health Club Child",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2015-07-22T15:21:34.460199Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2015-07-22T15:21:34.460199Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceAgeDefTModel(BaseModel):
    """Payload class for DREAMSPriceAgeDefTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Age Definition"
        stream_name = ""
        description = "A unique ID identifies age definitions including enterprise age definition that apply to different types of products"  # optional
        unique_identifier = ["data.AGE_DEF_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "AGE_DEF_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
