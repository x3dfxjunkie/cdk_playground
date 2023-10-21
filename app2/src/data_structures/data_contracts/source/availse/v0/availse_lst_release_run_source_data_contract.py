"""Source Data Contract Template for AvailSE - Last Release Run"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Last Release Run Data"""

    entrprs_fac_id: int = Field(
        ...,
        alias="ENTRPRS_FAC_ID",
        name="",
        description="",
        example=210507,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    lst_release_run: datetime = Field(
        ...,
        alias="LST_RELEASE_RUN",
        name="",
        description="",
        example="2023-08-04T12:01:01Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSELstReleaseRunModel(BaseModel):
    """Payload class for AvailSE - Last Release Run Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Last Release Run"
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "lst_release_run"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
