"""Source Data Contract Template for AvailSE - Production Servable Resource Xref"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Production Servable Resource Xref Data"""

    prd_rsrvbl_rsrc_xref_strt_dts: Optional[datetime] = Field(
        None,
        alias="PRD_RSRVBL_RSRC_XREF_STRT_DTS",
        name="",
        description="",
        example="2014-08-26T04:30:43Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=4710394,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_rsrvbl_rsrc_xref_id: str = Field(
        ...,
        alias="PROD_RSRVBL_RSRC_XREF_ID",
        name="",
        description="",
        example="aa11aa11-e891-4ab1-a455-5a6ccc72b08c",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-1535-40da-917a-feaa2a010a7c",
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


class AvailSEProdRsrvblRsrcXrefModel(BaseModel):
    """Payload class for AvailSE - Production Servable Resource Xref Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Production Reservable Resource Xref"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.PROD_RSRVBL_RSRC_XREF_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "prod_rsrvbl_rsrc_xref"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
