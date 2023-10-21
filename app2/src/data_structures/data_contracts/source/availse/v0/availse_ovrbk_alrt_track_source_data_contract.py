"""Source Data Contract Template for AvailSE - Overbook Alert Track"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Overbook Alert Track Data"""

    alrt_lvl: str = Field(
        ...,
        alias="ALRT_LVL",
        name="",
        description="",
        example="BOX",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_fac_id: int = Field(
        ...,
        alias="ENTRPRS_FAC_ID",
        name="",
        description="",
        example=90002032,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    id: str = Field(
        ...,
        alias="ID",
        name="",
        description="",
        example="aa11aa11-c6d1-7f6a-fa07-6332af326341",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-db1f-438a-ac1b-9200bfd10c07",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    srvc_dts: datetime = Field(
        ...,
        alias="SRVC_DTS",
        name="",
        description="",
        example="2023-05-21T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="Overbook Monitor",
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


class AvailSEOvrbkAlrtTrackModel(BaseModel):
    """Payload class for AvailSE - Overbook Alert Track Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Overbook Alert Track"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ovrbk_alrt_track"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
