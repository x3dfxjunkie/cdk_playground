"""Source Data Contract Template for AvailSE - Freeze"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Freeze Data"""

    chan_mtrx_id: str = Field(
        ...,
        alias="CHAN_MTRX_ID",
        name="",
        description="",
        example="aa11aa11-3513-44FB-A397-8EA22FFB7CBF",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    freeze_dts: datetime = Field(
        ...,
        alias="FREEZE_DTS",
        name="",
        description="",
        example="2023-08-04T10:52:37.571000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    freeze_exp_dts: datetime = Field(
        ...,
        alias="FREEZE_EXP_DTS",
        name="",
        description="",
        example="2023-08-04T11:02:37.571000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    freeze_id: str = Field(
        ...,
        alias="FREEZE_ID",
        name="",
        description="",
        example="aa11aa11-f3ac-4c26-8252-6cbe35f340eb",
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


class AvailSEFreezeModel(BaseModel):
    """Payload class for AvailSE - Freeze Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Freeze"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.CHAN_MTRX_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "freeze"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
