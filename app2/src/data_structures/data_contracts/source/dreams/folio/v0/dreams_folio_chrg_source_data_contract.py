"""Source Data Contract Template for CHRG.json"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """data for CHRG"""

    chrg_id: int = Field(
        ...,
        alias="CHRG_ID",
        name="",
        description="",
        example=3408477857,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_typ_nm: str = Field(
        ...,
        alias="CHRG_TYP_NM",
        name="",
        description="",
        example="POS Charge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    recog_sts_nm: Optional[str] = Field(
        None,
        alias="RECOG_STS_NM",
        name="",
        description="",
        example="APPROVED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_id: int = Field(
        ...,
        alias="CHRG_GRP_ID",
        name="",
        description="",
        example=936041354,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_by_nm: Optional[str] = Field(
        None,
        alias="CHRG_BY_NM",
        name="",
        description="",
        example="KREIBICH, PAUL",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_acct_ctr_id: int = Field(
        ...,
        alias="TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=151303,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_am: float = Field(
        ...,
        alias="CHRG_AM",
        name="",
        description="",
        example=5.23,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_crncy_cd: str = Field(
        ...,
        alias="CHRG_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_actv_in: str = Field(
        ...,
        alias="CHRG_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_ffl_dts: datetime = Field(
        ...,
        alias="CHRG_FFL_DTS",
        name="",
        description="",
        example="2023-06-09T23:01:56.749000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_ds: Optional[str] = Field(
        None,
        alias="CHRG_DS",
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
        example=7047,
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
    chrg_pst_st_nm: str = Field(
        ...,
        alias="CHRG_PST_ST_NM",
        name="",
        description="",
        example="Earned",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    wrk_loc_id: Optional[int] = Field(
        None,
        alias="WRK_LOC_ID",
        name="",
        description="",
        example=7012,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="2857",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T23:01:56Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="2857",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T23:01:56Z",
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
    chrg_itm_vsbl_in: str = Field(
        ...,
        alias="CHRG_ITM_VSBL_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: Optional[int] = Field(
        None,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=366927,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_nm: Optional[str] = Field(
        None,
        alias="REV_CLS_NM",
        name="",
        description="",
        example="Food POS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exprnc_card_nb: Optional[str] = Field(
        None,
        alias="EXPRNC_CARD_NB",
        name="",
        description="",
        example="994152208015804102",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_txn_typ_cd: Optional[str] = Field(
        None,
        alias="FOLIO_TXN_TYP_CD",
        name="",
        description="",
        example="SALE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_idvl_pty_id: Optional[int] = Field(
        None,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=682058547,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dvc_pts_vl: Optional[str] = Field(
        None,
        alias="DVC_PTS_VL",
        name="",
        description="",
        example="14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acct_dt: Optional[datetime] = Field(
        None,
        alias="ACCT_DT",
        name="",
        description="",
        example="2023-06-09T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_pst_dts: Optional[datetime] = Field(
        None,
        alias="CHRG_PST_DTS",
        name="",
        description="",
        example="2023-06-09T23:02:36Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sprsd_chrg_id: Optional[int] = Field(
        None,
        alias="SPRSD_CHRG_ID",
        name="",
        description="",
        example=3402552882,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    upgrd_chrg_id: Optional[int] = Field(
        None,
        alias="UPGRD_CHRG_ID",
        name="",
        description="",
        example=3408299514,
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
    chrg_pty_cn: Optional[int] = Field(
        None,
        alias="CHRG_PTY_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    aprv_by_nm: Optional[str] = Field(
        None,
        alias="APRV_BY_NM",
        name="",
        description="",
        example="test2100.user",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioChrgModel(BaseModel):
    """Payload class for DREAMSFolioChrgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
