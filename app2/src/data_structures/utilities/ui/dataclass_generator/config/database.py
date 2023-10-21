"""Database utils file"""
from abc import ABC, abstractmethod
import logging
import oracledb

import pymysql
import pandas as pd
from pypika import Table, Case
from pypika.dialects import Query, OracleQuery
from app.src.data_structures.utilities.ui.dataclass_generator.utils.utils import map_table_dets_with_example

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class DatabaseTypeNotSupportedException(Exception):
    """Custom exception for cases where we are supplied an unsupported database type"""


class MainDatabase(ABC):
    """Base class for all database classes. Implements all the database functions."""

    database_type: str = "main"

    def __init__(self, config_dict):
        self.host = config_dict["host"]
        self.port = config_dict["port"]
        self.database = config_dict["database"]
        self.username = config_dict["username"]
        self.password = config_dict["password"]
        self.db_type = config_dict["db_type"]
        self.schema_name = config_dict["schema_name"] if "schema_name" in config_dict else self.database
        self.owner = config_dict["database"]
        self.source = config_dict["source_name"]

    @classmethod
    def get_database(cls, database_type: str):
        try:
            return next(cl for cl in cls.__subclasses__() if cl.database_type == database_type)
        except StopIteration as e:
            raise DatabaseTypeNotSupportedException(
                f"{database_type} is not a Database type supported by Auto-Mater"
            ) from e

    @abstractmethod
    def db_connection(self):
        """
        Creates a database connection.
        Returns: Database connection.
        """

    @abstractmethod
    def get_sql_for_retrieving_table_list(self) -> str:
        """
        This function returns the list of all tables within a database
        """

    @abstractmethod
    def get_sql_for_retrieving_table_definition(self, table_name: str) -> str:
        """
        This function returns the sql statement to retrieve table definition
        Args:
            table_name: Table name to retrieve definition.

        Returns:
            str: SQL statement to retrieve table definition.
        """

    @abstractmethod
    def get_sql_for_retrieving_primary_key(self, table_name: str) -> str:
        """
        This function returns the sql statement to retrieve table definition
        :return: sql statement
        """

    @abstractmethod
    def get_sql_table_data_example(self, table_name: str, num_of_rows: int = 1):
        """
        This function returns the sql statement to retrieve 1 row of data for a table
        :return: sql statement
        """

    def execute_cur(self, sql: str):
        """
        Execute the provided SQL statement using cursor.
        Args:
            sql: SQL statement to execute

        Returns: Cursor.

        """
        with self.db_connection() as conn:
            curr = conn.cursor(prepared=True)
            res = curr.execute(sql)
            conn.commit()
        return res

    def get_list_of_tables(self) -> list:
        """
        :return:
        """
        with self.db_connection() as conn:
            table_list = pd.read_sql(sql=self.get_sql_for_retrieving_table_list(), con=conn)
            return table_list.iloc[:, 0].values.tolist()

    def get_table_details_from_db(self, table_name: str):
        """
        Execute the provided sql statement using cursor
        Args:
            sql: sql statement to execute

        Returns: dataframe.
        :param table_name:
        :param dbconn:
        :param table_name:

        """
        with self.db_connection() as conn:
            table_dets_df = pd.read_sql(sql=self.get_sql_for_retrieving_table_definition(table_name), con=conn)
            table_example_df = pd.read_sql(sql=self.get_sql_table_data_example(table_name), con=conn)
            table_dets_df = map_table_dets_with_example(table_dets_df, table_example_df)
            pk_dets_df = pd.read_sql(sql=self.get_sql_for_retrieving_primary_key(table_name), con=conn)
        return table_dets_df, pk_dets_df

    def get_test_data_from_table(self, table_name: str, num_of_rows: int = 1):
        """
        Execute the provided sql statement using cursor
        Args:
            sql: sql statement to execute

        Returns: dataframe.
        :param table_name:
        :param dbconn:
        :param table_name:

        """

        with self.db_connection() as conn:
            test_data_df = pd.read_sql(sql=self.get_sql_table_data_example(table_name, num_of_rows), con=conn)
        return test_data_df


class Maria(MainDatabase):
    """
    MariaDB class for database connection.
    Args:
        Database: Super class
    """

    database_type: str = "MariaDB"

    def db_connection(self):
        """db_connection [Return database context manager connection object for Mysqldb]

        Returns:
            [object]: [context manager database connection object]
        """
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                port=int(self.port),
                database=self.database,
                charset="utf8mb4",
                local_infile=True,
                autocommit=True,
            )

            return conn

        except Exception as e:
            print(e.__cause__)
            raise e

    def get_sql_for_retrieving_table_list(self) -> str:
        """
        This function returns the list of all tables within a database
        Returns:
            str: SQL statement to retrieve tables.
        """
        sql = "SHOW TABLES;"
        return sql

    def get_sql_for_retrieving_table_definition(self, table_name: str) -> str:
        table = Table("information_schema.columns")
        query_builder = (
            Query.from_(table)
            .select(
                table.column_name.as_("COLUMN_NAME"),
                table.data_type.as_("DATA_TYPE"),
                Case()
                .when(table.numeric_precision.notnull(), table.numeric_precision)
                .else_("character_maximum_length")
                .as_("LENGTH"),
                table.is_nullable.as_("NULLABLE"),
                table.column_default.as_("DEFAULT_VALUE"),
            )
            .where(table.table_name == table_name)
            .orderby(table.ordinal_position)
        )
        return query_builder.get_sql()

    def get_sql_for_retrieving_primary_key(self, table_name: str) -> str:
        """
        This function returns the sql statement to retrieve table definition from Mariadb
        :return: sql statement
        """
        table_constraints = Table("information_schema.table_constraints").as_("t")
        key_column_usage = Table("information_schema.key_column_usage").as_("k")
        query_builder = (
            Query.from_(table_constraints)
            .select(key_column_usage.COLUMN_NAME.as_("PRIMARY_KEY"))
            .left_join(key_column_usage)
            .using(table_constraints.constraint_name, table_constraints.table_schema, table_constraints.table_name)
            .where(table_constraints.constraint_type == "PRIMARY_KEY")
            .where(table_constraints.table_name == table_name)
        )

        return query_builder.get_sql()

    def get_sql_table_data_example(self, table_name: str, num_of_rows: int = 1) -> str:
        """
        This function returns the sql statement to retrieve 1 row of data for a table from Mariadb
        :return: sql statement
        """
        table = Table(f"{self.schema_name}.{table_name}")
        query_builder = Query.from_(table).select("*").limit(num_of_rows)
        return query_builder.get_sql()


class Oracle(MainDatabase):
    """OracleDB connection class"""

    database_type: str = "Oracle"

    def __init__(self, config_dict):
        super().__init__(config_dict)
        self.service_name = config_dict["service_name"]
        if config_dict.get("owner"):
            self.owner = config_dict["owner"]

    def db_connection(self):
        """db_connection [Return database context manager connection object for Mysqldb]

        Returns:
            [object]: [context manager database connection object]
        """

        dsn = f"{self.host}:{self.port}/{self.service_name}"
        conn = oracledb.connect(dsn=dsn, user=self.username, password=self.password)

        return conn

    def get_sql_for_retrieving_table_list(self) -> str:
        """
        This function returns the list of all tables within a database
        :return: sql statement
        """
        table = Table("ALL_TAB_COLUMNS")
        query_builder = (
            OracleQuery.from_("all_tables")
            .select(table.table_name.as_("TABLES"))
            .where(table.OWNER == self.owner)
            .orderby(table.table_name)
        )

        return query_builder.get_sql()

    def get_sql_for_retrieving_table_definition(self, table_name: str) -> str:
        """
        This function returns the sql statement to retrieve table definition from Oracle
        :return: sql statement
        """
        table = Table("ALL_TAB_COLUMNS")
        query_builder = (
            OracleQuery.from_(table)
            .select(
                table.table_name,
                table.column_name,
                table.data_type,
                table.data_length,
                table.nullable,
                table.data_default,
            )
            .where(table.table_name == table_name)
        )
        return query_builder.get_sql()

    def get_sql_for_retrieving_primary_key(self, table_name: str) -> str:
        """
        This function returns the sql statement to retrieve table definition from Oracle
        :return: sql statement
        """
        cons = Table("all_constraints").as_("cons")
        cols = Table("all_cons_columns").as_("cols")

        query_builder = (
            OracleQuery.from_(cols)
            .select(cols.column_name.as_("PRIMARY_KEY"))
            .join(cons)
            .on(cons.constraint_name == cols.constraint_name)
            .where(cons.owner == cols.owner)
            .where(cols.table_name == table_name)
            .where(cons.constraint_type == "P")
            .orderby(cols.table_name, cols.position)
        )
        return query_builder.get_sql()

    def get_sql_table_data_example(self, table_name: str, num_of_rows: int = 1) -> str:
        """
        This function returns 1 row of data from a selected table from Oracle
        :return: sql statement
        """
        # NOTE: 'fetch first' isn't supported by Pypika currently so we can't use that API to build the query here
        # https://github.com/kayak/pypika/blob/master/pypika/dialects.py
        sql = f"""SELECT * FROM {self.schema_name}.{table_name}  FETCH FIRST {num_of_rows} ROWS ONLY"""
        return sql
