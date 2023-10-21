"""Source Data Contract Template for DREAMS Price - Ticket Price Grid Site data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - TKT_PRICE_GRID_SITE_T Data"""

    tkt_price_grid_id: int = Field(
        ...,
        alias="TKT_PRICE_GRID_ID",
        name="",
        description="",
        example=289171,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tkt_price_grid_site_nm: str = Field(
        ...,
        alias="TKT_PRICE_GRID_SITE_NM",
        name="",
        description="",
        example="LILO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTktPriceGridSiteTModel(BaseModel):
    """Payload class for DREAMSPriceTktPriceGridSiteTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """This captures either a client (UI) or application that is a consumer of the ticket price grids.  This was added during LILO Project to filter only those ticket price grids sent to their UI (for Ticket Recommender).  """
        unique_identifier = ["data.TKT_PRICE_GRID_SITE_NM", "data.TKT_PRICE_GRID_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TKT_PRICE_GRID_SITE_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
