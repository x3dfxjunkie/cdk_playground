"""Source Data Contract for Dreams Guest Link GST_LNK_TXN_GST"""


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Guest Link Transaction Guest Data"""

    gst_lnk_txn_gst_id: int = Field(
        ...,
        alias="GST_LNK_TXN_GST_ID",
        name="",
        description="",
        example=1234567890,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gst_lnk_id: int = Field(
        ...,
        alias="GST_LNK_ID",
        name="",
        description="",
        example=1234567891,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_gst_id: int = Field(
        ...,
        alias="TXN_GST_ID",
        name="",
        description="",
        example=9876543210,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-22T08:32:28.870-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-22T08:32:28.870-05:00",
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
    txn_gst_inactv_dts: Optional[datetime] = Field(
        None,
        alias="TXN_GST_INACTV_DTS",
        name="",
        description="",
        example="2021-05-01T18:02:09.000-05:00",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestLinkGstLnkTxnGstModel(BaseModel):
    """Payload class for DREAMSGuestLinkGstLnkTxnGstModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Guest Link Transaction Guest"
        stream_name = ""
        description = """This table associates the guest link ID to the Guest Link Transaction Guest ID and the Transaction Guest ID and the inactive datetime would be populated if the record is inactive"""
        unique_identifier = ["data.GST_LNK_TXN_GST_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "gst_lnk_txn_gst"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
