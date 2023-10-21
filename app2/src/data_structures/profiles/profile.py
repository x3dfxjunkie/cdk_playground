from dataclasses import dataclass
from typing import List

from dataclasses_json import LetterCase, dataclass_json

from app.src.data_structures.events.attraction_ridden_event import \
    AttractionRideHistory


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Profile:
    """Class for encapsulating the data associated with a guest profile."""

    atomic_id: str
    associated_ids: List[str]
    attraction_ride_histories: List[AttractionRideHistory]
