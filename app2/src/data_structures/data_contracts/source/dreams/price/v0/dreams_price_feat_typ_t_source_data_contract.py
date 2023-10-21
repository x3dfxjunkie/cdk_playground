"""Source Data Contract Template for DREAMS Pricing Feature Type"""


from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - Feature Type Data"""

    feat_typ_nm: str = Field(
        ...,
        alias="FEAT_TYP_NM",
        name="",
        description="",
        example="Serving Size",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFeatTypTModel(BaseModel):
    """Payload class for DREAMSPriceFeatTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Feature Type"
        stream_name = ""
        description = """A more general classification of the details or characteristics of products.  For example, Kosher Products will have Appetizer, Entree and Dessert categories.  Cakes may have Flavor, Frosting, Size categories."""
        unique_identifier = ["data.FEAT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FEAT_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
