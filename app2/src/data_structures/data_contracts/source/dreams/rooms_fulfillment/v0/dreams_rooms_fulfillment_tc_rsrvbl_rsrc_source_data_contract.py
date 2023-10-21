"""Source Data Contract for Dreams TC RSRVBL RSRC"""

from __future__ import annotations
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTcId,
    GlobalDreamsData,
    GlobalDreamsTransactCommitTimestamp,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsTcId, GlobalDreamsData, GlobalDreamsTransactCommitTimestamp):
    """Class for Dreams TC RSRVBL RSRC Data"""

    tc_rsrvbl_rsrc_id: int = Field(
        ...,
        alias="TC_RSRVBL_RSRC_ID",
        name="Travel Component reservable resource Identificator",
        description="The system generated identification value for a reservable resource that is required to satisfy a specific travel component.",
        example=30012846221,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    rsrc_invtry_typ_cd: str = Field(
        ...,
        alias="RSRC_INVTRY_TYP_CD",
        name="Resource Inventory Type Code",
        description="The shortened designation for a kind of resource that is managed as inventory that is required to satisfy a particular travel component.  For an accommodation travel component the kind of inventory that is managed is the room type (Garden View).  For a Dinner Show travel component, the kind of inventory that is managed is the table top designation (Four Top, Six Top, Ten Top).",
        example="e572c4f8-2a1b-79d1-f0c9-7ff443006234",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )


class DREAMSRoomsFulfillmentTcRsrvblRsrcModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentTcRsrvblRsrcModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Reservable Resource"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table ties the reservable resource to certain travel components, it's the inventory item for that component ie: room type, table top type for Scheduled Events/Dining"  # optional
        unique_identifier = ["data.TC_RSRVBL_RSRC_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc_rsrvbl_rsrc"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
