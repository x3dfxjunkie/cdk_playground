"""Source Data Contract Template for DREAMS Price - Category"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field

from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - CTGY_T Data"""

    ctgy_id: int = Field(
        ...,
        alias="CTGY_ID",
        name="",
        description="",
        example=80000439,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ctgy_inactv_in: int = Field(
        ...,
        alias="CTGY_INACTV_IN",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ctgy_typ_lvl_nb: int = Field(
        ...,
        alias="CTGY_TYP_LVL_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ctgy_typ_nm: str = Field(
        ...,
        alias="CTGY_TYP_NM",
        name="",
        description="",
        example="Tax Jurisdiction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    eng_ctgy_nm: str = Field(
        ...,
        alias="ENG_CTGY_NM",
        name="",
        description="",
        example="Osceola County, Florida",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prnt_ctgy_id: Optional[int] = Field(
        None,
        alias="PRNT_CTGY_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceCtgyTModel(BaseModel):
    """Payload class for DREAMSPriceCtgyTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """The taxing authority to which Disney pays appropriate taxes due to having a facility within the area covered by that taxing authority."""
        unique_identifier = ["data.CTGY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "CTGY_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
