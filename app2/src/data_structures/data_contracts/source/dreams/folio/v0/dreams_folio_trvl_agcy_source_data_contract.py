"""Source Data Contract for Dreams Folio Travel Agency"""
from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Travel Agency Data"""

    cmps_id: int = Field(
        ...,
        alias="CMPS_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2012-02-03T12:37:59.331000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="PERXX057",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    glbl_tkt_comm_in: str = Field(
        ...,
        alias="GLBL_TKT_COMM_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    iata_id: str = Field(
        ...,
        alias="IATA_ID",
        name="",
        description="",
        example="99907253",
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
    sap_vndr_id: str = Field(
        ...,
        alias="SAP_VNDR_ID",
        name="",
        description="",
        example="99907253",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_actv_in: str = Field(
        ...,
        alias="TRVL_AGCY_ACTV_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_fm_create_dt: Optional[datetime] = Field(
        None,
        alias="TRVL_AGCY_FM_CREATE_DT",
        name="",
        description="",
        example="2010-10-13T05:21:08Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_id: int = Field(
        ...,
        alias="TRVL_AGCY_ID",
        name="",
        description="",
        example=36147771,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_nm: str = Field(
        ...,
        alias="TRVL_AGCY_NM",
        name="",
        description="",
        example="Reinke Travel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_ods_id: Optional[int] = Field(
        None,
        alias="TRVL_AGCY_ODS_ID",
        name="",
        description="",
        example=420786149,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_pay_comm_in: str = Field(
        ...,
        alias="TRVL_AGCY_PAY_COMM_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2012-02-03T12:39:28.982000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="PEREA057",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioTrvlAgcyModel(BaseModel):
    """Payload class for DREAMSFolioTrvlAgcyModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Agency"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.TRVL_AGCY_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TRVL_AGCY"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
