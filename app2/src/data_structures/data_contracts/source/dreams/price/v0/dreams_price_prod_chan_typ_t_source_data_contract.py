"""Source Data Contract Template for DREAMS Price - Product Channel Type"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - prod_chan_typ_t Data"""

    prod_chan_typ_nm: str = Field(
        ...,
        alias="PROD_CHAN_TYP_NM",
        name="",
        description="",
        example="Sales Zone",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdChanTypTModel(BaseModel):
    """Payload class for DREAMSPriceProdChanTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """A classification of Product and Package Channels."""
        unique_identifier = ["data.PROD_CHAN_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PROD_CHAN_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
