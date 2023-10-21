"""Source Data Contract for  Dreams Group Management Group"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Management Group Data"""

    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="TW16153710",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    hm_fac_id: int = Field(
        ...,
        alias="HM_FAC_ID",
        name="",
        description="",
        example=11,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_dlgt_bkng_meth_nm: Optional[str] = Field(
        None,
        alias="GRP_DLGT_BKNG_METH_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gro_nm: Optional[str] = Field(
        None,
        alias="GRO_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_bus_src_nm: Optional[str] = Field(
        None,
        alias="GRP_BUS_SRC_NM",
        name="",
        description="",
        example="TW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_free_tm_lvl_nm: Optional[str] = Field(
        None,
        alias="GRP_FREE_TM_LVL_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dlvr_meth_nm: Optional[str] = Field(
        None,
        alias="DLVR_METH_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    opty_typ_nm: str = Field(
        ...,
        alias="OPTY_TYP_NM",
        name="",
        description="",
        example="NONE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_acct_typ_nm: Optional[str] = Field(
        None,
        alias="GRP_ACCT_TYP_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_stg_nm: str = Field(
        ...,
        alias="GRP_STG_NM",
        name="",
        description="",
        example="Definite",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_bk_hm_fac_frst_in: str = Field(
        ...,
        alias="GRP_BK_HM_FAC_FRST_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_cl_acpt_dt: Optional[datetime] = Field(
        None,
        alias="GRP_CL_ACPT_DT",
        name="",
        description="",
        example="2022-08-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_ctf_dt: Optional[datetime] = Field(
        None,
        alias="GRP_CTF_DT",
        name="",
        description="",
        example="2022-08-02T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_arvl_dt: Optional[datetime] = Field(
        None,
        alias="GRP_ARVL_DT",
        name="",
        description="",
        example="2023-10-22T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_peak_arvl_dt: Optional[datetime] = Field(
        None,
        alias="GRP_PEAK_ARVL_DT",
        name="",
        description="",
        example="2023-10-21T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_peak_dprt_dt: Optional[datetime] = Field(
        None,
        alias="GRP_PEAK_DPRT_DT",
        name="",
        description="",
        example="2024-01-14T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_dprt_dt: Optional[datetime] = Field(
        None,
        alias="GRP_DPRT_DT",
        name="",
        description="",
        example="2024-03-25T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_peak_rm_cn: int = Field(
        ...,
        alias="GRP_PEAK_RM_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_tot_rm_cn: int = Field(
        ...,
        alias="GRP_TOT_RM_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_vchr_in: str = Field(
        ...,
        alias="GRP_VCHR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_comp_in: str = Field(
        ...,
        alias="GRP_COMP_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_run_hs_in: str = Field(
        ...,
        alias="GRP_RUN_HS_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_exprs_chk_out_in: str = Field(
        ...,
        alias="GRP_EXPRS_CHK_OUT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_hide_rt_in: str = Field(
        ...,
        alias="GRP_HIDE_RT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_comm_allow_in: str = Field(
        ...,
        alias="GRP_COMM_ALLOW_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_disc_promo_allow_in: str = Field(
        ...,
        alias="GRP_DISC_PROMO_ALLOW_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_sprd_dpst_in: str = Field(
        ...,
        alias="GRP_SPRD_DPST_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_rvrt_dpst_in: str = Field(
        ...,
        alias="GRP_RVRT_DPST_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_byps_auto_cncl_in: str = Field(
        ...,
        alias="GRP_BYPS_AUTO_CNCL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_byps_dpst_in: str = Field(
        ...,
        alias="GRP_BYPS_DPST_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_byps_cncl_fee_in: str = Field(
        ...,
        alias="GRP_BYPS_CNCL_FEE_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_byps_mod_fee_in: str = Field(
        ...,
        alias="GRP_BYPS_MOD_FEE_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_auto_cnfirm_in: str = Field(
        ...,
        alias="GRP_AUTO_CNFIRM_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_exprs_lug_in: str = Field(
        ...,
        alias="GRP_EXPRS_LUG_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_res_guar_in: str = Field(
        ...,
        alias="GRP_RES_GUAR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_whsl_in: str = Field(
        ...,
        alias="GRP_WHSL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_dlgt_wrtoff_in: str = Field(
        ...,
        alias="GRP_DLGT_WRTOFF_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_rsr_in: str = Field(
        ...,
        alias="GRP_RSR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_addl_adlt_am: Optional[float] = Field(
        None,
        alias="GRP_ADDL_ADLT_AM",
        name="",
        description="",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_nm: Optional[str] = Field(
        None,
        alias="GRP_NM",
        name="",
        description="",
        example="Mickey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gro_agt_nm: Optional[str] = Field(
        None,
        alias="GRO_AGT_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_dept_nm: Optional[str] = Field(
        None,
        alias="SLS_DEPT_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_mgr_nm: Optional[str] = Field(
        None,
        alias="SLS_MGR_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_phn_nb: Optional[str] = Field(
        None,
        alias="SLS_PHN_NB",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    srvc_dept_nm: Optional[str] = Field(
        None,
        alias="SRVC_DEPT_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    srvc_mgr_nm: Optional[str] = Field(
        None,
        alias="SRVC_MGR_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    srvc_phn_nb: Optional[str] = Field(
        None,
        alias="SRVC_PHN_NB",
        name="",
        description="",
        example="4079383430",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_comm_am_tx: Optional[str] = Field(
        None,
        alias="GRP_COMM_AM_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_comm_pc_tx: Optional[str] = Field(
        None,
        alias="GRP_COMM_PC_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_comm_rt_tx: Optional[str] = Field(
        None,
        alias="GRP_COMM_RT_TX",
        name="",
        description="",
        example="200",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-12T17:56:51Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="HERID003",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-12T17:56:51Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="HERID003",
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
    grp_cnfirm_dest_nm: Optional[str] = Field(
        None,
        alias="GRP_CNFIRM_DEST_NM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_min_los_nb_tx: Optional[str] = Field(
        None,
        alias="GRP_MIN_LOS_NB_TX",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_dlgt_chg_priv_in: str = Field(
        ...,
        alias="GRP_DLGT_CHG_PRIV_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_peak_arvl_tm_tx: Optional[str] = Field(
        None,
        alias="GRP_PEAK_ARVL_TM_TX",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_peak_dprt_tm_tx: Optional[str] = Field(
        None,
        alias="GRP_PEAK_DPRT_TM_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_alias_nm: Optional[str] = Field(
        None,
        alias="GRP_ALIAS_NM",
        name="",
        description="",
        example="19800 WHSl Test",
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


class DREAMSGroupManagementGrpModel(BaseModel):
    """Payload class for DREAMSGroupManagementGrpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Group"
        stream_name = ""
        description = "Information related to the group based on the profile created by the group office"
        unique_identifier = ["data.GRP_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "grp"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
