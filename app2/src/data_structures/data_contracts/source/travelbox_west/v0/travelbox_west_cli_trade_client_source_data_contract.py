"""Source Data Contract Template for CLI_TRADE_CLIENT"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_TRADE_CLIENT Data
    """

    ACCEPT_EBOOK_DETAILS: str = Field(
        ...,
        alias="ACCEPT_EBOOK_DETAILS",
        name="",
        description="""Flag to indicate if the Trade Client accepts Elect Booking Details (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATOL_AGENT: str = Field(
        ...,
        alias="ATOL_AGENT",
        name="",
        description="""Flag to indicate if the Trade Client is specified as an agent of ATOL (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    NETT_RATE: str = Field(
        ...,
        alias="NETT_RATE",
        name="",
        description="""A flag indicating the fares defined for the board basis are costs ( value is 1 ) or prices ( value is 0 )""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_RATING: Optional[str] = Field(
        None,
        alias="CLIENT_RATING",
        name="",
        description="""Client rating value""",
        example="""zBFNHCjxyxMlxmRiZHZu""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAL_NO: Optional[str] = Field(
        None,
        alias="TAL_NO",
        name="",
        description="""Deprecated""",
        example="""CrdzTWNEOLOtClVWRIsm""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ABN_NO: Optional[str] = Field(
        None,
        alias="ABN_NO",
        name="",
        description="""Deprecated""",
        example="""OTSjwiQpKJLFMfsqqdfm""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPOSIT_SCHEME: Optional[int] = Field(
        None,
        alias="DEPOSIT_SCHEME",
        name="",
        description="""Id of the Deposit Scheme associated with the Trade Client""",
        example=3452,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMP_REG: Optional[str] = Field(
        None,
        alias="COMP_REG",
        name="",
        description="""Company registration number""",
        example="""00332312""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ISSUE_INVOICE: str = Field(
        ...,
        alias="ISSUE_INVOICE",
        name="",
        description="""Flag to indicate Invoices are assigned to be issued (1) to the Trade Client or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COLLECT_FROM_CLIENT: str = Field(
        ...,
        alias="COLLECT_FROM_CLIENT",
        name="",
        description="""Flag to indicate if the Tour Agent is who collects the payments from clients (1) or not (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ISSUE_ITINERARY: str = Field(
        ...,
        alias="ISSUE_ITINERARY",
        name="",
        description="""Flag to indicate Itineraries are assigned to be issued (1) to the Trade Client or not (0)""",
        example="""0""",
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
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SHOW_COMMISSION: str = Field(
        ...,
        alias="SHOW_COMMISSION",
        name="",
        description="""Flag to indicate the commissions are shown on generated documents.""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GSA_NUMBER: Optional[str] = Field(
        None,
        alias="GSA_NUMBER",
        name="",
        description="""the trade client's GSA number""",
        example="""zTkDUbVCQiXpDMsdLTtZ""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GSA_JOIN_DATE: Optional[datetime] = Field(
        None,
        alias="GSA_JOIN_DATE",
        name="",
        description="""Grade Client GSA joined date""",
        example="""1989-01-09 02:00:22""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SELF_BILLING: str = Field(
        ...,
        alias="SELF_BILLING",
        name="",
        description="""Flag to indicate by whom the tax on commission is handled._x000D_
1 - by the tour operator_x000D_
0 - by the client """,
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AMENDEMENT_SCHEME: Optional[int] = Field(
        None,
        alias="AMENDEMENT_SCHEME",
        name="",
        description="""Deprecated""",
        example=4213,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CANX_SCHEME: Optional[int] = Field(
        None,
        alias="CANX_SCHEME",
        name="",
        description="""Id of the Cancellation Scheme associated with the Trade Client""",
        example=7429,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    OPTION_SCHEME: Optional[int] = Field(
        None,
        alias="OPTION_SCHEME",
        name="",
        description="""Id of the Option Rule associated with the Trade Client""",
        example=8235,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_REF_TYPE: Optional[str] = Field(
        None,
        alias="BOOKING_REF_TYPE",
        name="",
        description="""The terminology used by the Grade Client to name the booking reference""",
        example="""XlElKoUoVfpmojbXjGQH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BOOKING_REF_COMPULSARY: str = Field(
        ...,
        alias="BOOKING_REF_COMPULSARY",
        name="",
        description="""Flag to indicate if the Booking Ref Type is Compulsory""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PARTNER: str = Field(
        ...,
        alias="PARTNER",
        name="",
        description="""Flag to specify whether the Grade is applicable for Partners (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SEARCH_IN_CALL_CENTRE: str = Field(
        ...,
        alias="SEARCH_IN_CALL_CENTRE",
        name="",
        description="""Flag to indicate if the Trade Client has the ability of making call center bookings as well._x000D_
1 - can make call center bookings_x000D_
0 - web bookings only""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LOGO: Optional[str] = Field(
        None,
        alias="LOGO",
        name="",
        description="""path of the Logo associated with the client""",
        example="""rKjqzAhAMgaKufrPprkp""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREDIT_LIMIT_HO: str = Field(
        ...,
        alias="CREDIT_LIMIT_HO",
        name="",
        description="""Flag to indicate if the Head Office Credit Limit is used for Trade Client (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WRA_AGENTS: Optional[str] = Field(
        None,
        alias="WRA_AGENTS",
        name="",
        description="""Flag to indicate if the Trade Client is a Wholesaler Remittance Advice agent (1) or not (0)""",
        example="""sPAkXiVDhvNTNxEunCzo""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    GSA_CLIENT: Optional[str] = Field(
        None,
        alias="GSA_CLIENT",
        name="",
        description="""Flag to indicate if the Trade Client is a GSA Client""",
        example="""IXXavfzXMGaHJBvUfNkH""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYMENT_GROUP: Optional[int] = Field(
        None,
        alias="PAYMENT_GROUP",
        name="",
        description="""Name of the payment group associated with the scheme rule.""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HEAD_OFFICE_ID: Optional[int] = Field(
        None,
        alias="HEAD_OFFICE_ID",
        name="",
        description="""Deprecated""",
        example=870,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TAX_REG_NO: Optional[str] = Field(
        None,
        alias="TAX_REG_NO",
        name="",
        description="""Tax Register number of the Trade Client""",
        example="""86547-6485""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AREA: Optional[int] = Field(
        None,
        alias="AREA",
        name="",
        description="""The name of the Area""",
        example=6716,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LANGUAGE_CODE: Optional[str] = Field(
        None,
        alias="LANGUAGE_CODE",
        name="",
        description="""The code of the primary language used by the client""",
        example="""en""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PAYMENT_METHOD: Optional[str] = Field(
        None,
        alias="PAYMENT_METHOD",
        name="",
        description="""Payment methods associated with the Trade Client, as comma separated string""",
        example="""CASH,CHEQ,CRCD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CREDIT_AGENT_ID: Optional[str] = Field(
        None,
        alias="CREDIT_AGENT_ID",
        name="",
        description="""The client's reference if the Payment Group is credit Agent""",
        example="""nNBNroDeHIYaxdUQMVPb""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    INCLUDE_TAX_ON_COMM: str = Field(
        ...,
        alias="INCLUDE_TAX_ON_COMM",
        name="",
        description="""Flag to indicate if Tax on Commission should be added when calculating the balance due amount for Non-Self-Billing trade clients._x000D_
1 - Should be added_x000D_
0 - Not""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    SALES_ALLOWED: Optional[str] = Field(
        None,
        alias="SALES_ALLOWED",
        name="",
        description="""Flag to indicate if sales are allowed for the specific client (1) or not (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DOCUMENTS_ALLOWED: Optional[str] = Field(
        None,
        alias="DOCUMENTS_ALLOWED",
        name="",
        description="""Flag to indicate if documents are allowed for the specific client (1) or not (0)""",
        example="""1""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXCLUDE_PARTNER_EMAILING: str = Field(
        ...,
        alias="EXCLUDE_PARTNER_EMAILING",
        name="",
        description="""Flag to indicate if the direct client is Excluded from Partner E-mailings_x000D_
1 - Excluded_x000D_
0 - Not Excluded""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TRADE_CLIENT_TYPE: Optional[str] = Field(
        None,
        alias="TRADE_CLIENT_TYPE",
        name="",
        description="""Code of the Trade Client Type associated with the Trade Client""",
        example="""IND""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ACCEPT_EDOCS: str = Field(
        ...,
        alias="ACCEPT_EDOCS",
        name="",
        description="""Flag to indicate if the Trade Client accepts Elect Documents (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATOL_CERT_NOT_REQUIRED: Optional[str] = Field(
        None,
        alias="ATOL_CERT_NOT_REQUIRED",
        name="",
        description="""Flag to indicate if ATOL Certificate is note required (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ATOL_NAME: Optional[str] = Field(
        None,
        alias="ATOL_NAME",
        name="",
        description="""ATOL License Name""",
        example="""ZXNwdzixbANPovBUxYWc""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIL_METHOD: Optional[str] = Field(
        None,
        alias="MAIL_METHOD",
        name="",
        description="""Code of the Preferred Mail Method is included here""",
        example="""GgWXnDwQXcJEQObyTHhg""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ENABLE_CLIENT_MARKUP: str = Field(
        ...,
        alias="ENABLE_CLIENT_MARKUP",
        name="",
        description="""Deprecated""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_LEVEL: Optional[str] = Field(
        None,
        alias="CLIENT_LEVEL",
        name="",
        description="""Flag to specify the client level_x000D_
I - Independent Client_x000D_
S - Secondary Client_x000D_
P - Primary Client""",
        example="""I""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""2020-12-30 04:27:16""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COM_NETT_GROSS_OVERRIDE: Optional[str] = Field(
        None,
        alias="COM_NETT_GROSS_OVERRIDE",
        name="",
        description="""NaN""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROFILE_TYPE: str = Field(
        ...,
        alias="PROFILE_TYPE",
        name="",
        description="""NaN""",
        example="""STD""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BLOCK_CODE: Optional[str] = Field(
        None,
        alias="BLOCK_CODE",
        name="",
        description="""Unique code of the block""",
        example="""qUeLAKDDlDDByRlGCXcR""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HYBRID_MARKET_ID: Optional[float] = Field(
        None,
        alias="HYBRID_MARKET_ID",
        name="",
        description="""Hybrid Market ID of the Direct Connect Parameter""",
        example=92351.0,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CLIENT_ID: int = Field(
        ...,
        alias="CLIENT_ID",
        name="",
        description="""The TravelBox id of the trade client for which the commission rule is applied to. This field is null if the rule is applied to any client""",
        example=71488,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HEAD_OFFICE: str = Field(
        ...,
        alias="HEAD_OFFICE",
        name="",
        description="""Trade client's Head office ID (Trade Client ID)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    HEAD_OFFICE_REF: Optional[str] = Field(
        None,
        alias="HEAD_OFFICE_REF",
        name="",
        description="""Deprecated""",
        example="""fBKJZkAYvVPOnDbxEtth""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    REMIT_COMMISSION_HO: str = Field(
        ...,
        alias="REMIT_COMMISSION_HO",
        name="",
        description="""Flag to indicate that the Client's payments are done through their head offices (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DIVISION: Optional[str] = Field(
        None,
        alias="DIVISION",
        name="",
        description="""The TravelBox code of the division for which the limit is defined for""",
        example="""jULqXjakEaYclZZlvuSj""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TOWN: Optional[str] = Field(
        None,
        alias="TOWN",
        name="",
        description="""Town""",
        example="""ikUFUcHXrudGkvPmERJB""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MULTIPLE: Optional[str] = Field(
        None,
        alias="MULTIPLE",
        name="",
        description="""Multiple""",
        example="""tlaeXCutkepsdlhCmyjn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    PROMOTION: Optional[int] = Field(
        None,
        alias="PROMOTION",
        name="",
        description="""The selected promotion of the package""",
        example=7022,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    WEB: Optional[str] = Field(
        None,
        alias="WEB",
        name="",
        description="""Whether this transaction is initialized from web or TravelBox agent_x000D_
 - web site : true_x000D_
 - TravelBox agent : false""",
        example="""GzzFImHzPYzOnqPVdyII""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    BROCHURE_REQUEST: Optional[str] = Field(
        None,
        alias="BROCHURE_REQUEST",
        name="",
        description="""Deprecated""",
        example="""INAQjcmWzOGzVskgxOnn""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    AGREEMENT_STATUS: Optional[int] = Field(
        None,
        alias="AGREEMENT_STATUS",
        name="",
        description="""Flag to indicate ATOL Agreement status (1) or not (0)""",
        example=7915,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMISSION_FROM_HO: str = Field(
        ...,
        alias="COMISSION_FROM_HO",
        name="",
        description="""Flag to indicate if the Head Office Commission group is used for Trade Client (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COMM_GROUP: Optional[int] = Field(
        None,
        alias="COMM_GROUP",
        name="",
        description="""Id of the Commission Group associated with the Trade Client""",
        example=1946,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_TRADE_CLIENT Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 09:43:11.599315""",
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
        example="""CLI_TRADE_CLIENT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=43143578378647,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxWestCliTradeClientModel(BaseModel):
    """
    Payload class for TravelBox CLI_TRADE_CLIENT
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Trade Client"
        stream_name = "prd-use1-guest360-tbxw-stream"
        description = """This table is used to store Trade Client information, which are setup in Trade Client, Main Panel."""  # optional
        unique_identifier = ["data.CLIENT_ID"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_TRADE_CLIENT"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
