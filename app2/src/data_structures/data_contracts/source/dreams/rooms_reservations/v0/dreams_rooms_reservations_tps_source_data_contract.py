"""Source Data Contract for Dreams TPS"""
from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTpsId,
    GlobalDreamsTpId,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsTpsId, GlobalDreamsTpId):
    """Class for Dreams TPS Data"""

    trvl_sts_nm: str = Field(
        ...,
        alias="TRVL_STS_NM",
        name="Travel Status Name",
        description="The name of the state of the Travel Status.  For example, one status is Booked, which means that a reservation has been created for the guest.  Another example is Auto Cancelled, which means that the system cancelled the reservation because deposit requirements were not met.",
        example="Booked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    vip_lvl_nm: Optional[str] = Field(
        None,
        alias="VIP_LVL_NM",
        name="VIP Level Name",
        description="Words depicting the relative importance of guests.",
        example="0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_pty_id: Optional[str] = Field(
        None,
        alias="TRVL_AGCY_PTY_ID",
        name="Travel Agency Party Identification",
        description="The unique identification of the transaction organization who is identified as the travel agency for this travel plan segment.",
        example="62605193",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agt_pty_id: Optional[str] = Field(
        None,
        alias="TRVL_AGT_PTY_ID",
        name="Travel Agent Party Identification",
        description="The unique identification of the transaction individual who performs the role of travel agent for this travel plan segment.",
        example="999486097",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="indirect",
    )
    prmy_pty_id: Optional[str] = Field(
        None,
        alias="PRMY_PTY_ID",
        name="Primary Party Indicator",
        description="The unique identification of the transaction individual / organization who is identified as the primary party for this travel plan segment.",
        example="888675291",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="indirect",
    )
    tps_guar_in: str = Field(
        ...,
        alias="TPS_GUAR_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_secur_vl: Optional[str] = Field(
        None,
        alias="TPS_SECUR_VL",
        name="Travel Plan Segment Security Value",
        description="The amount of freedom from risk associated with a particular Travel Plan Segment.  For example, all TPS originating in a particular system may be NTP (No Touch Please).",
        example="NTP",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_ctct_nm: Optional[str] = Field(
        None,
        alias="TPS_CTCT_NM",
        name="Travel Plan Segment Contact Name",
        description="The contact person for a Travel Plan Segment when a formal Party Role is not created.  Example:  If an administrative assistant is booking one or more reservations but is not attending we would simply store her name.  It might only be the first name.  If a group delegate books herself, this element would be null because the Travel Plan Segment Party Role Primary Contact Indicator would be checked.",
        example="Mouse, Mickey",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Direct",
    )
    tps_cncl_dts: Optional[datetime] = Field(
        None,
        alias="TPS_CNCL_DTS",
        name="Travel Plan Segment Cancellation Date",
        description="The date and time when the complete Travel Plan Segment is cancelled.",
        example="2023-05-04T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_cncl_nb: Optional[int] = Field(
        None,
        alias="TPS_CNCL_NB",
        name="Travel Plan Segment Cancellation Number",
        description="A number that is generated and given to the guest when the entire Travel Plan Segment is cancelled.",
        example=212016,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_cnfm_updt_dts: Optional[datetime] = Field(
        None,
        alias="TPS_CNFM_UPDT_DTS",
        name="Travel Plan Segment Guarantee Indicator",
        description="Determines whether or not a Travel Plan Segment is Deposit Guaranteed.This is indicator which shows if reservation is guaranteed or not. It can be guaranteed by contract or by money . Reservation can be guaranteed if its done by wholesaler/group/travel agency or DVC member. Guest needs to pay deposit to get reservation guaranteed. If reservation is not cancelled according to terms and condition deposit is Forfeit .",
        example="2023-05-04T00:00:01Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_cnfrm_usr_id_cd: Optional[str] = Field(
        None,
        alias="TPS_CNFRM_USR_ID_CD",
        name="",
        description="",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_ppty_sync_in: str = Field(
        ...,
        alias="TPS_PPTY_SYNC_IN",
        name="Travel Plan Segment Confirm Update Date Time",
        description="The timestamp of when a confirmation was requested.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    src_acct_ctr_id: str = Field(
        ...,
        alias="SRC_ACCT_CTR_ID",
        name="Source Accounting Center Identifier",
        description="A kind of Accounting Center that financially owns a particular reservation. This will be used for filtering in the Accounting reports to distinguish Scheduled Event sales from Resort Sales.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_arvl_dt: Optional[datetime] = Field(
        None,
        alias="TPS_ARVL_DT",
        name="Travel Plan Segment Arrive Date",
        description="The earliest arrival date of all associated Travel Components.",
        example="2023-04-22T17:50:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_dprt_dt: Optional[datetime] = Field(
        None,
        alias="TPS_DPRT_DT",
        name="Travel Plan Segment Departure Date",
        description="The latest departure date of all associated Travel Components.",
        example="2023-04-22T17:50:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_est_arvl_tm: Optional[datetime] = Field(
        None,
        alias="TPS_EST_ARVL_TM",
        name="Travel Plan Segment Estimated Arrive Datetime",
        description="The time the guest is estimated to arrive on property, captured via the internet pre-arrival process.",
        example="2023-05-04T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tps_est_dprt_tm: Optional[datetime] = Field(
        None,
        alias="TPS_EST_DPRT_TM",
        name="Travel Plan Segment  Estimated Departure Datetime",
        description="The time the guest is estimated to leave property, captured via the internet pre-arrival process.",
        example="2023-05-04T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    onst_phn_nb: Optional[str] = Field(
        None,
        alias="ONST_PHN_NB",
        name="Onsite Phone Number",
        description="Local area contact phone number for the primary guest on the travel plan segment",
        example="4026129725",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    web_txfr_cd: Optional[str] = Field(
        None,
        alias="WEB_TXFR_CD",
        name="Website Transfer Code",
        description="The Web Transfer process is used by a Guest who used a certain web site to get to our booking site.  WDPRO currently passes a code to Accovia and this comes out in the 'Source of Business' attribute.  In the new process after TAP Migration, WDPRO will pass a code through EAI to DREAMS and stored in this field.  This is an interim solution until further requirements to track multiple sources are identified.",
        example="INTA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dnis_nb: Optional[str] = Field(
        None,
        alias="DNIS_NB",
        name="Dialed Number Identification Service Number",
        description="This is a 4 digit number used to identify the line associated with an inbound call. Usually , but not always, this number is the same as the last four digits of the phone number associated with the line. A DNIS number is assigned to a phone number used for inbound calls.",
        example="INTA",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trms_cndtns_vers_nb: Optional[str] = Field(
        None,
        alias="TRMS_CNDTNS_VERS_NB",
        name="Terms Conditions Version Number",
        description="Version number of the terms and conditions card the guest electronically accepted when completing the internet pre-arrival process.",
        example="11.27.2012_4_1.0",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    syw_opt_in: Optional[str] = Field(
        None,
        alias="SYW_OPT_IN",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_usr_id_cd: str = Field(
        ...,
        alias="CREATE_USR_ID_CD",
        name="Create User Identification Code",
        description="The identification value for the user or application that created a row in this table.",
        example="WDPRO",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )
    create_dts: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="Create Date Time",
        description="The month day century year hour minute and second when a row was created in this table.",
        example="2023-03-29T11:30:10.669000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_usr_id_cd: str = Field(
        ...,
        alias="UPDT_USR_ID_CD",
        name="Update User Identification Code",
        description="The identification value for the user or application that updated this row in this table.",
        example="WDPRO",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )
    updt_dts: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="",
        example="2023-07-21T15:45:54.055000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    jdo_seq_nb: int = Field(
        ...,
        alias="JDO_SEQ_NB",
        name="Java Data Object Sequence Number",
        description="A Java Data Object structure used to ensure that optimistic locking of rows in the database do not occur.",
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
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    onst_msg_in: Optional[str] = Field(
        None,
        alias="ONST_MSG_IN",
        name="Onsight Manager Indicator",
        description="Onsight Manager Indicator",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    incognito: Optional[str] = Field(
        None,
        alias="incognito",
        name="",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsReservationsTpsModel(BaseModel):
    """Payload class for DREAMSRoomsReservationsTpsModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan Segment"
        stream_name = "guest360-dreams-resm-stream"
        description = "This is the reservation level of the Travel Plan, the Travel Plan segment which contains information about your travel dates, contact name, ID for the travel agencies and agents, travel status, etc"
        unique_identifier = ["data.TPS_ID"]
        timezone = "UTC"
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tps"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
