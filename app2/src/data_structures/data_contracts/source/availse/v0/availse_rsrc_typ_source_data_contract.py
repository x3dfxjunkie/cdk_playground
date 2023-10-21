"""Source Data Contract Template for AvailSE - Resource Type"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Resource Type Data"""

    rsrc_typ_nm: str = Field(
        ...,
        alias="RSRC_TYP_NM",
        name="",
        description="",
        example="Room",
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


class AvailSERsrcTypModel(BaseModel):
    """Payload class for AvailSE - Resource Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Type"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRC_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
