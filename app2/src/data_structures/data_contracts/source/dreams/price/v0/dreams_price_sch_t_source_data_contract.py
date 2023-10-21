"""Source Data Contract Template for DREAMS Price - Schedule data"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - sch_t Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2017-09-04T10:12:27.847641Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=0,
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

    sch_actl_end_dt: datetime = Field(
        ...,
        alias="SCH_ACTL_END_DT",
        name="",
        description="",
        example="2010-01-03T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_actl_end_tm: datetime = Field(
        ...,
        alias="SCH_ACTL_END_TM",
        name="",
        description="",
        example="2010-01-03T23:59:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_end_dt: datetime = Field(
        ...,
        alias="SCH_END_DT",
        name="",
        description="",
        example="2010-01-03T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_end_tm: datetime = Field(
        ...,
        alias="SCH_END_TM",
        name="",
        description="",
        example="2010-01-03T23:59:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_id: int = Field(
        ...,
        alias="SCH_ID",
        name="",
        description="",
        example=2298669,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_strt_dt: datetime = Field(
        ...,
        alias="SCH_STRT_DT",
        name="",
        description="",
        example="2010-01-03T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    sch_strt_tm: datetime = Field(
        ...,
        alias="SCH_STRT_TM",
        name="",
        description="",
        example="2010-01-03T00:01:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2017-09-04T10:12:27.847641Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceSchTModel(BaseModel):
    """Payload class for DREAMSPriceSchTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Sourced from One Source, this table contains valid day and time combinations for the Discount Policies used in Schedule Events.  This can be extended for other uses."""
        unique_identifier = ["data.SCH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "SCH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
