"""Source Data Contract for DREAMS SAP Distribution Channel"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams SAP Distribution Channel Data"""

    sap_dstr_chan_nm: str = Field(
        ...,
        alias="SAP_DSTR_CHAN_NM",
        name="",
        description="",
        example="Retail Consumer",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_dstr_chan_cd: str = Field(
        ...,
        alias="SAP_DSTR_CHAN_CD",
        name="",
        description="",
        example="10",
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
        example="2006-10-18T19:46:43.648Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapDstrChanModel(BaseModel):
    """Payload class for DREAMSAccountingSapDstrChanModel"""

    class Config:
        """Payload Level Metadata"""

        title = "SAP Distribution Channel"
        stream_name = ""
        description = """SAP Distribution Channel names associated to Distribution Codes"""
        unique_identifier = ["data.SAP_DSTR_CHAN_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SAP_DSTR_CHAN"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
