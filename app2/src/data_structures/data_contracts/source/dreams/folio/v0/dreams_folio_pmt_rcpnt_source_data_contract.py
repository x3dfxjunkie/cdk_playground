"""Source Data Contract for Dreams Folio Payment Recipient"""
from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Payment Recipient Data"""

    addr_rfnd_nm_ovrd_in: str = Field(
        ...,
        alias="ADDR_RFND_NM_OVRD_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2020-12-12T03:05:42.137000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ProAppRef",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    memo_nm: Optional[str] = Field(
        None,
        alias="MEMO_NM",
        name="",
        description="",
        example="Mickey Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=255829580,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_addr_ln_1_val: str = Field(
        ...,
        alias="PMT_RCPNT_ADDR_LN_1_VAL",
        name="",
        description="",
        example="108xx Citron Oaks Dr",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_addr_ln_2_val: Optional[str] = Field(
        None,
        alias="PMT_RCPNT_ADDR_LN_2_VAL",
        name="",
        description="",
        example="Apt 102",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_cntry_cd: str = Field(
        ...,
        alias="PMT_RCPNT_CNTRY_CD",
        name="",
        description="",
        example="USA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_cty_nm: str = Field(
        ...,
        alias="PMT_RCPNT_CTY_NM",
        name="",
        description="",
        example="Orlando",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_id: int = Field(
        ...,
        alias="PMT_RCPNT_ID",
        name="",
        description="",
        example=3370900,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_nm: str = Field(
        ...,
        alias="PMT_RCPNT_NM",
        name="",
        description="",
        example="Minnie Mouse",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_pstl_cd: Optional[str] = Field(
        None,
        alias="PMT_RCPNT_PSTL_CD",
        name="",
        description="",
        example="32836-5031",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_rgn_cd: Optional[str] = Field(
        None,
        alias="PMT_RCPNT_RGN_CD",
        name="",
        description="",
        example="FL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_rcpnt_rgn_nm: Optional[str] = Field(
        None,
        alias="PMT_RCPNT_RGN_NM",
        name="",
        description="",
        example="FLORIDA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-01-11T02:18:05.515000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioPmtRcpntModel(BaseModel):
    """Payload class for DREAMSFolioPmtRcpntModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Payment Recipient"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.PMT_RCPNT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PMT_RCPNT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
