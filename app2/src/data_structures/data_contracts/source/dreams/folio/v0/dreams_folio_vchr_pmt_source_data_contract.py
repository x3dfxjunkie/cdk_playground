"""Source Data Contract for Dreams Folio Voucher Payment"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Voucher Payment Data"""

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281187544,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    vchr_id_val: Optional[str] = Field(
        None,
        alias="VCHR_ID_VAL",
        name="",
        description="",
        example="wdw76dsa",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="BURKT013",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-12T15:24:34.983000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-06-08T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioVchrPmtModel(BaseModel):
    """Payload class for DREAMSFolioVchrPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Voucher Payment"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.PMT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "VCHR_PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
