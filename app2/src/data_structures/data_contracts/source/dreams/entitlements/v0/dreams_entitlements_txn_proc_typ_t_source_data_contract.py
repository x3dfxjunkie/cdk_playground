"""Source Data Contract for Dreams Entitlement Transaction Process Type"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Transaction Process Type Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-07-13T18:51:52Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_proc_typ_nm: str = Field(
        ...,
        alias="TXN_PROC_TYP_NM",
        name="",
        description="",
        example="Created",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsTxnProcTypTModel(BaseModel):
    """Payload class for DREAMSEntitlementsTxnProcTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Process Type"
        stream_name = ""
        description = "Identifies how the COUPON TRANSACTION impacts a transaction item (either a charge or a payment).    Valid values:  Created, TransferFrom, TransferTo"
        unique_identifier = ["data.TXN_PROC_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TXN_PROC_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
