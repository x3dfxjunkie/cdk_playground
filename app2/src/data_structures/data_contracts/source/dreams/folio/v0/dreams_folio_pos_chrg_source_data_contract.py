"""Source Data Contract for Dreams Folio Point of Sale Charge"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Point of Sale Charge Data"""

    cpn_cd: Optional[str] = Field(
        None,
        alias="CPN_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_tndr_cd: Optional[str] = Field(
        None,
        alias="CPN_TNDR_CD",
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
        example="2023-08-22T14:18:03Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="9608",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dsny_id_cd: Optional[str] = Field(
        None,
        alias="DSNY_ID_CD",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    meal_prd_nm: str = Field(
        ...,
        alias="MEAL_PRD_NM",
        name="",
        description="",
        example="03",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    mrcht_nm: Optional[str] = Field(
        None,
        alias="MRCHT_NM",
        name="",
        description="",
        example="WDW F&B SALE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    msg_nb: Optional[str] = Field(
        None,
        alias="MSG_NB",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    pos_chrg_id: int = Field(
        ...,
        alias="POS_CHRG_ID",
        name="",
        description="",
        example=3425403527,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2011-01-26T01:41:32.803Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rtrv_ref_nb: Optional[str] = Field(
        None,
        alias="RTRV_REF_NB",
        name="",
        description="",
        example="242488441390",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sld_id_vl: Optional[str] = Field(
        None,
        alias="SLD_ID_VL",
        name="",
        description="",
        example="9608",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trmnl_ref_tx: Optional[str] = Field(
        None,
        alias="TRMNL_REF_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trmnl_seq_nb: Optional[str] = Field(
        None,
        alias="TRMNL_SEQ_NB",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioPosChrgModel(BaseModel):
    """Payload class for DREAMSFolioPosChrgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Point of Sale Charge"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.POS_CHRG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "POS_CHRG"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
