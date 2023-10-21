"""CME Global dataclass: for key fields and classes that will be repeated throughout CME only"""
from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

"""Dataclasses that need references to this will need to import the global_cme_source_data_contract.py file"""


class GlobalCMEWDWSchemaName(Enum):
    """Global CME schema name"""

    AWAKENING = "awakening"


class GlobalCMEWDWTableName(Enum):
    """Global CME list of tables"""

    AUDIT_INV_BUCKET_DATE_TIME = "audit_inv_bucket_date_time"
    BATCH_JOB = "batch_job"
    BATCH_JOB_DETAIL = "batch_job_detail"
    CHECKPOINT_LOCATION = "checkpoint_location"
    DESTINATION = "destination"
    INVENTORY_PRODUCT = "inventory_product"
    INV_BUCKET = "inv_bucket"
    INV_BUCKET_DATE_TIME = "inv_bucket_date_time"
    NODE_ID = "node_id"
    PARK = "park"
    PENALIZATION = "penalization"
    PRODUCT_CATEGORY = "product_category"
    PRODUCT_TYPE_PRODUCT_CATEGORY = "product_type_product_category"
    RESERVATION = "reservation"
    RESERVATION_COMMUNICATION = "reservation_communication"
    RESERVATION_MERGE_BCK = "reservation_merge_bck"
    RESERVATION_NOTE = "reservation_note"
    RES_BY_DATES_STATS = "res_by_dates_stats"
    RES_GUEST_LINKS = "res_guest_links"
    RES_SUMMARY_STATS = "res_summary_stats"
    RULE_CONSTRAINT = "rule_constraint"
    RULE_GROUP = "rule_group"
    RULE_SETTING = "rule_setting"
    SAP_CAST_MEMBER = "sap_cast_member"
    SHEDLOCK = "shedlock"
    SWIDS_TO_MERGE = "swids_to_merge"
    TICKET_CODE_MAPPING = "ticket_code_mapping"
    USERS = "users"
    PENDING_CANCEL_JOB = "pending_cancel_job"


class GlobalCMEWDWOperation(Enum):
    """CME Data Operation type"""

    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"
    LOAD = "load"


class GlobalCMEWDWMetadata(BaseModel):
    """Global CME Metadata Class Data"""

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="Record Timestamp",
        description="",
        example="2023-04-17T13:33:15.230Z",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    record_type: str = Field(
        ...,
        alias="record-type",
        name="Record Type",
        description="Record Type",
        example="data",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    operation: GlobalCMEWDWOperation = Field(
        ...,
        alias="operation",
        name="Operation",
        description="Specifies record operation as Insert or Update",
        example="Update",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="Partition Key Type",
        description="Partition Key Type",
        example="schema-table",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    schema_name: GlobalCMEWDWSchemaName = Field(
        ...,
        alias="schema-name",
        name="Schema Name",
        description="Database schema name storing the record",
        example="awakening",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    table_name: GlobalCMEWDWTableName = Field(
        ...,
        alias="table-name",
        name="Table Name",
        description="Database table name storing the record",
        example="park",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
    )
    transaction_id: Optional[str] = Field(
        None,
        alias="transaction-id",
        name="Transaction Identifier",
        description="Database transaction identifier for the specific record",
        example="806749481293512",
        guest_identifier=False,
        identifier_tag="",
        transaction_identifier=False,
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
