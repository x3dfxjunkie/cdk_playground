"""Source Data Contract for DREAMs Room Fulfillment Travel Component Experience Enhancement Criteria"""
from __future__ import annotations
from datetime import datetime
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTcId,
    GlobalDreamsData,
    GlobalDreamsTransactCommitTimestamp,
    GlobalDreamsMetadata,
)
from pydantic import BaseModel, Field


class Data(GlobalDreamsTcId, GlobalDreamsData, GlobalDreamsTransactCommitTimestamp):
    """Class for Dreams TC EXPRNC CRTR Data"""

    elig_crtr_nm: str = Field(
        ...,
        alias="ELIG_CRTR_NM",
        name="Eligibility Criteria Name",
        description="The name for a grouping of principles that govern qualifications and/or applicability",
        example="Experience Media",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exprnc_enhnc_nm: str = Field(
        ...,
        alias="EXPRNC_ENHNC_NM",
        name="Experiance Enhancment Name",
        description="The name of the enhancement to the participation in an event or activity",
        example="Bypass Front Desk",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    exprnc_enhnc_crtr_vl: str = Field(
        ...,
        alias="EXPRNC_ENHNC_CRTR_VL",
        name="Eligibility Enhancment Criteria Value",
        description="The value that is the principle that governs the qualification and/or applicability on an enhancement to a Disney experience",
        example="Yes",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_exprnc_enhnc_crtr_dts: datetime = Field(
        ...,
        alias="TC_EXPRNC_ENHNC_CRTR_DTS",
        name="Travel Componenet Eligibility Enhancment Criteria Datetime",
        description="The date and time when a particular criterium for the enhancement of an experience has been met for a travel component.",
        example="2023-04-03T14:22:55.173000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentTcExprncEnhncCrtrModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentTcExprncEnhncCrtrModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component Experience Enhacement Criteria"
        stream_name = ""
        description = """Criteria required to be able to experience the enhancement"""
        unique_identifier = ["data.ELIG_CRTR_NM"]
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = False
        version = "0.0.1"
        key_path_name = "metadata.table-name"
        key_path_value = "tc_exprnc_enhnc_crtr"

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
