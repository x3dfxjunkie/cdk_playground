"""Source Data Contract Template for AvailSE - Reservable Resource Unit of Measure"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reservable Resource Unit of Measure Data"""

    rsrvbl_rsrc_uom_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_UOM_ID",
        name="",
        description="",
        example="aa11aa11-3703-442e-8449-d0c0a8b4be71",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uom_cn: int = Field(
        ...,
        alias="UOM_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    uom_typ_nm: str = Field(
        ...,
        alias="UOM_TYP_NM",
        name="",
        description="",
        example="Hour",
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


class AvailSERsrvblRsrcUomModel(BaseModel):
    """Payload class for AvailSE - Reservable Resource Unit of Measure Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservable Resource Unit of Measure"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRVBL_RSRC_UOM_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrvbl_rsrc_uom"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
