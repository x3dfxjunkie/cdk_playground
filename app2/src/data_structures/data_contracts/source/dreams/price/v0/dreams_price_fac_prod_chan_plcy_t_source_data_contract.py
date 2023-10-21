"""Source Data Contract Template for DREAMS Price - Facility Product Channel Policy Data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - fac_prod_chan_plcy_t Data"""

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=80007944,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_prod_chan_plcy_dflt_in: str = Field(
        ...,
        alias="FAC_PROD_CHAN_PLCY_DFLT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_prod_chan_plcy_ds: Optional[str] = Field(
        None,
        alias="FAC_PROD_CHAN_PLCY_DS",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_prod_chan_plcy_id: int = Field(
        ...,
        alias="FAC_PROD_CHAN_PLCY_ID",
        name="",
        description="",
        example=984159,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=1000004,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-08-25T20:35:22.703832Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_chan_id: int = Field(
        ...,
        alias="PROD_CHAN_ID",
        name="",
        description="",
        example=67180,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prod_id: int = Field(
        ...,
        alias="PROD_ID",
        name="",
        description="",
        example=53898,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFacProdChanPlcyTModel(BaseModel):
    """Payload class for DREAMSPriceFacProdChanPlcyTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """The association of Policy to Product, Product Channels and Facilities."""
        unique_identifier = ["data.FAC_PROD_CHAN_PLCY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FAC_PROD_CHAN_PLCY_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
