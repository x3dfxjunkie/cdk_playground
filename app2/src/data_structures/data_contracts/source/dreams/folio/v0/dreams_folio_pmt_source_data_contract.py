"""Source Data Contract for Dreams Folio Payment"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """data for PMT"""

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281114071,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_item_id: int = Field(
        ...,
        alias="FOLIO_ITEM_ID",
        name="",
        description="",
        example=18202917947,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    recog_sts_nm: str = Field(
        ...,
        alias="RECOG_STS_NM",
        name="",
        description="",
        example="APPROVED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tndr_am: Optional[float] = Field(
        None,
        alias="TNDR_AM",
        name="",
        description="",
        example=-307.66,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tndr_crncy_cd: Optional[str] = Field(
        None,
        alias="TNDR_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_ds: Optional[str] = Field(
        None,
        alias="PMT_DS",
        name="",
        description="",
        example="American Express ***********2006",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_dt: Optional[datetime] = Field(
        None,
        alias="ACCT_DT",
        name="",
        description="",
        example="2023-06-10T06:41:07Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_dts: datetime = Field(
        ...,
        alias="PMT_DTS",
        name="",
        description="",
        example="2023-06-10T06:41:07.464000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_exchg_rt: float = Field(
        ...,
        alias="PMT_EXCHG_RT",
        name="",
        description="",
        example=0.951,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_nm: str = Field(
        ...,
        alias="PMT_METH_NM",
        name="",
        description="",
        example="American Express",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_meth_typ_nm: str = Field(
        ...,
        alias="PMT_METH_TYP_NM",
        name="",
        description="",
        example="CreditCard",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_typ_cd: str = Field(
        ...,
        alias="FOLIO_TXN_TYP_CD",
        name="",
        description="",
        example="REC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ovrd_rfnd_pmt_meth_in: str = Field(
        ...,
        alias="OVRD_RFND_PMT_METH_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_pst_st_nm: str = Field(
        ...,
        alias="PMT_PST_ST_NM",
        name="",
        description="",
        example="UnEarned",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wrk_loc_id: int = Field(
        ...,
        alias="WRK_LOC_ID",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_acct_ctr_id: int = Field(
        ...,
        alias="BANK_ACCT_CTR_ID",
        name="",
        description="",
        example=174,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_ref_vl: str = Field(
        ...,
        alias="PMT_REF_VL",
        name="",
        description="",
        example="353161349747",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-24T09:18:43Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-05-24T09:18:43Z",
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
    jdo_cls_nm: str = Field(
        ...,
        alias="JDO_CLS_NM",
        name="",
        description="",
        example="CreditCard",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_in_id: Optional[int] = Field(
        None,
        alias="BANK_IN_ID",
        name="",
        description="",
        example=27349719,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    appl_by_nm: Optional[str] = Field(
        None,
        alias="APPL_BY_NM",
        name="",
        description="",
        example="Mullenix, Nicole",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_cd: Optional[str] = Field(
        None,
        alias="GRP_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sprs_pmt_id: Optional[int] = Field(
        None,
        alias="SPRS_PMT_ID",
        name="",
        description="",
        example=1563912555,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_pst_dts: Optional[datetime] = Field(
        None,
        alias="PMT_PST_DTS",
        name="",
        description="",
        example="2023-06-10T06:46:06Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cap_intf_in: Optional[str] = Field(
        None,
        alias="CAP_INTF_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioPmtModel(BaseModel):
    """Payload class for DREAMSFolioPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Payment"
        stream_name = ""
        description = "This table holds the payment information such as payment method type name, payment method name, account date, payment datetime"
        unique_identifier = ["data.PMT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
