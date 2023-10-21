import datetime
from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json
from app.src.data_structures.events.base_experience_event import BaseExperienceEvent


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Facility:
    """Class that represents a facility within Disney properties."""

    facility_id: str
    facility_name: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LocationHierarchy:
    """Class the represents a location within Disney properties."""

    destination: Facility
    resort_area: Facility
    park_or_resort: Facility
    land: Facility
    pavillion: Facility


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Experience:
    """Class that represents an experience within Disney properties."""

    experience_id: str
    experience_category: str
    experience_name: str
    location_id: str
    location_name: str
    location_hierarchy: LocationHierarchy


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LightningLaneEvent(BaseExperienceEvent):
    """Class that represents a lightning lane event."""

    object_type: str
    event_type: str
    atomic_id: str
    guest_id: str
    transaction_id: str
    experience: Experience
    remaining_count: int
    event_time: datetime.datetime
    created_time: datetime.datetime
    last_modified: datetime.datetime
    experience_start: datetime.datetime
    experience_end: datetime.datetime
    event_status: str
    curated_status: str
    curated_confidence_score: int
    curated_confidence_label: str
