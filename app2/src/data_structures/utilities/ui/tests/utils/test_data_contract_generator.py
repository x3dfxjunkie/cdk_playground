import json
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from datamodel_code_generator import InputFileType
from app.src.data_structures.utilities.ui.tests.conftest import (
    PATCH_DATACLASS_GEN_DIR,
    JSON_SCHEMA,
    DB_MARIA_CONFIG,
    DDL_DF_DATA,
    DDL_PK_DATA,
)
from app.src.data_structures.utilities.ui.dataclass_generator.utils.data_contract_generator import (
    DataContractGenerator,
    generate_data_contract,
    get_custom_template_path,
)
from app.src.data_structures.utilities.ui.dataclass_generator.config.database import DatabaseTypeNotSupportedException


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
class TestDataContractGenerator:
    def test___init__(self, connect_mock):
        contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
        assert contract_gen.config_dict == DB_MARIA_CONFIG
        assert contract_gen.db.db_type == DB_MARIA_CONFIG["db_type"]
        with pytest.raises(DatabaseTypeNotSupportedException):
            db_wrong_config = DB_MARIA_CONFIG.copy()
            db_wrong_config["db_type"] = "NotSupportedDB"
            DataContractGenerator(db_wrong_config)

    def test_get_source_name(self, connect_mock):
        contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
        assert contract_gen.get_source_name() == DB_MARIA_CONFIG["source_name"]

    def test_get_schema_namee(self, connect_mock):
        contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
        assert contract_gen.get_schema_name() == DB_MARIA_CONFIG["schema_name"]

    def test_generate_class_name(self, connect_mock):
        contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
        contract_gen.generate_class_name("Test")
        assert contract_gen.model_name

    def test_get_list_of_tables(self, connect_mock):
        orig_tables = [
            ("table_1",),
            ("table_2",),
            ("table_3",),
        ]
        cursor = MagicMock()
        connect_mock.return_value.__enter__.return_value.cursor.return_value = cursor

        connect_mock.return_value.cursor.return_value = cursor
        cursor.fetchall.return_value = orig_tables
        cursor.description = [("TABLES",)]

        contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
        tables = contract_gen.get_list_of_tables()
        assert isinstance(tables, list)
        assert tables == list(map(lambda _: _[0], orig_tables))

    def test_get_json_schema(self, connect_mock):
        contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
        df = pd.DataFrame(DDL_DF_DATA)
        df_pk = pd.DataFrame(DDL_PK_DATA)
        json_schema = contract_gen.get_json_schema(df, df_pk)
        assert isinstance(json_schema, str)
        assert "$schema" in json_schema

    def test_generate_data_contract_file_name(self, connect_mock):
        contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
        table_name = "Test"
        contract_gen.generate_data_contract_file_name(table_name)
        assert contract_gen.data_contract_file_name
        assert table_name.lower() in contract_gen.data_contract_file_name
        assert "source_data_contract" in contract_gen.data_contract_file_name

    def test_init_contract_details(self, connect_mock):
        contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
        table_name = "Test"
        contract_gen.init_contract_details(table_name)
        assert contract_gen.model_name
        assert contract_gen.data_contract_file_name

    def test_get_data_contracts(self, connect_mock):
        with patch(
            "app.src.data_structures.utilities.ui.dataclass_generator.config.database.Maria.get_table_details_from_db",
            return_value=(
                pd.DataFrame(DDL_DF_DATA),
                pd.DataFrame(DDL_PK_DATA),
            ),
        ):
            contract_gen = DataContractGenerator(DB_MARIA_CONFIG)
            contracts = contract_gen.get_data_contracts(["table_1", "table_2"])
            for i, contract in enumerate(contracts):
                assert f"TestTable{i+1}Model" in contract

    def test_get_custom_template_path(self, connect_mock):
        assert "custom_templates" in str(get_custom_template_path())

    def test_generate_data_contract(self, connect_mock):
        model_name = "TestDataContract"
        data_contract = generate_data_contract(
            model_name, json.dumps(JSON_SCHEMA), InputFileType.JsonSchema, {"example"}
        )
        assert isinstance(data_contract, str)
        assert model_name in data_contract
