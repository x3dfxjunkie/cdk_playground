"""Source Data Contract Template for AvailSE - Reservable Resource Type"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reservable Resource Type Data"""

    rsrvbl_rsrc_typ_nm: str = Field(
        ...,
        alias="RSRVBL_RSRC_TYP_NM",
        name="",
        description="",
        example="FixDineNonYieldLastSinglePeriodAuthSameResource",
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


class AvailSERsrvblRsrcTypModel(BaseModel):
    """Payload class for AvailSE - Reservable Resource Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservable Resource Type"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRVBL_RSRC_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrvbl_rsrc_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
