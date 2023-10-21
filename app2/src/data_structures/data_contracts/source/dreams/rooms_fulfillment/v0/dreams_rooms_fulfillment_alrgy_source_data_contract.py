"""Source Data Contract for Dreams - Room Fulfillment Allergy Status"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Fulfillment Allergy Status data"""

    alrgy_ds: str = Field(
        ...,
        alias="ALRGY_DS",
        name="",
        description="",
        example="No Egg",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    alrgy_id: int = Field(
        ...,
        alias="ALRGY_ID",
        name="",
        description="",
        example=1,
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
        example="DINECOR-656",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentAlrgyModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Allergy Status Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Allergy"
        stream_name = ""
        description = "This is table contains Food Allergies and descriptions"
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
