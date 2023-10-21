"""Source Data Contract Template for DREAMS Opportunity Type"""


from __future__ import annotations
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Opportunity Type Data"""

    opty_typ_nm: str = Field(
        ...,
        alias="OPTY_TYP_NM",
        name="",
        description="",
        example="Content Group",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="ADMINUID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2007-04-26 04:27:47",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSGroupManagementOptyTypModel(BaseModel):
    """Payload class for DREAMSGroupManagementOptyTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Opportunity Type"
        stream_name = ""
        description = "Domain"
        unique_identifier = ["data.OPTY_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "opty_typ"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
