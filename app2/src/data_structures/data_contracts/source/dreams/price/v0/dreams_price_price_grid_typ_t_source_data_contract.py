"""Source Data Contract Template for DREAMS Price - Price Grid Type"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - price_grid_typ_t Data"""

    price_grid_typ_nm: str = Field(
        ...,
        alias="PRICE_GRID_TYP_NM",
        name="",
        description="",
        example="Room",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePriceGridTypTModel(BaseModel):
    """Payload class for DREAMSPricePriceGridTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Added for LILO, these values will classify a Price Grid into either a Room Price Grid or a Ticket Price Grid."""
        unique_identifier = ["data.PRICE_GRID_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PRICE_GRID_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
