"""Source Data Contract for Level-N EXTNL_ACCT_LNK"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N EXTNL_ACCT_LNK Data
    """

    EXTNL_ACCT_LNK_ID: int = Field(
        ...,
        alias="EXTNL_ACCT_LNK_ID",
        name="",
        description="""""",
        example=264051,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_SYS_ID: int = Field(
        ...,
        alias="EXTNL_SYS_ID",
        name="",
        description="""""",
        example=27,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTNL_SYS_ENTTY_NM: str = Field(
        ...,
        alias="EXTNL_SYS_ENTTY_NM",
        name="",
        description="""""",
        example="""swid""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NTV_ID: str = Field(
        ...,
        alias="NTV_ID",
        name="",
        description="""""",
        example="""{69D00BE4-ABB0-4E5C-900B-E4ABB0AE5CED}""",
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
        example="""2013-03-07 23:03:59""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""SFLNSAPP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2014-10-08 20:09:20""",
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
    Class for Level N EXTNL_ACCT_LNK Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:05.256397""",
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
        example="""EXTNL_ACCT_LNK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=77906967044149,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWExtnlAcctLnkModel(BaseModel):
    """
    Payload class for Level N EXTNL_ACCT_LNK
    """

    class Config:
        """Payload Level Metadata"""

        title = "External Account Link"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Contains external account links from the GAM Keyring (admission-link-id, transactional-guest-id) that are sent in by the source systems (DREAMS, SNAPP, TITUS) when they first make the request to level N entitlement to make the entitlement."""  # optional
        unique_identifier = ["data.EXTNL_ACCT_LNK_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "EXTNL_ACCT_LNK"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
