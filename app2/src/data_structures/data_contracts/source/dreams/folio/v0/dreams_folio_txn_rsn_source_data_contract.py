"""Source Data Contract Template for DREAMS Folio Transaction Reason"""


from __future__ import annotations
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Transaction Reason Data"""

    txn_rsn_cd: str = Field(
        ...,
        alias="TXN_RSN_CD",
        name="",
        description="",
        example="ADDL_CHG",
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
    txn_rsn_nm: str = Field(
        ...,
        alias="TXN_RSN_NM",
        name="",
        description="",
        example="Additional Charge",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rsn_dspl_seq_nb: int = Field(
        ...,
        alias="RSN_DSPL_SEQ_NB",
        name="",
        description="",
        example=1,
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
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T19:46:49.172Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="ADMINUID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2007-04-26T08:27:30.971Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioTxnRsnModel(BaseModel):
    """Payload class for DREAMSFolioTxnRsnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Reason"
        stream_name = ""
        description = """This table associates a transaction reason type and transaction reason name to a transaction reason code"""
        unique_identifier = ["data.TXN_RSN_CD"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TXN_RSN"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
