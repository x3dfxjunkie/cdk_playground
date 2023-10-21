"""Source Data Contract Template for DREAMS Price - Policy Type"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - plcy_typ_t Data"""

    entrprs_plcy_typ_id: int = Field(
        ...,
        alias="ENTRPRS_PLCY_TYP_ID",
        name="",
        description="",
        example=152781,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plcy_typ_nm: str = Field(
        ...,
        alias="PLCY_TYP_NM",
        name="",
        description="",
        example="Required Remark",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prnt_plcy_typ_nm: Optional[str] = Field(
        None,
        alias="PRNT_PLCY_TYP_NM",
        name="",
        description="",
        example="Cast Member Procedure",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePlcyTypTModel(BaseModel):
    """Payload class for DREAMSPricePlcyTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """A low taxonomic category selected as a standard of reference for Policy."""
        unique_identifier = ["data.PLCY_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PLCY_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
