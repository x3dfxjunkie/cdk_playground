"""Source Data Contract Template for AvailSE - Physical Resource Status"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Physical Resource Status Data"""

    phys_rsrc_id: str = Field(
        ...,
        alias="PHYS_RSRC_ID",
        name="",
        description="",
        example="AA11AA11-25FD-71F6-E053-BABD06991F38",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    phys_rsrc_strt_dts: datetime = Field(
        ...,
        alias="PHYS_RSRC_STRT_DTS",
        name="",
        description="",
        example="2023-08-04T18:15:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    phys_rsrc_sts_id: str = Field(
        ...,
        alias="PHYS_RSRC_STS_ID",
        name="",
        description="",
        example="aa11aa11-b988-c99e-9713-7b547bbb4155",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

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
        example="0001-01-01ST00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    version_sn: int = Field(
        ...,
        alias="VERSION_SN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSEPhysRsrcStsModel(BaseModel):
    """Payload class for AvailSE - Physical Resource Status Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Physical Resource Status"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.PHYS_RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "phys_rsrc_sts"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
