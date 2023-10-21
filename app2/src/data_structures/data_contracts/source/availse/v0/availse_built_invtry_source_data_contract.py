"""Source Data Contract Template for AvailSE - Built Inventory"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Built Inventory Data"""

    built_invtry_cn: int = Field(
        ...,
        alias="BUILT_INVTRY_CN",
        name="",
        description="",
        example=39,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_id: str = Field(
        ...,
        alias="BUILT_INVTRY_ID",
        name="",
        description="",
        example="11aa11aa-e8ee-42eb-bea6-ebd55ad5a1d8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    built_invtry_strt_dts: datetime = Field(
        ...,
        alias="BUILT_INVTRY_STRT_DTS",
        name="",
        description="",
        example="2016-12-25T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="11aa11aa-AE92-D2C4-E043-9906F4D1D2C4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="fakeu003",
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


class AvailSEBuiltInvtryModel(BaseModel):
    """Payload class for AvailSE - Built Inventory Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Built Inventory"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.BUILT_INVTRY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "built_invtry"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
