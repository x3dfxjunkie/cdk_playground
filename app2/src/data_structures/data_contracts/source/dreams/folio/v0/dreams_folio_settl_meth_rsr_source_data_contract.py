"""Source Data Contract for Dreams Folio Settlement Method Resort Special Reservations"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Settlement Method Resort Special Reservations Data"""

    acct_ctr_sap_id: int = Field(
        ...,
        alias="ACCT_CTR_SAP_ID",
        name="",
        description="",
        example=1177900,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_ref_id: int = Field(
        ...,
        alias="SAP_GL_REF_ID",
        name="",
        description="",
        example=3113582,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsr_apprv_nm: str = Field(
        ...,
        alias="RSR_APPRV_NM",
        name="",
        description="",
        example="marlie morrison",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsr_apprv_title_nm: str = Field(
        ...,
        alias="RSR_APPRV_TITLE_NM",
        name="",
        description="",
        example="dir",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsr_req_nm: str = Field(
        ...,
        alias="RSR_REQ_NM",
        name="",
        description="",
        example="kazu aoi",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsr_req_phn_nb: str = Field(
        ...,
        alias="RSR_REQ_PHN_NB",
        name="",
        description="",
        example="4075666328",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsr_prps_tx: str = Field(
        ...,
        alias="RSR_PRPS_TX",
        name="",
        description="",
        example="FAM trip",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dept_nm: str = Field(
        ...,
        alias="DEPT_NM",
        name="",
        description="",
        example="International Travel Industry Sales",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_id: int = Field(
        ...,
        alias="SETTL_METH_ID",
        name="",
        description="",
        example=426222147,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ESCOS026",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-29T12:38:00.198000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="ESCOS026",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-05-29T12:38:00.198000Z",
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
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-05-29T12:38:00.198000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioSettlMethRsrModel(BaseModel):
    """Payload class for DREAMSFolioSettlMethRsrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Settlement Method Resort Special Reservations"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.SETTL_METH_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SETTL_METH_RSR"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
