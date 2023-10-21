"""Source Data Contract Template for AvailSE - Reason Type"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reason Type Data"""

    rsn_typ_nm: str = Field(
        ...,
        alias="RSN_TYP_NM",
        name="",
        description="",
        example="Box Reason",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsn_typ_nm_end_dts: Optional[str] = Field(
        None,
        alias="RSN_TYP_NM_END_DTS",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsn_typ_nm_strt_dts: datetime = Field(
        ...,
        alias="RSN_TYP_NM_STRT_DTS",
        name="",
        description="",
        example="2008-04-14T00:00:00Z",
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


class AvailSERsnTypModel(BaseModel):
    """Payload class for AvailSE - Reason Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reason Type"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSN_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsn_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
