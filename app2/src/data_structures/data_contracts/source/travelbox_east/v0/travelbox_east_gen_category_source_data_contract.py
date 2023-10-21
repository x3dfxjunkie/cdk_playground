"""Source Data Contract Template for GEN_CATEGORY"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox GEN_CATEGORY Data
    """

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2006-06-15 05:22:15""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHER_CODE: Optional[str] = Field(
        None,
        alias="VOUCHER_CODE",
        name="",
        description="""Voucher Code assigned to the contract""",
        example="""kEZtQxlxyAGJzSbzlwqW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FULFILLMENT_FREQ: Optional[str] = Field(
        None,
        alias="FULFILLMENT_FREQ",
        name="",
        description="""Specify the frequency type of gategory, P: per Person, I: Per Item""",
        example="""P""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOS_VARIATION_CODE: Optional[str] = Field(
        None,
        alias="LOS_VARIATION_CODE",
        name="",
        description="""NaN""",
        example="""WcpJEYtAxMzhZArQqkhE""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DYNAMIC: str = Field(
        ...,
        alias="DYNAMIC",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DYNAMIC_NAME: Optional[str] = Field(
        None,
        alias="DYNAMIC_NAME",
        name="",
        description="""NaN""",
        example="""JDlZYINAsbRDIHLKkYok""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DAILY: str = Field(
        ...,
        alias="DAILY",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SINGLE_DAY: str = Field(
        ...,
        alias="SINGLE_DAY",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=10332,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CATEGORY_NO: int = Field(
        ...,
        alias="CATEGORY_NO",
        name="",
        description="""Refer to CATEGORY_NO in GEN_CATEGORY table""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CODE: Optional[str] = Field(
        None,
        alias="CODE",
        name="",
        description="""The TravelBox code of the board basis""",
        example="""TRANSFEE30""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME: Optional[str] = Field(
        None,
        alias="NAME",
        name="",
        description="""The name of the contract type""",
        example="""Transportation Fee Disney Cup""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ERRATA_GROUP: Optional[int] = Field(
        None,
        alias="ERRATA_GROUP",
        name="",
        description="""Refers to the errata_group_id of errata_group table when user adds Free Text Conditions in contract level.  The option is available in 'Free Text Conditions' node in contract.""",
        example=277638,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PREPAID: str = Field(
        ...,
        alias="PREPAID",
        name="",
        description="""SOME PASSES ARE PREPAID. FOR EXAMPLE GOWAY MAY BUY 100 PASSES FOR 30 EACH. BOOKING STATUS SHOULD BE CONFIRMED AND SUPPLIER STATUS SHOULD BE SET TO PAID.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_ADULTS: Optional[int] = Field(
        None,
        alias="MAX_ADULTS",
        name="",
        description="""The maximum number of adults a booking from this category can have""",
        example=50,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_CHILD: Optional[int] = Field(
        None,
        alias="MAX_CHILD",
        name="",
        description="""Maximum number of children that needs to satisfy the Rule""",
        example=10,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""Transportation Fee for Disney Cup""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_INFANT: Optional[int] = Field(
        None,
        alias="MAX_INFANT",
        name="",
        description="""Maximum number of infants that needs to satisfy the Rule""",
        example=5,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_ADULTS: Optional[int] = Field(
        None,
        alias="MIN_ADULTS",
        name="",
        description="""The minimum number of adults a booking from this category needs to have""",
        example=6986,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COST_TYPE: Optional[str] = Field(
        None,
        alias="COST_TYPE",
        name="",
        description="""PS - Per Stay, PN - Per Night""",
        example="""PS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_TEENS: Optional[str] = Field(
        None,
        alias="MAX_TEENS",
        name="",
        description="""The maximum number of teens a booking from this category can have""",
        example="""PrFXuFvRaHmsHXsCWFwS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_BEFORE: Optional[int] = Field(
        None,
        alias="VALID_BEFORE",
        name="",
        description="""The number of days the bokking should be in the Category""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox GEN_CATEGORY Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:47:54.860283""",
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
        example="""GEN_CATEGORY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=10528943449892,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastGenCategoryModel(BaseModel):
    """
    Payload class for TravelBox GEN_CATEGORY
    """

    class Config:
        """Payload Level Metadata"""

        title = "Generic Category"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """Contract level categorized product type(s) basic information defined under the selected element group in contract main panel. Set up at 'Categories' branch of a contract tree in Contract Loading Client"""  # optional
        unique_identifier = ["data.CONTRACT_ID", "data.CATEGORY_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "GEN_CATEGORY"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
