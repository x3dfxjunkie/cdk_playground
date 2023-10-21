"""Source Data Contract Template for DREAMS Price - Daily Schedule"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - DLY_SCH_T Data"""

    all_dy_in: str = Field(
        ...,
        alias="ALL_DY_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-06-09T08:13:05.747370Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dly_sch_end_dts: datetime = Field(
        ...,
        alias="DLY_SCH_END_DTS",
        name="",
        description="",
        example="2023-09-08T15:15:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dly_sch_id: int = Field(
        ...,
        alias="DLY_SCH_ID",
        name="",
        description="",
        example=9976502,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dly_sch_strt_dts: datetime = Field(
        ...,
        alias="DLY_SCH_STRT_DTS",
        name="",
        description="",
        example="2023-09-08T15:15:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    dow_nm: str = Field(
        ...,
        alias="DOW_NM",
        name="",
        description="",
        example="Friday",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    end_tm_in: str = Field(
        ...,
        alias="END_TM_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_sch_id: int = Field(
        ...,
        alias="ENTRPRS_SCH_ID",
        name="",
        description="",
        example=18419674,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_sub_sch_id: int = Field(
        ...,
        alias="ENTRPRS_SUB_SCH_ID",
        name="",
        description="",
        example=80000427,
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

    sch_typ_nm: str = Field(
        ...,
        alias="SCH_TYP_NM",
        name="",
        description="",
        example="Operating",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txlt_srvc_in: str = Field(
        ...,
        alias="TXLT_SRVC_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-06-09T08:13:05.747370Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceDlySchTModel(BaseModel):
    """Payload class for DREAMSPriceDlySchTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """A daily snapshot of anything that can occur at WDW.  It includes all the Product schedules. """
        unique_identifier = ["data.DLY_SCH_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "DLY_SCH_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
