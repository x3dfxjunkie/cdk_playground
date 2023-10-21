import datetime
from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json

from app.src.data_structures.events.base_event import BaseEvent


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AttractionRideHistory:
    """Class for encapsulating the data associated with a single ride completed history."""

    attraction_id: str
    attraction_name: str
    attraction_ride_count: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AttractionRiddenEvent(BaseEvent):
    """Class that represents an attraction that has just been ridden."""

    atomic_id: str
    attraction_id: str
    attraction_name: str
    attraction_ridden_timestamp: datetime.datetime
