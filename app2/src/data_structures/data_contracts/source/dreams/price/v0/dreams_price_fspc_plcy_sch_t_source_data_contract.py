"""Source Data Contract Template for DREAMS Pricing FSPC_PLCY_SCH_T Data"""


from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - Fee Data"""

    fac_srvc_prd_chan_plcy_id: int = Field(
        ...,
        alias="FAC_SRVC_PRD_CHAN_PLCY_ID",
        name="",
        description="",
        example=5003314,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2017-12-18T10:36:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_id: int = Field(
        ...,
        alias="SCH_ID",
        name="",
        description="",
        example=1030475,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFspcPlcySchTModel(BaseModel):
    """Payload class for DREAMSPriceFspcPlcySchTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Associates a schedule of valid days and times for discounts (via a membership) valid for specified service periods at certain facilities."""
        unique_identifier = ["data.FAC_SRVC_PRD_CHAN_PLCY_ID", "data.SCH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FSPC_PLCY_SCH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
