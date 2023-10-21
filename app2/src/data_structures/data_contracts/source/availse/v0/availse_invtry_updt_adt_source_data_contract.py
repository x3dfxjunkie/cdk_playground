"""Source Data Contract Template for AvailSE - Inventory Update Audit"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Inventory Update Audit Data"""

    bkng_actn_nm: str = Field(
        ...,
        alias="BKNG_ACTN_NM",
        name="",
        description="",
        example="CREATE_WANT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    cnvrs_id_vl: str = Field(
        ...,
        alias="CNVRS_ID_VL",
        name="",
        description="",
        example="mdx-AA11AA11-74C1-496B-9F9D-070FF7C82E0C",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    error_ds: str = Field(
        ...,
        alias="ERROR_DS",
        name="",
        description="",
        example="Success",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    err_cd: str = Field(
        ...,
        alias="ERR_CD",
        name="",
        description="",
        example="Success",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    freeze_id: str = Field(
        ...,
        alias="FREEZE_ID",
        name="",
        description="",
        example="aa11aa11-837b-44ee-b3d9-676f4067caae",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    invtry_updt_adt_id: str = Field(
        ...,
        alias="INVTRY_UPDT_ADT_ID",
        name="",
        description="",
        example="aa11aa11-19cf-f138-4d64-c660ebedab14",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    los_cn: int = Field(
        ...,
        alias="LOS_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    qty_cn: int = Field(
        ...,
        alias="QTY_CN",
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
        example="AA11AA11-EA6D-1440-142E-F86D8ED27275",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    srvc_dts: datetime = Field(
        ...,
        alias="SRVC_DTS",
        name="",
        description="",
        example="2023-10-15T10:25:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="1@7d7758ef3a59",
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


class AvailSEInvtryUpdtAdtModel(BaseModel):
    """Payload class for AvailSE - Inventory Update Audit Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Inventory Update Audit"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.FREEZE_ID", "data.INVTRY_UPDT_ADT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "invtry_updt_adt"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
