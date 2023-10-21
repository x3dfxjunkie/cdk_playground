"""Source Data Contract for DREAMS Accounting SAP Account"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Accounting SAP Account Data"""

    sap_gl_acct_nm: str = Field(
        ...,
        alias="SAP_GL_ACCT_NM",
        name="",
        description="",
        example="Per Diem",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_gl_acct_nb: str = Field(
        ...,
        alias="SAP_GL_ACCT_NB",
        name="",
        description="",
        example="0000620150",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="SAP Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-18T15:47:52Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapAcctModel(BaseModel):
    """Payload class for DREAMSAccountingSapAcctModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Accounting SAP Account"
        stream_name = ""
        description = "SAP General Ledger Account names associated to SAP General Ledger Account Numbers"  # optional
        unique_identifier = ["data.SAP_GL_ACCT_NB"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "sap_acct"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
