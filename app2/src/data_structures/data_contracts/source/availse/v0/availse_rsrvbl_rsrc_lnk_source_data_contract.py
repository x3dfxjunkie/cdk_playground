"""Source Data Contract Template for AvailSE - Reservable Resource Link"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reservable Resource Link Data"""

    prmy_rsrvbl_rsrc_id: str = Field(
        ...,
        alias="PRMY_RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-019c-44b7-b6a7-a4fdb696e9a7",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    scnd_rsrvbl_rsrc_id: str = Field(
        ...,
        alias="SCND_RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-817a-44bd-8a33-1bb9fd7aa915",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: Optional[str] = Field(
        None,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="fakeu",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: Optional[str] = Field(
        None,
        alias="UPDT_DTS",
        name="",
        description="",
        example="0001-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSERsrvblRsrcLnkModel(BaseModel):
    """Payload class for AvailSE - Reservable Resource Link Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservable Resource Link"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.SCND_RSRVBL_RSRC_ID", "data.PRMY_RSRVBL_RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrvbl_rsrc_lnk"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
