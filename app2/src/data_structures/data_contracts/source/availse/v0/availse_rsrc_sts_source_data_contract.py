"""Source Data Contract Template for AvailSE - Resource Status"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Resource Status Data"""

    rsrc_sts_nm: str = Field(
        ...,
        alias="RSRC_STS_NM",
        name="",
        description="",
        example="Open",
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


class AvailSERsrcStsModel(BaseModel):
    """Payload class for AvailSE - Resource Status Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Status"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRC_STS_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_sts"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
