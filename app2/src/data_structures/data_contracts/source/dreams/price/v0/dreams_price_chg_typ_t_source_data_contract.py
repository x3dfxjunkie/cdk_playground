"""Source Data Contract Template for CHG_TYP"""


from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - CHG_TYP Data"""

    chg_typ_nm: str = Field(
        ...,
        alias="CHG_TYP_NM",
        name="",
        description="",
        example="Additional Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prnt_chg_typ_nm: Optional[str] = Field(
        None,
        alias="PRNT_CHG_TYP_NM",
        name="",
        description="",
        example="Additional Adult",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chg_typ_lvl_nb: int = Field(
        ...,
        alias="CHG_TYP_LVL_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceChgTypTModel(BaseModel):
    """Payload class for DREAMSPriceChgTypTModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Charge Type"
        stream_name = ""
        description = "List of charge types: Sales Tax - Beaufort County (SC) - Merchandise, Communications Tax - Beaufort County (SC), Adjust for Discount, Sales Tax - Beaufort County (SC) - Food, Osceola County Accommodation Tax, Osceola County Tourist Development Tax, Indian River FL Tourist Development Tax, Anaheim Room Occupancy Tax, ATID Assessment, Indian River County Accommodation Tax, Accommodations Tax - Hawaii State, Orange County Tourist Development Tax, Orange County Sales Tax, Indian River County Sales Tax, South Carolina State Accommodation Tax, Sales Tax - Beaufort County (SC) - Liquor, Orange County California Sales Tax, Osceola County Sales Tax, Transportation Tax - Beaufort County (SC), Base, Sales Tax - Beaufort County (SC), Brevard County Sales Tax, Accommodations Tax - Honolulu County (HI), Reverse Original, Sales Tax - South Carolina State (not rooms), Cross County Tax Adjustment, Hilton Head City Accommodation Tax, Osceola County Sales Tax, Additional Adult, Orange County Accommodation Tax, Indian River Tourist Development Tax, Communications Tax - Osceola County (FL), California State Sales Tax, Deposit Requirement, General Excise Tax - Hawaii State, Communications Tax - Orange County (FL), Florida State Accommodations Tax, Tax, Discount, South Carolina State Sales Tax, Communications Tax - Indian River County (FL), City of Anaheim Sales Tax"  # optional
        unique_identifier = ["data.CHG_TYP_NM"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "CHG_TYP_T"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
