"""Source Data Contract Template for DREAMS Price - Deliver Method Name Toggle"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - fflmt_dlvr_meth_t Data"""

    fflmt_dlvr_meth_nm: str = Field(
        ...,
        alias="FFLMT_DLVR_METH_NM",
        name="",
        description="",
        example="WDTC Voucher",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFflmtDlvrMethTModel(BaseModel):
    """Payload class for DREAMSPriceFflmtDlvrMethTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Describes how Disney will deliver product to the guest to satisfy the order of product."""
        unique_identifier = ["data.FFLMT_DLVR_METH_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FFLMT_DLVR_METH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
