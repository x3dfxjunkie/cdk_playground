"""Source Data Contract for Dreams Guest Link TXN_GST_XREF"""


from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Guest Link Transaction Guest Crossreference Data"""

    txn_gst_xref_src_nm: str = Field(
        ...,
        alias="TXN_GST_XREF_SRC_NM",
        name="",
        description="",
        example="CHARGE_ACCOUNT_ID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gst_lnk_txn_gst_id: int = Field(
        ...,
        alias="GST_LNK_TXN_GST_ID",
        name="",
        description="",
        example=8841033400,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_gst_xref_vl: str = Field(
        ...,
        alias="TXN_GST_XREF_VL",
        name="",
        description="",
        example="12345678",
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
        example="2023-07-06T13:08:21.319762Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGuestLinkTxnGstXrefModel(BaseModel):
    """Payload class for DREAMSGuestLinkTxnGstXrefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Guest Crossreference"
        stream_name = ""
        description = """This table links the Transaction Guest Crossreference source name: CHARGE_ACCOUNT_ID to the Guest Link Transaction Guest ID to provide the Transaction Guest Crossreference value"""
        unique_identifier = ["data.GST_LNK_TXN_GST_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_gst_xref"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
