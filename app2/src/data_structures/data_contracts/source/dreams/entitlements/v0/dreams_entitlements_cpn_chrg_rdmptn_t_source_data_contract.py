"""Source Data Contract for Dreams Entitlement Coupon Charge Redemption"""


from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Charge Redemption Data"""

    cpn_chrg_id: int = Field(
        ...,
        alias="CPN_CHRG_ID",
        name="",
        description="",
        example=111111307,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_rdmptn_am: int = Field(
        ...,
        alias="CPN_RDMPTN_AM",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_rdmptn_id: int = Field(
        ...,
        alias="CPN_RDMPTN_ID",
        name="",
        description="",
        example=111111407,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-18T11:50:57.954000Z",
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

    enttl_pln_id: int = Field(
        ...,
        alias="ENTTL_PLN_ID",
        name="",
        description="",
        example=11111710,
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-18T11:50:57.954000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="Mobile-Order",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsCpnChrgRdmptnTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnChrgRdmptnTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Charge Redemption"
        stream_name = ""
        description = """This table associates the coupon charge to the Entitlement Plan providing the count of coupons redeemed"""
        unique_identifier = ["data.CPN_RDMPTN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_CHRG_RDMPTN_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
