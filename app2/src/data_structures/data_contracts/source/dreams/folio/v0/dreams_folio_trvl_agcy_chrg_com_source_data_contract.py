"""Source Data Contract for Dreams Folio Travel Agency Charge Commission"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Travel Agency Charge Commission Data"""

    base_chrg_am: float = Field(
        ...,
        alias="BASE_CHRG_AM",
        name="",
        description="",
        example=230.35,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    base_chrg_crncy_cd: str = Field(
        ...,
        alias="BASE_CHRG_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    calc_comm_am: float = Field(
        ...,
        alias="CALC_COMM_AM",
        name="",
        description="",
        example=23.04,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    calc_comm_crncy_cd: str = Field(
        ...,
        alias="CALC_COMM_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_id: Optional[int] = Field(
        None,
        alias="CHRG_ID",
        name="",
        description="",
        example=3402403522,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_unit_cn: int = Field(
        ...,
        alias="CHRG_UNIT_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_cls_nm: str = Field(
        ...,
        alias="COMM_CLS_NM",
        name="",
        description="",
        example="ACCOMMODATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_rt: int = Field(
        ...,
        alias="COMM_RT",
        name="",
        description="",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_unit_ds: Optional[str] = Field(
        None,
        alias="COMM_UNIT_DS",
        name="",
        description="",
        example="The Little Mermaid Standard Room - VA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-21T02:21:25.566000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="CalCmsn_2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_class_typ_nm: str = Field(
        ...,
        alias="JDO_CLASS_TYP_NM",
        name="",
        description="",
        example="ACCOMMODATION",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pd_comm_am: float = Field(
        ...,
        alias="PD_COMM_AM",
        name="",
        description="",
        example=23.04,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pd_comm_crncy_cd: str = Field(
        ...,
        alias="PD_COMM_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_id: Optional[int] = Field(
        None,
        alias="PKG_ID",
        name="",
        description="",
        example=7981720,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ptntl_comm_am: float = Field(
        ...,
        alias="PTNTL_COMM_AM",
        name="",
        description="",
        example=23.04,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ptntl_comm_crncy_cd: str = Field(
        ...,
        alias="PTNTL_COMM_CRNCY_CD",
        name="",
        description="",
        example="USD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rate_typ_nm: str = Field(
        ...,
        alias="RATE_TYP_NM",
        name="",
        description="",
        example="Percentage",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: Optional[int] = Field(
        None,
        alias="REV_CLS_ID",
        name="",
        description="",
        example=16603198,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_bus_area_cd: Optional[str] = Field(
        None,
        alias="SAP_BUS_AREA_CD",
        name="",
        description="",
        example="138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_cost_ctr_cd: str = Field(
        ...,
        alias="SAP_COST_CTR_CD",
        name="",
        description="",
        example="0005156333",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_co_cd: Optional[str] = Field(
        None,
        alias="SAP_CO_CD",
        name="",
        description="",
        example="1001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_acct_nb: str = Field(
        ...,
        alias="SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000674001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_wbs_cd: Optional[str] = Field(
        None,
        alias="SAP_WBS_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ta_chrg_comm_cmt_tx: Optional[str] = Field(
        None,
        alias="TA_CHRG_COMM_CMT_TX",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_chrg_comm_id: int = Field(
        ...,
        alias="TRVL_AGCY_CHRG_COMM_ID",
        name="",
        description="",
        example=14076305,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_comm_id: int = Field(
        ...,
        alias="TRVL_AGCY_COMM_ID",
        name="",
        description="",
        example=13185880,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-21T02:21:25.566000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="CalCmsn_2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioTrvlAgcyChrgComModel(BaseModel):
    """Payload class for DREAMSFolioTrvlAgcyChrgComModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Agency Charge Commission"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.TRVL_AGCY_CHRG_COMM_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TRVL_AGCY_CHRG_COM"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
