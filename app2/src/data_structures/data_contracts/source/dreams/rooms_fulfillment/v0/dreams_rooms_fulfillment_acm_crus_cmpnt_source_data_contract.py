"""Source Data Contract for DREAMS Accommodation Cruise Component"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Accommodation Cruise Component Data"""

    acm_crus_cmpnt_id: int = Field(
        ...,
        alias="ACM_CRUS_CMPNT_ID",
        name="",
        description="",
        example=210889300,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    acm_tc_id: int = Field(
        ...,
        alias="ACM_TC_ID",
        name="",
        description="",
        example=22087356994,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    ship_cd: str = Field(
        ...,
        alias="SHIP_CD",
        name="",
        description="",
        example="WW",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    vyge_nb: int = Field(
        ...,
        alias="VYGE_NB",
        name="",
        description="",
        example=2305,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-20T10:35:11.931000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MOUSM001",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-05-20T10:35:11.931000Z",
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
    transact_commit_timestamp: Optional[datetime] = Field(
        None,
        alias="transact_commit_timestamp",
        name="",
        description="",
        example="2023-05-21T06:15:24Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    transact_seq: Optional[str] = Field(
        None,
        alias="transact_seq",
        name="",
        description="",
        example="20230521061524000000000001867101213",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentAcmCrusCmpntModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentAcmCrusCmpntModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Accommodation Cruise Component"
        stream_name = ""
        description = "If the guest has booked a room reservation and a Disney Cruise Line reservation, the accommodation component provides the Ship code and the voyage number for the guests cruise."  # optional
        unique_identifier = ["data.ACM_CRUS_CMPNT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "acm_crus_cmpnt"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
