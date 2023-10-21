"""Source Data Contract Template for DREAMS Price - SCH_DOW_INCLSN_T data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - SCH_DOW_INCLSN_T Data"""

    dow_nm: str = Field(
        ...,
        alias="DOW_NM",
        name="",
        description="",
        example="Saturday",
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
        example=646101,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceSchDowInclsnTModel(BaseModel):
    """Payload class for DREAMSPriceSchDowInclsnTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Captures the days of week of a schedule that the discounts are valid for. Could be extended for other uses."""
        unique_identifier = ["data.SCH_ID", "data.DOW_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SCH_DOW_INCLSN_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
