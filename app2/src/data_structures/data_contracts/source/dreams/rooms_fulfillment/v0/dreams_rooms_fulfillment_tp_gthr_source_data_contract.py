"""Source Data Contract for Dreams TP GTHR"""

from __future__ import annotations
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTpId,
    GlobalDreamsData,
    GlobalDreamsTransactCommitTimestamp,
    GlobalDreamsMetadata,
)
from pydantic import BaseModel, Field


class Data(GlobalDreamsTpId, GlobalDreamsData, GlobalDreamsTransactCommitTimestamp):
    """Class for Dreams TP GTHR Data"""

    gthr_cd: str = Field(
        ...,
        alias="GTHR_CD",
        name="Gathering Code",
        description="The Enterprise identifier of a gathering.",
        example="TW09365081",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gthr_typ_nm: str = Field(
        ...,
        alias="GTHR_TYP_NM",
        name="Gathering Type Name",
        description="Words identifying a Gathering Type.   An example is Grand Gathering, which is based upon the family reunion concept.  This is a group too small to protect inventory for and only becomes an official group if function space is required.  Another example is a Travel With, which is even smaller.",
        example="TW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    gthr_nm: str = Field(
        ...,
        alias="GTHR_NM",
        name="Gathering Name",
        description="The desgination for a particular gathering.",
        example="Magical",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentTpGthrModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentTpGthrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan Gather"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table provides an association between travel parties who have separate reservations. It's called Gather Code that is a retired product we had, it's better known as a Travel With Code."  # optional
        unique_identifier = ["data.TP_ID", "data.GTHR_CD"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tp_gthr"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
