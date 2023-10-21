"""Source Data Contract Template for CHRG_GRP_TRVL_GST.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for CHRG_GRP_TRVL_GST"""

    chrg_grp_trvl_gst_id: int = Field(
        ...,
        alias="CHRG_GRP_TRVL_GST_ID",
        name="",
        description="",
        example=564082031,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    root_chrg_grp_id: int = Field(
        ...,
        alias="ROOT_CHRG_GRP_ID",
        name="",
        description="",
        example=983317311,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    txn_idvl_pty_id: int = Field(
        ...,
        alias="TXN_IDVL_PTY_ID",
        name="",
        description="",
        example=760603142,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="TradeOrderSv",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T09:16:04.868000Z",
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


class DREAMSFolioChrgGrpTrvlGstModel(BaseModel):
    """Payload class for DREAMSFolioChrgGrpTrvlGstModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Group Travel Guest"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_GRP_TRVL_GST_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CHRG_GRP_TRVL_GST"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
