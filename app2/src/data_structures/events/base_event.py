from dataclasses import dataclass, field

from dataclasses_json import LetterCase, dataclass_json


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class BaseEvent:

    class_name: str = field(init=False)

    def __post_init__(self):
        self.class_name = self.__class__.__name__
