"""Source Data Contract Template for AvailSE - Unit of Measure Type"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Unit of Measure Type Data"""

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


class AvailSEUomTypModel(BaseModel):
    """Payload class for AvailSE - Unit of Measure Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Unit of Measure Type"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.UOM_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "uom_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
