"""Source Data Contract Template for AvailSE - Freeze Freesell Inventory"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Freeze Freesell Inventory Data"""

    freeze_fsell_invtry_id: str = Field(
        ...,
        alias="FREEZE_FSELL_INVTRY_ID",
        name="",
        description="",
        example="aa11aa11-1f17-44e4-969e-a9851cb1b0b8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    freeze_id: str = Field(
        ...,
        alias="FREEZE_ID",
        name="",
        description="",
        example="aa11aa11-92d4-46f2-851d-565afc811bd8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fsell_invtry_id: str = Field(
        ...,
        alias="FSELL_INVTRY_ID",
        name="",
        description="",
        example="aa11aa11-887b-c532-f9c3-2fd7573018ee",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_qty_cn: int = Field(
        ...,
        alias="INVTRY_QTY_CN",
        name="",
        description="",
        example=0,
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


class AvailSEFreezeFsellInvtryModel(BaseModel):
    """Payload class for AvailSE - Freeze Freesell Inventory Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Freeze Freesell Inventory"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.FREEZE_FSELL_INVTRY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "freeze_fsell_invtry"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
