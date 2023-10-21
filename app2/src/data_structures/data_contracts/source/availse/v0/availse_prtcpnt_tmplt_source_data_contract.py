"""Source Data Contract Template for AvailSE - Participant Template"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Participant Template Data"""

    dy_tm: Optional[str] = Field(
        None,
        alias="DY_TM",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_fac_id: int = Field(
        ...,
        alias="ENTRPRS_FAC_ID",
        name="",
        description="",
        example=90001879,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_auth_cn: Optional[str] = Field(
        None,
        alias="PRTCPNT_TMPLT_AUTH_CN",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_id: str = Field(
        ...,
        alias="PRTCPNT_TMPLT_ID",
        name="",
        description="",
        example="aa11aa11-554e-49a9-adf8-71579a1a2cff",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_invtry_id: Optional[str] = Field(
        None,
        alias="PRTCPNT_TMPLT_INVTRY_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_nm: str = Field(
        ...,
        alias="PRTCPNT_TMPLT_NM",
        name="",
        description="",
        example="Standard",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_strt_dt: datetime = Field(
        ...,
        alias="PRTCPNT_TMPLT_STRT_DT",
        name="",
        description="",
        example="2021-07-07T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: Optional[str] = Field(
        None,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="FAKEU001",
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
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSEPrtcpntTmpltModel(BaseModel):
    """Payload class for AvailSE - Participant Template Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Participant Template"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.PRTCPNT_TMPLT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prtcpnt_tmplt"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
