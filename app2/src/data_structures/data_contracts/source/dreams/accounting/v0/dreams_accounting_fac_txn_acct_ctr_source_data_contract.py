"""Source Data Contract for Dreams Facility Transaction Account Center"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data Class for Dreams Facility Transaction Account Center"""

    dflt_txn_acct_ctr_id: int = Field(
        ...,
        alias="DFLT_TXN_ACCT_CTR_ID",
        name="",
        description="",
        example=1412,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=221626,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingFacTxnAcctCtrModel(BaseModel):
    """Payload class for Dreams Facility Transaction Account Center"""

    class Config:
        """Payload Level Metadata"""

        title = "Facility Transaction Account Center"
        stream_name = ""
        description = """Ties the Facility to the Default Transaction Account Center ID"""
        unique_identifier = ["data.FAC_ID", "data.DFLT_TXN_ACCT_CTR_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FAC_TXN_ACCT_CTR"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
