"""Source Data Contract for DREAMS Product Link"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Product Link Data"""

    entrprs_meal_prd_id: Optional[int] = Field(
        None,
        alias="ENTRPRS_MEAL_PRD_ID",
        name="",
        description="",
        example=296027,
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

    prmy_prod_id: int = Field(
        ...,
        alias="PRMY_PROD_ID",
        name="",
        description="",
        example=54000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_lnk_end_dt: Optional[datetime] = Field(
        None,
        alias="PROD_LNK_END_DT",
        name="",
        description="",
        example="2011-12-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_lnk_id: int = Field(
        ...,
        alias="PROD_LNK_ID",
        name="",
        description="",
        example=914035,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_lnk_strt_dt: datetime = Field(
        ...,
        alias="PROD_LNK_STRT_DT",
        name="",
        description="",
        example="2011-11-25T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_lnk_typ_nm: str = Field(
        ...,
        alias="PROD_LNK_TYP_NM",
        name="",
        description="",
        example="Redeemable",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sec_prod_id: Optional[int] = Field(
        None,
        alias="SEC_PROD_ID",
        name="",
        description="",
        example=94835,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdLnkTModel(BaseModel):
    """Payload class for DREAMSPriceProdLnkTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Product Link"
        stream_name = ""
        description = "Table that links together parent and child products"  # optional
        unique_identifier = ["data.PROD_LNK_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "PROD_LNK_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
