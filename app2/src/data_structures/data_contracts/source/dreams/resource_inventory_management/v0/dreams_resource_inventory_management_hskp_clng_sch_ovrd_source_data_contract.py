"""Source Data Contract for Dreams Resource Inventory Management Housekeeping Cleaning Schedule Override"""


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Resource Inventory Management Housekeeping Cleaning Schedule Override"""

    asgn_ownr_id: int = Field(
        ...,
        alias="ASGN_OWNR_ID",
        name="",
        description="",
        example=111111111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    clng_sch_ovrd_dt: datetime = Field(
        ...,
        alias="CLNG_SCH_OVRD_DT",
        name="",
        description="",
        example="2023-07-29T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2023-07-25T17:36:25.507000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LYONK034",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    hskp_clng_sch_ovrd_id: int = Field(
        ...,
        alias="HSKP_CLNG_SCH_OVRD_ID",
        name="",
        description="",
        example=23098192,
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

    ovrd_hskp_srvc_in: str = Field(
        ...,
        alias="OVRD_HSKP_SRVC_IN",
        name="",
        description="",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-25T17:36:25.507000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="LYONK034",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_invtry_sts_id: Optional[int] = Field(
        None,
        alias="RSRC_INVTRY_STS_ID",
        name="",
        description="",
        example=7,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementHskpClngSchOvrdModel(BaseModel):

    """Payload class for for Dreams Resource Inventory Management Housekeeping Cleaning Schedule Override"""

    class Config:
        """Payload Level Metadata"""

        title = "Housekeeping Cleaning Schedule Override"
        stream_name = ""
        description = """This table indicates when a housekeeping schedule is overridden or not"""
        unique_identifier = ["data.HSKP_CLNG_SCH_OVRD_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "hskp_clng_sch_ovrd"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
