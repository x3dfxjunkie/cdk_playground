"""Source Data Contract for Dreams Entitlement Transaction Reason Type"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Transaction Reason Type Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T15:46:49.094168Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Initial Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_rsn_typ_nm: str = Field(
        ...,
        alias="TXN_RSN_TYP_NM",
        name="",
        description="",
        example="CHARGE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsTxnRsnTypTModel(BaseModel):
    """Payload class for DREAMSEntitlementsTxnRsnTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Reason Type"
        stream_name = ""
        description = "The grouping of rationales by similar characteristics or functionality.  The rationales that explain or describe the transactions that are processed within Folio Management"
        unique_identifier = ["data.TXN_RSN_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TXN_RSN_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
