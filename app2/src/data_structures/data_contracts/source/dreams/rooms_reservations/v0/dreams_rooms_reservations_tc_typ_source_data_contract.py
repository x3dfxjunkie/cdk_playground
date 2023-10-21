"""Source Data Contract for Dreams - Room Reservations Travel Component Type"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsMetadata,
)


class Data(BaseModel):
    """Class for Dreams - Room Reservations Travel Component Type data"""

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

    tc_typ_nm: str = Field(
        ...,
        alias="TC_TYP_NM",
        name="",
        description="",
        example="AdmissionComponent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsReservationsTcTypModel(BaseModel):
    """Payload class for Dreams - Room Reservations Travel Component Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Type"
        stream_name = ""
        description = "List of travel component types:AccommodationComponent, Service, PackageTravelComponent, AdmissionComponent, ComponentTravelComponent"
        unique_identifier = ["data.TC_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
