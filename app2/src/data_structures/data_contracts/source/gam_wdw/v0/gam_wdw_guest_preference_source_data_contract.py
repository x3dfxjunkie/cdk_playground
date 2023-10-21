"""Source Data Contract Template for GAM WDW Guest Preferences"""

from __future__ import annotations
from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field


class Preference(BaseModel):
    brand_codes: str = Field(
        ...,
        alias="brandCodes",
        name="",
        description="",
        example="all",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    description: str = Field(
        ...,
        alias="description",
        name="",
        description="",
        example="Favorite Experiences for the guest with multiple selections for the Disneyland Resort's Disneyland Park.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    display_detailed_text: Optional[str] = Field(
        None,
        alias="displayDetailedText",
        name="",
        description="",
        example="Choose up to 20 experiences that you want Genie to prioritize for your day.",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    display_name: str = Field(
        ...,
        alias="displayName",
        name="",
        description="",
        example="Disneyland Favorite Experiences",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    expires_in_day_count: int = Field(
        ...,
        alias="expiresInDayCount",
        name="",
        description="",
        example=30,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="ihNlIZm1JInjbYT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_default_options_selected: Optional[bool] = Field(
        None,
        alias="isDefaultOptionsSelected",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_option_search_enabled: Optional[bool] = Field(
        None,
        alias="isOptionSearchEnabled",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_preference_active: bool = Field(
        ...,
        alias="isPreferenceActive",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_read_only: bool = Field(
        ...,
        alias="isReadOnly",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_required: bool = Field(
        ...,
        alias="isRequired",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_sample_data_preference: bool = Field(
        ...,
        alias="isSampleDataPreference",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_test_preference: bool = Field(
        ...,
        alias="isTestPreference",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        example="disneyland-resort-disneyland-park-favorite-experiences",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_option_item_ids: Optional[List[str]] = Field(
        None,
        alias="preferenceOptionItemIds",
        name="",
        description="",
        example=[""],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_option_sort_type_id: Optional[str] = Field(
        None,
        alias="preferenceOptionSortTypeId",
        name="",
        description="",
        example="ASCENDING_SORT_TYPE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_option_type_id: Optional[str] = Field(
        None,
        alias="preferenceOptionTypeId",
        name="",
        description="",
        example="FACILITY_PREFERENCE_OPTION_TYPE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_sub_type_id: Optional[str] = Field(
        None,
        alias="preferenceSubTypeId",
        name="",
        description="",
        example="MULTI_SELECT_THEME_PARK_FAVORITE_FACILITIES_PREFERENCE_SUB_TYPE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_type_id: str = Field(
        ...,
        alias="preferenceTypeId",
        name="",
        description="",
        example="MULTI_SELECT_OPTION_PREFERENCE_TYPE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sample_id: str = Field(
        ...,
        alias="sampleId",
        name="",
        description="",
        example="71",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    theme_park_facility_id: Optional[str] = Field(
        None,
        alias="themeParkFacilityId",
        name="",
        description="",
        example="330339;entityType=theme-park",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    theme_park_name: Optional[str] = Field(
        None,
        alias="themeParkName",
        name="",
        description="",
        example="Disneyland Park",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    valid_max_selection_count: Optional[int] = Field(
        None,
        alias="validMaxSelectionCount",
        name="",
        description="",
        example=20,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    condition_true_preference_id: Optional[str] = Field(
        None,
        alias="conditionTruePreferenceId",
        name="",
        description="",
        example="DW7xUVhe4f",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    condition_true_preference_sample_id: Optional[str] = Field(
        None,
        alias="conditionTruePreferenceSampleId",
        name="",
        description="",
        example="31",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    display_summary_text: Optional[str] = Field(
        None,
        alias="displaySummaryText",
        name="",
        description="",
        example="Should we limit experiences based on height?",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_dining_item_preference: Optional[bool] = Field(
        None,
        alias="isDiningItemPreference",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_selected: Optional[bool] = Field(
        None,
        alias="isSelected",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PreferenceOptionListItem(BaseModel):
    display_name: str = Field(
        ...,
        alias="displayName",
        name="",
        description="",
        example="Disneyland Favorite Experiences",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="ihNlIZm1JInjbYT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_preference_option_active: bool = Field(
        ...,
        alias="isPreferenceOptionActive",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    is_preference_option_disabled: Optional[bool] = Field(
        None,
        alias="isPreferenceOptionDisabled",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_option_type_id: str = Field(
        ...,
        alias="preferenceOptionTypeId",
        name="",
        description="",
        example="FACILITY_PREFERENCE_OPTION_TYPE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    sample_id: str = Field(
        ...,
        alias="sampleId",
        name="",
        description="",
        example="71",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    value: str = Field(
        ...,
        alias="value",
        name="",
        description="",
        example="367495;entityType=Attraction",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    facet_id: Optional[str] = Field(
        None,
        alias="facetId",
        name="",
        description="",
        example="19534743",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PreferenceDetailListItem(BaseModel):
    preference: Preference = Field(
        ...,
        alias="preference",
        name="",
        description="",
        example="",
    )
    preference_date: Optional[date] = Field(
        None,
        alias="preferenceDate",
        name="",
        description="",
        example="2023-09-25",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_id: str = Field(
        ...,
        alias="preferenceId",
        name="",
        description="",
        example="1fFyZuZ0jc",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_option_list: Optional[List[PreferenceOptionListItem]] = Field(
        None, alias="preferenceOptionList", name="", description=""
    )
    update_time: datetime = Field(
        ...,
        alias="updateTime",
        name="",
        description="",
        example="2023-09-20T10:28:21.487222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    valid_preference_date: Optional[int] = Field(
        None,
        alias="validPreferenceDate",
        name="",
        description="",
        example=1695168000000,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_boolean_value: Optional[bool] = Field(
        None,
        alias="preferenceBooleanValue",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class PreferenceSummaryListItem(BaseModel):
    preference_date: Optional[date] = Field(
        None,
        alias="preferenceDate",
        name="",
        description="",
        example="2023-09-25",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_display_name: str = Field(
        ...,
        alias="preferenceDisplayName",
        name="",
        description="",
        example="Hollywood Studios Favorite Experiences",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_id: str = Field(
        ...,
        alias="preferenceId",
        name="",
        description="",
        example="1fFyZuZ0jc",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_option_id_list: Optional[List[str]] = Field(
        None,
        alias="preferenceOptionIdList",
        name="",
        description="",
        example=[],
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_type_id: str = Field(
        ...,
        alias="preferenceTypeId",
        name="",
        description="",
        example="MULTI_SELECT_OPTION_PREFERENCE_TYPE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    update_time: datetime = Field(
        ...,
        alias="updateTime",
        name="",
        description="",
        example="2023-09-20T10:28:21.487222Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_boolean_value: Optional[bool] = Field(
        None,
        alias="preferenceBooleanValue",
        name="",
        description="",
        example=False,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class NotificationDetailListItem(BaseModel):
    notification_date: Optional[date] = Field(
        None,
        alias="notificationDate",
        name="",
        description="",
        example="2023-09-25",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class NotificationSummaryListItem(BaseModel):
    notification_date: Optional[date] = Field(
        None,
        alias="notificationDate",
        name="",
        description="",
        example="2023-09-25",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Payload(BaseModel):
    id: str = Field(
        ...,
        alias="id",
        name="",
        description="",
        example="ihNlIZm1JInjbYT",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    notification_detail_list: Optional[List[NotificationDetailListItem]] = Field(
        None,
        alias="notificationDetailList",
        name="",
        description="",
        example=[],
    )
    notification_summary_list: Optional[List[NotificationSummaryListItem]] = Field(
        None,
        alias="notificationSummaryList",
        name="",
        description="",
        example=[],
    )
    preference_detail_list: Optional[List[PreferenceDetailListItem]] = Field(
        None,
        alias="preferenceDetailList",
        name="",
        description="",
        example=[],
    )
    preference_summary_list: Optional[List[PreferenceSummaryListItem]] = Field(
        None,
        alias="preferenceSummaryList",
        name="",
        description="",
        example=[],
    )
    preference_ids: Optional[str] = Field(
        None,
        alias="preferenceIds",
        name="",
        description="",
        example="1fFyZuZ0jc,ptkj4iXnGW,9azPR263AG",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_option_ids: Optional[str] = Field(
        None,
        alias="preferenceOptionIds",
        name="",
        description="",
        example="bZhVYpHsY,42hZgWAWe",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_option_sample_ids: Optional[str] = Field(
        None,
        alias="preferenceOptionSampleIds",
        name="",
        description="",
        example="609,610",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    preference_sample_ids: Optional[str] = Field(
        None,
        alias="preferenceSampleIds",
        name="",
        description="",
        example="80,30,32",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    guest_locator_id: Optional[str] = Field(
        None,
        alias="guestLocatorId",
        name="",
        description="",
        example="MERGE_TO_RECORD",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    merged_correlation_ids: Optional[str] = Field(
        None,
        alias="mergedCorrelationIds",
        name="",
        description="",
        example="b32f3a44-f80d-49c0-9954-098617d938d4",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    merged_to_date_time: Optional[datetime] = Field(
        None,
        alias="mergedToDateTime",
        name="",
        description="",
        example="2023-09-20T10:40:33.778940Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    merged_to_id: Optional[str] = Field(
        None,
        alias="mergedToId",
        name="",
        description="",
        example="cV0WHaHPGrOJINS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    merged_from_date_time: Optional[datetime] = Field(
        None,
        alias="mergedFromDateTime",
        name="",
        description="",
        example="2023-09-20T10:41:55.063205Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    merged_from_ids: Optional[str] = Field(
        None,
        alias="mergedFromIds",
        name="",
        description="",
        example="VzqHzkhmrsSHHfa,JhCQMt6ImLQ8DJK,VzqHzkhmrsSHHfa,JhCQMt6ImLQ8DJK",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class GAMWDWGuestPreferenceModel(BaseModel):
    """Payload class for GAMWDWGuestPreferenceModel"""

    class Config:
        """Payload Level Metadata"""

        title = "GAM WDW Guest Preference"
        stream_name = ""
        description = """WDW Guest preferences associated with Genie"""
        unique_identifier = []
        timezone = "UTC"
        pi_category = [""]
        isps = "Internal Use"
        financial_data = ""
        version = "0.0.1"
        key_path_name = "eventType"
        key_path_value = "PREFERENCE_GUEST_SELECTION_UPDATE"

    correlation_id: str = Field(
        ...,
        alias="correlationId",
        name="",
        description="",
        example="QkqT9zgQ9TsaBDvedOLN",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    event_type: str = Field(
        ...,
        alias="eventType",
        name="",
        description="",
        example="PREFERENCE_GUEST_SELECTION_UPDATE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    location: str = Field(
        ...,
        alias="location",
        name="",
        description="",
        example="PROFILE.PREFERENCE_SERVICE",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    orchestration_id: str = Field(
        ...,
        alias="orchestrationId",
        name="",
        description="",
        example="Test9Test9TestTest99",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    payload: Payload = Field(..., alias="payload", name="", description="")
    sor: str = Field(
        ...,
        alias="sor",
        name="",
        description="",
        example="PROFILEPREFS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    status: str = Field(
        ...,
        alias="status",
        name="",
        description="",
        example="SUCCESS",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    time_stamp: datetime = Field(
        ...,
        alias="timeStamp",
        name="",
        description="",
        example="2023-09-20T10:23:56.429038445Z",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
