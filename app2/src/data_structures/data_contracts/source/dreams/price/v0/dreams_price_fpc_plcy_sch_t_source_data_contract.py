"""Source Data Contract Template for DREAMS Price - fpc_plcy_sch_t"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - fpc_plcy_sch_t Data"""

    fac_prod_chan_plcy_id: int = Field(
        ...,
        alias="FAC_PROD_CHAN_PLCY_ID",
        name="",
        description="",
        example=1738197,
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

    sch_id: int = Field(
        ...,
        alias="SCH_ID",
        name="",
        description="",
        example=3152625,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFpcPlcySchTModel(BaseModel):
    """Payload class for DREAMSPriceFpcPlcySchTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Associates a schedule of valid days and times for discounts (via a membership) valid at a facility for certain products."""
        unique_identifier = ["data.FAC_PROD_CHAN_PLCY_ID", "data.SCH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FPC_PLCY_SCH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
