"""Source Data Contract Template for AvailSE - Physical Resource"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.availse.global_availse_source_data_contract import (
    GlobalAvailSEMetadata,
)


class Data(BaseModel):
    """Class Data Contract Template for AvailSE - Physical Resource Data"""

    phys_rsrc_hs_in: str = Field(
        ...,
        alias="PHYS_RSRC_HS_IN",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    phys_rsrc_id: str = Field(
        ...,
        alias="PHYS_RSRC_ID",
        name="",
        description="",
        example="AA11AA11-25FA-71F6-E053-BABD06991F38",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    phys_rsrc_id_vl: str = Field(
        ...,
        alias="PHYS_RSRC_ID_VL",
        name="",
        description="",
        example="36",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    phys_rsrc_prrty_nb: int = Field(
        ...,
        alias="PHYS_RSRC_PRRTY_NB",
        name="",
        description="",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    phys_rsrc_rgn_nb: int = Field(
        ...,
        alias="PHYS_RSRC_RGN_NB",
        name="",
        description="",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrvbl_rsrc_id: str = Field(
        ...,
        alias="RSRVBL_RSRC_ID",
        name="",
        description="",
        example="aa11aa11-aa10-439c-9dcf-7d65b6cb05f8",
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
        example=4718,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AvailSEPhysRsrcModel(BaseModel):
    """Payload class for AvailSE - Physical Resource Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Physical Resource"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.PHYS_RSRC_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "phys_rsrc"

    data: Data = Field(..., alias="data")
    metadata: GlobalAvailSEMetadata = Field(..., alias="metadata")
