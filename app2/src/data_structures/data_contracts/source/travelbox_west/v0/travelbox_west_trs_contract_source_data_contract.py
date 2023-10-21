"""Source Data Contract Template for TRS_CONTRACT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox TRS_CONTRACT Data
    """

    VOUCHER_CODE: Optional[str] = Field(
        None,
        alias="VOUCHER_CODE",
        name="",
        description="""Voucher Code assigned to the contract""",
        example="""16ICTYSSDAHTL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIMESTAMP: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIMESTAMP",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1972-01-24 05:27:13""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_ID: Optional[int] = Field(
        None,
        alias="PROD_DEFN_ID",
        name="",
        description="""NaN""",
        example=638,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROD_DEFN_TEMP_GRP_CODE: Optional[str] = Field(
        None,
        alias="PROD_DEFN_TEMP_GRP_CODE",
        name="",
        description="""NaN""",
        example="""vJjCtqLHBbnRkvfmUviw""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FULFILLMENT_FREQ: str = Field(
        ...,
        alias="FULFILLMENT_FREQ",
        name="",
        description="""Specify the frequency type of gategory, P: per Person, I: Per Item""",
        example="""I""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_ID: int = Field(
        ...,
        alias="CONTRACT_ID",
        name="",
        description="""The system generated id of the contract""",
        example=18312,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTRACT_GROUP_ID: int = Field(
        ...,
        alias="CONTRACT_GROUP_ID",
        name="",
        description="""The system generated id of the contract group""",
        example=55787,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VERSION: int = Field(
        ...,
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
        example=-1,
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
        example="""2020-02-03 20:29:27""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID_TO: datetime = Field(
        ...,
        alias="VALID_TO",
        name="",
        description="""The end date of the valid stay date period of the contract. A booking from this contract needs to be within this range.""",
        example="""2012-09-30 01:19:15""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_FROM: datetime = Field(
        ...,
        alias="SALES_FROM",
        name="",
        description="""The start date of the valid sales period of this contract""",
        example="""2018-10-26 03:37:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_TO: datetime = Field(
        ...,
        alias="SALES_TO",
        name="",
        description="""The end date of the valid sales period of this contract""",
        example="""1984-06-29 19:12:51""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_ON: Optional[datetime] = Field(
        None,
        alias="ENTERED_ON",
        name="",
        description="""The date/time on which this accomodation contract is entered into the system""",
        example="""2010-04-23 09:50:09""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_BY: Optional[int] = Field(
        None,
        alias="ENTERED_BY",
        name="",
        description="""The TravelBox user id of the user who has entered this accomodation contract in to system""",
        example=15195,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_ON: Optional[datetime] = Field(
        None,
        alias="MODIFIED_ON",
        name="",
        description="""The date on which the contract get modified. If no modifications done after the creation, this field holds the contract created date.""",
        example="""2015-02-15 05:42:08""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED_BY: Optional[int] = Field(
        None,
        alias="MODIFIED_BY",
        name="",
        description="""The TravelBox user id of the user who modified the contract. If no modification done after the creation, this field holds the user id of the user who created the contract""",
        example=15097,
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

    PAY_SUPPLIER_GROSS: Optional[str] = Field(
        None,
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
        example=276474,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STAGE_REASON: Optional[str] = Field(
        None,
        alias="STAGE_REASON",
        name="",
        description="""The TravelBox name of the reason for the stage of the contract""",
        example="""MopzohoYmuHirkVQpJtC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_EXEMPT: str = Field(
        ...,
        alias="TAX_EXEMPT",
        name="",
        description="""A flag indicating whether the contract is excempt from tax ( value is 1 ) or not ( value is 0 )""",
        example="""1""",
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

    GROUP_RATES: Optional[str] = Field(
        None,
        alias="GROUP_RATES",
        name="",
        description="""A flag indicating the group rates are enabled for the contract ( value is 1 ) or not ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DATE_WISE_SUPPLIER: Optional[str] = Field(
        None,
        alias="DATE_WISE_SUPPLIER",
        name="",
        description="""Flag for Date wise Suplier Enable (1) or not (0)""",
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
    Class for TravelBox TRS_CONTRACT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:55.164123""",
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
        example="""TRS_CONTRACT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=50536657744588,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestTrsContractModel(BaseModel):
    """
    Payload class for TravelBox TRS_CONTRACT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Transfer Contracts"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """store Transfer and Excursion contract related basic data, this table will populate when we add the transfer or excursion item to the transfer contract"""  # optional
        unique_identifier = ["data.CONTRACT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "TRS_CONTRACT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
