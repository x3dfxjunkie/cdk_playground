"""Source Data Contract for DREAMS Payment Method"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Payment Method Data"""

    pmt_meth_id: int = Field(
        ...,
        alias="PMT_METH_ID",
        name="",
        description="",
        example=10001,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_typ_nm: str = Field(
        ...,
        alias="PMT_METH_TYP_NM",
        name="",
        description="",
        example="Voucher",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_cd: str = Field(
        ...,
        alias="PMT_METH_CD",
        name="",
        description="",
        example="10 GIFT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rfnd_ovrd_pmt_meth_in: str = Field(
        ...,
        alias="RFND_OVRD_PMT_METH_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    max_allw_am: Optional[int] = Field(
        None,
        alias="MAX_ALLW_AM",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    max_allw_crncy_cd: str = Field(
        ...,
        alias="MAX_ALLW_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    strts_pmt_auth_cd: Optional[str] = Field(
        None,
        alias="STRTS_PMT_AUTH_CD",
        name="",
        description="",
        example="NONE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    strts_card_cls_cd: Optional[str] = Field(
        None,
        alias="STRTS_CARD_CLS_CD",
        name="",
        description="",
        example="NONE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    non_csh_cd: Optional[str] = Field(
        None,
        alias="NON_CSH_CD",
        name="",
        description="",
        example="8230",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cpn_tndr_cd: Optional[str] = Field(
        None,
        alias="CPN_TNDR_CD",
        name="",
        description="",
        example="26",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_in: str = Field(
        ...,
        alias="SETTL_METH_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mod_10_in: str = Field(
        ...,
        alias="MOD_10_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILOCONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-01-20T05:57:55.535Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="SC5a_S1_BHM",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-05-04T18:29:39.893Z",
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
    tap_to_pay_in: str = Field(
        ...,
        alias="TAP_TO_PAY_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingPmtMethModel(BaseModel):
    """Payload class for DREAMSAccountingPmtMethModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Payment Method"
        stream_name = ""
        description = """Information associated to a Payment Method type: Bill to A/R, CreditCard, Hotel Charges, Entitlements, DisneyRewardCard, PaidOut, Voucher, Check, Cash, Redeem, Settle to Folio, System, PaymentSystem, Direct Bill, PrePaidCard, RSR, Non-Folio Refunds"""
        unique_identifier = ["data.PMT_METH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PMT_METH"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
