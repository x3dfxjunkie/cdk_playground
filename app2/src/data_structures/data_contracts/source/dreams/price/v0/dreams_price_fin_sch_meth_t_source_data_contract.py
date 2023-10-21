"""Source Data Contract Template for DREAMS Pricing Finance Schedule Method data"""


from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - FIN_SCH_METH_T"""

    sch_meth_nm: str = Field(
        ...,
        alias="SCH_METH_NM",
        name="",
        description="",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFinSchMethTModel(BaseModel):
    """Payload class for DREAMSPriceFinSchMethTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Finance Schedule Method"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.SCH_METH_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FIN_SCH_METH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
