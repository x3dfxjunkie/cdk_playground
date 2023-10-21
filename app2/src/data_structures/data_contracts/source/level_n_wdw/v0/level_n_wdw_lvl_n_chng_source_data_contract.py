"""Source Data Contract for Level-N LVL_N_CHNG"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N LVL_N_CHNG Data
    """

    LVL_N_ENTTL_ID: int = Field(
        ...,
        alias="LVL_N_ENTTL_ID",
        name="",
        description="""""",
        example=215051,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_CHNG_DT: datetime = Field(
        ...,
        alias="LVL_N_ENTTL_CHNG_DT",
        name="",
        description="""""",
        example="""1974-05-17 11:58:48""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_STS_ID: int = Field(
        ...,
        alias="LVL_N_ENTTL_STS_ID",
        name="",
        description="""""",
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RL_ID: int = Field(
        ...,
        alias="LVL_N_RL_ID",
        name="",
        description="""""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_LNK_ID: str = Field(
        ...,
        alias="LVL_N_LNK_ID",
        name="",
        description="""""",
        example="""8AB2A36448572220014857241A7E0009""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_STRT_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_ENTTL_STRT_DT",
        name="",
        description="""""",
        example="""1972-06-04 10:01:32""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_PLAN_ARVL_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_PLAN_ARVL_DT",
        name="",
        description="""""",
        example="""2002-09-19 12:30:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_END_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_ENTTL_END_DT",
        name="",
        description="""""",
        example="""1987-10-21 15:06:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_EXP_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_ENTTL_EXP_DT",
        name="",
        description="""""",
        example="""1986-12-08 08:48:23""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_UPDT_DTS: Optional[datetime] = Field(
        None,
        alias="LVL_N_UPDT_DTS",
        name="",
        description="""""",
        example="""1990-02-28 03:17:29""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_DELEGATED_UPDT_USR_ID: Optional[str] = Field(
        None,
        alias="LVL_N_DELEGATED_UPDT_USR_ID",
        name="",
        description="""""",
        example="""ogEAcofCDAvuqFLklSSu""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_DELEGATED_UPDT_DTS: Optional[datetime] = Field(
        None,
        alias="LVL_N_DELEGATED_UPDT_DTS",
        name="",
        description="""""",
        example="""1999-10-20 07:27:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SETTL_DT: Optional[datetime] = Field(
        None,
        alias="SETTL_DT",
        name="",
        description="""""",
        example="""1986-09-29 08:28:49""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ONLN_ENGAGEMENT_DT: Optional[datetime] = Field(
        None,
        alias="ONLN_ENGAGEMENT_DT",
        name="",
        description="""""",
        example="""2018-01-16 12:04:37""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""SFLNSAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""1978-06-18 21:11:27""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""S-15022""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2014-12-31 03:05:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LGCL_DEL_IN: str = Field(
        ...,
        alias="LGCL_DEL_IN",
        name="",
        description="""""",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_CAPTR_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_CAPTR_DT",
        name="",
        description="""""",
        example="""1997-05-18 00:22:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RDMPT_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_RDMPT_DT",
        name="",
        description="""""",
        example="""1986-12-31 15:01:27""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RVN_STS_ID: Optional[int] = Field(
        None,
        alias="LVL_N_RVN_STS_ID",
        name="",
        description="""""",
        example=6,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RVN_DTS: Optional[datetime] = Field(
        None,
        alias="LVL_N_RVN_DTS",
        name="",
        description="""""",
        example="""2008-09-06 11:12:20""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RVN_IN: Optional[str] = Field(
        None,
        alias="LVL_N_RVN_IN",
        name="",
        description="""""",
        example="""N""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for Level N LVL_N_CHNG Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:25.468327""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    record_type: str = Field(
        ...,
        alias="record-type",
        name="",
        description="""Type of record""",
        example="""data""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    operation: str = Field(
        ...,
        alias="operation",
        name="",
        description="""Type of operation [insert, delete, update]""",
        example="""update""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    partition_key_type: str = Field(
        ...,
        alias="partition-key-type",
        name="",
        description="""Partition key""",
        example="""schema-table""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schema_name: str = Field(
        ...,
        alias="schema-name",
        name="",
        description="""Name of schema""",
        example="""SFLNSMD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""LVL_N_CHNG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=83183805994381,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWLvlNChngModel(BaseModel):
    """
    Payload class for Level N LVL_N_CHNG
    """

    class Config:
        """Payload Level Metadata"""

        title = "Level N Change"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Captures all changes for a Level N Entitlement - such as when the Guest changes their arrival date, or when the status of the entitlement changes."""  # optional
        unique_identifier = ["data.LVL_N_ENTTL_ID", "data.LVL_N_ENTTL_CHNG_DT"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "LVL_N_CHNG"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
