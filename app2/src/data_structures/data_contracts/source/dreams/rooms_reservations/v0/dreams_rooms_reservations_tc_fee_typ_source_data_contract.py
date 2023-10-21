"""Source Data Contract for Dreams - Room Reservations Travel Component Fee Type"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservations Travel Component Fee Type data"""

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


class DREAMSRoomsReservationsTcFeeTypModel(BaseModel):
    """Payload class for Dreams - Room Reservations Travel Component Fee Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Fee Type"
        stream_name = ""
        description = "Types of fees associated to certain component types."
        unique_identifier = ["data.TC_FEE_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_fee_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
