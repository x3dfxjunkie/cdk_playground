"""Source Data Contract for Dreams TC"""

from __future__ import annotations
from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional
from app.src.data_structures.data_contracts.source.dreams.global_dreams_source_data_contract import (
    GlobalDreamsTcId,
    GlobalDreamsData,
    GlobalDreamsMetadata,
)


class Data(GlobalDreamsTcId, GlobalDreamsData):
    """Class for Dreams TC Data"""

    tc_typ_nm: str = Field(
        ...,
        alias="TC_TYP_NM",
        name="Travel Component Type Name",
        description="The designation for the kind of travel component.",
        example="AccommodationComponent",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prnt_tc_id: Optional[str] = Field(
        None,
        alias="PRNT_TC_ID",
        name="Parent Travel Component Identification",
        description="The unique identifier for a Travel Component.  Identifies the parent Travel Component for a Travel Component that has been combined with one or more travel components to form a complete travel component.",
        example="2085313432",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    upgrd_tc_id: Optional[str] = Field(
        None,
        alias="UPGRD_TC_ID",
        name="Upgrade Travel Component Identification",
        description="The unique identifier for a Travel Component.  Identifies the travel component that was upgraded to this instance of a travel component.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_grp_nb: str = Field(
        ...,
        alias="TC_GRP_NB",
        name="Travel Component Group Number",
        description="A unique sequential numeric identifier for a Travel Component Grouping.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_id: Optional[str] = Field(
        None,
        alias="PROD_ID",
        name="Product Identification",
        description="A unique sequential numeric identifier for a product.",
        example="106091",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_chkot_dts: Optional[datetime] = Field(
        None,
        alias="TC_CHKOT_DTS",
        name="Travel Component Check-Out Date Time",
        description="The timestamp when the guest no longer used the product.",
        example="2023-05-04T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_strt_dts: datetime = Field(
        ...,
        alias="TC_STRT_DTS",
        name="Travel Component Start Date Time",
        description="Effective date and time for when a travel component, a product or service, can be used",
        example="2023-06-22T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_end_dts: Optional[datetime] = Field(
        None,
        alias="TC_END_DTS",
        name="Travel Component End Date Time",
        description="Last date and time that a product or service can be actively used.",
        example="2023-07-06T00:00:00Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_bk_dts: datetime = Field(
        ...,
        alias="TC_BK_DTS",
        name="Travel Component Book Date Time",
        description="The date and time that the travel component was booked with Disney.",
        example="2023-03-29T15:30:10Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_slct_in: str = Field(
        ...,
        alias="TC_SLCT_IN",
        name="Travel Component Select Indicator",
        description="Determines whether (Y) or not (N) that a Travel Component can be selected by the guest as opposed to being a fixed component for the package.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_chkin_dts: Optional[datetime] = Field(
        None,
        alias="TC_CHKIN_DTS",
        name="Travel Component Check-In Date Time",
        description="The month day century and year hour minute and second when a guest checked in for a particular travel component",
        example="2023-03-29T15:30:11Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prod_typ_nm: Optional[str] = Field(
        None,
        alias="PROD_TYP_NM",
        name="Product Type Name",
        description="Designation that uniquely identifies a kind of product.",
        example="AccommodationProduct",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    blk_cd: Optional[str] = Field(
        None,
        alias="BLK_CD",
        name="Block Code",
        description="The unique identifier of a Block. ",
        example="01825",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    comnctn_chan_id: int = Field(
        ...,
        alias="COMNCTN_CHAN_ID",
        name="Communication Channel Identification",
        description="A unique sequential numeric identifier for a Communication Channel.",
        example=2,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sls_chan_id: int = Field(
        ...,
        alias="SLS_CHAN_ID",
        name="Sales Channel Identification",
        description="A unique sequential numeric identifier for a Sales Channel.",
        example=3,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    fac_id: Optional[str] = Field(
        None,
        alias="FAC_ID",
        name="Facility Identification",
        description="The identification of the facility (place) that is associated with this instance of a travel component.",
        example="80010397",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_sts_nm: str = Field(
        ...,
        alias="TRVL_STS_NM",
        name="Travel Status Name",
        description="The name of the state of the Travel Status.  For example, one status is Booked, which means that a reservation has been created for the guest.  Another example is Auto Cancelled, which means that the system cancelled the reservation because deposit requirements were not met.",
        example="Booked",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    upgrd_typ_nm: Optional[str] = Field(
        None,
        alias="UPGRD_TYP_NM",
        name="Upgrade Type Name",
        description="Identifies the kind of upgrade that occurred on a travel component.",
        example="None",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    trvl_agcy_pty_id: Optional[int] = Field(
        None,
        alias="TRVL_AGCY_PTY_ID",
        name="Travel Agency Party Identification",
        description="The unique identification of an individual / organization who performs a particular role or function.",
        example=14869011,
        guest_identifier=True,
        transaction_identifier=False,
        identifier_tag="indirect",
    )
    tc_lst_sty_dt: Optional[date] = Field(
        None,
        alias="TC_LST_STY_DT",
        name="Travel Component Last Stay Date",
        description="The last time that the guest stayed at the resort that was booked.",
        example="2023-03-29",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_req_fac_tx: Optional[str] = Field(
        None,
        alias="TC_REQ_FAC_TX",
        name="Travel Component Request Facility Text",
        description="Free form text from the Booking Client capturing what resort or category (tier) was requested by the guest.  Examples include ANIMAL KINGDOM LODGE, ANIMAL KINGDOM LODGE RESORT, ANY DISNEYLAND PARIS RESORT, ANY DLP SELECT HOTEL, BAHAMA HOUSE, BEACH CLUB, BEACH CLUB RESORT, BEACH CLUB VILLAS, BEACH RESORTS.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_cncl_dts: Optional[datetime] = Field(
        None,
        alias="TC_CNCL_DTS",
        name="Travel Component Cancel Date Time",
        description="The month day century and year hour minute and second when a particular travel component was cancelled.",
        example="2023-03-29T15:30:20Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_chrg_in: str = Field(
        ...,
        alias="TC_CHRG_IN",
        name="Travel Component Charge Indicator",
        description="Identifies that a travel component has (Y) or has not (N) charges on the travel component.  Default setting is Y, the travel component has charges.",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    asgn_own_id: Optional[str] = Field(
        None,
        alias="ASGN_OWN_ID",
        name="Assign Owner Identification",
        description="The unique identification for the assignment of ownership for the corresponding inventory for a component.",
        example="336576209",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    tc_invtry_in: str = Field(
        ...,
        alias="TC_INVTRY_IN",
        name="Travel Component Inventory Indicator",
        description="Identifies that a travel component has (Y) or has not (N) an equivalent inventory.  Default setting is Y, the travel component has an equivalent inventory.",
        example="Y",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    srvc_prd_id: Optional[str] = Field(
        None,
        alias="SRVC_PRD_ID",
        name="Service Period Identification",
        description="The identification value for a particular service period for which this instance of a travel component is valid.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    rev_cls_id: str = Field(
        ...,
        alias="REV_CLS_ID",
        name="Revenue Classification Identification",
        description="The unique identifier of Revenue Classification.",
        example="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    prge_dts: Optional[datetime] = Field(
        None,
        alias="PRGE_DTS",
        name="",
        description="",
        example="2023-07-18T06:30:37.488000Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DREAMSRoomsReservationsTcModel(BaseModel):
    """Payload class for DREAMSRoomsReservationsTcModel"""

    class Config:
        """Payload Level Metadata"""

        title = "Travel Component"
        stream_name = "guest360-dreams-resm-stream"
        description = "This table holds information about the detailed parts, items, components of the reservation and/or the package ie: AccommodationComponent; Service; PackageTravelComponent; AdmissionComponent; ComponentTravelComponent)"  # optional
        unique_identifier = ["data.TC_ID"]
        timezone = "UTC"  # optional
        pi_category = [""]  # optional
        isps = "Internal Use"  # optional
        financial_data = False  # optional
        version = "0.0.1"
        key_path_name = "metadata.table-name"  # optional
        key_path_value = "tc"  # optional

    data: Data = Field(..., alias="data")
    metadata: GlobalDreamsMetadata = Field(..., alias="metadata")
