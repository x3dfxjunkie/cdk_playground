"""Source Data Contract Template for ACT_CLIENT_CC_RECEIPT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACT_CLIENT_CC_RECEIPT Data
    """

    FUTURE_PAYMENT: Optional[str] = Field(
        None,
        alias="FUTURE_PAYMENT",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CARD_TOKEN: Optional[str] = Field(
        None,
        alias="CARD_TOKEN",
        name="",
        description="""NaN""",
        example="""ptlkiQSPYFYnuRLgpFbu""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOKEN_VAULT: Optional[str] = Field(
        None,
        alias="TOKEN_VAULT",
        name="",
        description="""NaN""",
        example="""epaHBqoHZRbUyxyhTuum""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXT_TRANSACTION_ID: Optional[str] = Field(
        None,
        alias="EXT_TRANSACTION_ID",
        name="",
        description="""NaN""",
        example="""QFMiyrQVarIAVkghxtQU""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=1003805614,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_INDEX: int = Field(
        ...,
        alias="RECEIPT_INDEX",
        name="",
        description="""A foreign key which refers to the field RECEIPT_INDEX of the ACT_CLIENT_ACCOUNT_RECEIPT table""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CC_FEE_PRICE: float = Field(
        ...,
        alias="CC_FEE_PRICE",
        name="",
        description="""Price for credit card feee""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CARD_NO: str = Field(
        ...,
        alias="CARD_NO",
        name="",
        description="""Credit card number (stores only gateway have permissions to store those data)""",
        example="""yL28kLE9rT4+93YbWxLgG5TSSGTUpNBC53MR0THK0tYw2vzCcLMOKa+Yw5XE1Qhi""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ISSUE_DATE: Optional[datetime] = Field(
        None,
        alias="ISSUE_DATE",
        name="",
        description="""Issue date of the credit card for credit card batch payment""",
        example="""1999-10-17 17:54:39""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXPIRY_DATE: datetime = Field(
        ...,
        alias="EXPIRY_DATE",
        name="",
        description="""Credit card expire date""",
        example="""1985-04-04 15:48:41""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GATEWAY_REF: str = Field(
        ...,
        alias="GATEWAY_REF",
        name="",
        description="""Credit card payment gateway reference/code""",
        example="""DSN_APP""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSACTION_REF: str = Field(
        ...,
        alias="TRANSACTION_REF",
        name="",
        description="""Transaction reference for the credit card transaction""",
        example="""ed2b6f21ca154e32b962cdd3e21b8b6a""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CARD_TYPE: str = Field(
        ...,
        alias="CARD_TYPE",
        name="",
        description="""Accounting rule applicable credit card types""",
        example="""MAS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NAME_OF_CARD: str = Field(
        ...,
        alias="NAME_OF_CARD",
        name="",
        description="""Credit card holders name (encrypted or plain text)""",
        example="""nHFxxPpRsSnNCFvxUIBIdmY8nzy5mLSt3e+1qUu1/kG/PRLnOZxBxYJMRTJD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POST_CODE: Optional[str] = Field(
        None,
        alias="POST_CODE",
        name="",
        description="""Postal code of the credit card holder for credit card batch payment""",
        example="""60069""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS: Optional[str] = Field(
        None,
        alias="ADDRESS",
        name="",
        description="""Address of the credit card holder for credit card batch payment""",
        example="""14 Wellington Court""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CC_FEE_INCLUDED: str = Field(
        ...,
        alias="CC_FEE_INCLUDED",
        name="",
        description="""Whether credit card fee is included in the charging amount or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTHORISED_TO_TAKE_BALANCE: Optional[str] = Field(
        None,
        alias="AUTHORISED_TO_TAKE_BALANCE",
        name="",
        description="""Whether it is authorized to take the balance for credit card batch payment""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSACTION_STATUS: Optional[str] = Field(
        None,
        alias="TRANSACTION_STATUS",
        name="",
        description="""State of the transaction (Ex: SUCCESS, FAILED, etc...)""",
        example="""QbEAXGvpDBSHBPRpRRka""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTH_CODE: Optional[str] = Field(
        None,
        alias="AUTH_CODE",
        name="",
        description="""Auth code for the credit card (provided from bank)""",
        example="""81310Z""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSACTION_REF_ID_RETURNED: Optional[str] = Field(
        None,
        alias="TRANSACTION_REF_ID_RETURNED",
        name="",
        description="""Returned transaction reference id for the transaction from the credit card payment gateway""",
        example="""208480586575""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSACTION_REF_NO_RETURNED: Optional[str] = Field(
        None,
        alias="TRANSACTION_REF_NO_RETURNED",
        name="",
        description="""Returned transaction reference number for the transaction from the credit card payment gateway""",
        example="""csFGMK""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CC_LAST_FIVE_DIGITS: Optional[str] = Field(
        None,
        alias="CC_LAST_FIVE_DIGITS",
        name="",
        description="""Last 5 digits of the credit card number (only if the system allows to store those)""",
        example="""*""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SETTLEMENT_DATE: Optional[datetime] = Field(
        None,
        alias="SETTLEMENT_DATE",
        name="",
        description="""Settlement date for the credit card payment""",
        example="""2001-01-28 23:35:03""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CC_FEE_COST: float = Field(
        ...,
        alias="CC_FEE_COST",
        name="",
        description="""Cost for credit card feee""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIRLINE_MERCHANT: Optional[str] = Field(
        None,
        alias="AIRLINE_MERCHANT",
        name="",
        description="""Whether rule is only for airline merchants or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CC_FEE_PRICE_TAX: Optional[float] = Field(
        None,
        alias="CC_FEE_PRICE_TAX",
        name="",
        description="""Tax for the price of credit card feee""",
        example=3842.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CC_FEE_COST_TAX: Optional[float] = Field(
        None,
        alias="CC_FEE_COST_TAX",
        name="",
        description="""Tax for the cost of credit card feee""",
        example=74995.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HOUSE_NO: Optional[str] = Field(
        None,
        alias="HOUSE_NO",
        name="",
        description="""House number of the credit card holder for credit card batch payment""",
        example="""SZHhDsOpPbxIbXPpykdI""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AIRLINE_COMMISSION_AMOUNT: Optional[float] = Field(
        None,
        alias="AIRLINE_COMMISSION_AMOUNT",
        name="",
        description="""If you pay with the airline merchant commission charged for that facility""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMPANY_CREDIT_CARD: Optional[str] = Field(
        None,
        alias="COMPANY_CREDIT_CARD",
        name="",
        description="""Whether this is a company credit card or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CARD_NO_FIRST_SIX_DIGITS: Optional[str] = Field(
        None,
        alias="CARD_NO_FIRST_SIX_DIGITS",
        name="",
        description="""First 6 digits of the credit card number""",
        example="""*""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ISSUE_NO: Optional[str] = Field(
        None,
        alias="ISSUE_NO",
        name="",
        description="""Issue number of the credit card details""",
        example="""aOIfwcOoPjCeqwqfjEaT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PASSENGER_NO: Optional[int] = Field(
        None,
        alias="PASSENGER_NO",
        name="",
        description="""Passnger number of the details entered passenger""",
        example=548,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PRODUCT_CODE: Optional[str] = Field(
        None,
        alias="PRODUCT_CODE",
        name="",
        description="""Deprecated""",
        example="""OUguCahzIvlMupnkJmwv""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ITEM_NO: Optional[int] = Field(
        None,
        alias="ITEM_NO",
        name="",
        description="""Deprecated""",
        example=5573,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SECURITY_NO: Optional[str] = Field(
        None,
        alias="SECURITY_NO",
        name="",
        description="""Security no of the credit card (stores only system allows to store credit card details)""",
        example="""RQQEgYhLwFrGniJVkGEk""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS2: Optional[str] = Field(
        None,
        alias="ADDRESS2",
        name="",
        description="""Second section of the given credit card details address""",
        example="""vxKQrZQdyQrVbQGBtLKC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""Lincolnshire""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATE: Optional[str] = Field(
        None,
        alias="STATE",
        name="",
        description="""State of the given credit card details address""",
        example="""IL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SUBSCRIPTION_NO_DELETED: Optional[str] = Field(
        None,
        alias="SUBSCRIPTION_NO_DELETED",
        name="",
        description="""Flag to check whether the Subscription_x000D_
number is deleted or not. There is a job called_x000D_
Subscription  Deletion. """,
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REMITTANCE_NO: Optional[int] = Field(
        None,
        alias="REMITTANCE_NO",
        name="",
        description="""Payment remittance number""",
        example=8837,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REMT_DATE: Optional[datetime] = Field(
        None,
        alias="REMT_DATE",
        name="",
        description="""Payment remitted date""",
        example="""1998-03-01 22:15:04""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HASH_CARD_NO: Optional[str] = Field(
        None,
        alias="HASH_CARD_NO",
        name="",
        description="""This is used to store the credit card number_x000D_
information in hashed format. The format_x000D_
is vary depending_x000D_
on the client requirment and the gateway._x000D_
Not the plain text of the card number it self.""",
        example="""MJngRXtVsXIsIKqjaQiy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MERCHANT: Optional[str] = Field(
        None,
        alias="MERCHANT",
        name="",
        description="""Code of the merchant""",
        example="""FiwGVGCcKZbdXGwYzZJn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREDIT_CARD_BRAND: Optional[str] = Field(
        None,
        alias="CREDIT_CARD_BRAND",
        name="",
        description="""NaN""",
        example="""VezHpwWeNJYVNhVDHAZy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1977-07-15 15:54:26""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CARD_CATEGORY: Optional[str] = Field(
        None,
        alias="CARD_CATEGORY",
        name="",
        description="""Card category of the payment""",
        example="""CreditCard""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACT_CLIENT_CC_RECEIPT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:42:48.902082""",
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
        example="""ACT_CLIENT_CC_RECEIPT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=92749561650537,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestActClientCcReceiptModel(BaseModel):
    """
    Payload class for TravelBox ACT_CLIENT_CC_RECEIPT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accounts Client Credit Card Receipt"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store information of payments done using Credit Card as the payment Type.
The values are setup in adding Receipts by selecting the Credit Card as the payment type."""  # optional
        unique_identifier = [
            "data.BOOKING_ID",
            "data.RECEIPT_INDEX",
        ]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "ACT_CLIENT_CC_RECEIPT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
