"""Source Data Contract Template for DREAMS Price - Policy Marketing Message"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - plcy_mkt_msg_t Data"""

    mkt_msg_id: int = Field(
        ...,
        alias="MKT_MSG_ID",
        name="",
        description="",
        example=627,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=326373,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPricePlcyMktMsgTModel(BaseModel):
    """Payload class for DREAMSPricePlcyMktMsgTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Associates a set of messages to a policy.  Note the messages are cited for different consumers such as Portal or DRC."""
        unique_identifier = ["data.PLCY_ID", "data.MKT_MSG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PLCY_MKT_MSG_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
