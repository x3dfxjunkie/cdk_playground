"""Source Data Contract Template for CHRG_ALLOC.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for CHRG_ALLOC"""

    chrg_alloc_id: int = Field(
        ...,
        alias="CHRG_ALLOC_ID",
        name="",
        description="",
        example=46490419,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    own_chrg_grp_id: int = Field(
        ...,
        alias="OWN_CHRG_GRP_ID",
        name="",
        description="",
        example=983314188,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_alloc_typ_nm: str = Field(
        ...,
        alias="CHRG_ALLOC_TYP_NM",
        name="",
        description="",
        example="Default",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pick_chrg_grp_id: Optional[int] = Field(
        None,
        alias="PICK_CHRG_GRP_ID",
        name="",
        description="",
        example=983314189,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_chrg_alloc_in: str = Field(
        ...,
        alias="BILL_CHRG_ALLOC_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    splt_typ_nm: str = Field(
        ...,
        alias="SPLT_TYP_NM",
        name="",
        description="",
        example="Percentage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    splt_vl: float = Field(
        ...,
        alias="SPLT_VL",
        name="",
        description="",
        example=354.38,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    asgn_seq_nb: int = Field(
        ...,
        alias="ASGN_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_fac_id: Optional[int] = Field(
        None,
        alias="TXN_FAC_ID",
        name="",
        description="",
        example=343233,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pick_all_in: str = Field(
        ...,
        alias="PICK_ALL_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_folio_id: Optional[int] = Field(
        None,
        alias="CHRG_GRP_FOLIO_ID",
        name="",
        description="",
        example=276584374,
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
        example="2023-06-09T08:59:47Z",
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
        example="2023-06-09T08:59:47Z",
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
    bill_chrg_grp_id: Optional[int] = Field(
        None,
        alias="BILL_CHRG_GRP_ID",
        name="",
        description="",
        example=82031,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_idvl_pty_id: Optional[int] = Field(
        None,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=724747030,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    alloc_strt_dt: Optional[datetime] = Field(
        None,
        alias="ALLOC_STRT_DT",
        name="",
        description="",
        example="2023-06-09T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    alloc_end_dt: Optional[datetime] = Field(
        None,
        alias="ALLOC_END_DT",
        name="",
        description="",
        example="2023-06-12T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: Optional[int] = Field(
        None,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=366850,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_alloc_inactv_dt: Optional[datetime] = Field(
        None,
        alias="CHRG_ALLOC_INACTV_DT",
        name="",
        description="",
        example="2023-06-09T07:40:46Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_id: Optional[int] = Field(
        None,
        alias="BILL_ID",
        name="",
        description="",
        example=19,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    appr_by_nm: Optional[str] = Field(
        None,
        alias="APPR_BY_NM",
        name="",
        description="",
        example="KAYLA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_prfl_id: Optional[int] = Field(
        None,
        alias="FOLIO_PRFL_ID",
        name="",
        description="",
        example=16053113,
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
    flat_am_crncy_cd: Optional[str] = Field(
        None,
        alias="FLAT_AM_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioChrgAllocModel(BaseModel):
    """Payload class for DREAMSFolioChrgAllocModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Allocation"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_ALLOC_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_ALLOC"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
