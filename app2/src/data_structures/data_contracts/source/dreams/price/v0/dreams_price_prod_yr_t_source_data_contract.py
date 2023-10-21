"""Source Data Contract Template for DREAMS Price - Product Year data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - prod_yr_t Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2021-05-26T17:20:33.484842Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_prod_yr_id: int = Field(
        ...,
        alias="ENTRPRS_PROD_YR_ID",
        name="",
        description="",
        example=19625434,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_yr_end_dt: datetime = Field(
        ...,
        alias="PROD_YR_END_DT",
        name="",
        description="",
        example="2048-04-30T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_yr_nb: int = Field(
        ...,
        alias="PROD_YR_NB",
        name="",
        description="",
        example=2047,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_yr_nm: str = Field(
        ...,
        alias="PROD_YR_NM",
        name="",
        description="",
        example="Product Year 2047",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_yr_strt_dt: datetime = Field(
        ...,
        alias="PROD_YR_STRT_DT",
        name="",
        description="",
        example="2047-01-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2021-05-26T17:20:33.484842Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceProdYrTModel(BaseModel):
    """Payload class for DREAMSPriceProdYrTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """A copy of the One Source materialized look at the dates for a contract.  Matches the year established for the product line.  Example:  2006."""
        unique_identifier = ["data.PROD_YR_NB"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "PROD_YR_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
