"""Source Data Contract Template for DREAMS Resource Inventory Management Work Location Till"""


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2009-12-09T18:02:41.396749Z",
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

    max_till_am: int = Field(
        ...,
        alias="MAX_TILL_AM",
        name="",
        description="",
        example=2000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    till_id: int = Field(
        ...,
        alias="TILL_ID",
        name="",
        description="",
        example=50,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    till_typ_nm: str = Field(
        ...,
        alias="TILL_TYP_NM",
        name="",
        description="",
        example="Frontline Service Advisor",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    wrk_loc_id: int = Field(
        ...,
        alias="WRK_LOC_ID",
        name="",
        description="",
        example=56,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSResourceInventoryManagementWrkLocTillModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementWrkLocTillModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Work Location Till"
        stream_name = ""
        description = """Till and work location IDs associated to a till type
Frontline Service Advisor
Manager
Graveyard
Cashier"""
        unique_identifier = ["data.TILL_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "wrk_loc_till"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
