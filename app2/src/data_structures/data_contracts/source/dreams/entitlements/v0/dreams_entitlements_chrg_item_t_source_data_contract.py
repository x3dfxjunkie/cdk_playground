"""Source Data Contract for Dreams Entitlement Charge Item"""


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Charge Item Data"""

    chrg_item_am: float = Field(
        ...,
        alias="CHRG_ITEM_AM",
        name="",
        description="",
        example=49.81,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_item_id: int = Field(
        ...,
        alias="CHRG_ITEM_ID",
        name="",
        description="",
        example=111111554,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_chrg_id: int = Field(
        ...,
        alias="CPN_CHRG_ID",
        name="",
        description="",
        example=111111154,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-20T10:47:55.257000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="unknown",
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

    rev_typ_id: int = Field(
        ...,
        alias="REV_TYP_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rev_typ_nm: str = Field(
        ...,
        alias="REV_TYP_NM",
        name="",
        description="",
        example="Base",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-20T10:47:55.257000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="unknown",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsChrgItemTModel(BaseModel):
    """Payload class for DREAMSEntitlementsChrgItemTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Item"
        stream_name = ""
        description = """Provides information regarding the Coupon Charge, down at the item level"""
        unique_identifier = ["data.CHRG_ITEM_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_ITEM_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
