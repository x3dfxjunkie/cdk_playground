"""Source Data Contract Template for DREAMS Resource Inventory Management Resource Assignment Request"""


from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata
from datetime import datetime


class Data(BaseModel):
    all_dy_in: str = Field(
        ...,
        alias="ALL_DY_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    asgn_ownr_id: int = Field(
        ...,
        alias="ASGN_OWNR_ID",
        name="",
        description="",
        example=52966278,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    asgn_req_dt: datetime = Field(
        ...,
        alias="ASGN_REQ_DT",
        name="",
        description="",
        example="2012-12-07T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    asgn_req_end_tm: Optional[datetime] = Field(
        None,
        alias="ASGN_REQ_END_TM",
        name="",
        description="",
        example="2012-12-06T19:18:31Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    asgn_req_strt_tm: Optional[datetime] = Field(
        None,
        alias="ASGN_REQ_STRT_TM",
        name="",
        description="",
        example="2012-12-07T14:50:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2012-12-06T19:18:30.062000Z",
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

    rsrc_asgn_req_id: int = Field(
        ...,
        alias="RSRC_ASGN_REQ_ID",
        name="",
        description="",
        example=101781634,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2012-12-06T19:18:30.062000Z",
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

    rt_ctgy_nm: Optional[str] = Field(
        None,
        alias="RT_CTGY_NM",
        name="",
        description="",
        example="GRP",
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


class DREAMSResourceInventoryManagementRsrcAsgnReqModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcAsgnReqModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Assignment Request"
        stream_name = ""
        description = """This table provides the the date the inventory is requested for, the rate category, if it's an all day request or not"""
        unique_identifier = ["data.RSRC_ASGN_REQ_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_asgn_req"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
