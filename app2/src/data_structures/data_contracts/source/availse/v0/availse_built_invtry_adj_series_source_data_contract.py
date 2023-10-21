"""Source Data Contract Template for AvailSE - Built Inventory Adjusted Series"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Built Inventory Adjusted Series Data"""

    built_invtry_adj_series_end_dt: datetime = Field(
        ...,
        alias="BUILT_INVTRY_ADJ_SERIES_END_DT",
        name="",
        description="",
        example="2023-07-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_adj_series_id: str = Field(
        ...,
        alias="BUILT_INVTRY_ADJ_SERIES_ID",
        name="",
        description="",
        example="aa11aa11-59c4-dd52-a5aa-1f7b808b7fbf",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_adj_series_st_dt: datetime = Field(
        ...,
        alias="BUILT_INVTRY_ADJ_SERIES_ST_DT",
        name="",
        description="",
        example="2023-07-16T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU005",
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


class AvailSEBuiltInvtryAdjSeriesModel(BaseModel):
    """Payload class for AvailSE - Built Inventory Adjusted Series Model"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """"""
        unique_identifier = ["data.BUILT_INVTRY_ADJ_SERIES_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "built_invtry_adj_series"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
