"""Source Data Contract for Dreams Point of Sale Coupon Charge"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Point of Sale Coupon Charge Data"""

    cpn_cd: str = Field(
        ...,
        alias="CPN_CD",
        name="",
        description="",
        example="QA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_chrg_id: int = Field(
        ...,
        alias="CPN_CHRG_ID",
        name="",
        description="",
        example=111111106,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_tndr_cd: str = Field(
        ...,
        alias="CPN_TNDR_CD",
        name="",
        description="",
        example="35",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-18T11:12:48.320000Z",
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

    dsny_id_cd: str = Field(
        ...,
        alias="DSNY_ID_CD",
        name="",
        description="",
        example="N",
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

    meal_prd_nm: str = Field(
        ...,
        alias="MEAL_PRD_NM",
        name="",
        description="",
        example="02",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mrcht_nm: Optional[str] = Field(
        None,
        alias="MRCHT_NM",
        name="",
        description="",
        example="WDW F&B SALES",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    msg_nb: Optional[str] = Field(
        None,
        alias="MSG_NB",
        name="",
        description="",
        example="0001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pos_cpn_chrg_id: int = Field(
        ...,
        alias="POS_CPN_CHRG_ID",
        name="",
        description="",
        example=111111506,
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

    rtrv_ref_nb: Optional[str] = Field(
        None,
        alias="RTRV_REF_NB",
        name="",
        description="",
        example="111111111422",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sld_id_vl: str = Field(
        ...,
        alias="SLD_ID_VL",
        name="",
        description="",
        example="7034",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trmnl_ref_tx: Optional[str] = Field(
        None,
        alias="TRMNL_REF_TX",
        name="",
        description="",
        example="aaaaaaaa-1111-aaaa-8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trmnl_seq_nb: Optional[str] = Field(
        None,
        alias="TRMNL_SEQ_NB",
        name="",
        description="",
        example="00001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-18T11:12:48.320000Z",
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


class DREAMSEntitlementsPosCpnChrgTModel(BaseModel):
    """Payload class for DREAMSEntitlementsPosCpnChrgTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Point of Sale Coupon Charge"
        stream_name = ""
        description = """This table ties the source POS charge ID to the Coupon charge ID to provide additional information about the source transaction."""
        unique_identifier = ["data.POS_CPN_CHRG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "POS_CPN_CHRG_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
