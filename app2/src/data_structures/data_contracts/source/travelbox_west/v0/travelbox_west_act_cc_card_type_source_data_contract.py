"""Source Data Contract Template for ACT_CC_CARD_TYPE"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACT_CC_CARD_TYPE Data
    """

    CODE: str = Field(
        ...,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""DVA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: str = Field(
        ...,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Disney Vacation Account""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MERCHANT_FEE: Optional[float] = Field(
        None,
        alias="MERCHANT_FEE",
        name="",
        description="""The merchant fee amount of the credit card""",
        example=21916.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MERCHANT_FEE_CUST: Optional[float] = Field(
        None,
        alias="MERCHANT_FEE_CUST",
        name="",
        description="""Refers to the value which is charged to the customer when a value is added""",
        example=35509.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAXABLE: str = Field(
        ...,
        alias="TAXABLE",
        name="",
        description="""Whether accounting rule is applicable for taxable items or non taxable items""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACT_CC_CARD_TYPE Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:48.806061""",
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
        example="""ACT_CC_CARD_TYPE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=52094092584575,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestActCcCardTypeModel(BaseModel):
    """
    Payload class for TravelBox ACT_CC_CARD_TYPE
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accounts Credit Card Card Type"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store information of Credit Cards. The values are setup in 'Setup->Card Types' in
the Accounts Client"""  # optional
        unique_identifier = ["data.CODE"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ACT_CC_CARD_TYPE"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
