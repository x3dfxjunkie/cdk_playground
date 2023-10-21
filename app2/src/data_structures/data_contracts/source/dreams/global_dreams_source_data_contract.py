"""Global Dreams Data Contract: for key fields and classes that will be repeated throughout sources"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# This file allows users to reuse the classes below for inheritance in child data contracts in order to save repeating code
# To use, user needs import the file and then use the necessary class as inheritance for their contract
class GlobalDreamsSchemaName(Enum):
    """Global Dreams Database schema name Enum"""

    RES_MGMT = "res_mgmt"


# possible payload tables
class GlobalDreamsTableName(Enum):
    """Global Dreams Database Table name Enum"""

    ACM_CMPNT = "ACM_CMPNT"
    ACM_CMPNT_CHRNLGY = "ACM_CMPNT_CHRNLGY"
    ACM_CRUS_CMPNT = "ACM_CRUS_CMPNT"
    ADM_CMPNT = "ADM_CMPNT"
    ADM_CMPNT_ENTTL = "ADM_CMPNT_ENTTL"
    COMNCTN_CHAN = "COMNCTN_CHAN"
    DVC_PT_PMT_REF = "DVC_PT_PMT_REF"
    EXPRNC_ENHNC_ELIG_CRTR = "EXPRNC_ENHNC_ELIG_CRTR"
    EXPRNC_ENHNC_PROD = "EXPRNC_ENHNC_PROD"
    GRP_TM = "GRP_TM"
    HT_GNR_ITEM = "HT_GNR_ITEM"
    PKG_TC = "PKG_TC"
    PKG_TC_TKT = "PKG_TC_TKT"
    PRDF_TC_RSN = "PRDF_TC_RSN"
    RES_HIST = "RES_HIST"
    RES_MGMT_FEAT_REQ = "RES_MGMT_FEAT_REQ"
    RES_MGMT_MSG = "RES_MGMT_MSG"
    RES_MGMT_REQ = "RES_MGMT_REQ"
    RES_MGMT_REQ_RTE = "RES_MGMT_REQ_RTE"
    RSRT_GST_BKNG_WNDW_OPT = "RSRT_GST_BKNG_WNDW_OPT"
    SLS_CHAN = "SLS_CHAN"
    TC = "TC"
    TC_EXPRNC_ENHNC_CRTR = "TC_EXPRNC_ENHNC_CRTR"
    TC_EXTNL_REF = "TC_EXTNL_REF"
    TC_FEE = "TC_FEE"
    TC_FEE_TYP = "TC_FEE_TYP"
    TC_GRP = "TC_GRP"
    TC_GRP_TYP = "TC_GRP_TYP"
    TC_GST = "TC_GST"
    TC_RSN = "TC_RSN"
    TC_RSN_TYP = "TC_RSN_TYP"
    TC_RSRVBL_RSRC = "TC_RSRVBL_RSRC"
    TC_TYP = "TC_TYP"
    TP = "TP"
    TPS = "TPS"
    TPS_ALRGY = "TPS_ALRGY"
    TPS_CNFIRM_RCPNT = "TPS_CNFIRM_RCPNT"
    TPS_EXTNL_REF = "TPS_EXTNL_REF"
    TPS_EXTNL_REF_TYP = "TPS_EXTNL_REF_TYP"
    TPS_LCTR = "TPS_LCTR"
    TPS_PTY_LCTR = "TPS_PTY_LCTR"
    TP_EXTNL_REF = "TP_EXTNL_REF"
    TP_GTHR = "TP_GTHR"
    TP_PTY = "TP_PTY"
    TRVL_STS = "TRVL_STS"
    TXN_ACTVY_TRK = "TXN_ACTVY_TRK"
    VIP_LVL = "VIP_LVL"
    VST_PRPS = "VST_PRPS"
    V_BYPS_FRNT_DSK = "V_BYPS_FRNT_DSK"


# table metadata
class GlobalDreamsMetadata(BaseModel):
    """Global Dreams Metadata Class"""

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Date Time stamp",
        description="Timestamp for when the record was sent in the stream",
        example="2023-03-29T15:30:19.109655Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    record_type: str = Field(
        ...,
        alias="record-type",
        name="Record Type",
        description="data",
        example="data",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    operation: str = Field(
        ...,
        alias="operation",
        name="Operation",
        description="",
        example="update",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="Partiction Key Type",
        description="",
        example="schema-table",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    schema_name: str = Field(
        ...,
        alias="schema-name",
        name="Schema Name",
        description="Name of the schema in snowflake",
        example="res_mgmt",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    table_name: str = Field(
        ...,
        alias="table-name",
        name="Table Name",
        description="name of the table in snowflake",
        example="tc",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="Transaction Identifyer",
        description="unique ID for the stream record",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    transaction_record_id: Optional[int] = Field(
        None,
        alias="transaction-record-id",
        name="Transaction Record ID",
        description="Transaction Record ID",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prev_transaction_id: Optional[int] = Field(
        None,
        alias="prev-transaction-id",
        name="Previous Transaction ID",
        description="Previous Transaction ID",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prev_transaction_record_id: Optional[int] = Field(
        None,
        alias="prev-transaction-record-id",
        name="Previous Transaction Record ID",
        description="Previous Transaction Record ID",
        example=70974432245344,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    commit_timestamp: Optional[datetime] = Field(
        None,
        alias="commit-timestamp",
        name="Commit Timestamp",
        description="Commit Timestamp",
        example="2023-03-29T15:30:19.109655Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    stream_position: Optional[str] = Field(
        None,
        alias="stream-position",
        name="Stream Position",
        description="Stream Position",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalDreamsData(BaseModel):
    """Class for Dreams ACM CMPNT CHRNLGY Data Payload"""

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
        name="Update Date Time",
        description="The month day century year hour minute and second when a row in this table was updated.",
        example="2023-03-29T11:30:10.669000Z",
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


class GlobalDreamsTransactCommitTimestamp(BaseModel):
    """Class for Dreams ACM CMPNT CHRNLGY Data"""

    transact_commit_timestamp: Optional[datetime] = Field(
        None,
        alias="transact_commit_timestamp",
        name="Transact Commit Timestamp",
        description="Transact Commit Timestamp",
        example="2023-03-29T15:30:15Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalDreamsAcmTcId(BaseModel):
    """Global Dreams Accommodation TC ID Class"""

    acm_tc_id: int = Field(
        ...,
        alias="ACM_TC_ID",
        name="Accommodation Travel Component Identification",
        description="System generated identification value. The unique identifier for a Travel Component.  The identification value for an accommodation travel component.",
        example=2079447498,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GlobalDreamsTcId(BaseModel):
    """Global Dreams Travel Component Class"""

    tc_id: int = Field(
        ...,
        alias="TC_ID",
        name="Travel Component Identification",
        description="System generated identification value. The unique identifier for a Travel Component.",
        example=32097276021,
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=True,
    )


class GlobalDreamsTpId(BaseModel):
    """Global Dreams Travel Party ID Class"""

    tp_id: int = Field(
        ...,
        alias="TP_ID",
        name="Travel Plan Party Identification",
        description="The unique identification of a travel plan.",
        example=530620488799,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="indirect",
    )


class GlobalDreamsTpsId(BaseModel):
    """Global Dreams Travel Plan Segment ID Class"""

    tps_id: int = Field(
        ...,
        alias="TPS_ID",
        name="Travel Plan Segment Identification",
        description="A unique numeric identifier for a travel plan segment.",
        example=530631525237,
        guest_identifier=True,
        identifier_tag="indirect",
        transaction_identifier=False,
    )
