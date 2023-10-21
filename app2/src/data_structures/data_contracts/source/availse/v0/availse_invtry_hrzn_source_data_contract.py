"""Source Data Contract Template for AvailSE - Inventory Horizon"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Inventory Horizon Data"""

    bkng_hrzn_dy_cn: int = Field(
        ...,
        alias="BKNG_HRZN_DY_CN",
        name="",
        description="",
        example=191,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bkng_hrzn_ext_dy_cn: int = Field(
        ...,
        alias="BKNG_HRZN_EXT_DY_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_hrzn_cd: str = Field(
        ...,
        alias="INVTRY_HRZN_CD",
        name="",
        description="",
        example="16580",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="LOAD",
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


class AvailSEInvtryHrznModel(BaseModel):
    """Payload class for AvailSE - Inventory Horizon Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Inventory Horizon"
        stream_name = ""
        description = """"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "invtry_hrzn"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
