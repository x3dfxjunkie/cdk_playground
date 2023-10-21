"""Source Data Contract Template for DREAMS Delivery Method"""


from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Delivery Method Data"""

    dlvr_meth_nm: str = Field(
        ...,
        alias="DLVR_METH_NM",
        name="",
        description="",
        example="Print",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementDlvrMethModel(BaseModel):
    """Payload class for DREAMSGroupManagementDlvrMethModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Delivery Method"
        stream_name = ""
        description = "Domain"
        unique_identifier = ["data.DLVR_METH_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "dlvr_meth"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
