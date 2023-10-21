"""Source Data Contract for Dreams - Room Reservations Travel Status"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservations Travel Status data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="1980-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Lilo Conv",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    trvl_sts_nm: str = Field(
        ...,
        alias="TRVL_STS_NM",
        name="",
        description="",
        example="Arrived",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsReservationsTrvlStsModel(BaseModel):
    """Payload class for Dreams - Room Reservations Travel Status Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Status"
        stream_name = ""
        description = "List of travel statuses: TRVL_STS_NM, Past Visit, Checked In, Auto Arrived, Arrived, Not Arrived, Checking In, DF Checked Out, Early Check Out, Auto Cancelled, No Show, Cancelled, Booked"
        unique_identifier = ["data.TRVL_STS_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "trvl_sts"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
