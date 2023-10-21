"""Source Data Contract for Dreams PKG TC"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsData,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsData):
    """Class for Dreams PKG TC"""

    pkg_tc_id: int = Field(
        ...,
        alias="PKG_TC_ID",
        name="Package Travel Component Identifier",
        description="The identification of a travel component that is the package travel component.",
        example=2085474030,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    rsr_in: str = Field(
        ...,
        alias="RSR_IN",
        name="Resort Special Reservation Identifier",
        description="Identifies that a package is (Y) or is not (N) a Resort Special Reservation travel component.",
        example="N",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    rm_only_pkg_in: str = Field(
        ...,
        alias="RM_ONLY_PKG_IN",
        name="Room Only Package Identifier",
        description="Identifies that a package travel component is (Y) or is not (N) a room only package travel component.  Default setting is N, the package travel component is not a room only package.",
        example="N",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    whls_pkg_in: str = Field(
        ...,
        alias="WHLS_PKG_IN",
        name="Wholesale Package Identifier",
        description="Identifies that the package component is (Y) or is not (N) a wholesaler package.",
        example="N",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
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


class DREAMSRoomsReservationsPkgTcModel(BaseModel):
    """Payload class for DREAMSRoomsReservationsPkgTcModel"""

    class Config:
        """Payload Level Metadata for DreamsPkgTcModel"""

        title = "Package Travel Component"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table provides indicators for Resort Special Reservations, Room only and wholesale packages"
        unique_identifier = ["data.PKG_TC_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "pkg_tc"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
