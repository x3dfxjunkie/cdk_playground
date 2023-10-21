"""Source Data Contract Template for CAR_CONTRACT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CAR_CONTRACT Data
    """

    MIN_BKG_TO_DEP_DAYS: Optional[int] = Field(
        None,
        alias="MIN_BKG_TO_DEP_DAYS",
        name="",
        description="""Required minimum number of days between the booking date and departure date""",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VOUCHER_CODE: Optional[str] = Field(
        None,
        alias="VOUCHER_CODE",
        name="",
        description="""Voucher Code assigned to the contract""",
        example="""16CALA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_ID: Optional[int] = Field(
        None,
        alias="PROD_DEFN_ID",
        name="",
        description="""NaN""",
        example=2824,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_TEMP_GRP_CODE: Optional[str] = Field(
        None,
        alias="PROD_DEFN_TEMP_GRP_CODE",
        name="",
        description="""NaN""",
        example="""qGBTJzfrTHcyDYYeCmNQ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=5743,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_GROUP_ID: int = Field(
        ...,
        alias="CONTRACT_GROUP_ID",
        name="",
        description="""The system generated id of the contract group""",
        example=56394,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_TYPE: int = Field(
        ...,
        alias="CONTRACT_TYPE",
        name="",
        description="""H = HOTEL, A = APARTMENT, G = GROUP""",
        example=2,
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
        example=8328,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATUS: int = Field(
        ...,
        alias="STATUS",
        name="",
        description="""The TravelBox code of the status of the contract""",
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
        example="""2015-07-29 10:17:18""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_TO: datetime = Field(
        ...,
        alias="VALID_TO",
        name="",
        description="""The end date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""1986-07-15 18:27:42""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_FROM: datetime = Field(
        ...,
        alias="SALES_FROM",
        name="",
        description="""The start date of the valid sales period of this contract""",
        example="""1984-08-04 00:33:22""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_TO: datetime = Field(
        ...,
        alias="SALES_TO",
        name="",
        description="""The end date of the valid sales period of this contract""",
        example="""1983-04-18 07:38:54""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: int = Field(
        ...,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=15059,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_ON: datetime = Field(
        ...,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""1992-10-19 21:19:50""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=15538,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: datetime = Field(
        ...,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""2020-11-16 23:52:55""",
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

    NETT_CURRENCY: Optional[str] = Field(
        None,
        alias="NETT_CURRENCY",
        name="",
        description="""If the contract is a nett contract, this field holds the TravelBox code of the currency in which the costs are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEFAULT_GROSS_CURRENCY: Optional[str] = Field(
        None,
        alias="DEFAULT_GROSS_CURRENCY",
        name="",
        description="""If the contract rate type is CM / GC / GM / GO or NG, this field holds the TravelBox code of the default currency in which prices are defined""",
        example="""USD""",
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

    ERRATA_GROUP: int = Field(
        ...,
        alias="ERRATA_GROUP",
        name="",
        description="""Refers to the errata_group_id of errata_group table when user adds Free Text Conditions in contract level.  The option is available in 'Free Text Conditions' node in contract.""",
        example=277641,
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

    TAX_OVERRIDE: str = Field(
        ...,
        alias="TAX_OVERRIDE",
        name="",
        description="""A flag indicating whether the tax is overriden at the contract ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTRY: str = Field(
        ...,
        alias="COUNTRY",
        name="",
        description="""The TravelBox code of the country for which the rule is defined""",
        example="""US""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DAILY_WEEKLY_RENTAL: str = Field(
        ...,
        alias="DAILY_WEEKLY_RENTAL",
        name="",
        description="""Wether or not a Daily and Weekly rental or not, 1 - Daily and Weekly, 0 - other type""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ONE_WAY_FREE: str = Field(
        ...,
        alias="ONE_WAY_FREE",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIN_AGE: int = Field(
        ...,
        alias="MIN_AGE",
        name="",
        description="""Min age value of age range""",
        example=21,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_AGE: int = Field(
        ...,
        alias="MAX_AGE",
        name="",
        description="""Max age value of age range""",
        example=120,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ISSUE_VOUCHER: str = Field(
        ...,
        alias="ISSUE_VOUCHER",
        name="",
        description="""If the check box is enabled a Voucher will be issued to customer_x000D_
when a booking is made from the contract. 1 - enable , 0 disable""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MULTI_HIRE: str = Field(
        ...,
        alias="MULTI_HIRE",
        name="",
        description="""Specifies whether multiple car hires are enabled for contract or not_x000D_
Enabled - 1, Not enabled - 0_x000D_
""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ONE_WAY_FEE_PAYABLE_LOCALLY: str = Field(
        ...,
        alias="ONE_WAY_FEE_PAYABLE_LOCALLY",
        name="",
        description="""Pay supplier directly. 1 - pay supplier directly, 0 otherwise""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TERMS_CONDITIONS: Optional[str] = Field(
        None,
        alias="TERMS_CONDITIONS",
        name="",
        description="""The terms and conditions associated with the car contract""",
        example="""vxxWhTvDLWBNcQsvIMMT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DAILY_OR_24HOURLY_RATE: str = Field(
        ...,
        alias="DAILY_OR_24HOURLY_RATE",
        name="",
        description="""Specifies whether calculation type is daily or 24hourly rate_x000D_
Daily- 1, 24hourly rate - 0""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAX_DURAITON: Optional[int] = Field(
        None,
        alias="MAX_DURAITON",
        name="",
        description="""Defines the maximum duration allowed by the contract""",
        example=0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PERIODIC_FACTOR: Optional[str] = Field(
        None,
        alias="PERIODIC_FACTOR",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CALCULATION_TYPE: Optional[int] = Field(
        None,
        alias="CALCULATION_TYPE",
        name="",
        description="""Calculation type. 1 - Daily and Weekly,2 - Daily Rate by duration, 3 - Extra day for long durations""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FC: str = Field(
        ...,
        alias="FC",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRACKABLE: Optional[str] = Field(
        None,
        alias="TRACKABLE",
        name="",
        description="""Whether the voucher code is trackable or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CAR_CONTRACT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:47:30.277324""",
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
        example="""CAR_CONTRACT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=10782448202565,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCarContractModel(BaseModel):
    """
    Payload class for TravelBox CAR_CONTRACT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Pass Through Car Contracts"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Pass through view of car contracts"""  # optional
        unique_identifier = ["data.CONTRACT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CAR_CONTRACT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
