"""Source Data Contract Template for DREAMS Price - Feature Toggle"""


from __future__ import annotations

# from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for DREAMS Price - feature_toggle_t Data"""

    feature_code: str = Field(
        ...,
        alias="FEATURE_CODE",
        name="",
        description="",
        example="TOG_PUB_ONLY_ALLOW_MISC_UPD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feature_desc: str = Field(
        ...,
        alias="FEATURE_DESC",
        name="",
        description="",
        example="Only allow Misc accommodation packages that existed prior to ARP WDW Go-live to be updated in Publish process",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feature_enabled: int = Field(
        ...,
        alias="FEATURE_ENABLED",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    feature_id: int = Field(
        ...,
        alias="FEATURE_ID",
        name="",
        description="",
        example=4,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    last_update_datetime: datetime = Field(
        ...,
        alias="LAST_UPDATE_DATETIME",
        name="",
        description="",
        example="2017-08-07T15:03:01.583304Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSPriceFeatureToggleTModel(BaseModel):
    """Payload class for DREAMSPriceFeatureToggleTModel"""

    class Config:
        """Payload Level Metadata"""

        title = ""
        stream_name = ""
        description = """"""
        unique_identifier = ["data.FEATURE_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = ""
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "FEATURE_TOGGLE_T"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
