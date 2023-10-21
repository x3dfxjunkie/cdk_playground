"""
Guest360 Module with the table field definition
"""

from dataclasses import dataclass, field
from pathlib import Path
import re
import yaml

from app.src.data_service.marketplace.sql_generator.helpers import to_snake_case

FIELDS_PATH = Path(__file__).resolve().parent / "field-types.yaml"
FIELD_TYPES = yaml.safe_load(FIELDS_PATH.open())

LANDING_TABLE_FIELDS_PATH = Path(__file__).resolve().parent / "landing_table_fields.yaml"
LANDING_TABLE_FIELDS = yaml.safe_load(LANDING_TABLE_FIELDS_PATH.open())


@dataclass
class TableField:
    """Table fields/columns coming from a dataclass definition"""

    _name: str
    title: str
    _type: str
    format: str = ""
    description: str = ""
    example: str = ""
    guest_identifier: bool = False
    transaction_identifier: bool = False
    identifier_tag: str = ""
    is_primary_key: bool = False
    nullable: bool = True

    _tags: list[str] = field(default_factory=list)
    padded_name: str = field(compare=False, default="", repr=False)
    padded_name_dot: str = field(compare=False, default="", repr=False)
    object_element: str = field(compare=False, default="", repr=False)
    is_landing_field: bool = field(compare=False, default=False, repr=False)

    @property
    def name(self):
        return re.sub("__+", "__", to_snake_case(self._name))

    @property
    def full_name(self):
        return self._name

    @property
    def alias(self):
        return re.sub("__+", "__", self._name)

    def pad_name(self, padding: int) -> None:
        """This pads the field's name to the longest chain and add some extra spaces

        Args:
            padding (int): Number of extra spaces to be added to the max-length chain
        """
        name = re.sub("__+", "__", self.name)
        self.padded_name = f"{name:<{padding}}"

    def pad_name_dot(self, padding: int, is_landing: bool) -> None:
        """This pads the field's name to the longest chain and add some extra spaces
        it also replaces the '__' with '.'

        Args:
            padding (int): Number of extra spaces to be added to the max-length chain
        """
        landing_table_fields = ["id"] + [field["_name"] for field in LANDING_TABLE_FIELDS]
        name = ".".join(self.alias.split("__")[:-1] + ['"' + self.alias.split("__")[-1] + '"'])
        if is_landing:
            if name not in [f'"{i}"' for i in landing_table_fields]:
                name = "landing_data:data." + name
            else:
                name = name.replace('"', "")
            padding = padding + len("landing_data:data.")
        self.padded_name_dot = f"{name:<{padding}}"

    def object_element_val(
        self,
    ) -> None:
        self.object_element = self.padded_name_dot.strip().split(".")[-1]

    @property
    def type(self):
        if "date" in self.format:
            return self.format.replace("-", "")
        return FIELD_TYPES[self._type.upper()]

    @property
    def tags(self):
        return {
            "guest_identifier": self.guest_identifier,
            "identifier_tag": self.identifier_tag,
            "transaction_identifier": self.transaction_identifier,
        }

    @property
    def comment(self) -> str | None:
        if self.description:
            return f"{self.description} | example: {self.example}".strip()
