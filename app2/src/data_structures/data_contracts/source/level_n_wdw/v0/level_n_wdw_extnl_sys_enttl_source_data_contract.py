"""Source Data Contract for Level-N EXTNL_SYS_ENTTL"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N EXTNL_SYS_ENTTL Data
    """

    EXTNL_SYS_LVL_N_ENTTL_ID: str = Field(
        ...,
        alias="EXTNL_SYS_LVL_N_ENTTL_ID",
        name="",
        description="""""",
        example="""2C91808279F8D8540179F8D8BCCB0000""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_ID: int = Field(
        ...,
        alias="LVL_N_ENTTL_ID",
        name="",
        description="""""",
        example=5661515,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_SYS_ID: int = Field(
        ...,
        alias="EXTNL_SYS_ID",
        name="",
        description="""""",
        example=2009,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_SYS_ENTTY_NM: str = Field(
        ...,
        alias="EXTNL_SYS_ENTTY_NM",
        name="",
        description="""""",
        example="""Ticketing""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_SYS_ENTTL_ID: str = Field(
        ...,
        alias="EXTNL_SYS_ENTTL_ID",
        name="",
        description="""""",
        example="""21300010062103525""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""f-sflnsmd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""2009-07-07 01:21:31""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""f-sflnsmd""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2021-04-26 00:17:14""",
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


class Metadata(BaseModel):
    """
    Class for Level N EXTNL_SYS_ENTTL Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:11.405728""",
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
        example="""EXTNL_SYS_ENTTL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=93082369186111,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWExtnlSysEnttlModel(BaseModel):
    """
    Payload class for Level N EXTNL_SYS_ENTTL
    """

    class Config:
        """Payload Level Metadata"""

        title = "External System Entitlement"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Contains external system entitlement names and ID such as TDSSN, ATS Reservation ID of the Level N entitlement sent in by the external systems that talk to Level N."""  # optional
        unique_identifier = ["data.EXTNL_SYS_LVL_N_ENTTL_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXTNL_SYS_ENTTL"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
