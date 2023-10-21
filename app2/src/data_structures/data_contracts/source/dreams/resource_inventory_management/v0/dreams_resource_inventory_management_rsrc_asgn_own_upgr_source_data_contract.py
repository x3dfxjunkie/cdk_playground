"""Source Data Contract Template for DREAMS Resource Inventory Management Campus Resource Assignment Owner Upgrade"""


from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    asgn_ownr_id: int = Field(
        ...,
        alias="ASGN_OWNR_ID",
        name="",
        description="",
        example=15574215,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2010-12-23T15:42:36.562000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="MOUSM002",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2010-12-23T15:42:36.562000Z",
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

    upgrd_cmt_tx: Optional[str] = Field(
        None,
        alias="UPGRD_CMT_TX",
        name="",
        description="",
        example="0|470|500|44|0|1014",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrd_rsn_tx: str = Field(
        ...,
        alias="UPGRD_RSN_TX",
        name="",
        description="",
        example="COUNTS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrd_rsrc_invtry_typ_id: int = Field(
        ...,
        alias="UPGRD_RSRC_INVTRY_TYP_ID",
        name="",
        description="",
        example=126,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    upgrd_scr_nb: int = Field(
        ...,
        alias="UPGRD_SCR_NB",
        name="",
        description="",
        example=1014,
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


class DREAMSResourceInventoryManagementRsrcAsgnOwnUpgrModel(BaseModel):
    """Payload class for DREAMSResourceInventoryManagementRsrcAsgnOwnUpgrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Resource Assignment Owner Upgrade"
        stream_name = ""
        description = """If a room type is upgraded, the new room type will live in this table"""
        unique_identifier = ["data.ASGN_OWNR_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "rsrc_asgn_own_upgr"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
