"""
Guest360 Module with the table definition
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import re
from app.src.data_service.marketplace.sql_generator.helpers import to_snake_case
from app.src.data_service.marketplace.sql_generator.table_field import (
    TableField,
    LANDING_TABLE_FIELDS,
)


class Table(ABC):
    """Table Protocol"""

    def add_fields(self, fields: list[TableField]) -> None:
        self.fields.extend(fields)

    def _pad_fields(self):
        """Pads the names of the fields to make the generated SQL it human readable"""
        padding = [len(field.name) for field in self.fields]
        max_pad = max(padding)

        for f in self.fields:
            f.pad_name(max_pad + 2)
            f.pad_name_dot(max_pad + 2, True)
            f.object_element_val()

    @abstractmethod
    def format_fields(self) -> None:
        pass

    @property
    def json_name(self) -> str:
        return self._name

    @property
    def name(self) -> str:
        return to_snake_case(self._name)

    @property
    def id_field(self) -> TableField:
        for f in self.fields:
            if f.name == "id":
                return f

    @property
    def all_tag_names(self):
        table_tags = [tag.split("=")[0] for tag in self.tags]
        field_tags = []
        for t_field in self.fields:
            field_tags.extend(list(t_field.tags.keys()))

        table_tags.extend(field_tags)
        return sorted(list(set(table_tags)))

    def insert_route(self, route_elements: dict, route: list[str]) -> None:
        """Transform a route into dictionaries with a parent-child relationship.
            e.g. ele1____ele2____sub1__sub2____ele3 ==> {'ele1':{'ele2':{'sub1__sub2':{'ele3':{}}}}}
        Args:
            route_elements (dict): Saves the current element and its children ones.
            route (list[str]): list containing each of one the route's components.
        """
        if route:  # if route is not empty
            key = route[0]
            sub_route = route[1:]

            # if the key is not empty then add an empty sub-dictionary
            if key not in route_elements:
                route_elements[key] = {}

            # Recursive call for the remaining route
            self.insert_route(route_elements[key], sub_route)

    def generate_flatten_str(self, dic: dict, current_route: str = "", father_route: str = "") -> list[str]:
        """Recursively transform each of the dictionary elements  in a element that must be flatten
        by using the snowflake LATERAL FLATTEN operation. The most recent flatten object from the dictionary serves as input for its child.

        Args:
            dic (dict): Holds the elements to be flatten.
            current_route (str, optional): Current element to be flatten. Defaults to "".
            father_route (str, optional): Previous flatten element. Defaults to "".

        Returns:
            list[str]: list containing each one the flatten operations.
        """
        res = []
        for key, subdic in dic.items():
            if current_route:
                new_route = current_route + "." + '"' + key + '"'
                key_dot = '"."'.join(key.split("__"))
                father_key = father_route + "_" + key if father_route else key
                father_key = father_key.replace("-", "_")
                res.append(
                    f"""LATERAL FLATTEN (input => {father_route}.value:"{key_dot}" , outer => true ) as {father_key}"""
                )
            else:
                key_dot = '"."'.join(key.split("__"))
                new_route = key
                father_key = father_route + "_" + key if father_route else key
                father_key = father_key.replace("-", "_")
                res.append(
                    f"""LATERAL FLATTEN (input => ST.LANDING_DATA:data."{key_dot}" , outer => true ) as {father_key}"""
                )
            res.extend(self.generate_flatten_str(subdic, new_route, father_key))
        return res

    def compute_flatten_routes(
        self,
    ) -> None:
        """When an element is of type array it needs to be flatten in order to have access to each one of its elements.
        The number of flatted objects will depend on the recursive depth set for the data contract itself.
        """
        main_route_elements = {}
        for field in self.fields:
            full_name = field.full_name
            if "____" in full_name:
                self.insert_route(main_route_elements, full_name.split("____")[:-1])
        self.flatten_routes = "\n ,".join(self.generate_flatten_str(main_route_elements))
        self.flatten_routes = re.sub("_+", "_", self.flatten_routes)


@dataclass
class UnblobbedTable(Table):
    """Unblobbed Table definition"""

    _name: str

    comment: str = ""
    unique_identifier: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    json_path: str = ""

    fields: list[TableField] = field(default_factory=list)

    def format_fields(self) -> None:
        """Pads the names and types to the longest chain in the list of fields"""
        self._add_metadata()
        self._pad_fields()

    def _add_metadata(self) -> None:
        """Add metadata fields from the landing table"""
        for i in LANDING_TABLE_FIELDS:
            landing_field = TableField(_name=i["_name"], title=i["title"], _type=i["_type"])
            landing_field.is_landing_field = True
            self.fields.append(landing_field)


@dataclass
class ChildTable(Table):
    """Child Table definition"""

    _name: str

    fields: list[TableField] = field(default_factory=list)
    root_parent_table: Table = None
    parent_table: Table = None

    def add_id_columns(self) -> None:
        """Adds id columns"""
        id_columns = ("id", f"{self.parent_table.name}_id")
        for id_column in id_columns:
            self.add_id_column(id_column)

    def add_id_column(self, name: str) -> None:
        self.fields.append(TableField(_name=name, _type="STRING", title=name))

    def format_fields(self) -> None:
        """Pads the names and types to the longest chain in the list of fields"""
        self._pad_fields()

    @property
    def parents(self):
        return self.name.split("__")[:-1]
