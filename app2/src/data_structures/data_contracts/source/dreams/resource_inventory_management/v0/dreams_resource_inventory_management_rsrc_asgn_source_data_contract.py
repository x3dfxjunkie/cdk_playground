"""Source Data Contract Template for DREAMS Resource Inventory Management Resource Assignment """


from __future__ import annotations

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    asgn_id: int = Field(
        ...,
        alias="ASGN_ID",
        name="",
        description="",
        example=22941925,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    asgn_lck_in: str = Field(
        ...,
        alias="ASGN_LCK_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    asgn_sts_nm: Optional[str] = Field(
        None,
        alias="ASGN_STS_NM",
        name="",
        description="",
        example="BOOKED",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-12-01T13:00:35.904000Z",
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
        example=23352103,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rsrc_id: Optional[int] = Field(
        None,
        alias="RSRC_ID",
        name="",
        description="",
        example=23059,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-12-01T13:00:35.904000Z",
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

    tmp_sts_usr_nm: Optional[str] = Field(
        None,
        alias="TMP_STS_USR_NM",
        name="",
        description="",
        example="MOUSM002",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    tmp_asgn_sts_end_dts: Optional[datetime] = Field(
        None,
        alias="TMP_ASGN_STS_END_DTS",
        name="",
        description="",
        example="2020-02-03 07:20:11.225",
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


class DREAMSResourceInventoryManagementRsrcAsgnModel(BaseModel):
    """Payload class forDREAMSResourceInventoryManagementRsrcAsgnModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Assignment"
        stream_name = ""
        description = "This table provides the assignment status of a given resource. It also indicates if an assignment is locked."
        unique_identifier = ["data.ASGN_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_asgn"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
