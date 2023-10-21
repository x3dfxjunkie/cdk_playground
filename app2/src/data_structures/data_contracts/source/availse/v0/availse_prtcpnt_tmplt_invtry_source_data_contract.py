"""Source Data Contract Template for AvailSE - Participant Template Inventory"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Participant Template Inventory Data"""

    dy_tm: datetime = Field(
        ...,
        alias="DY_TM",
        name="",
        description="",
        example="1970-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_auth_cn: int = Field(
        ...,
        alias="PRTCPNT_TMPLT_AUTH_CN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_id: str = Field(
        ...,
        alias="PRTCPNT_TMPLT_ID",
        name="",
        description="",
        example="aa11aa11-d868-15f8-dd79-81df472a2ec8",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_invtry_id: str = Field(
        ...,
        alias="PRTCPNT_TMPLT_INVTRY_ID",
        name="",
        description="",
        example="aa11aa11-3bea-bf3a-d913-9c18c90d6e3e",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="AA11AA11-06A6-2170-E043-9906F4D12170",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU015",
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


class AvailSEPrtcpntTmpltInvtryModel(BaseModel):
    """Payload class for AvailSE - Participant Template Inventory Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Participant Template Inventory"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.PRTCPNT_TMPLT_INVTRY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prtcpnt_tmplt_invtry"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
