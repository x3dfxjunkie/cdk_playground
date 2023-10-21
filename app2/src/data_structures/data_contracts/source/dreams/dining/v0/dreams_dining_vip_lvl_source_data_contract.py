"""Source Data Contract Template for Dreams Dining - VIP Level Data"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Dining - VIP Level Data"""

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

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-06 10:36:34.000000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningVipLvlModel(BaseModel):
    """Payload class for DREAMSDiningVipLvlModel"""

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
