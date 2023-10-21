"""
Guest360 Module to create a table DDL from a given DataClass (pydantic)
"""

import importlib
import json

from app.src.data_service.marketplace.sql_generator.generator_config import (
    DataContractConfig,
    SnowflakeConfig,
)

import jsonref

from app.src.data_service.marketplace.sql_generator.helpers import (
    get_logger,
    to_snake_case,
)
from app.src.data_service.marketplace.sql_generator.table import (
    ChildTable,
    Table,
    UnblobbedTable,
)
from app.src.data_service.marketplace.sql_generator.table_field import TableField

logger = get_logger(__file__)

# Character used to identify object components (python-like dictionaries)
OBJECT_TYPE_DELIMITER = "__"
# Character used to identify parent-child relationship between tables.
ARRAY_TYPE_DELIMITER = "____"


class TableParser:
    """Helper class for parsing a given data contract into Table and TableField objects"""

    def __init__(self, data_contract_config: DataContractConfig, table_parser_config: SnowflakeConfig) -> None:
        self.tables = {}
        self.parsed_schema = {}
        self.landing_config = {}
        self.data_contract_config = data_contract_config
        self.table_parser_config = table_parser_config

    def parse_tables(self, module_name: str, class_name: str):
        """Transform a data contract class into TableField and Table objects"""
        self._dataclass_to_dict(module_name=module_name, class_name=class_name)
        table_name = self.data_contract_config.router_table
        self.tables[table_name] = self.tables.get(table_name, [])
        # All fields inside  the properties field are already at a depth of 2.
        current_recursive_depth = 1
        # Maximun recursive calls for the current data contract
        global RECURSIVE_DEPTH
        RECURSIVE_DEPTH = self.data_contract_config.recursive_depth
        self._data_contract_parser(
            fields=self.parsed_schema["properties"],
            current_recursive_depth=current_recursive_depth,
            table_name=table_name,
        )

    def _dataclass_to_dict(self, module_name: str, class_name: str) -> None:
        """Loads a data contract class and returns its json schema definition as a dict"""
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        schema = class_.schema_json()

        # Remove any internal properties of the dictionary (anything that starts with double dunder / __ ):
        if "Config" in class_.__dict__:
            self.landing_config = {
                k: v for k, v in class_.__dict__["Config"].__dict__.items() if not k.startswith("__")
            }
        self.parsed_schema = jsonref.loads(schema)

    def schema_to_json(self, filename: str) -> None:
        """Writes schema definition as JSON in a specified file.

        Args:
            filename (str): Name of destination file for schema JSON
        """
        with open(filename, "w", encoding="utf8") as f:
            json.dump(self.parsed_schema, f, indent=2)

    def field_parser(
        self,
        table_name,
        field_name,
        fields,
    ):
        """Parses json field into a TableField object

        Args:
            fields (dict[str, Any]): Field's metadata
            field_name (str): name of the field
            table_name (str): current table name
        """

        self.tables[table_name].append(
            TableField(
                _name=field_name,
                title=str(fields.get("title", "")),
                description=str(fields.get("description", "")),
                example=str(fields.get("example", "")),
                guest_identifier=bool(fields.get("guest_identifier", False)),
                transaction_identifier=bool(fields.get("guest_identifier", False)),
                identifier_tag=str(fields.get("identifier_tag", "")),
                _type=str("STRING" if "enum" in fields else fields.get("type")),
                format=fields.get("format", ""),
            )
        )

    def _data_contract_parser_helper(
        self,
        current_recursive_depth,
        fields,
        table_name: str = "",
        field_name: str = "",
        prefix: str = "",
        field_name_delimiter: str = OBJECT_TYPE_DELIMITER,
    ):
        if isinstance(fields, dict):
            field_name = f"{prefix}{field_name_delimiter}{field_name}" if prefix else field_name
            if "allOf" in fields:
                fields["type"] = "object"
                self.field_parser(table_name, field_name, fields)
                self._data_contract_parser(
                    fields["allOf"], current_recursive_depth + 1, table_name=table_name, prefix=field_name
                )
            elif "properties" in fields:
                if fields["type"] == "object":
                    self.field_parser(table_name, field_name, fields)
                self._data_contract_parser(
                    fields, current_recursive_depth + 1, table_name=table_name, prefix=field_name
                )
            # Handle arrays of objects, but arrays of strings should be left as variant:
            elif fields["type"] == "array" and fields["items"]["type"] == "object":
                self.field_parser(table_name, field_name, fields)  # Add variant columns to current table
                self._data_contract_parser(
                    fields["items"],
                    current_recursive_depth + 1,
                    table_name=table_name,
                    prefix=field_name,
                    field_name_delimiter=ARRAY_TYPE_DELIMITER,
                )
            else:
                self.field_parser(table_name, field_name, fields)

    def _data_contract_parser(
        self,
        fields,
        current_recursive_depth,
        table_name: str = "",
        prefix: str = "",
        field_name_delimiter: str = OBJECT_TYPE_DELIMITER,
    ):
        """Recursively extracts the properties of the data contracts. Stops when
           current_recursive_depth in greater than RECURSIVE_DEPTH.

        Args:
            fields (dict[str, Any]): a dictionary containing the dataclass properties
            current_recursive_depth (int): Keeps track of the current recursive call
            table_name (str, optional): current dataclass name/alias.
            prefix (str, optional): Prefix to be added to the current field name. Defaults to "".
            field_name_delimiter (str, optional): Helps to determine whether the current property is of object or array type.
        """

        if current_recursive_depth > RECURSIVE_DEPTH:
            return

        if isinstance(fields, dict):
            fields_dict = fields["properties"] if "properties" in fields else fields
            for key, val in fields_dict.items():
                if key == "required":
                    continue

                self._data_contract_parser_helper(
                    current_recursive_depth,
                    val,
                    table_name=table_name,
                    field_name=key,
                    prefix=prefix,
                    field_name_delimiter=field_name_delimiter,
                )

        elif isinstance(fields, list):
            for val in fields:
                self._data_contract_parser(
                    val,
                    current_recursive_depth,
                    table_name=table_name,
                    prefix=prefix,
                    field_name_delimiter=field_name_delimiter,
                )

    def _get_tables(self) -> list[Table]:
        tables = []
        for idx, (t_name, values) in enumerate(self.tables.items()):
            table_cls = UnblobbedTable if idx == 0 else ChildTable
            table = table_cls(_name=t_name)
            table.add_fields(values)
            table.compute_flatten_routes()
            tables.append(table)
        return tables

    def setup_landing_config(
        self,
        table: UnblobbedTable,
        field_name_delimiter: str = OBJECT_TYPE_DELIMITER,
    ) -> None:
        table.comment = self.landing_config.get("description", "")
        uniq_id = self.landing_config.get("unique_identifier", [])

        if isinstance(uniq_id, str):
            table.unique_identifier = [to_snake_case(uniq_id.strip().replace(".", field_name_delimiter))]
        elif uniq_id and len(uniq_id) and uniq_id != [""]:
            table.unique_identifier = list(
                map(lambda x: to_snake_case(x.strip().replace(".", field_name_delimiter)), uniq_id)
            )

        table.tags.append(f"data_classification_tag='{self.landing_config.get('data_classification_tag', '')}'")
        table.tags.append(f"data_category_tag='{self.landing_config.get('data_category_tag', '')}'")
        table.tags.append(f"pi_data='{self.landing_config.get('pi_data', False)}'")
        table.tags.append(f"timezone='{self.landing_config.get('timezone', 'UTC')}'")
        table.tags.append(f"isps='{self.landing_config.get('isps')}'")

        table.json_path = self.landing_config.get("json_path", "")

    def get_tables(self) -> list[Table]:
        tables: Table = self._get_tables()

        table_tracker = {}

        for table in tables:
            if isinstance(table, UnblobbedTable):
                table_tracker[table.name] = table
            elif isinstance(table, ChildTable):
                table_name_arr = table.name.split(ARRAY_TYPE_DELIMITER)
                table.root_parent_table = table_tracker[table_name_arr[0]]
                parent_table_name = ARRAY_TYPE_DELIMITER.join(table_name_arr[:-1])
                table.parent_table = table_tracker[parent_table_name]
                table_tracker[table.name] = table

        for table in tables:
            if isinstance(table, UnblobbedTable):
                self.setup_landing_config(table)
            elif isinstance(table, ChildTable):
                table.add_id_columns()
            table.format_fields()
        return tables
