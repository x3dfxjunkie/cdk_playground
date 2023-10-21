"""Source Data Contract for Dreams Folio Settlement Method Card"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Folio Dreams Folio Settlement Method Card Data"""

    settl_meth_id: int = Field(
        ...,
        alias="SETTL_METH_ID",
        name="",
        description="",
        example=427415667,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_id: int = Field(
        ...,
        alias="PMT_CARD_ID",
        name="",
        description="",
        example=264069231,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-24T09:25:51Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-05-24T09:25:51Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSFolioSettlMethCardModel(BaseModel):
    """Payload class for DREAMSFolioSettlMethCardModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Settlement Method Card"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.SETTL_METH_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SETTL_METH_CARD"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
