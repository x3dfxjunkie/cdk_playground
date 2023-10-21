"""Source Data Contract Template for AvailSE - Reservable Resource"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Reservable Resource Data"""

    entrprs_fac_id: int = Field(
        ...,
        alias="ENTRPRS_FAC_ID",
        name="",
        description="",
        example=90001833,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_typ_nm: str = Field(
        ...,
        alias="RSRC_TYP_NM",
        name="",
        description="",
        example="Table",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_end_dts: Optional[datetime] = Field(
        None,
        alias="RSRVBL_RSRC_END_DTS",
        name="",
        description="",
        example="2023-09-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-ccbf-40e1-bd87-4653ffee611b",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_strt_dts: datetime = Field(
        ...,
        alias="RSRVBL_RSRC_STRT_DTS",
        name="",
        description="",
        example="2008-12-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_typ_nm: str = Field(
        ...,
        alias="RSRVBL_RSRC_TYP_NM",
        name="",
        description="",
        example="FixDineNonYieldLastSinglePeriodAuthSameResource",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_uom_id: Optional[str] = Field(
        None,
        alias="RSRVBL_RSRC_UOM_ID",
        name="",
        description="",
        example="aa11aa11-ac89-4658-9754-c57cc37344ba",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_adt_vl: str = Field(
        ...,
        alias="UPDT_ADT_VL",
        name="",
        description="",
        example="Fakeu015",
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
        example=17,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSERsrvblRsrcModel(BaseModel):
    """Payload class for AvailSE - Reservable Resource Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Reservable Resource"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.RSRVBL_RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrvbl_rsrc"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
