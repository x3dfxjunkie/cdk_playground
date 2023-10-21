"""Source Data Contract Template for CLI_ADDRESS"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from app.src.data_structures.data_contracts.source.global_source_data_contract import (
    SourceMetadataAndGlobalAdditionalDMSMetadata,
)


class Data(BaseModel):
    """
    Class for TravelBox CLI_ADDRESS Data
    """

    CLIENT_ID: int = Field(
        ...,
        alias="CLIENT_ID",
        name="",
        description="""The TravelBox id of the trade client for which the commission rule is applied to. This field is null if the rule is applied to any client""",
        example=10491,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ADDRESS_NO: int = Field(
        ...,
        alias="ADDRESS_NO",
        name="",
        description="""Address no of the airline""",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    TITLE: Optional[str] = Field(
        None,
        alias="TITLE",
        name="",
        description="""The title of the accommodation image""",
        example="""ptPFHqGuYsMeIEbZkdhL""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    FIRST_NAME: Optional[str] = Field(
        None,
        alias="FIRST_NAME",
        name="",
        description="""First Name of the person associated with the contact""",
        example="""CHRISTA J HESS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_NAME: Optional[str] = Field(
        None,
        alias="LAST_NAME",
        name="",
        description="""Last Name of the person associated with the contact""",
        example="""dwrYgoQOsiAVFeRenDNT""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DEPARTMENT: Optional[str] = Field(
        None,
        alias="DEPARTMENT",
        name="",
        description="""Department of the person associated with the contact""",
        example="""BiUiswdvPUrSlNihscQz""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    DESIGNATION: Optional[str] = Field(
        None,
        alias="DESIGNATION",
        name="",
        description="""Designation of the person associated with the contact""",
        example="""shFoZZWClvHgnSvnXefh""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    STREET: Optional[str] = Field(
        None,
        alias="STREET",
        name="",
        description="""Street of the address associated with the contact""",
        example="""IwyPUQaxWgiHrygrghUg""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CITY: Optional[str] = Field(
        None,
        alias="CITY",
        name="",
        description="""The TravelBox code of the city for which the rule is defined""",
        example="""eDrDVSLdHGemPztJgzLM""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    COUNTY: Optional[str] = Field(
        None,
        alias="COUNTY",
        name="",
        description="""Code of the county""",
        example="""VA""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    POSTAL_CODE: str = Field(
        ...,
        alias="POSTAL_CODE",
        name="",
        description="""Postal code of the address associated with the contact""",
        example="""23005""",
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

    CONTACT_TYPE: Optional[int] = Field(
        None,
        alias="CONTACT_TYPE",
        name="",
        description="""Id of the Contract type associated with the Address""",
        example=1,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MAIN: str = Field(
        ...,
        alias="MAIN",
        name="",
        description="""Flag to indicate of the address is the main address of the Client (1) or not (0)""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    MIDDLE_NAME: Optional[str] = Field(
        None,
        alias="MIDDLE_NAME",
        name="",
        description="""Middle Name of the person associated with the contact""",
        example="""GbbWMqZFtvqLbjNLGUUN""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    CONTACT_CATEGORY: Optional[int] = Field(
        None,
        alias="CONTACT_CATEGORY",
        name="",
        description="""Id of the contact category associated with the Address""",
        example=2004,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    LAST_MODIFIED_TIME: datetime = Field(
        ...,
        alias="LAST_MODIFIED_TIME",
        name="",
        description="""The time at which the last modification has done.""",
        example="""1982-10-25 01:11:38""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    EXTERNAL: Optional[str] = Field(
        None,
        alias="EXTERNAL",
        name="",
        description="""Whether the ledger entries created by the rule is eligible to be exported by the external interface.""",
        example="""0""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metadata(BaseModel):
    """
    Class for TravelBox CLI_ADDRESS Metadata
    """

    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        name="",
        description="""Timestamp of when the record was sent to the stream""",
        example="""2023-08-16 08:50:31.790104""",
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
        example="""CLI_ADDRESS""",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    transaction_id: Optional[int] = Field(
        None,
        alias="transaction-id",
        name="",
        description="""Unique Transaction Identifier""",
        example=59506731534418,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TravelBoxEastCliAddressModel(BaseModel):
    """
    Payload class for TravelBox CLI_ADDRESS
    """

    class Config:
        """Payload Level Metadata"""

        title = "Client Address"
        stream_name = "prd-use1-guest360-tbxe-stream"
        description = """This table is used to store Address information of Trade Clients and Trade Agents.
The values are setup in 'Agents and Contacts' node for Trade Clients and in 'Contacts' node for Trade Agents, in Customer Profiles Setup"""  # optional
        unique_identifier = ["data.CLIENT_ID", "data.ADDRESS_NO"]
        timezone = ""  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.tablename"
        key_path_value = "CLI_ADDRESS"

    data: Data = Field(..., alias="data")
    metadata: SourceMetadataAndGlobalAdditionalDMSMetadata = Field(..., alias="metadata")
