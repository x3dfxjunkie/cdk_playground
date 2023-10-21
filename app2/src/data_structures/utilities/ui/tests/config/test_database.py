from unittest.mock import patch, MagicMock

import pandas as pd

from app.src.data_structures.utilities.ui.dataclass_generator.config.database import MainDatabase
from app.src.data_structures.utilities.ui.tests.conftest import (
    PATCH_DATACLASS_GEN_DIR,
    DB_MARIA_CONFIG,
    DB_ORACLE_CONFIG,
)


def test_create_maria_db():
    main_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    assert main_db.host == "test.db"
    assert main_db.username == "test"
    assert main_db.password == DB_MARIA_CONFIG["password"]


def test_create_oracle_db():
    db = MainDatabase.get_database("Oracle")(DB_ORACLE_CONFIG)
    assert db.host == "test.db"
    assert db.username == "test"
    assert db.password == DB_ORACLE_CONFIG["password"]
    assert db.service_name == DB_ORACLE_CONFIG["service_name"]


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
def test_execute_cur(connect_mock):
    sql_response = [{"col_1": "val_1"}]
    connector = MagicMock()
    cursor = MagicMock()
    connect_mock().__enter__.return_value = connector
    connector.cursor.return_value = cursor
    cursor.execute.return_value = sql_response

    maria_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    res = maria_db.execute_cur("SELECT * FROM TEST;")
    assert res == sql_response


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
def test_get_list_of_tables(connect_mock):
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

    maria_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    table_list = maria_db.get_list_of_tables()
    assert isinstance(table_list, list)
    assert table_list == list(map(lambda _: _[0], orig_tables))


def test_get_table_details_from_db():
    pass


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
def test_get_test_data_from_table(connect_mock):
    orig_tables = [
        ("val_1",),
        ("val_2",),
        ("val_3",),
    ]
    cursor = MagicMock()
    connect_mock.return_value.cursor.return_value = cursor
    cursor.fetchall.return_value = orig_tables
    cursor.description = [("DATA",)]

    maria_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    test_data_df = maria_db.get_test_data_from_table("test_table")
    assert isinstance(test_data_df, pd.DataFrame)


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
def test_maria_db_connection(connect_mock):
    maria_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    assert maria_db.db_connection()


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
def test_maria_get_sql_for_retrieving_table_list(connect_mock):
    maria_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    tables_sql = maria_db.get_sql_for_retrieving_table_list()
    assert tables_sql == "SHOW TABLES;"


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
def test_maria_get_sql_for_retrieving_table_definition(connect_mock):
    maria_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    table_name = "Test"
    definition_sql = maria_db.get_sql_for_retrieving_table_definition(table_name)
    assert table_name in definition_sql


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
def test_maria_get_sql_for_retrieving_primary_key(connect_mock):
    maria_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    table_name = "Test"
    definition_sql = maria_db.get_sql_for_retrieving_primary_key(table_name)
    assert table_name in definition_sql


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.pymysql.connect")
def test_maria_get_sql_table_data_example(connect_mock):
    maria_db = MainDatabase.get_database("MariaDB")(DB_MARIA_CONFIG)
    table_name = "Test"
    sample_sql = maria_db.get_sql_table_data_example(table_name)
    assert table_name in sample_sql
    assert maria_db.schema_name in sample_sql


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.Oracle.db_connection")
def test_oracle_db_connection(connect_mock):
    oracle_db = MainDatabase.get_database("Oracle")(DB_ORACLE_CONFIG)
    assert oracle_db.db_connection()


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.Oracle.db_connection")
def test_oracle_get_sql_for_retrieving_table_list(connect_mock):
    oracle_db = MainDatabase.get_database("Oracle")(DB_ORACLE_CONFIG)
    tables_sql = oracle_db.get_sql_for_retrieving_table_list()
    assert oracle_db.owner in tables_sql
    assert "all_tables" in tables_sql


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.Oracle.db_connection")
def test_oracle_get_sql_for_retrieving_table_definition(connect_mock):
    oracle_db = MainDatabase.get_database("Oracle")(DB_ORACLE_CONFIG)
    table_name = "Test"
    definition_sql = oracle_db.get_sql_for_retrieving_table_definition(table_name)
    assert table_name in definition_sql


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.Oracle.db_connection")
def test_oracle_get_sql_for_retrieving_primary_key(connect_mock):
    oracle_db = MainDatabase.get_database("Oracle")(DB_ORACLE_CONFIG)
    table_name = "Test"
    definition_sql = oracle_db.get_sql_for_retrieving_primary_key(table_name)
    assert table_name in definition_sql


@patch(f"{PATCH_DATACLASS_GEN_DIR}.config.database.Oracle.db_connection")
def test_oracle_get_sql_table_data_example(connect_mock):
    oracle_db = MainDatabase.get_database("Oracle")(DB_ORACLE_CONFIG)
    table_name = "Test"
    sample_sql = oracle_db.get_sql_table_data_example(table_name)
    assert table_name in sample_sql
    assert oracle_db.schema_name in sample_sql
