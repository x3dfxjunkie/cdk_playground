"""Source Data Contract for Dreams Entitlement Coupon Charge External Reference"""


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Charge External Reference Data"""

    chrg_extnl_ref_id: int = Field(
        ...,
        alias="CHRG_EXTNL_REF_ID",
        name="",
        description="",
        example=111111618,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_extnl_ref_val: str = Field(
        ...,
        alias="CHRG_EXTNL_REF_VAL",
        name="",
        description="",
        example="11111111-aaaa-1111-aaaa-111111553cbf",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_chrg_id: int = Field(
        ...,
        alias="CPN_CHRG_ID",
        name="",
        description="",
        example=111111118,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-18T12:08:33.510000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Mobile-Order",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    extnl_src_nm: str = Field(
        ...,
        alias="EXTNL_SRC_NM",
        name="",
        description="",
        example="MOBILE_TXN_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsCpnChrgExtnlRefTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnChrgExtnlRefTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Charge External Reference"
        stream_name = ""
        description = """This table associates the coupon charge to various external source types: EXTNL_SRC_NM
        APP
        DPMSGroupProfile
        HOTEL_EXPERIENCE
        KTTW
        LILO_UI
        MOBILE_TXN_ID
        ROOM
        RTP
        SECURE_ID
        VISUAL_ID
        providing the external reference value"""
        unique_identifier = ["data.CHRG_EXTNL_REF_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_CHRG_EXTNL_REF_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
