"""Source Data Contract Template for Dreams - Dining Travel Component Reason Type"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Dining Travel Component Reason Type Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-08-06T10:36:30Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ABCDEONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsn_typ_nm: str = Field(
        ...,
        alias="TC_RSN_TYP_NM",
        name="",
        description="",
        example="Change",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningTcRsnTypModel(BaseModel):
    """Payload class for Dreams - Dining Travel Component Reason Type Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Reason Type"
        stream_name = ""
        description = """The distinct list of Reason types: TC_RSN_TYP_NM A la Carte Cancel Cancel Change Complimentary Ticket Early Checkout Fee Waive Inventory Override Mass Cancel Rate Override Reinstate Ticket Reprint Upgrade"""
        unique_identifier = ["data.TC_RSN_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_rsn_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
