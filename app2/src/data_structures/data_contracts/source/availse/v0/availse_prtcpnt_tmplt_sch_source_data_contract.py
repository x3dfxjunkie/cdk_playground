"""Source Data Contract Template for AvailSE - Participant Template Schedule"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Participant Template Schedule Data"""

    entrprs_fac_id: int = Field(
        ...,
        alias="ENTRPRS_FAC_ID",
        name="",
        description="",
        example=19124370,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_id: str = Field(
        ...,
        alias="PRTCPNT_TMPLT_ID",
        name="",
        description="",
        example="aa11aa11-6d5c-35c8-8bc6-3fab6b22f730",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_sch_id: str = Field(
        ...,
        alias="PRTCPNT_TMPLT_SCH_ID",
        name="",
        description="",
        example="aa11aa11-0d94-62e3-09bb-f517eab5ac4f",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prtcpnt_tmplt_sch_strt_dt: datetime = Field(
        ...,
        alias="PRTCPNT_TMPLT_SCH_STRT_DT",
        name="",
        description="",
        example="2023-07-29T00:00:00Z",
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


class AvailSEPrtcpntTmpltSchModel(BaseModel):
    """Payload class for AvailSE - Participant Template Schedule Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Participant Template Schedule"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.PRTCPNT_TMPLT_SCH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prtcpnt_tmplt_sch"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
