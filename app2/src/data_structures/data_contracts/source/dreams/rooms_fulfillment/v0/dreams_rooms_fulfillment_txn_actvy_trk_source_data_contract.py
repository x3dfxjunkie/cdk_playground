"""Source Data Contract Template for Dreams - Room Fulfillment Transaction Activity Tracking"""

from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import GlobalDreamsMetadata


class Data(BaseModel):
    """Class for Dreams - Room Fulfillment Transaction Activity Tracking Data"""

    usr_id: str = Field(
        ...,
        alias="USR_ID",
        name="",
        description="",
        example="WDPRT-DISNEY",
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

    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2020-01-01 00:01:57.166000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usr_rl_nm: Optional[str] = Field(
        None,
        alias="USR_RL_NM",
        name="",
        description="",
        example="1-4JXE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    app_txn_id: str = Field(
        ...,
        alias="APP_TXN_ID",
        name="",
        description="",
        example="123456702167",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="",
        example="2020-01-01 00:01:57.166000",
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

    actvy_app_nm: str = Field(
        ...,
        alias="ACTVY_APP_NM",
        name="",
        description="",
        example="LILO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_actvy_ds: Optional[str] = Field(
        None,
        alias="TXN_ACTVY_DS",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_actvy_nm: str = Field(
        ...,
        alias="TXN_ACTVY_NM",
        name="",
        description="",
        example="MODIFYGUEST",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    actvy_trmnl_id: Optional[str] = Field(
        None,
        alias="ACTVY_TRMNL_ID",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    app_txn_src_nm: str = Field(
        ...,
        alias="APP_TXN_SRC_NM",
        name="",
        description="",
        example="DREAMS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    app_txn_typ_nm: str = Field(
        ...,
        alias="APP_TXN_TYP_NM",
        name="",
        description="",
        example="TRAVEL_PLAN_SEGMENT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="",
        description="",
        example="WDPRT-DISNEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usr_site_loc_nm: Optional[str] = Field(
        None,
        alias="USR_SITE_LOC_NM",
        name="",
        description="",
        example="BO",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    actvy_ip_addr_tx: Optional[str] = Field(
        None,
        alias="ACTVY_IP_ADDR_TX",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    actvy_wrk_loc_id: int = Field(
        ...,
        alias="ACTVY_WRK_LOC_ID",
        name="",
        description="",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="",
        description="",
        example="WDPRT-DISNEY",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_actvy_nm_dts: datetime = Field(
        ...,
        alias="TXN_ACTVY_NM_DTS",
        name="",
        description="",
        example="2020-01-01 00:01:57.367000",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    txn_actvy_trk_id: int = Field(
        ...,
        alias="TXN_ACTVY_TRK_ID",
        name="",
        description="",
        example=22159987,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    usr_actvy_impct_tx: str = Field(
        ...,
        alias="USR_ACTVY_IMPCT_TX",
        name="",
        description="",
        example="DTR",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentTxnActvyTrkModel(BaseModel):
    """Payload class for Dreams - Room Fulfillment Transaction Activity Tracking Model"""

    class Config:
        """Payload Level Metadata"""

        title = "Transaction Activity Tracking"
        stream_name = ""
        description = """"""
        unique_identifier = ["data.TXN_ACTVY_TRK_ID"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "txn_actvy_trk"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
