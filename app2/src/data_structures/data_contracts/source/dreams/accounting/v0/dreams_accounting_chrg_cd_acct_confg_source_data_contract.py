"""Source Data Contract for DREAMS Charge Code Account Configuration"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Account Charge Code Account Configuration Data"""

    chrg_cd_acct_config_id: int = Field(
        ...,
        alias="CHRG_CD_ACCT_CONFIG_ID",
        name="",
        description="",
        example=1,
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
    sap_co_cd: str = Field(
        ...,
        alias="SAP_CO_CD",
        name="",
        description="",
        example="1001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_prft_ctr_cd: str = Field(
        ...,
        alias="SAP_PRFT_CTR_CD",
        name="",
        description="",
        example="0001142222",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_cost_ctr_cd: str = Field(
        ...,
        alias="SAP_COST_CTR_CD",
        name="",
        description="",
        example="0005146043",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_acct_nb: str = Field(
        ...,
        alias="SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000260075",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_mtrl_cd: str = Field(
        ...,
        alias="SAP_MTRL_CD",
        name="",
        description="",
        example="8230",
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
    non_csh_cd: str = Field(
        ...,
        alias="NON_CSH_CD",
        name="",
        description="",
        example="8230",
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
    chrg_cd_acct_cfg_strt_dt: datetime = Field(
        ...,
        alias="CHRG_CD_ACCT_CFG_STRT_DT",
        name="",
        description="",
        example="1999-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_cd_acct_cfg_end_dt: Optional[datetime] = Field(
        None,
        alias="CHRG_CD_ACCT_CFG_END_DT",
        name="",
        description="",
        example="1999-01-01T05:00:00.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingChrgCdAcctConfgModel(BaseModel):
    """Payload class for DREAMSAccountingChrgCdAcctConfgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Code Account Configuration"
        stream_name = ""
        description = """Configuration of SAP IDs that are associated to a charge code"""
        unique_identifier = ["data.CHRG_CD_ACCT_CONFIG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHRG_CD_ACCT_CONFG"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
