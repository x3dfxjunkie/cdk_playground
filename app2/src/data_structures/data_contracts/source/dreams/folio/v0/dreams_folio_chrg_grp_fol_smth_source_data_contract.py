"""Source Data Contract Template for CHRG_GRP_FOL_SMTH.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data for CHRG_GRP_FOL_SMTH"""

    chrg_grp_folio_id: int = Field(
        ...,
        alias="CHRG_GRP_FOLIO_ID",
        name="",
        description="",
        example=276602936,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    settl_meth_id: int = Field(
        ...,
        alias="SETTL_METH_ID",
        name="",
        description="",
        example=427365914,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioChrgGrpFolSmthModel(BaseModel):
    """Payload class for DREAMSFolioChrgGrpFolSmthModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Group Folio Settlement Method"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.CHRG_GRP_FOLIO_ID", "data.SETTL_METH_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CHRG_GRP_FOL_SMTH"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
