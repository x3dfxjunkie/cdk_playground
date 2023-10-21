"""Source Data Contract for DREAMS Group Travel Component Group"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams Group Travel Component Group Data"""

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2011-02-06T20:57:38.071000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MASSMod",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_cd: str = Field(
        ...,
        alias="GRP_CD",
        name="",
        description="",
        example="G0570881",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    grp_tm_id: int = Field(
        ...,
        alias="GRP_TM_ID",
        name="",
        description="",
        example=1111612,
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

    tc_grp_nb: int = Field(
        ...,
        alias="TC_GRP_NB",
        name="",
        description="",
        example=111111111127,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2011-02-06T20:57:38.071000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="MASSMod",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSDiningGrpTcGrpModel(BaseModel):
    """Payload class for DREAMSDiningGrpTcGrpModel"""

    class Config:
        """Payload Level Metadata"""

        title = "DREAMS Group Travel Component Group"
        stream_name = ""
        description = "When a reservation is a part of a convention, wedding, sporting event, there is a Group/Block code that identifies the group and is used for blocking rooms and also for billing. This table holds that Group code and the Group Team ID"  # optional
        unique_identifier = ["data.TC_GRP_NB"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "grp_tc_grp"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
