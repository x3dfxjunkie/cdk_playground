"""AvailSE Global dataclass: for key fields and classes that will be repeated throughout AvailSE only"""
from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

"""Dataclasses that need references to this will need to import the global_availse file"""


class GlobalAvailSESchemaName(Enum):
    """Global AvailSE schema name"""

    AVAILSE = "availse"  # Schema for the database - Check with Chiu. Something with Source DB


class GlobalAvailSETableName(Enum):
    """Global AvailSE list of tables"""

    BID_PRICE_CTRL = "bid_price_ctrl"
    BUILT_INVTRY_ADJ_SERIES = "built_invtry_adj_series"
    BUILT_INVTRY_ADJ = "built_invtry_adj"
    BUILT_INVTRY = "built_invtry"
    CHAN_MTRX = "chan_mtrx"
    COMNCTN_CHAN = "comnctn_chan"
    CPCTY = "cpcty"
    DOW = "dow"
    DSNY_CTRL_CONFIG = "dsny_ctrl_config"
    FREEZE_FSELL_INVTRY = "freeze_fsell_invtry"
    FREEZE = "freeze"
    FSELL_INVTRY = "fsell_invtry"
    INVTRY_HRZN = "invtry_hrzn"
    INVTRY_UPDT_ADT = "invtry_updt_adt"
    LST_RELEASE_RUN = "lst_release_run"
    METRIC_ADT = "metric_adt"
    OVRBK_ALRT_TRACK = "ovrbk_alrt_track"
    PHYS_RSRC = "phys_rsrc"
    PHYS_RSRC_STS = "phys_rsrc_sts"
    PROD_RSRVBL_RSRC_XREF = "prod_rsrvbl_rsrc_xref"
    PRTCPNT_TMPLT_INVTRY = "prtcpnt_tmplt_invtry"
    PRTCPNT_TMPLT_SCH = "prtcpnt_tmplt_sch"
    PRTCPNT_TMPLT = "prtcpnt_tmplt"
    RSN = "rsn"
    RSN_TYP = "rsn_typ"
    RSRC_FEAT = "rsrc_feat"
    RSRC_FEAT_TYP = "rsrc_feat_typ"
    RSRC_STS = "rsrc_sts"
    RSRC_TYP = "rsrc_typ"
    RSRT_GST_HLDBCK_CONFIG = "rsrt_gst_hldbck_config"
    RSRVBL_RSRC_CPCTY = "rsrvbl_rsrc_cpcty"
    RSRVBL_RSRC_FEAT = "rsrvbl_rsrc_feat"
    RSRVBL_RSRC_LNK = "rsrvbl_rsrc_lnk"
    RSRVBL_RSRC = "rsrvbl_rsrc"
    RSRVBL_RSRC_TYP = "rsrvbl_rsrc_typ"
    RSRVBL_RSRC_UOM = "rsrvbl_rsrc_uom"
    SLS_CHAN = "sls_chan"
    TBL_COMBO_INVTRY_RULE = "tbl_combo_invtry_rule"
    TBL_COMBO_QTY_RULE = "tbl_combo_qty_rule"
    TBL_COMBO_UTLZ_RULE = "tbl_combo_utlz_rule"
    UOM = "uom"
    UOM_TYP = "uom_typ"


class GlobalCMEDLROperation(Enum):
    """AvailSE Data Operation type"""

    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"
    LOAD = "load"


class GlobalAvailSEMetadata(BaseModel):
    """Global AvailSE Metadata Class Data"""

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
