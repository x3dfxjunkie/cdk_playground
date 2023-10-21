"""Source Data Contract Template for DREAMS Price - Entitlement Frequency Data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - enttl_frq_t Data"""

    enttl_frq_nm: str = Field(
        ...,
        alias="ENTTL_FRQ_NM",
        name="",
        description="",
        example="Per Meal Period",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceEnttlFrqTModel(BaseModel):
    """Payload class for DREAMSPriceEnttlFrqTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Type of Entitlement Frequency associated to the Method selected."""
        unique_identifier = ["data.ENTTL_FRQ_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ENTTL_FRQ_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
