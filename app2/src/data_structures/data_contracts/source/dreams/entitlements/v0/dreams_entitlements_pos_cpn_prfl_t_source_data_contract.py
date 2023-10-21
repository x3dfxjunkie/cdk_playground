"""Source Data Contract Template Point of Sale Coupon Profile"""


from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Point of Sale Coupon Profile Data"""

    cpn_pos_loc_config_id: int = Field(
        ...,
        alias="CPN_POS_LOC_CONFIG_ID",
        name="",
        description="",
        example=1111111340,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_prfl_id: int = Field(
        ...,
        alias="CPN_PRFL_ID",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_rstrct_cn: Optional[int] = Field(
        None,
        alias="CPN_RSTRCT_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_rstrct_typ_nm: Optional[str] = Field(
        None,
        alias="CPN_RSTRCT_TYP_NM",
        name="",
        description="",
        example="PER_PERSON_PER_TRAVEL_PLAN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2018-02-09T15:01:49.722000Z",
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

    pos_cpn_prfl_id: int = Field(
        ...,
        alias="POS_CPN_PRFL_ID",
        name="",
        description="",
        example=1111119040,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsPosCpnPrflTModel(BaseModel):
    """Payload class for DREAMSEntitlementsPosCpnPrflTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Point of Sale Coupon Profile"
        stream_name = ""
        description = """This table associates the Point of Sale Coupon Profile ID to the Coupon Profile ID to provide the type of restrictions associated to the use of the coupon: CPN_RSTRCT_TYP_NM
        PER_PERSON_PER_NIGHT
        PER_PERSON_PER_TRAVEL_PLAN"""
        unique_identifier = ["data.POS_CPN_PRFL_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "POS_CPN_PRFL_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
