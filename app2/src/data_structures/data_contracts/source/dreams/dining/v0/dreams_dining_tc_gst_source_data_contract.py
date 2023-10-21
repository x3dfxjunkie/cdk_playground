"""Source Data Contract for Dreams TC GST"""
from __future__ import annotations
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from pydantic import BaseModel, Field


class Data(BaseModel):
    """Class for Dreams TC GST Data"""

    age_nb: int = Field(
        ...,
        alias="AGE_NB",
        name="",
        description="",
        example=31,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_typ_nm: str = Field(
        ...,
        alias="AGE_TYP_NM",
        name="",
        description="",
        example="ADULT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-14T14:58:30Z",
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

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_gst_id: int = Field(
        ...,
        alias="TC_GST_ID",
        name="",
        description="",
        example=11111111416,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="",
        description="",
        example=11111110229,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_idvl_mbrshp_id: Optional[int] = Field(
        None,
        alias="TXN_IDVL_MBRSHP_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_idvl_pty_id: Optional[int] = Field(
        None,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=775919534,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_pty_rl_id: Optional[str] = Field(
        None,
        alias="TXN_PTY_RL_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-14T14:58:30Z",
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

    vst_prps_nm: str = Field(
        ...,
        alias="VST_PRPS_NM",
        name="",
        description="",
        example="Leisure",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    incognito: Optional[str] = Field(
        None,
        alias="incognito",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningTcGstModel(BaseModel):
    """Payload class for DREAMSDiningTcGstModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Guest"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table provides the age type and age number for the guests associated to that travel component, as well as the transactional individual ID and the visit purpose."
        unique_identifier = ["data.TC_GST_ID"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc_gst"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
