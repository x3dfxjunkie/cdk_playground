"""Source Data Contract Template for FEE_CHRG.json"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Data in FEE_CHRG table"""

    fee_chrg_id: int = Field(
        ...,
        alias="FEE_CHRG_ID",
        name="",
        description="",
        example=3408295197,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fee_nm: str = Field(
        ...,
        alias="FEE_NM",
        name="",
        description="",
        example="Cancellation Fee",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="IVRNuance",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T10:40:42.176000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pkg_id: Optional[int] = Field(
        None,
        alias="PKG_ID",
        name="",
        description="",
        example=149855,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_id: Optional[int] = Field(
        None,
        alias="PROD_ID",
        name="",
        description="",
        example=53905,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioFeeChrgModel(BaseModel):
    """Payload class for DREAMSFolioFeeChrgModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Fee Charge"
        stream_name = ""
        description = (
            """Charge IDs that are only associated to a Fee, usually for cancellation of a reservation"""  # optional
        )
        unique_identifier = ["data.FEE_CHRG_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FEE_CHRG"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
