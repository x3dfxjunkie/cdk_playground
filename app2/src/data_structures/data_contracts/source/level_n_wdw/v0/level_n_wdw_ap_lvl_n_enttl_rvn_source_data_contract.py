"""Source Data Contract for Level-N AP_LVL_N_ENTTL_RVN"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for Level N AP_LVL_N_ENTTL_RVN Data
    """

    LVL_N_ENTTL_ID: int = Field(
        ...,
        alias="LVL_N_ENTTL_ID",
        name="",
        description="""""",
        example=466627,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_CHNG_DT: datetime = Field(
        ...,
        alias="LVL_N_ENTTL_CHNG_DT",
        name="",
        description="""""",
        example="""1980-12-04 10:22:23""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_STS_ID: int = Field(
        ...,
        alias="LVL_N_ENTTL_STS_ID",
        name="",
        description="""""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_ENTTL_PRICE: float = Field(
        ...,
        alias="LVL_N_ENTTL_PRICE",
        name="",
        description="""""",
        example=699.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ONLIN_ENGAGEMENT_DT: Optional[datetime] = Field(
        None,
        alias="ONLIN_ENGAGEMENT_DT",
        name="",
        description="""""",
        example="""2011-06-30 16:19:17""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RDMPT_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_RDMPT_DT",
        name="",
        description="""""",
        example="""1982-04-28 18:59:58""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_CAPTR_DT: Optional[datetime] = Field(
        None,
        alias="LVL_N_CAPTR_DT",
        name="",
        description="""""",
        example="""1997-05-16 20:29:32""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RVN_DTS: Optional[datetime] = Field(
        None,
        alias="LVL_N_RVN_DTS",
        name="",
        description="""""",
        example="""1973-01-08 20:41:32""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LVL_N_RVN_STS_ID: Optional[int] = Field(
        None,
        alias="LVL_N_RVN_STS_ID",
        name="",
        description="""""",
        example=1,
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
        example="""1995-12-19 00:03:51""",
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
        example="""1984-12-07 22:13:07""",
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
    Class for Level N AP_LVL_N_ENTTL_RVN Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-11 14:37:07.783714""",
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
        example="""AP_LVL_N_ENTTL_RVN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=51501697768459,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class LevelNWDWApLvlNEnttlRvnModel(BaseModel):
    """
    Payload class for Level N AP_LVL_N_ENTTL_RVN
    """

    class Config:
        """Payload Level Metadata"""

        title = "Annual Passholder Level N Entitlement Revenue"
        stream_name = "prd-use1-guest360-level-n-wdw-stream"
        description = """Contains revenue information (such as price) of the level n entitlement for annual passholders."""  # optional
        unique_identifier = ["data.LVL_N_ENTTL_ID", "data.LVL_N_ENTTL_CHNG_DT"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "AP_LVL_N_ENTTL_RVN"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
