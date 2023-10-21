"""Source Data Contract for DREAMS Accounting SAP Profit Center"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Accounting SAP Profit Center Data"""

    sap_prft_ctr_cd: str = Field(
        ...,
        alias="SAP_PRFT_CTR_CD",
        name="",
        description="",
        example="0001147586",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sap_prft_ctr_nm: str = Field(
        ...,
        alias="SAP_PRFT_CTR_NM",
        name="",
        description="",
        example="0001147586",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="SAP_Load",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-16T00:04:44.057035Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSAccountingSapPrftCtrModel(BaseModel):
    """Payload class for DREAMSAccountingSapPrftCtrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Accounting SAP Profit Center"
        stream_name = ""
        description = "SAP Profit Center Names associated to SAP Profit Center Codes"  # optional
        unique_identifier = ["data.SAP_PRFT_CTR_CD"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "sap_prft_ctr"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
