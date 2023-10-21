"""Source Data Contract Template for DREAMS Folio Tax Exempt type"""


from __future__ import annotations
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Folio Tax Exempt type Data"""

    tax_exmpt_typ_nm: str = Field(
        ...,
        alias="TAX_EXMPT_TYP_NM",
        name="",
        description="",
        example="DIPLOMATS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="PMSRAPPID",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-04-08T22:44:21.000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioTaxExmptTypModel(BaseModel):
    """Payload class for DREAMSFolioTaxExmptTypModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Tax Exempt type"
        stream_name = ""
        description = """Domain table for the types of organizations that are exempt from paying tax"""
        unique_identifier = ["data.TAX_EXMPT_TYP_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Confidential"
        financial_data = "TRUE"
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TAX_EXMPT_TYP"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
