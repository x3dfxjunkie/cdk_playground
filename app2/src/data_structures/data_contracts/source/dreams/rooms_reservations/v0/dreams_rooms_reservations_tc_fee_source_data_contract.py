"""Source Data Contract for DREAMS Rooms Reservation Travel Component Fee"""

from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsData,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsData):
    """Class for Dreams Rooms Reservation Travel Component Fee Data"""

    tc_fee_id: int = Field(
        ...,
        alias="TC_FEE_ID",
        name="",
        description="",
        example=30004883640,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="",
        description="",
        example=32095602942,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_fee_typ_nm: str = Field(
        ...,
        alias="TC_FEE_TYP_NM",
        name="",
        description="",
        example="Cancel",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_fee_ovrd_in: str = Field(
        ...,
        alias="TC_FEE_OVRD_IN",
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


class DREAMSRoomsReservationsTcFeeModel(BaseModel):
    """Payload class for DREAMSRoomsReservationsTcFeeModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Rooms Reservation Travel Component Fee"
        stream_name = ""
        description = "There are fees associated to certain types of components that indicate that a fee was one of these types: Exchange Cancel"
        unique_identifier = ["data.TC_FEE_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_fee"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
