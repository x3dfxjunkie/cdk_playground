"""Source Data Contract Template for DREAMS Folio Check Payment"""


from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Check Payment"""

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=31,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chk_orig_nm: Optional[str] = Field(
        None,
        alias="CHK_ORIG_NM",
        name="",
        description="",
        example="The School District of Gadsden Count",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chk_nb_val: str = Field(
        ...,
        alias="CHK_NB_VAL",
        name="",
        description="",
        example="140965",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    auth_nb: Optional[str] = Field(
        None,
        alias="AUTH_NB",
        name="",
        description="",
        example="1234",
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
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2006-10-22T05:52:02.906Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2006-10-27T14:22:29.706Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioChkPmtModel(BaseModel):
    """Payload class for DREAMSFolioChkPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Check Payment"
        stream_name = ""
        description = """Payments that are made exclusively with Checks"""
        unique_identifier = ["data.PMT_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CHK_PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
