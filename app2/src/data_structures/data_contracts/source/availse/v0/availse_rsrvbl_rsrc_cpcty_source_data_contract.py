"""Source Data Contract Template for AvailSE - Reservable Resource Capacity"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reservable Resource Capacity Data"""

    max_cpcty_cn: int = Field(
        ...,
        alias="MAX_CPCTY_CN",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    min_cpcty_cn: int = Field(
        ...,
        alias="MIN_CPCTY_CN",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_cpcty_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_CPCTY_ID",
        name="",
        description="",
        example="aa11aa11-60b1-4945-9974-a37f8a4c3b42",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_cpcty_strt_dts: datetime = Field(
        ...,
        alias="RSRVBL_RSRC_CPCTY_STRT_DTS",
        name="",
        description="",
        example="2021-07-06T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-67a8-4b5f-94c8-2a39175795f3",
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


class AvailSERsrvblRsrcCpctyModel(BaseModel):
    """Payload class for AvailSE - Reservable Resource Capacity Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservable Resource Capacity"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRVBL_RSRC_CPCTY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrvbl_rsrc_cpcty"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
