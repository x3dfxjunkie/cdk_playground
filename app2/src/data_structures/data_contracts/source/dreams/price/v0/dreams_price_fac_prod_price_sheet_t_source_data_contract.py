"""Source Data Contract Template for FAC_PROD_PRICE_SHEET"""


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    fac_prod_price_sheet_id: float = Field(
        ...,
        alias="FAC_PROD_PRICE_SHEET_ID",
        name="",
        description="",
        example=6268975.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tax_grp_id: float = Field(
        ...,
        alias="TAX_GRP_ID",
        name="",
        description="",
        example=4325.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_id: float = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=109134.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_prod_typ_nm: str = Field(
        ...,
        alias="FAC_PROD_TYP_NM",
        name="",
        description="",
        example="AccountingFacility",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_id: float = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=80010405.0,
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


class DREAMSPriceFacProdPriceSheetTModel(BaseModel):
    """Payload class for DREAMSPriceFacProdPriceSheetTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Facility Product Price Sheet"
        stream_name = ""
        description = "Associates a Price Sheet to Products by Facility - Resort specific products: WDW Rollaway Bed Rental, Self Parking Fees at Aulani (Hawaii), Refrigerator, Pet Fee, Internet- Wireless Internet Access (WiFi), Internet - High Speed Internet Access (HSIA), Hawaii Accom Tax-V6-Hotel Room-Standard, Hawaii Accom Tax-Honolulu County (HI)-V6-Hotel Room-Standard, DVC Member Towel Package, DVC Member Shampoo and Conditioner, DVC Member Laundry Detergent, DVC Member Coffee Package, DVC Member - Room Change Service, DVC Housekeeping - Trash and Towel Service, DVC Housekeeping - Full Cleaning Service, Areobed Rental - Aulani, Aerobed Rental - WDW, Aerobed Rental - Vero Beach, Aerobed Rental - Hilton Head, Accommodations Tax DVC - Honolulu County (HI)- 6S - Deluxe Studio - Poolside Gardens View, Accommodations Tax DVC - Honolulu County (HI) - 6A - Deluxe Studio - Ocean View, Accommodations Tax DVC - Hawaii State - 6S - Deluxe Studio - Poolside Gardens View, Accommodation Tax DVC - Honolulu County (HI)- 6Y - Dedicated Two Bedroom Villa - Standard View, Accommodation Tax DVC - Honolulu County (HI)- 6W - Deluxe Studio - Standard View, Accommodation Tax DVC - Honolulu County (HI)- 6V - Grand Villa - Stand"  # optional
        unique_identifier = ["data.FAC_PROD_PRICE_SHEET_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "FAC_PROD_PRICE_SHEET_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
