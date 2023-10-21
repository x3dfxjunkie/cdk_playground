"""Source Data Contract for Dreams TC RSN"""

from __future__ import annotations
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTcId,
    GlobalDreamsData,
    GlobalDreamsTransactCommitTimestamp,
    GlobalDreamsMetadata,
)
from pydantic import BaseModel, Field
from typing import Optional


class Data(GlobalDreamsTcId, GlobalDreamsData, GlobalDreamsTransactCommitTimestamp):
    """Class for Dreams TC RSN Data"""

    tc_rsn_id: int = Field(
        ...,
        alias="TC_RSN_ID",
        name="PreDefined Travel Component Reason Identification",
        description="Unique identifier for the explanation of an action that occurred on a travel component(action can be cancellation , upgrade , change etc)",
        example=30035020461,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tc_rsn_typ_nm: str = Field(
        ...,
        alias="TC_RSN_TYP_NM",
        name="Travel Component Reason Type Name",
        description="Type of reason that affects a travel component.Type of reasons can be change, upgrade, early check out, mass cancellation etc.",
        example="Cancel",
        guest_identifier=False,
        identifier_tag="Indirect",
        transaction_identifier=False,
    )
    prdf_tc_rsn_id: Optional[int] = Field(
        None,
        alias="PRDF_TC_RSN_ID",
        name="Predefined Travel Component Reason Identification",
        description="Unique identifier for a pre-defined reason that affects a travel component.",
        example=3,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tc_rsn_cntct_nm: Optional[str] = Field(
        None,
        alias="TC_RSN_CNTCT_NM",
        name="Travel Component Reason Contact Name",
        description="",
        example="Mouse, Mickey",
        guest_identifier=True,
        identifier_tag="Direct",
        transaction_identifier=False,
    )
    rev_cls_id: Optional[str] = Field(
        None,
        alias="REV_CLS_ID",
        name="Revenue Classification Identification",
        description="The unique identifier of Revenue Classification.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentTcRsnModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentTcRsnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Reason"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table provides the reason for certain actions associated to a travel component. It also has the FK for the Preferred Travel Component Reason"  # optional
        unique_identifier = ["data.TC_RSN_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc_rsn"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
