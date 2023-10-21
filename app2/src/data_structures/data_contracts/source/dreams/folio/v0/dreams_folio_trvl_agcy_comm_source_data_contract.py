"""Source Data Contract for Dreams Folio Travel Agency Commission"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Travel Agency Commission Data"""

    chrg_grp_chkin_dt: datetime = Field(
        ...,
        alias="CHRG_GRP_CHKIN_DT",
        name="",
        description="",
        example="2023-08-27T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_chkot_dt: datetime = Field(
        ...,
        alias="CHRG_GRP_CHKOT_DT",
        name="",
        description="",
        example="2023-08-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
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
    comm_apprvl_dt: Optional[datetime] = Field(
        None,
        alias="COMM_APPRVL_DT",
        name="",
        description="",
        example="2023-08-28T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_ap_intfc_id: Optional[str] = Field(
        None,
        alias="COMM_AP_INTFC_ID",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_pst_dts: Optional[datetime] = Field(
        None,
        alias="COMM_PST_DTS",
        name="",
        description="",
        example="2023-08-29T02:20:45.928000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comm_sts_nm: str = Field(
        ...,
        alias="COMM_STS_NM",
        name="",
        description="",
        example="PENDING",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-29T02:20:35.420000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="CalCxxn_2",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=80010402,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    res_rspb_pty_id: int = Field(
        ...,
        alias="RES_RSPB_PTY_ID",
        name="",
        description="",
        example=750902445,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    root_chrg_grp_id: int = Field(
        ...,
        alias="ROOT_CHRG_GRP_ID",
        name="",
        description="",
        example=977415829,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_comm_id: int = Field(
        ...,
        alias="TRVL_AGCY_COMM_ID",
        name="",
        description="",
        example=13187576,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_id: int = Field(
        ...,
        alias="TRVL_AGCY_ID",
        name="",
        description="",
        example=19512431,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioTrvlAgcyCommModel(BaseModel):
    """Payload class for DREAMSFolioTrvlAgcyCommModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Agency Commission"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.TRVL_AGCY_COMM_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TRVL_AGCY_COMM"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
