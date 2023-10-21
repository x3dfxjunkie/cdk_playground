"""Source Data Contract Template for Dreams - Dining Allergy"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Dining Allergy Data"""

    alrgy_ds: str = Field(
        ...,
        alias="ALRGY_DS",
        name="",
        description="",
        example="Other",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    alrgy_id: int = Field(
        ...,
        alias="ALRGY_ID",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    alrgy_typ_nm: str = Field(
        ...,
        alias="ALRGY_TYP_NM",
        name="",
        description="",
        example="Food Allergy",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-01-30T23:43:08Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningAlrgyModel(BaseModel):
    """Payload class for Dreams - Dining Allergy Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Allergy"
        stream_name = ""
        description = """This is table contains Food Allergies and descriptions"""
        unique_identifier = ["data.ALRGY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "alrgy"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
