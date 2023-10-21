"""Source Data Contract for Dreams ADM CMPNT ENTTL"""

from __future__ import annotations
from pydantic import Field, BaseModel
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsData,
    GlobalDreamsMetadata,
)


# Any classes using (BaseModel) are net new classes, classes that have other classes inherited are calling those from Global Contract files to bring in fields already defined in another file.
# The class below inherits from the global_dreams_source_data_contract file listed above and uses the GlobalDreamsData class as base fields
class Data(GlobalDreamsData):
    """Class for Dreams ADM CMPNT ENTTL Data"""

    adm_enttl_id: int = Field(
        ...,
        alias="ADM_ENTTL_ID",
        name="Admission Entitlement Identification",
        description="Uniquely identifies an admission entitlement for a particular admission travel component.",
        example=33525799,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    adm_tc_id: int = Field(
        ...,
        alias="ADM_TC_ID",
        name="Admission Travel Component Identification",
        description="The unique identification of a travel component that is an admission to gain access to the likes of a Disney attraction, dining experience, theatrical experience, special occasion, etc.",
        example=2075207822,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    brcd_vl: str = Field(
        ...,
        alias="BRCD_VL",
        name="Barcode Value",
        description="The barcode representation of the entitlement information for a Admission Travel Component.",
        example="LPBQRT1SCVSCKZ65D3",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    mag_strp_vl: str = Field(
        ...,
        alias="MAG_STRP_VL",
        name="Magnetic Strip Value",
        description="The entitlement information as encoded on the magnetic strip for an Admission Travel Component.",
        example="CJ5FF1F3FLCBC63C2CJT0FFFBFL2BCDTCZC0FF4F2B8LC0CDTCZ0JTF12FBFLCBCDTCZ0JT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    serial_nb_vl: str = Field(
        ...,
        alias="SERIAL_NB_VL",
        name="Serial Number Value",
        description="The serial number of the entitlement as recorded for an Admission Travel Component.",
        example="25100003042328126",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    e_enttl_in: str = Field(
        ...,
        alias="E_ENTTL_IN",
        name="Electronic Entitlement Indicator",
        description="Identifies that the ticketing entitlement is either an Electronic Entitlement (Y) or is not an Electronic Entitlement (N).  Default is that the ticketing entitlement is not (N) an Electronic Entitlement.",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tkt_bank_in: str = Field(
        ...,
        alias="TKT_BANK_IN",
        name="ticket Bank Indicter",
        description="Identifies that when the Automated Ticketing Service (ATS) is not operatioinal, tickets are obtained from the ticket bank.  The valid values are (Y)es - ATS is not operational, so tickets are fulfilled from the Ticket Bank, (N)o - ATS is operational, tickets are not fulfilled from theTicket Bank.  Default value is (N)o - ATS is operational, tickets are not fulfilled from theTicket Bank but from ATS.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsFulfillmentAdmCmpntEnttlModel(BaseModel):
    """Payload class for DREAMSRoomsFulfillmentAdmCmpntEnttlModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Admission Component Entitlement"
        stream_name = "guest360-dreams-resm-stream"
        description = "When a room reservation includes Admissions to the park, the ticket is fulfilled in Snapp - the system of record for Tickets. It contains barcode, magnetic strip and serial number value - which is the Ticket identifier in Snapp. Any updates to the ticket after that will occur in Snapp"  # optional
        unique_identifier = ["data.ADM_ENTTL_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "adm_cmpnt_enttl"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
