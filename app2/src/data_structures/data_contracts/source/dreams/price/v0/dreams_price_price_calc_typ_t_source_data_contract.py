"""Source Data Contract Template for DREAMS Pricing Price Schedule Type data"""


from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - PRICE_CALC_TYP_T"""

    price_calc_typ_nm: str = Field(
        ...,
        alias="PRICE_CALC_TYP_NM",
        name="",
        description="",
        example="Package Calculator",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePriceCalcTypTModel(BaseModel):
    """Payload class for DREAMSPricePriceCalcTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Price Calculator Type"
        stream_name = ""
        description = """A category of method, which is used to determine how to price a product in a particular revenue classification."""
        unique_identifier = ["data.PRICE_CALC_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PRICE_CALC_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
