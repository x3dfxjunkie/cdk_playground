"""Source Data Contract Template for INS_CONTRACT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox INS_CONTRACT Data
    """

    ENTERED_ON: Optional[datetime] = Field(
        None,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""2014-09-22 22:56:52""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=17592,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""1996-06-14 07:06:39""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FAMILY_POLICY: str = Field(
        ...,
        alias="FAMILY_POLICY",
        name="",
        description="""Specifies whether contract type is set as Family Policy or not_x000D_
Family policy - 1, Not - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ANNUAL_POLICY: str = Field(
        ...,
        alias="ANNUAL_POLICY",
        name="",
        description="""Specifies whether contract type is set as Annual Policy or not_x000D_
Annual policy - 1, Not - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NET_CURRENCY: Optional[str] = Field(
        None,
        alias="NET_CURRENCY",
        name="",
        description="""IfthecontractratetypeisGM/NGorNM,thisfieldholdstheTravelBoxcodeofthecurrencyinwhichthecostsaredefined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RATE_TYPE: str = Field(
        ...,
        alias="RATE_TYPE",
        name="",
        description="""NM = NETT AND MARKUP, GC = GROSS AND COMMISSION, NG = GROSS OEM_sqlplus_input_finished, GO = GROSS ONLY""",
        example="""NG""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GROSS_DEFAULT_CURRENCY: Optional[str] = Field(
        None,
        alias="GROSS_DEFAULT_CURRENCY",
        name="",
        description="""If the contract is a gross contract, this field holds the TravelBox code of the currency in which the prices are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMMISSION: Optional[float] = Field(
        None,
        alias="COMMISSION",
        name="",
        description="""The commission percentage recieved by the tour operator""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_SUPPLIER_GROSS: str = Field(
        ...,
        alias="PAY_SUPPLIER_GROSS",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ERRATA_GROUP: Optional[int] = Field(
        None,
        alias="ERRATA_GROUP",
        name="",
        description="""Refers to the errata_group_id of errata_group table when user adds Free Text Conditions in contract level.  The option is available in 'Free Text Conditions' node in contract.""",
        example=348304,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POLICY_TYPE: str = Field(
        ...,
        alias="POLICY_TYPE",
        name="",
        description="""The insurance policy type code as defined in policy types""",
        example="""TI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_OVERRIDE: str = Field(
        ...,
        alias="TAX_OVERRIDE",
        name="",
        description="""A flag indicating whether the tax is overriden at the contract ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXCEMPT: str = Field(
        ...,
        alias="TAX_EXCEMPT",
        name="",
        description="""Specifies whether to disable any taxes from being applied to the contract_x000D_
Disable - 1, Not disable - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE_REASON: Optional[str] = Field(
        None,
        alias="STAGE_REASON",
        name="",
        description="""The TravelBox name of the reason for the stage of the contract""",
        example="""pSUUEvzpeuSdBPyIsIbY""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_DURATION: Optional[int] = Field(
        None,
        alias="MAX_DURATION",
        name="",
        description="""The maximum duration of the holiday that is covered from insurance policy""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_PRICE_ALLOWED: Optional[float] = Field(
        None,
        alias="MAX_PRICE_ALLOWED",
        name="",
        description="""Maximum Price of the package""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIR_ONLY: str = Field(
        ...,
        alias="AIR_ONLY",
        name="",
        description="""Specifies whether the contract insurance policy is air only or not_x000D_
Air only - 1, Not air only - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    UNIT_COST: str = Field(
        ...,
        alias="UNIT_COST",
        name="",
        description="""Flag to indicate if the fare is specified per person ( 0 ) or as a unit cost ( 1 ) when fare defined method is selected as 'Amount'""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PERCENTAGE: str = Field(
        ...,
        alias="PERCENTAGE",
        name="",
        description="""GET DISCOUNTED NIGHTS NOT FREE NIGHTS. IN THIS CASE THE DISCOUNT AMOUNT IS STORED HERE""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WINTER_SPORTS: str = Field(
        ...,
        alias="WINTER_SPORTS",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUPPLIER_REF: Optional[str] = Field(
        None,
        alias="SUPPLIER_REF",
        name="",
        description="""Insurance policy in supplier point of view""",
        example="""SDA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RISK_NO: Optional[str] = Field(
        None,
        alias="RISK_NO",
        name="",
        description="""Policy Risk reference number is used to identify an insurance policy from the supplier point of view""",
        example="""lGtLLPapSIfysHQYYnBI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHER_CODE: Optional[str] = Field(
        None,
        alias="VOUCHER_CODE",
        name="",
        description="""Voucher Code assigned to the contract""",
        example="""BYyccBhalkkKtEzxspno""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1976-02-14 05:48:18""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_ID: Optional[int] = Field(
        None,
        alias="PROD_DEFN_ID",
        name="",
        description="""NaN""",
        example=1643,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_TEMP_GRP_CODE: Optional[str] = Field(
        None,
        alias="PROD_DEFN_TEMP_GRP_CODE",
        name="",
        description="""NaN""",
        example="""CCfuYmxDqsvEhgztyPhW""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=3975,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_GROUP: int = Field(
        ...,
        alias="CONTRACT_GROUP",
        name="",
        description="""System generated id of insurance contract group""",
        example=91946,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VERSION: Optional[int] = Field(
        None,
        alias="VERSION",
        name="",
        description="""The version of the contract""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PARENT_VERSION: Optional[int] = Field(
        None,
        alias="PARENT_VERSION",
        name="",
        description="""Deprecated""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_STATUS: int = Field(
        ...,
        alias="CONTRACT_STATUS",
        name="",
        description="""The Travelbox code of the status of the contract""",
        example=503,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE: int = Field(
        ...,
        alias="STAGE",
        name="",
        description="""The TravelBox code of the stage of the contract""",
        example=50301,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_FROM: datetime = Field(
        ...,
        alias="VALID_FROM",
        name="",
        description="""The start date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""1976-01-30 11:25:21""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_TO: datetime = Field(
        ...,
        alias="VALID_TO",
        name="",
        description="""The end date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""1993-05-31 05:05:24""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_FROM: datetime = Field(
        ...,
        alias="SALES_FROM",
        name="",
        description="""The start date of the valid sales period of this contract""",
        example="""2013-07-02 03:01:45""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_TO: datetime = Field(
        ...,
        alias="SALES_TO",
        name="",
        description="""The end date of the valid sales period of this contract""",
        example="""2002-12-23 07:14:33""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: int = Field(
        ...,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=17592,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox INS_CONTRACT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:49:16.070515""",
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
        example="""INS_CONTRACT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=50260506533969,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastInsContractModel(BaseModel):
    """
    Payload class for TravelBox INS_CONTRACT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Pass Through Insurance Contracts"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """Pass through view of insurance contracts"""  # optional
        unique_identifier = ["data.CONTRACT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "INS_CONTRACT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
