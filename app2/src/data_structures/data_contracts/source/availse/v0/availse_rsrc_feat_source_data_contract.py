"""Source Data Contract Template for AvailSE - Reason Feature"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reason Feature Data"""

    rsrc_feat_id: str = Field(
        ...,
        alias="RSRC_FEAT_ID",
        name="",
        description="",
        example="aa11aa11-b73a-4071-9626-538986991948",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_feat_nm: str = Field(
        ...,
        alias="RSRC_FEAT_NM",
        name="",
        description="",
        example="Cal F&W Exp - Dis Fam Wines",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_feat_shrt_nm: str = Field(
        ...,
        alias="RSRC_FEAT_SHRT_NM",
        name="",
        description="",
        example="Family",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_feat_typ_nm: str = Field(
        ...,
        alias="RSRC_FEAT_TYP_NM",
        name="",
        description="",
        example="Activity",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_typ_nm: str = Field(
        ...,
        alias="RSRC_TYP_NM",
        name="",
        description="",
        example="Seat",
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


class AvailSERsrcFeatModel(BaseModel):
    """Payload class for AvailSE - Reason Feature Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Feature"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRC_FEAT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_feat"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
