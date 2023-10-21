"""Source Data Contract Template for AvailSE - Sales Channel"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Sales Channel Data"""

    sls_chan_id: int = Field(
        ...,
        alias="SLS_CHAN_ID",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sls_chan_nm: str = Field(
        ...,
        alias="SLS_CHAN_NM",
        name="",
        description="",
        example="Consumer Direct",
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


class AvailSESlsChanModel(BaseModel):
    """Payload class for AvailSE - Sales Channel Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Sales Channel"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.SLS_CHAN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "sls_chan"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
