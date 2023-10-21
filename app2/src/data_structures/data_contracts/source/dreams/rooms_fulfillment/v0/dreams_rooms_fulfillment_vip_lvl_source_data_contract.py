"""Source Data Contract Template for Dreams - Room Fulfillment Very Important Person Level"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for Dreams - Room Fulfillment Very Important Person Level Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-06T10:36:34Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    vip_lvl_nm: str = Field(
        ...,
        alias="VIP_LVL_NM",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentVipLvlModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Very Important Person Level Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Very Important Person Level"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.VIP_LVL_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "vip_lvl"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
