"""Source Data Contract Template for DREAMS Price - Entitlement Method Data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - enttl_meth_t Data"""

    enttl_meth_nm: str = Field(
        ...,
        alias="ENTTL_METH_NM",
        name="",
        description="",
        example="Per Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceEnttlMethTModel(BaseModel):
    """Payload class for DREAMSPriceEnttlMethTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = (
            """Entity listing all the possible entitlement types: These define how the entitlement is fulfilled."""
        )
        unique_identifier = ["data.ENTTL_METH_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "ENTTL_METH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
