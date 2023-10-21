"""Source Data Contract Template for Dreams - Room Fulfillment Travel Component Guest"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Room Fulfillment Travel Component Guest Data"""

    age_nb: int = Field(
        ...,
        alias="AGE_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    age_typ_nm: str = Field(
        ...,
        alias="AGE_TYP_NM",
        name="",
        description="",
        example="INFANT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-21T16:18:56.116000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="FAKEU028",
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

    tc_gst_id: int = Field(
        ...,
        alias="TC_GST_ID",
        name="",
        description="",
        example=11897046006,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="",
        description="",
        example=12097622084,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_idvl_pty_id: Optional[int] = Field(
        None,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=770546142,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-21T16:18:56.116000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="FAKEU028",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    vst_prps_nm: Optional[str] = Field(
        None,
        alias="VST_PRPS_NM",
        name="",
        description="",
        example="Leisure",
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


class DREAMSRoomsFulfillmentTcGstModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Travel Component Guest Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Guest"
        stream_name = ""
        description = """This table provides the age type and age number for the guests associated to that travel component, as well as the transactional individual ID and the visit purpose."""
        unique_identifier = ["data.TC_GST_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_gst"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
