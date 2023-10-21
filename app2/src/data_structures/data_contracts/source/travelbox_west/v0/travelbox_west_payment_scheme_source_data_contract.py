"""Source Data Contract Template for PAYMENT_SCHEME"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox PAYMENT_SCHEME Data
    """

    PRE_AMOUNT: Optional[float] = Field(
        None,
        alias="PRE_AMOUNT",
        name="",
        description="""Amount of pre payment""",
        example=100.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_AMOUNT_TYPE: Optional[str] = Field(
        None,
        alias="PRE_AMOUNT_TYPE",
        name="",
        description="""What type of pre payment should can be done.  A - Amount, P - Presentage, N - for Nights""",
        example="""P""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_CURRENCY: Optional[str] = Field(
        None,
        alias="PRE_CURRENCY",
        name="",
        description="""Foreign key to field CODE in the CURRENCY table""",
        example="""AfrzuslgwzAtKtGjzXqC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_PAYMENT_METHOD: str = Field(
        ...,
        alias="POST_PAYMENT_METHOD",
        name="",
        description="""Post payment method.  B - Before departure, I - After Invoice, D - After deposit, G - After booking""",
        example="""X""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_PAYMENT_TYPE: str = Field(
        ...,
        alias="POST_PAYMENT_TYPE",
        name="",
        description="""Post payment type, M - Mothly payment, D - Payment on date, P - Monthly payment on a date""",
        example="""X""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_PAYMENT_MONTH_NO: Optional[int] = Field(
        None,
        alias="POST_PAYMENT_MONTH_NO",
        name="",
        description="""Month which the payment should be settled. Depend on the choices of the balanced payment section of the payment scheme setup.""",
        example=1597,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_DATE: Optional[int] = Field(
        None,
        alias="POST_DATE",
        name="",
        description="""Date that the dispatch document is posted""",
        example=4693,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INV_DUE_PERIOD: Optional[int] = Field(
        None,
        alias="INV_DUE_PERIOD",
        name="",
        description="""Specify the number of days to settle the due payment to the supplier after receiving the invoice.""",
        example=644,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CHECKOUT_DATE_CONSIDER: Optional[str] = Field(
        None,
        alias="CHECKOUT_DATE_CONSIDER",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTO_PAYMENT: str = Field(
        ...,
        alias="AUTO_PAYMENT",
        name="",
        description="""Flag to indicate this payment is auto payment or not""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INTERFACE_CODE: Optional[str] = Field(
        None,
        alias="INTERFACE_CODE",
        name="",
        description="""Interface code that payment recode should be posted""",
        example="""FI001D""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPO_AFT_BKG_BEF_DEPT: Optional[str] = Field(
        None,
        alias="DEPO_AFT_BKG_BEF_DEPT",
        name="",
        description="""If the deposit payment selected as after booking, there is a choice of selecting 'But before departure', if that is selected this will be set to 1, otherwise 0.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BAL_AFT_BKG_BEF_DEPT: Optional[str] = Field(
        None,
        alias="BAL_AFT_BKG_BEF_DEPT",
        name="",
        description="""If the balance payment selected as after booking, there is a choice of selecting 'But before departure', if that is selected this will be set to 1, otherwise 0.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYMENT_MEDIA: Optional[str] = Field(
        None,
        alias="PAYMENT_MEDIA",
        name="",
        description="""if the virutal creditd card is enable from the configuration, this will be filled with the available transaction types""",
        example="""yanLzdHldJSJAJOjVyYN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_SCHEME_ID: int = Field(
        ...,
        alias="PAY_SCHEME_ID",
        name="",
        description="""Primary key of the table""",
        example=2773,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYMENT_REF: str = Field(
        ...,
        alias="PAYMENT_REF",
        name="",
        description="""Deprecated""",
        example="""TRAVELEX 44 DAYS PRIOR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESCRIPTION: Optional[str] = Field(
        None,
        alias="DESCRIPTION",
        name="",
        description="""The TravelBox name of the board basis""",
        example="""Pay Travelex 44 days prior to guest departure""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT: Optional[str] = Field(
        None,
        alias="PRODUCT",
        name="",
        description="""Selected product type codes_x000D_
""",
        example="""INS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_PAYMENT_METHOD: Optional[str] = Field(
        None,
        alias="PRE_PAYMENT_METHOD",
        name="",
        description="""Pre payment method.  B - Before departure, I - After Invoice, D - After deposit, G - After booking""",
        example="""B""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_PAYMENT_TYPE: Optional[str] = Field(
        None,
        alias="PRE_PAYMENT_TYPE",
        name="",
        description="""Deprecated""",
        example="""tRuRbOlLWbhrxbShYEAp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRE_DATE: Optional[int] = Field(
        None,
        alias="PRE_DATE",
        name="",
        description="""Days relevant for the deposit payment can be_x000D_
specified._x000D_
Ex:_x000D_
If the number of Days is 3, and Å‚efore_x000D_
Departure? radio button is selected, the deposit_x000D_
should be paid to the supplier 3 days before the_x000D_
departure date. """,
        example=44,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox PAYMENT_SCHEME Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:45:13.769571""",
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
        example="""PAYMENT_SCHEME""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=18484798511486,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestPaymentSchemeModel(BaseModel):
    """
    Payload class for TravelBox PAYMENT_SCHEME
    """

    class Config:
        """Payload Level Metadata"""

        title = "Payment Scheme"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """Globally defined payment scheme informations are stored here. Set up under 'Payment Schemes' in 'Setup' menu of Supplier Client"""  # optional
        unique_identifier = ["data.PAY_SCHEME_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "PAYMENT_SCHEME"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
