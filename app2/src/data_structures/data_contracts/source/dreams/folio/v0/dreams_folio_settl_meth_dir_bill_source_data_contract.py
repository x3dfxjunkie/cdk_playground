"""Source Data Contract Template for DREAMS Folio Settlement Method Direct Billing"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Settlement Method Direct Billing Data"""

    settl_meth_id: int = Field(
        ...,
        alias="SETTL_METH_ID",
        name="",
        description="",
        example=6807,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    bank_acct_ctr_id: Optional[int] = Field(
        None,
        alias="BANK_ACCT_CTR_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_cust_nb: Optional[str] = Field(
        None,
        alias="SAP_CUST_NB",
        name="",
        description="",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="UNKNOWN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2008-12-05T09:00:12.180Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2008-12-05T08:48:59.915Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioSettlMethDirBillModel(BaseModel):
    """Payload class for DREAMSFolioSettlMethDirBillModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Settlement Method Direct Billing"
        stream_name = ""
        description = """This table contains the settlement method that is to Directly Bill the guest/Organization"""
        unique_identifier = ["data.SETTL_METH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SETTL_METH_DIR_BILL"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
