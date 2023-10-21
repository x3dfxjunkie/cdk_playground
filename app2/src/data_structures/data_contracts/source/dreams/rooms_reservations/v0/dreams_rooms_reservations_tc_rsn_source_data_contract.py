"""Source Data Contract for Dreams - Travel Component Reason"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):

    """Data Class for Dreams - Travel Component Reason"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-29T00:44:48.594000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="TbxSyncUser",
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

    prdf_tc_rsn_id: Optional[int] = Field(
        None,
        alias="PRDF_TC_RSN_ID",
        name="",
        description="",
        example=12,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="",
        description="",
        example=12097954742,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_cntct_nm: Optional[str] = Field(
        None,
        alias="TC_RSN_CNTCT_NM",
        name="",
        description="",
        example="scheduler",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_id: int = Field(
        ...,
        alias="TC_RSN_ID",
        name="",
        description="",
        example=1164653985,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_typ_nm: str = Field(
        ...,
        alias="TC_RSN_TYP_NM",
        name="",
        description="",
        example="Cancel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-29T00:44:48.594000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="TbxSyncUser",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_tx: Optional[str] = Field(
        None,
        alias="TC_RSN_TX",
        name="",
        description="",
        example="INTAUTO",
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


class DREAMSRoomsReservationsTcRsnModel(BaseModel):

    """Payload Class for Dreams - Travel Component Reason"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Reason"
        stream_name = ""
        description = """This table provides the reason for certain actions associated to a travel component. It also has the FK for the Preferred Travel Component Reason"""
        unique_identifier = ["data.TC_RSN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_rsn"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
