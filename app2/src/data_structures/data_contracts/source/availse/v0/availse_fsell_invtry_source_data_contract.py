"""Source Data Contract Template for AvailSE - Freesell Inventory"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Freesell Inventory Data"""

    auth_invtry_cn: int = Field(
        ...,
        alias="AUTH_INVTRY_CN",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    bk_cn: int = Field(
        ...,
        alias="BK_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    combo_bk_cn: int = Field(
        ...,
        alias="COMBO_BK_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dsny_ctrl_invtry_cn: Optional[int] = Field(
        None,
        alias="DSNY_CTRL_INVTRY_CN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    freeze_cn: int = Field(
        ...,
        alias="FREEZE_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fsell_invtry_id: str = Field(
        ...,
        alias="FSELL_INVTRY_ID",
        name="",
        description="",
        example="aa11aa11-d531-f67d-3a0b-9c0b4c26b4c4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fsell_invtry_srvc_dts: datetime = Field(
        ...,
        alias="FSELL_INVTRY_SRVC_DTS",
        name="",
        description="",
        example="2023-10-16T08:35:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fsell_invtry_typ_nm: str = Field(
        ...,
        alias="FSELL_INVTRY_TYP_NM",
        name="",
        description="",
        example="free sell invtry",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="AA11AA11-B686-D771-18BD-E3A504C58440",
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
        example=18,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSEFsellInvtryModel(BaseModel):
    """Payload class for AvailSE - Freesell Inventory Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Freesell Inventory"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.FSELL_INVTRY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "fsell_invtry"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
