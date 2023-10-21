"""Source Data Contract for Dreams TC RSRVBL RSRC"""

from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams TC RSRVBL RSRC Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-08-14T14:48:38Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2020-12-12T12:12:12",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_typ_cd: str = Field(
        ...,
        alias="RSRC_INVTRY_TYP_CD",
        name="",
        description="",
        example="86e0a670-87e4-474c-8ec6-8b786b2ed537",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="",
        description="",
        example=11111119999,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsrc_invtry_id_vl: Optional[str] = Field(
        None,
        alias="TC_RSRC_INVTRY_ID_VL",
        name="",
        description="",
        example="23",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tc_rsrvbl_rsrc_id: int = Field(
        ...,
        alias="TC_RSRVBL_RSRC_ID",
        name="",
        description="",
        example=30021292258,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-14T14:48:38Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningTcRsrvblRsrcModel(BaseModel):
    """Payload class for DREAMSDiningTcRsrvblRsrcModel"""

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
