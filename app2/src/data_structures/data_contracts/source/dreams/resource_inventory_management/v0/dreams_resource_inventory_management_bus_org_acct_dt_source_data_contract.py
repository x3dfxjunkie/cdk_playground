"""Source Data Contract for Dreams Resource Inventory Management Business Organization Accounting Date"""

from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):

    """Data Class for Dreams Resource Inventory Management Business Organization Accounting Date"""

    bus_org_id: int = Field(
        ...,
        alias="BUS_ORG_ID",
        name="",
        description="",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-09-10T14:08:30Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="LILO CONV",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    curr_acct_dt: datetime = Field(
        ...,
        alias="CURR_ACCT_DT",
        name="",
        description="",
        example="2023-08-06T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="",
        description="",
        example=4706,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-08-06T07:12:05.279000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="rolAcctDtJob",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementBusOrgAcctDtModel(BaseModel):

    """Payload class for Dreams Resource Inventory Management Business Organization Accounting Date"""

    class Config:
        """Payload Level Metadata"""

        title = "Business Organization Accounting Date"
        stream_name = ""
        description = """This table is updated by the Accounting Date Roll job by business organization"""
        unique_identifier = ["data.BUS_ORG_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "bus_org_acct_dt"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
