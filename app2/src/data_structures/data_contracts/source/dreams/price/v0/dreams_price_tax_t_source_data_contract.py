"""Source Data Contract Template for DREAMS Pricing Tax"""


from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - TAX_T Data"""

    tax_ds: str = Field(
        ...,
        alias="TAX_DS",
        name="",
        description="",
        example="South Carolina State Sales Tax",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_end_dt: datetime = Field(
        ...,
        alias="TAX_END_DT",
        name="",
        description="",
        example="2030-12-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_id: int = Field(
        ...,
        alias="TAX_ID",
        name="",
        description="",
        example=80007081,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_pct_in: int = Field(
        ...,
        alias="TAX_PCT_IN",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_rt_fee_am: Optional[int] = Field(
        None,
        alias="TAX_RT_FEE_AM",
        name="",
        description="",
        example=15,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_rt_pc: float = Field(
        ...,
        alias="TAX_RT_PC",
        name="",
        description="",
        example=5.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_strt_dt: datetime = Field(
        ...,
        alias="TAX_STRT_DT",
        name="",
        description="",
        example="2007-05-01T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tax_typ_id: int = Field(
        ...,
        alias="TAX_TYP_ID",
        name="",
        description="",
        example=80007072,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceTaxTModel(BaseModel):
    """Payload class for DREAMSPriceTaxTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Tax"
        stream_name = ""
        description = """The detail of a specific tax by percent or by amount that can be attached to a product.  A Tax Type  can be the composite of many Tax Detail instances."""
        unique_identifier = ["data.TAX_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "TAX_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
