"""Source Data Contract for Dreams Dining TPS CONFIRM RCPNT"""
from __future__ import annotations
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTpsId,
    GlobalDreamsData,
    GlobalDreamsTransactCommitTimestamp,
    GlobalDreamsMetadata,
)
from pydantic import BaseModel, Field


class Data(GlobalDreamsTpsId, GlobalDreamsData, GlobalDreamsTransactCommitTimestamp):
    """Class for Dreams Dining TPS CONFIRM RCPNT Data"""

    tps_cnfirm_rcpnt_id: int = Field(
        ...,
        alias="TPS_CNFIRM_RCPNT_ID",
        name="Travel Plans Segment Confirmation Receipt Identification",
        description="The unique identification of the individual or organization who is designated as the recipient of a confirmation of a travel plan segment reservation.",
        example=65329681,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dlvr_meth_nm: str = Field(
        ...,
        alias="DLVR_METH_NM",
        name="Delivery Method Name",
        description="The designation for the way a communication is to be delivered.",
        example="Email",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    pty_id: int = Field(
        ...,
        alias="PTY_ID",
        name="Party Identification",
        description="The unique identification of a party (either an organization or individual) who is important to the management of guest accounts. The party can perform the role of either responsible party for the folio or the billing party for the folio.",
        example=743727060,
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="Indirect",
    )
    lctr_id: int = Field(
        ...,
        alias="LCTR_ID",
        name="Locator Identification",
        description="The identification of the locator that will be used to disseminate the confirmation.",
        example=892604092,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dflt_cnfirm_in: str = Field(
        ...,
        alias="DFLT_CNFIRM_IN",
        name="Default Confirmation Indicator",
        description="Identifies that a confirmation on a reservation for a travel plan segment that is being sent to a party is (Y) or is not (N) the default confirmation.  Default setting is N, the confirmation is not the default confirmation that is being sent to a party for a reservation on a Travel Plan Segment.",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    dvc_mbrshp_in: str = Field(
        ...,
        alias="DVC_MBRSHP_IN",
        name="Disney Vacation Club Membership IN",
        description="Identifies that the recipient of this confirmation for a travel plan segment is (Y) or is not (N) for a member of the Disney Vacation Club. Default setting is N, the confirmation is to an individual who is not a member of the Disney Vacation Club.",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cnfirm_sent_in: str = Field(
        ...,
        alias="CNFIRM_SENT_IN",
        name="Confirmation Sent Indicator",
        description="Identifies that a confirmation was/has (Y) or was not/has not (N) been sent to the recipient.  Default setting is N, the recipient has not been sent the confirmation.",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cnfirm_sprs_in: str = Field(
        ...,
        alias="CNFIRM_SPRS_IN",
        name="Confirmation Suppress Indicator",
        description="Identifies that the confirmation is (Y) or is not (N) to be suppressed.  Default setting is N, the confirmation is to be sent.  ",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    cntct_nm: str = Field(
        ...,
        alias="CNTCT_NM",
        name="Cancellation Contact Name",
        description="The designation for the contact for the cancellation of the accommodation reservation.",
        example="Mickey, Mouse",
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="",
    )
    lacd_in: str = Field(
        ...,
        alias="LACD_IN",
        name="Latin American indicator",
        description="",
        example="N",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="Protected",
    )


class DREAMSDiningTpsCnfirmRcpntModel(BaseModel):
    """Payload class for DREAMSDiningTpsCnfirmRcpntModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Plan Segment Confirmation Recipient"
        stream_name = "prd-use1-guest360-dreams-resm-stream"
        description = "Table holds the information about who gets the confirmation of the reservation and where it goes"
        unique_identifier = ["data.TPS_CNFIRM_RCPNT_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tps_cnfirm_rcpnt"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
