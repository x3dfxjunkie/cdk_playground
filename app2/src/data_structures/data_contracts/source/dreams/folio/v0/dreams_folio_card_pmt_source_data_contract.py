"""Source Data Contract Template for CARD_PMT.json"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """data for CARD_PMT"""

    pmt_id: int = Field(
        ...,
        alias="PMT_ID",
        name="",
        description="",
        example=281086363,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pmt_card_id: int = Field(
        ...,
        alias="PMT_CARD_ID",
        name="",
        description="",
        example=264020002,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO1",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T15:00:29.072000Z",
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


class DREAMSFolioCardPmtModel(BaseModel):
    """Payload class for DREAMSFolioCardPmtModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Card Payment"
        stream_name = ""
        description = ""  # optional
        unique_identifier = ["data.PMT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Confidential"  # optional
        financial_data = True  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CARD_PMT"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
