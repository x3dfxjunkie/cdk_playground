"""Source Data Contract Template for AvailSE - Reason Feature Type"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reason Feature Type Data"""

    rsrc_feat_typ_max_cn: int = Field(
        ...,
        alias="RSRC_FEAT_TYP_MAX_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_feat_typ_nm: str = Field(
        ...,
        alias="RSRC_FEAT_TYP_NM",
        name="",
        description="",
        example="Boat Type",
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


class AvailSERsrcFeatTypModel(BaseModel):
    """Payload class for AvailSE - Reason Feature Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Feature Type"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRC_FEAT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_feat_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
