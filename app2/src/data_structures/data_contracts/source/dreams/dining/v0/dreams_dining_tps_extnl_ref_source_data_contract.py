"""Source Data Contract for Dreams Dining TPS EXTRNL REF"""
from __future__ import annotations
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTpsId,
    GlobalDreamsData,
    GlobalDreamsTransactCommitTimestamp,
    GlobalDreamsMetadata,
)
from pydantic import BaseModel, Field


class Data(GlobalDreamsTpsId, GlobalDreamsData, GlobalDreamsTransactCommitTimestamp):
    """Class for Dreams Dining TPS EXTRNL REF Data"""

    tps_extnl_ref_id: int = Field(
        ...,
        alias="TPS_EXTNL_REF_ID",
        name="The unique identifier of Travel Plan Segment External Reference.",
        description="",
        example=30004500114,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tps_extnl_ref_typ_nm: str = Field(
        ...,
        alias="TPS_EXTNL_REF_TYP_NM",
        name="Travel Plan Segment External Reference Type Name",
        description="The kind of external reference that is applicable to a travel plan segment.  Valid kinds include: Travel With, Linkage or Reservation.",
        example="RESERVATION",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tps_src_nm: str = Field(
        ...,
        alias="TPS_SRC_NM",
        name="Travel Plan Segment Source Name",
        description="The source of the booking of the travel plan segment.",
        example="TravelBox-DLR",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    tps_extnl_ref_vl: str = Field(
        ...,
        alias="TPS_EXTNL_REF_VL",
        name="Travel Plan Segment External Reference Value",
        description="The value for the travel plan segment as referenced externally.",
        example="15097346",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class DREAMSDiningTpsExtnlRefModel(BaseModel):
    """Payload class for DREAMSDiningTpsExtnlRefModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan Segment External Reference"
        stream_name = "guest360-dreams-resm-stream"
        description = "Reservation level travel plan segment records can have associated external references from various sources. External References are: TPS_EXTNL_REF_TYP_NM, RESERVATION, ORIGINAL_TP_ID, MEMBERSHIP, LINKAGE, APP_REF"
        unique_identifier = ["data.TPS_EXTNL_REF_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tps_extnt_ref"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
