"""Source Data Contract Template for CHRG_GRP_FOLIO.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for CHRG_GRP_FOLIO"""

    folio_acct_typ_nm: str = Field(
        ...,
        alias="FOLIO_ACCT_TYP_NM",
        name="",
        description="",
        example="MAIN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_sts_nm: str = Field(
        ...,
        alias="FOLIO_STS_NM",
        name="",
        description="",
        example="UnEarned",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    respb_pty_id: Optional[int] = Field(
        None,
        alias="RESPB_PTY_ID",
        name="",
        description="",
        example=760778912,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prmy_pty_gst_nm: str = Field(
        ...,
        alias="PRMY_PTY_GST_NM",
        name="",
        description="",
        example="Hay, Caroline",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sml_bal_wrtoff_in: str = Field(
        ...,
        alias="SML_BAL_WRTOFF_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    zero_bal_verif_in: str = Field(
        ...,
        alias="ZERO_BAL_VERIF_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_frq_typ_nm: str = Field(
        ...,
        alias="SETTL_FRQ_TYP_NM",
        name="",
        description="",
        example="Past Visit",
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
        example="2023-06-10T06:08:48Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    incognito: Optional[str] = Field(
        None,
        alias="INCOGNITO",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_folio_id: int = Field(
        ...,
        alias="CHRG_GRP_FOLIO_ID",
        name="",
        description="",
        example=276631528,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    root_chrg_grp_id: int = Field(
        ...,
        alias="ROOT_CHRG_GRP_ID",
        name="",
        description="",
        example=983425825,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dflt_chrg_grp_id: Optional[int] = Field(
        None,
        alias="DFLT_CHRG_GRP_ID",
        name="",
        description="",
        example=983425826,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_actv_in: str = Field(
        ...,
        alias="FOLIO_ACTV_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    onsite_in: str = Field(
        ...,
        alias="ONSITE_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prmy_folio_in: str = Field(
        ...,
        alias="PRMY_FOLIO_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_ownr_in: str = Field(
        ...,
        alias="PMT_OWNR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_folio_strt_dt: datetime = Field(
        ...,
        alias="CHRG_GRP_FOLIO_STRT_DT",
        name="",
        description="",
        example="2023-08-09T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_folio_end_dt: Optional[datetime] = Field(
        None,
        alias="CHRG_GRP_FOLIO_END_DT",
        name="",
        description="",
        example="2023-08-11T13:50:00Z",
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
        example="2023-06-10T06:05:40Z",
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
    folio_acct_lim_am: Optional[float] = Field(
        None,
        alias="FOLIO_ACCT_LIM_AM",
        name="",
        description="",
        example=2000.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    folio_acct_lim_crncy_cd: Optional[str] = Field(
        None,
        alias="FOLIO_ACCT_LIM_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dpst_ext_dt: Optional[datetime] = Field(
        None,
        alias="DPST_EXT_DT",
        name="",
        description="",
        example="2023-06-09T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_exmpt_id: Optional[int] = Field(
        None,
        alias="TAX_EXMPT_ID",
        name="",
        description="",
        example=57922303,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bill_pty_id: Optional[int] = Field(
        None,
        alias="BILL_PTY_ID",
        name="",
        description="",
        example=656276880,
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


class DREAMSFolioChrgGrpFolioModel(BaseModel):
    """Payload class for DREAMSFolioChrgGrpFolioModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Group Folio"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_GRP_FOLIO_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_GRP_FOLIO"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
