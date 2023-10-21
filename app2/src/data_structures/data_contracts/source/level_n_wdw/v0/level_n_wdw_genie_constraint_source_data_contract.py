"""Source Data Contract for Level-N GENIE_CONSTRAINT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N GENIE_CONSTRAINT Data
    """

    CONSTRAINT_ID: str = Field(
        ...,
        alias="CONSTRAINT_ID",
        name="",
        description="""""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CNTNT_CACHE_ID: int = Field(
        ...,
        alias="CNTNT_CACHE_ID",
        name="",
        description="""""",
        example=501855592,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONSTRAINT_TYPE: str = Field(
        ...,
        alias="CONSTRAINT_TYPE",
        name="",
        description="""""",
        example="""THEME_PARK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONSTRAINT_VALUES: str = Field(
        ...,
        alias="CONSTRAINT_VALUES",
        name="",
        description="""""",
        example="""80007944,80007838,80007998,80007823""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_USR_ID: str = Field(
        ...,
        alias="CREATE_USR_ID",
        name="",
        description="""""",
        example="""f-sflnsmd@%""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREATE_DTS: datetime = Field(
        ...,
        alias="CREATE_DTS",
        name="",
        description="""""",
        example="""1998-02-01 14:37:19""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_USR_ID: str = Field(
        ...,
        alias="UPDT_USR_ID",
        name="",
        description="""""",
        example="""f-sflnsmd@%""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UPDT_DTS: datetime = Field(
        ...,
        alias="UPDT_DTS",
        name="",
        description="""""",
        example="""2007-08-28 21:35:32""",
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
    Class for Level N GENIE_CONSTRAINT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:38:14.280204""",
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
        example="""GENIE_CONSTRAINT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=60388835053679,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWGenieConstraintModel(BaseModel):
    """
    Payload class for Level N GENIE_CONSTRAINT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Genie Constraint"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Reference table for the 'constraints' in Level N. A constraint is currently used for the Genie+ park specific products and contains what entitlements can be used in which park. For example, there are entitlements for Magic Kingdom only or for All 4 WDW parks."""  # optional
        unique_identifier = ["data.CONSTRAINT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GENIE_CONSTRAINT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
