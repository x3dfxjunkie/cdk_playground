"""Source Data Contract Template Point of Sale Coupon Meal Period"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Point of Sale Coupon Meal Period Data"""

    cpn_meal_prd_nm: str = Field(
        ...,
        alias="CPN_MEAL_PRD_NM",
        name="",
        description="",
        example="00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2017-12-08T11:27:40.453000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="SMALS022",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pos_cpn_meal_prd_end_dts: datetime = Field(
        ...,
        alias="POS_CPN_MEAL_PRD_END_DTS",
        name="",
        description="",
        example="2099-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pos_cpn_meal_prd_id: int = Field(
        ...,
        alias="POS_CPN_MEAL_PRD_ID",
        name="",
        description="",
        example=1111119550,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pos_cpn_meal_prd_strt_dts: datetime = Field(
        ...,
        alias="POS_CPN_MEAL_PRD_STRT_DTS",
        name="",
        description="",
        example="1999-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pos_cpn_prfl_id: int = Field(
        ...,
        alias="POS_CPN_PRFL_ID",
        name="",
        description="",
        example=1111119490,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pos_meal_prd_cpn_cn: int = Field(
        ...,
        alias="POS_MEAL_PRD_CPN_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsPosCpnMealPrdTModel(BaseModel):
    """Payload class for DREAMSEntitlementsPosCpnMealPrdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Point of Sale Coupon Meal Period"
        stream_name = ""
        description = """This table associates the Point of Sale Profile ID to the Point of Sale Meal Period codes: CPN_MEAL_PRD_NM
        0
        00
        01
        04
        05"""
        unique_identifier = ["data.POS_CPN_MEAL_PRD_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "POS_CPN_MEAL_PRD_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
