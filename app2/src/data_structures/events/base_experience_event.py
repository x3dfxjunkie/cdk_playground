from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json
from app.src.data_structures.events.base_event import BaseEvent


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class BaseExperienceEvent(BaseEvent):
    ...