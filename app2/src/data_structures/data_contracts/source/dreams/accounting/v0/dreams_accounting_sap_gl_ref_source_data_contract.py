"""Source Data Contract for DREAMS Accounting SAP General Ledger Reference"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Accounting SAP General Ledger Reference Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-29T10:56:25.421000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MIXXM005",
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
    pst_gl_in: str = Field(
        ...,
        alias="PST_GL_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsr_in: str = Field(
        ...,
        alias="RSR_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_acct_nb: str = Field(
        ...,
        alias="SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000700001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_ref_id: int = Field(
        ...,
        alias="SAP_GL_REF_ID",
        name="",
        description="",
        example=3123036,
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
    sap_mtrl_cd: Optional[str] = Field(
        None,
        alias="SAP_MTRL_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_tax_cd: Optional[str] = Field(
        None,
        alias="SAP_TAX_CD",
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
    tax_exmpt_sap_gl_acct_nb: str = Field(
        ...,
        alias="TAX_EXMPT_SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000700001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_exmpt_tax_cd: Optional[str] = Field(
        None,
        alias="TAX_EXMPT_TAX_CD",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trdg_ptnr_bus_area_cd: str = Field(
        ...,
        alias="TRDG_PTNR_BUS_AREA_CD",
        name="",
        description="",
        example="138",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trdg_ptnr_co_cd: str = Field(
        ...,
        alias="TRDG_PTNR_CO_CD",
        name="",
        description="",
        example="1005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-29T10:56:25.421000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MIXXM005",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapGlRefModel(BaseModel):
    """Payload class for DREAMSAccountingSapGlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Accounting SAP General Ledger Reference"
        stream_name = ""
        description = "SAP General Ledger References associated to a SAP General Ledger Reference IDs"  # optional
        unique_identifier = ["data.SAP_GL_REF_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "sap_gl_ref"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
