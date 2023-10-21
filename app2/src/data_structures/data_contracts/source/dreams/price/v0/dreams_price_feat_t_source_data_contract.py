"""Source Data Contract Template for FEAT"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - Feat Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2016-07-21T09:45:22.227277Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_ds: str = Field(
        ...,
        alias="FEAT_DS",
        name="",
        description="",
        example="4 Day Park Hopper & Water Park Fun & More Timeshare Tour Ticket",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_frq_nm: str = Field(
        ...,
        alias="FEAT_FRQ_NM",
        name="",
        description="",
        example="Day",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_id: int = Field(
        ...,
        alias="FEAT_ID",
        name="",
        description="",
        example=18458782,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_nm: str = Field(
        ...,
        alias="FEAT_NM",
        name="",
        description="",
        example="Main",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feat_typ_nm: Optional[str] = Field(
        None,
        alias="FEAT_TYP_NM",
        name="",
        description="",
        example="Icing",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2016-07-21T09:45:22.227277Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFeatTModel(BaseModel):
    """Payload class for DREAMSPriceFeatTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Feature"
        stream_name = ""
        description = "List of features: Sales Tax - Beaufort County (SC) - Merchandise, Communications Tax - Beaufort County (SC), Adjust for Discount, Sales Tax - Beaufort County (SC) - Food, Osceola County Accommodation Tax, Osceola County Tourist Development Tax, Indian River"  # optional
        unique_identifier = ["data.FEAT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FEAT_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
