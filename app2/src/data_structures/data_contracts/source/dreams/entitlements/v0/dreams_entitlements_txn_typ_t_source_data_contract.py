"""Source Data Contract for Dreams Entitlement Transaction Type"""


from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Transaction Type Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-07-13T18:51:47Z",
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

    txn_typ_cd: str = Field(
        ...,
        alias="TXN_TYP_CD",
        name="",
        description="",
        example="REC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_typ_nm: str = Field(
        ...,
        alias="TXN_TYP_NM",
        name="",
        description="",
        example="REC",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSEntitlementsTxnTypTModel(BaseModel):
    """Payload class for DREAMSEntitlementsTxnTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Type"
        stream_name = ""
        description = "An action that can be performed include the adjusting of folios, the recording of receipt of money and recording the receipt to folios, processing of charges against folios and the settling of charges and payments to folios. Valid values:  SALE, TRF, REV"
        unique_identifier = ["data.TXN_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TXN_TYP_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
