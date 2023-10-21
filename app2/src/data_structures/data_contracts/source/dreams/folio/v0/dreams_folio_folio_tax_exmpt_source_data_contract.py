"""Source Data Contract Template for FOLIO_TAX_EXMPT.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for FOLIO_TAX_EXMPT"""

    tax_exmpt_id: int = Field(
        ...,
        alias="TAX_EXMPT_ID",
        name="",
        description="",
        example=57927193,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_exmpt_typ_nm: str = Field(
        ...,
        alias="TAX_EXMPT_TYP_NM",
        name="",
        description="",
        example="RSR Non-Taxable",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_exmpt_cert_nb_val: str = Field(
        ...,
        alias="TAX_EXMPT_CERT_NB_VAL",
        name="",
        description="",
        example="RSR Non-Taxable",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="RoomingLst",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-12T16:28:49.404000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioFolioTaxExmptModel(BaseModel):
    """Payload class for DREAMSFolioFolioTaxExmptModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Folio Tax Exempt"
        stream_name = ""
        description = "This table ties the Tax Exempt ID to the Tax Exempt Certification number value"  # optional
        unique_identifier = ["data.TAX_EXMPT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FOLIO_TAX_EXMPT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
