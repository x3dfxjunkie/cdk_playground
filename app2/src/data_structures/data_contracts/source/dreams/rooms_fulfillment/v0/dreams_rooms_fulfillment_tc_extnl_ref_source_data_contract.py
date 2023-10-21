"""Source Data Contract for Dreams Travel Component External Reference"""

from __future__ import annotations
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTcId,
    GlobalDreamsData,
    GlobalDreamsMetadata,
)
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class Data(GlobalDreamsTcId, GlobalDreamsData):
    """Class for Dreams Travel Component External Reference Data"""

    tc_extnl_ref_id: int = Field(
        ...,
        alias="TC_EXTNL_REF_ID",
        name="Travel Component External Reference ID",
        description="The unique identifier of Travel Component External Reference. This determines how the Travel Component is recognized in another system.",
        example=310707440,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tc_extnl_ref_typ_nm: str = Field(
        ...,
        alias="TC_EXTNL_REF_TYP_NM",
        name="Travel Component External Reference Type Name",
        description="The designation for the kind of external reference for a travel component",
        example="RESERVATION",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tc_extnl_src_nm: str = Field(
        ...,
        alias="TC_EXTNL_SRC_NM",
        name="Travel Component External Source Name",
        description="The name of the external source for the travel component external reference.",
        example="Accovia",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tc_extnl_ref_vl: str = Field(
        ...,
        alias="TC_EXTNL_REF_VL",
        name="Travel Component External Reference Value",
        description="The reservation number for this Travel Plan Segment in another system.",
        example="28166715#PBP#5",
        guest_identifier=False,
        identifier_tag="",
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


class DREAMSRoomsFulfillmentTcExtnlRefModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentTcExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component External Reference"
        stream_name = "guest360-dreams-resm-stream"
        description = "Components of the reservation/package can have external source references ie: Wholesaler identifiers, Accovia, etc."
        unique_identifier = ["data.TC_EXTNL_REF_ID"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc_extnl_ref"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
