"""Source Data Contract Template for AvailSE - Reason"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reason Data"""

    rsn_id: str = Field(
        ...,
        alias="RSN_ID",
        name="",
        description="",
        example="aa11aa11-9d94-139c-9b86-fe369d681e01",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsn_nm: str = Field(
        ...,
        alias="RSN_NM",
        name="",
        description="",
        example="Hold for Caputo/Fiammi",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsn_nm_end_dts: Optional[str] = Field(
        None,
        alias="RSN_NM_END_DTS",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsn_nm_strt_dts: Optional[datetime] = Field(
        None,
        alias="RSN_NM_STRT_DTS",
        name="",
        description="",
        example="2008-04-14T16:15:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

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

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU101",
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
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSERsnModel(BaseModel):
    """Payload class for AvailSE - Reason Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reason"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsn"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
