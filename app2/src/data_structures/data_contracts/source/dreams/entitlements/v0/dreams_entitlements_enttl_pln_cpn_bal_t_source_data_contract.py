"""Source Data Contract for Dreams Entitlement Plan Coupon Balance"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Entitlement Plan Coupon Balance Data"""

    cpn_bal_am: int = Field(
        ...,
        alias="CPN_BAL_AM",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-17T11:58:10.042000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ENTITLTLEMEN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    enttl_pln_id: int = Field(
        ...,
        alias="ENTTL_PLN_ID",
        name="",
        description="",
        example=111111512,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=0,
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
        example="2023-08-17T11:58:10.042000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="ENTITLTLEMEN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsEnttlPlnCpnBalTModel(BaseModel):
    """Payload class for DREAMSEntitlementsEnttlPlnCpnBalTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Entitlement Plan Coupon Balance"
        stream_name = ""
        description = """This table tracks the number of Coupons as they are posted against the Entitlement Plan"""
        unique_identifier = ["data.ENTTL_PLN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ENTTL_PLN_CPN_BAL_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
