"""Source Data Contract Template for Dreams - Room Reservation Travel Plan Party"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservation Travel Plan Party Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-13T21:53:38.786000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="FAKEU004",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gst_fst_nm: Optional[str] = Field(
        None,
        alias="GST_FST_NM",
        name="",
        description="",
        example="Fake",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    gst_lst_nm: Optional[str] = Field(
        None,
        alias="GST_LST_NM",
        name="",
        description="",
        example="User",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    idvl_pty_in: str = Field(
        ...,
        alias="IDVL_PTY_IN",
        name="",
        description="",
        example="Y",
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

    prmy_pty_in: str = Field(
        ...,
        alias="PRMY_PTY_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tp_id: int = Field(
        ...,
        alias="TP_ID",
        name="",
        description="",
        example=753192630348,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_pty_id: int = Field(
        ...,
        alias="TXN_PTY_ID",
        name="",
        description="",
        example=768136555,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-13T21:53:38.786000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="FAKEU004",
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


class DREAMSRoomsReservationsTpPtyModel(BaseModel):
    """Payload class for Dreams - Room Reservation Travel Plan Party Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan Party"
        stream_name = ""
        description = """This table provides all the guest IDs associated to their Travel Plan"""
        unique_identifier = ["data.TP_ID", "data.TXN_PTY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tp_pty"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
