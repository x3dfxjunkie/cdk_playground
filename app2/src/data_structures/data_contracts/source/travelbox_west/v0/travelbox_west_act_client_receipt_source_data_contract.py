"""Source Data Contract Template for ACT_CLIENT_RECEIPT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox ACT_CLIENT_RECEIPT Data
    """

    EXT_INT_RECONSILED: Optional[str] = Field(
        None,
        alias="EXT_INT_RECONSILED",
        name="",
        description="""Whether the payment was written to an external interface file or not.""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRANSACTION_ID: Optional[str] = Field(
        None,
        alias="TRANSACTION_ID",
        name="",
        description="""A foreign key which refers to the field TRANSACTION_ID of the ACT_CLIENT_ADVANCE_RECEIPT table""",
        example="""qgyWOkITNcfMeMVqXiGX""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2018-01-07 07:02:19""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_DETAILS: Optional[str] = Field(
        None,
        alias="PAY_DETAILS",
        name="",
        description="""NaN""",
        example="""aKvMGwmsAZGPfhQtoCrB""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SLIP_REF: Optional[str] = Field(
        None,
        alias="SLIP_REF",
        name="",
        description="""NaN""",
        example="""IumPXDgneAwaVYNtiEox""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BALANCE_DUE_HIS: Optional[float] = Field(
        None,
        alias="BALANCE_DUE_HIS",
        name="",
        description="""NaN""",
        example=0.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_CATEGORY: Optional[str] = Field(
        None,
        alias="RECEIPT_CATEGORY",
        name="",
        description="""NaN""",
        example="""tSHsWGbVeGoHOPGWvzdC""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_ID: int = Field(
        ...,
        alias="BOOKING_ID",
        name="",
        description="""The system generated id of the booking""",
        example=1003890608,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_INDEX: int = Field(
        ...,
        alias="RECEIPT_INDEX",
        name="",
        description="""A foreign key which refers to the field RECEIPT_INDEX of the ACT_CLIENT_ACCOUNT_RECEIPT table""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CURRENCY: str = Field(
        ...,
        alias="CURRENCY",
        name="",
        description="""The TravelBox code of the currency in which the board basis fares are defined""",
        example="""USD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMOUNT: float = Field(
        ...,
        alias="AMOUNT",
        name="",
        description="""Deprecated""",
        example=40.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAY_OR_REFUND: str = Field(
        ...,
        alias="PAY_OR_REFUND",
        name="",
        description="""RECEIPTS - THIS FLAG IS SET TO 1_x000D_
 REFUNDS - THIS FLAG IS SET TO 0""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NOTE: Optional[str] = Field(
        None,
        alias="NOTE",
        name="",
        description="""The note of Special Rate""",
        example="""null\nSet as unreconciled on 24/09/2022""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REALISED: str = Field(
        ...,
        alias="REALISED",
        name="",
        description="""Indicate whether payment is realized or not""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_DATE: datetime = Field(
        ...,
        alias="RECEIPT_DATE",
        name="",
        description="""The date of the receipt""",
        example="""2014-05-06 13:37:26""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REALISED_DATE: Optional[datetime] = Field(
        None,
        alias="REALISED_DATE",
        name="",
        description="""Payment realized date""",
        example="""1975-12-15 23:59:28""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AUTHORISED: str = Field(
        ...,
        alias="AUTHORISED",
        name="",
        description="""Whether this is an authorized payment or not""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_TO_SELLING_EX_RATE: float = Field(
        ...,
        alias="RECEIPT_TO_SELLING_EX_RATE",
        name="",
        description="""Payment currency to selling currency exchange rate""",
        example=1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_TO_BASE_EX_RATE: float = Field(
        ...,
        alias="RECEIPT_TO_BASE_EX_RATE",
        name="",
        description="""EX. RATE CAN BE MODIFIED IN CLIENT BATCH RECEIPTS PANEL. CHANDANA: NOT USED IN DOCUMENT RECEIPT. WE SAVE THIS INTO CLIENT_RECEIPT TABLE.""",
        example=1.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECEIPT_TYPE: Optional[str] = Field(
        None,
        alias="RECEIPT_TYPE",
        name="",
        description="""A foreign key which refers to the field CODE of the_x000D_
ACT_TRANSACTION_TYPE table""",
        example="""CRCD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BATCH_NO: Optional[str] = Field(
        None,
        alias="BATCH_NO",
        name="",
        description="""Batch number for credit card batch payment""",
        example="""gRnNZZilvppiGgTdrdNy""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    VALID: str = Field(
        ...,
        alias="VALID",
        name="",
        description="""If there is no blackout for the date, the valus is 0._x000D_
If there is a blackout for the date, the value is 1.""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PENDING: str = Field(
        ...,
        alias="PENDING",
        name="",
        description="""Indicates whether this is a pending payment or not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    IBTX_EXIST: Optional[str] = Field(
        None,
        alias="IBTX_EXIST",
        name="",
        description="""Whether Inter Booking Tansactions exist""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECONCILED: Optional[str] = Field(
        None,
        alias="RECONCILED",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    RECONCILED_DATE: Optional[datetime] = Field(
        None,
        alias="RECONCILED_DATE",
        name="",
        description="""Deprecated""",
        example="""1987-06-23 18:34:52""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    JOURNAL_BATCH_NO: Optional[int] = Field(
        None,
        alias="JOURNAL_BATCH_NO",
        name="",
        description="""Deprecated""",
        example=8298,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MODIFIED: Optional[str] = Field(
        None,
        alias="MODIFIED",
        name="",
        description="""Indicate whether this payment is modified after insertion (Ex: for IBTX)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STATEMENT_ID: Optional[int] = Field(
        None,
        alias="STATEMENT_ID",
        name="",
        description="""Unique id to identify the bank statement - system generated""",
        example=4277,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REVERSE_JOURNAL_BATCH_NO: Optional[int] = Field(
        None,
        alias="REVERSE_JOURNAL_BATCH_NO",
        name="",
        description="""Deprecated""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REVERSED_FOR_JOURNAL_BATCH_NO: Optional[int] = Field(
        None,
        alias="REVERSED_FOR_JOURNAL_BATCH_NO",
        name="",
        description="""Deprecated""",
        example=-1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BANK_TRANSACTION_ID: Optional[int] = Field(
        None,
        alias="BANK_TRANSACTION_ID",
        name="",
        description="""Bank transaction id for the payment""",
        example=4751,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENTERED_USER: Optional[int] = Field(
        None,
        alias="ENTERED_USER",
        name="",
        description="""A foreign key which refers to the field USER_ID of the ADM_USER table""",
        example=79682,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TEMP_USER: Optional[str] = Field(
        None,
        alias="TEMP_USER",
        name="",
        description="""Deprecated""",
        example="""AlnuJUehMJaPjJVmyRoJ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPOSITED_BY: Optional[int] = Field(
        None,
        alias="DEPOSITED_BY",
        name="",
        description="""Deprecated""",
        example=5698,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BANK_CODE: Optional[str] = Field(
        None,
        alias="BANK_CODE",
        name="",
        description="""A Foreign key which refers to the CODE field of the ACT_BANK table""",
        example="""ptoWjGxDUawttdNaMCxs""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACCOUNT_NO: Optional[str] = Field(
        None,
        alias="ACCOUNT_NO",
        name="",
        description="""Bank account number""",
        example="""GJFPFqoRlARrNVpVugYj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOUNCED_RCPTS_EXIST: Optional[str] = Field(
        None,
        alias="BOUNCED_RCPTS_EXIST",
        name="",
        description="""Flag to check whether there is a bounced receipt exists(TRUE)_x000D_
or not (FALSE)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOUNCED_RECEIPT_INDEX: Optional[int] = Field(
        None,
        alias="BOUNCED_RECEIPT_INDEX",
        name="",
        description="""If there is bound receipts, then the bounced receipt index_x000D_
will be set, else null value is saved""",
        example=5502,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPOSIT_BATCH_NO: Optional[int] = Field(
        None,
        alias="DEPOSIT_BATCH_NO",
        name="",
        description="""Deprecated""",
        example=3633,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BATCH_ID: Optional[int] = Field(
        None,
        alias="BATCH_ID",
        name="",
        description="""Batch Id for the credit card batch payment""",
        example=84,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOC_EXISTS: Optional[str] = Field(
        None,
        alias="DOC_EXISTS",
        name="",
        description="""IF PAYMENTS DONE AS DOCUMENT PAYMENT THIS FLAG WILL BE SET TO 1""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REMITTANCE_ID: Optional[str] = Field(
        None,
        alias="REMITTANCE_ID",
        name="",
        description="""The Remittance number""",
        example="""zvAZEMgNlTdvhqCmGLUn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOCATION_ID: Optional[int] = Field(
        None,
        alias="LOCATION_ID",
        name="",
        description="""Location id is saved when the module configuration_x000D_
'STORE_LOCATION_ID' is enabled, otherwise_x000D_
-1""",
        example=4021,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox ACT_CLIENT_RECEIPT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:44:44.248803""",
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
        example="""ACT_CLIENT_RECEIPT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=91178616096365,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestActClientReceiptModel(BaseModel):
    """
    Payload class for TravelBox ACT_CLIENT_RECEIPT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Accounts Client Receipt"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store information of Client Receipt Details. The values are saved when proceeding in the
following path. In Accounts Client go to 'Receipts->Single Receipts'. Then 'Search' for the bookings to add receipts.
then select the booking to add the receipt from the 'Select booking/s Grid', then click'Add New Receipt'. Then
select any payment type from the 'Type/Amount' dropdown and click 'Add' button from the dropdown  and
then 'Save'. And also values are saved when proceeding in the 'payment' node in Reservetion Manger.Then click
'Payment' button and add the payment in 'Payment Detail Panel'."""  # optional
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
        key_path_value = "ACT_CLIENT_RECEIPT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
