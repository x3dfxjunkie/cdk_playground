"""Source Data Contract for DREAMS Group Team"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Team Data"""

    grp_tm_id: int = Field(
        ...,
        alias="GRP_TM_ID",
        name="",
        description="",
        example=113202808,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="G0762963",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    grp_tm_nm: str = Field(
        ...,
        alias="GRP_TM_NM",
        name="",
        description="",
        example="CWD friends for life conference",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="Passkey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-05-20T20:32:21Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="Passkey",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-05-20T20:32:21Z",
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


class DREAMSRoomsFulfillmentGrpTmModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentGrpTmModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Group Team"
        stream_name = ""
        description = (
            "This table provides the Group Team Name (or just the group name, if it's not a sporting event)"  # optional
        )
        unique_identifier = ["data.GRP_TM_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "grp_tm"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
