"""Source Data Contract Template for DREAMS Price - fsp_chan_plcy_t"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - fsp_chan_plcy_t Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-02-01T17:45:51.320817Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    entrprs_meal_prd_id: int = Field(
        ...,
        alias="ENTRPRS_MEAL_PRD_ID",
        name="",
        description="",
        example=15579103,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_id: int = Field(
        ...,
        alias="FAC_ID",
        name="",
        description="",
        example=244731,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    fac_srvc_prd_chan_plcy_id: int = Field(
        ...,
        alias="FAC_SRVC_PRD_CHAN_PLCY_ID",
        name="",
        description="",
        example=5064090,
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

    plcy_id: int = Field(
        ...,
        alias="PLCY_ID",
        name="",
        description="",
        example=19344344,
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

    prod_chan_id: Optional[int] = Field(
        None,
        alias="PROD_CHAN_ID",
        name="",
        description="",
        example=107,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-02-01T17:45:51.320817Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFspChanPlcyTModel(BaseModel):
    """Payload class for DREAMSPriceFspChanPlcyTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """Associates a policy to a service period at a facility.  For Scheduled Events,this is primarily a Cancellation Policy or discount policy."""
        unique_identifier = ["data.FAC_SRVC_PRD_CHAN_PLCY_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FSP_CHAN_PLCY_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
