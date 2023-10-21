"""Source Data Contract for DREAMS Charge Code Interface Payment Method"""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Charge Code Interface Payment Method Data"""

    chrg_cd_infc_pmt_meth_id: int = Field(
        ...,
        alias="CHRG_CD_INFC_PMT_METH_ID",
        name="",
        description="",
        example=11111111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_cd_infc_smry_id: int = Field(
        ...,
        alias="CHRG_CD_INFC_SMRY_ID",
        name="",
        description="",
        example=22222222,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_acct_nb: str = Field(
        ...,
        alias="SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000121096",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_prft_ctr_cd: str = Field(
        ...,
        alias="SAP_PRFT_CTR_CD",
        name="",
        description="",
        example="0001155917",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_bus_area_cd: str = Field(
        ...,
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
        example="0005151604",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_co_cd: str = Field(
        ...,
        alias="SRC_CO_CD",
        name="",
        description="",
        example="1001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_co_cd: str = Field(
        ...,
        alias="CHRG_CO_CD",
        name="",
        description="",
        example="1001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_dstr_chan_nm: str = Field(
        ...,
        alias="SAP_DSTR_CHAN_NM",
        name="",
        description="",
        example="Retail Consumer",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_mtrl_cd: str = Field(
        ...,
        alias="SAP_MTRL_CD",
        name="",
        description="",
        example="7184",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mtrl_id_vl: str = Field(
        ...,
        alias="MTRL_ID_VL",
        name="",
        description="",
        example="7184",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_qty_cn: Optional[int] = Field(
        None,
        alias="PMT_QTY_CN",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    non_csh_cd: Optional[str] = Field(
        None,
        alias="NON_CSH_CD",
        name="",
        description="",
        example="7184",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tot_non_csh_pmt_meth_am: float = Field(
        ...,
        alias="TOT_NON_CSH_PMT_METH_AM",
        name="",
        description="",
        example=122.45,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dest_geo_cd: str = Field(
        ...,
        alias="DEST_GEO_CD",
        name="",
        description="",
        example="US",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="BBBBB000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-23T18:20:37.652000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_iss_cd: Optional[str] = Field(
        None,
        alias="SAP_ISS_CD",
        name="",
        description="",
        example="None",
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
    ord_nb: Optional[str] = Field(
        None,
        alias="ORD_NB",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-05-23T18:20:37.652000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingChrgCdInfcPmthModel(BaseModel):
    """Payload class for DREAMSAccountingChrgCdInfcPmthModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Code Interface Payment Method"
        stream_name = ""
        description = "Configuration of SAP IDs that are associated to a payment method"  # optional
        unique_identifier = ["data.CHRG_CD_INFC_PMT_METH_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "chrg_cd_infc_pmth"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
