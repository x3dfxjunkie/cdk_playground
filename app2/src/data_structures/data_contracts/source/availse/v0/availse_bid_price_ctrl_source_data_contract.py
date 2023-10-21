"""Source Data Contract Template for AvailSE - Bid Price Control"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Bid Price Control Data"""

    bid_price_ctrl_cpcty_nb: int = Field(
        ...,
        alias="BID_PRICE_CTRL_CPCTY_NB",
        name="",
        description="",
        example=11,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bid_price_ctrl_end_dts: Optional[str] = Field(
        None,
        alias="BID_PRICE_CTRL_END_DTS",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bid_price_ctrl_srvc_dts: datetime = Field(
        ...,
        alias="BID_PRICE_CTRL_SRVC_DTS",
        name="",
        description="",
        example="2023-08-23T08:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bid_price_ctrl_strt_dts: datetime = Field(
        ...,
        alias="BID_PRICE_CTRL_STRT_DTS",
        name="",
        description="",
        example="2023-08-18T00:38:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bid_price_ctrl_vl: int = Field(
        ...,
        alias="BID_PRICE_CTRL_VL",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="AA11AA11-01B9-CD2F-3ED7-AF568ED258C6",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: str = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="0001-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSEBidPriceCtrlModel(BaseModel):
    """Payload class for AvailSE - Bid Price Control Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Bid Price Control"
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "bid_price_ctrl"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
