"""Source Data Contract Template for CONTRACT_GROUP"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CONTRACT_GROUP Data
    """

    GROUP_ID: int = Field(
        ...,
        alias="GROUP_ID",
        name="",
        description="""System generated group id""",
        example=55445,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_ID: int = Field(
        ...,
        alias="SUPPLIER_ID",
        name="",
        description="""Not in DSN Scope""",
        example=29943,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REFERENCE: str = Field(
        ...,
        alias="REFERENCE",
        name="",
        description="""CODE TO IDENTIFY THE DISCOUNT (OPTIONAL)""",
        example="""2016_TLEGOSEA_WDTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""rhciLSogeVqIbbyTWXKw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMPANY: str = Field(
        ...,
        alias="COMPANY",
        name="",
        description="""The TravelBox code of the company for which the limit is defined for""",
        example="""WDTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DIVISION: Optional[str] = Field(
        None,
        alias="DIVISION",
        name="",
        description="""The TravelBox code of the division for which the limit is defined for""",
        example="""WDTCDLR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESTINATION: Optional[int] = Field(
        None,
        alias="DESTINATION",
        name="",
        description="""Destination location code for flight booking items""",
        example=9108,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT: str = Field(
        ...,
        alias="PRODUCT",
        name="",
        description="""Selected product type codes_x000D_
""",
        example="""GEN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDON: Optional[str] = Field(
        None,
        alias="ADDON",
        name="",
        description="""For the generic contracts, a flag to indicate whether the contract is an addon or not.""",
        example="""TRDQfhitWeRCsrxLtmXO""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDON_PRIORITY: Optional[int] = Field(
        None,
        alias="ADDON_PRIORITY",
        name="",
        description="""If the contract is an addon, addon priority.""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_DEPARTURE: Optional[str] = Field(
        None,
        alias="PRE_DEPARTURE",
        name="",
        description="""For the generic contracts, a flag to indicate whether the contract is pre departure or not.""",
        example="""jeVwCaegZCOGtrpqrgjc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_SOURCE: int = Field(
        ...,
        alias="CONTRACT_SOURCE",
        name="",
        description="""Deprecated""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2016-11-08 22:30:22""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""2016_TLEGOSEA_WDTC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CONTRACT_GROUP Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:43:53.053670""",
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
        example="""TBX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="""Name of table""",
        example="""CONTRACT_GROUP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=81821818242215,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestContractGroupModel(BaseModel):
    """
    Payload class for TravelBox CONTRACT_GROUP
    """

    class Config:
        """Payload Level Metadata"""

        title = "Contract Group"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This contains the contract group defined based on a unique REFERENCE. There can be one or more version(s) under different contract ID from the same contract group in the relavent product contract table ( e.g: ACC_CONTRACT, TRS_CONTRACT). User can set up a contract group from any product client (Accomadation Client, Transfer Client)."""  # optional
        unique_identifier = ["data.GROUP_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CONTRACT_GROUP"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
