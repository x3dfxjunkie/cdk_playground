"""Source Data Contract Template for AvailSE - Reservable Resource Feature"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reservable Resource Feature Data"""

    rsrc_feat_id: str = Field(
        ...,
        alias="RSRC_FEAT_ID",
        name="",
        description="",
        example="aa11aa11-35c7-b7ac-e92d-e2aa74ab6961",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-357f-4d6c-5c77-f506c37dac84",
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


class AvailSERsrvblRsrcFeatModel(BaseModel):
    """Payload class for AvailSE - Reservable Resource Feature Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservable Resource Feature"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRVBL_RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrvbl_rsrc_feat"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
