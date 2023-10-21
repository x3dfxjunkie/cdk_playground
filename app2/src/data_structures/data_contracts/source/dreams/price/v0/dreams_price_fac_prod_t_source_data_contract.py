"""Source Data Contract Template for FAC_PROD"""


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - FAC_PROD Data"""

    chk_in_loc_tx: Optional[str] = Field(
        None,
        alias="CHK_IN_LOC_TX",
        name="",
        description="",
        example="Disney's VIP Tour Experience Check-In Location will be at The Plaza Restaurant inside the Magic Kingdom  Proceed to the end of Main Street USA, turn right and The Plaza Restaurant is on the right side",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=90002464,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_prod_end_dt: Optional[datetime] = Field(
        None,
        alias="FAC_PROD_END_DT",
        name="",
        description="",
        example="2021-01-31T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_prod_strt_dt: Optional[datetime] = Field(
        None,
        alias="FAC_PROD_STRT_DT",
        name="",
        description="",
        example="2009-03-09T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_prod_typ_nm: str = Field(
        ...,
        alias="FAC_PROD_TYP_NM",
        name="",
        description="",
        example="Meal Period Location",
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

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=54176,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFacProdTModel(BaseModel):
    """Payload class for DREAMSPriceFacProdTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Facility Product"
        stream_name = ""
        description = "Associates products to enterprise facility IDs"  # optional
        unique_identifier = ["data.PROD_ID", "data.FAC_PROD_TYP_NM", "data.FAC_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FAC_PROD_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
