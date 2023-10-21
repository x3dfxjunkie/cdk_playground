"""Source Data Contract Template for FEAT_PRICE"""


from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - FEAT_PRICE Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2007-08-06T05:46:42.856584Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=73592,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_price_am: int = Field(
        ...,
        alias="FEAT_PRICE_AM",
        name="",
        description="",
        example=155,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_price_id: int = Field(
        ...,
        alias="FEAT_PRICE_ID",
        name="",
        description="",
        example=1593779,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-10T14:58:46.221222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_def_id: Optional[str] = Field(
        None,
        alias="PRICE_DEF_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    price_sheet_elmnt_id: int = Field(
        ...,
        alias="PRICE_SHEET_ELMNT_ID",
        name="",
        description="",
        example=2742711,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2007-08-06T05:46:42.856584Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFeatPriceTModel(BaseModel):
    """Payload class for DREAMSPriceFeatPriceTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Feature Price"
        stream_name = ""
        description = "Features and Products associated to a price sheet"  # optional
        unique_identifier = ["data.FEAT_PRICE_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FEAT_PRICE_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
