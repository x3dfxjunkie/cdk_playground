"""Source Data Contract for Dreams Entitlement Coupon Charge"""


from __future__ import annotations
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Coupon Charge Data"""

    aprv_by_nm: Optional[str] = Field(
        None,
        alias="APRV_BY_NM",
        name="",
        description="",
        example="text",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_am: float = Field(
        ...,
        alias="CHRG_AM",
        name="",
        description="",
        example=32.15,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_am_crncy_cd: str = Field(
        ...,
        alias="CHRG_AM_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_by_nm: str = Field(
        ...,
        alias="CHRG_BY_NM",
        name="",
        description="",
        example="Mouse, Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_ds: str = Field(
        ...,
        alias="CHRG_DS",
        name="",
        description="",
        example="Food POS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_ffl_dts: datetime = Field(
        ...,
        alias="CHRG_FFL_DTS",
        name="",
        description="",
        example="2023-08-18T12:15:32Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_pst_dt: datetime = Field(
        ...,
        alias="CHRG_PST_DT",
        name="",
        description="",
        example="2023-08-18T12:15:32Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chrg_rpst_in: str = Field(
        ...,
        alias="CHRG_RPST_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_chrg_id: int = Field(
        ...,
        alias="CPN_CHRG_ID",
        name="",
        description="",
        example=111111123,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cpn_pty_cn: Optional[int] = Field(
        None,
        alias="CPN_PTY_CN",
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
        example="2023-08-18T12:15:32.946000Z",
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

    dup_chrg_in: str = Field(
        ...,
        alias="DUP_CHRG_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    exprnc_card_nb: Optional[str] = Field(
        None,
        alias="EXPRNC_CARD_NB",
        name="",
        description="",
        example="111111111111111603",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    incognito: Optional[str] = Field(
        None,
        alias="INCOGNITO",
        name="",
        description="",
        example="Y",
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

    rev_cls_id: int = Field(
        ...,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=111127,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rev_cls_nm: str = Field(
        ...,
        alias="REV_CLS_NM",
        name="",
        description="",
        example="Food POS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    src_acct_ctr_id: int = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_acct_ctr_id: int = Field(
        ...,
        alias="TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=111500,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_idvl_pty_id: int = Field(
        ...,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=111111196,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-18T12:15:32.946000Z",
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


class DREAMSEntitlementsCpnChrgTModel(BaseModel):
    """Payload class for DREAMSEntitlementsCpnChrgTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Coupon Charge"
        stream_name = ""
        description = """Transactional information regarding a charge that is related to a coupon/entitlement"""
        unique_identifier = ["data.CPN_CHRG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = True
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CPN_CHRG_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
