"""Source Data Contract Template for AvailSE - Metric Audit"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Metric Audit Data"""

    actn_nm: str = Field(
        ...,
        alias="ACTN_NM",
        name="",
        description="",
        example="BOOK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    arvl_dts: datetime = Field(
        ...,
        alias="ARVL_DTS",
        name="",
        description="",
        example="2023-09-28T17:10:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    chan_mtrx_id: str = Field(
        ...,
        alias="CHAN_MTRX_ID",
        name="",
        description="",
        example="AA11AA11-2974-41EA-E043-8B681C5641EA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    freeze_id: str = Field(
        ...,
        alias="FREEZE_ID",
        name="",
        description="",
        example="aa11aa11-322f-4ac9-9b9e-9cf8e5394c69",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    metric_adt_id: str = Field(
        ...,
        alias="METRIC_ADT_ID",
        name="",
        description="",
        example="aa11aa11-837b-4c9d-bca4-e88978aeefe1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    quantity_cn: int = Field(
        ...,
        alias="QUANTITY_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-79c6-43b9-85f2-3113c2634c37",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="mdx-AA11AA11-12A2-4BAA-959B-330BBAC95375",
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


class AvailSEMetricAdtModel(BaseModel):
    """Payload class for AvailSE - Metric Audit Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Metric Audit"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.CHAN_MTRX_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "metric_adt"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
