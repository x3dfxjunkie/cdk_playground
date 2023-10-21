"""''
The SqlTransactionGenerator class is designed for creating and manipulating SQL tables based on Pydantic data contracts.
It simulates database transactions, such as insert, update, and delete operations, on a SQL database.
The class offers customization options like adding prefixes to column names, dropping existing tables and more.
"""

import random
import importlib
from pydantic import BaseModel
from typing import Dict, Type, Optional, List, Any
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, MetaData, Table, inspect, Date
from sqlalchemy.orm import sessionmaker, Session
from app.src.load_testing.app.targets.target import Target


metadata = MetaData()
tables: Dict[str, Table] = {}


class SqlTransactionConfig(BaseModel):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    add_prefix: bool = False
    drop_existing: bool = True
    only_payload_data: bool = True
    all_columns_as_varchar: bool = False
    number_of_items: int = 100
    prob_update: float = 0.0
    prob_delete: float = 0.0
    use_alias: bool = False


class SqlTransactionGenerator(Target):
    """Class for creating and manipulating SQL tables based on Pydantic data contract.
    Args:
        data_contract_batch (list): List of data contracts, path and class name for each item.
        db_user (str): Database username.
        db_password (str): Database password.
        db_host (str): Database host address.
        db_port (int): Database port number.
        db_name (str): Name of the database.
        add_prefix (bool, optional): Flag to add prefix to column names. Default is True.
        drop_existing (bool, optional): Flag to drop existing tables. Default is True.
        only_payload_data (bool, optional): Flag to use only payload data. Default is True.
        all_columns_as_varchar (bool, optional): Flag to make all columns VARCHAR type. Default is False.
        number_of_items (int, optional): Number of items to simulate. Default is 100.
        prob_update (float, optional): Probability of an update operation. Default is 0.0.*
        prob_delete (float, optional): Probability of a delete operation. Default is 0.0.*

        * Randomly choose an action (update, delete, or insert) based on given probabilities.
        The action is chosen based on weights for each action, defined as follows:

        Let P(update) = self.prob_update, P(delete) = self.prob_delete
        Then, P(insert) = 1 - P(update) - P(delete)

        The weights [P(update), P(delete), P(insert)] are used to randomly select an action.

        Constraints Ranges:
        - 1. 0 <= P(update), P(delete) <= 1
        - 2. P(update) + P(delete) < 1 to ensure a non-zero probability for insert action.
    """

    def __init__(self, data_contract_batch: List[Dict[str, Any]], config: SqlTransactionConfig):
        """Initializes SqlTransactionGenerator with database configuration and transaction options."""
        self.data_contract_batch = data_contract_batch
        self.connection_string = (
            f"mysql+pymysql://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}"
        )
        self.add_prefix = config.add_prefix
        self.drop_existing = config.drop_existing
        self.engine = create_engine(self.connection_string, echo=True)
        self.only_payload_data = config.only_payload_data
        self.all_columns_as_varchar = config.all_columns_as_varchar
        self.number_of_items = config.number_of_items
        self.prob_update = config.prob_update
        self.prob_delete = config.prob_delete
        self.use_alias = config.use_alias
        self._target_type = "DMS"
        self.class_name = data_contract_batch[0]["class_name"]  # just initial value

    @property
    def target_type(self) -> str:
        return self._target_type

    def _map_pydantic_field_to_column(self, prefix: str, name: str, field: Type[BaseModel]) -> Optional[Column]:
        """
        Maps a Pydantic field to an SQLAlchemy Column.

        Parameters:
        - prefix (str): The prefix to add to the column name.
        - name (str): The name of the Pydantic field.
        - field (Type[BaseModel]): The Pydantic field.

        Returns:
        Optional[Column]: An SQLAlchemy Column object or None.
        """
        if self.use_alias and field.alias != name:
            column_name = f"{prefix}{field.alias}" if self.add_prefix else field.alias
        else:
            column_name = f"{prefix}{name}" if self.add_prefix else name

        if self.all_columns_as_varchar:
            return Column(column_name, String(255))

        match field.type_.__name__:
            case "int":
                return Column(column_name, Integer)
            case "str":
                return Column(column_name, String(255))
            case "datetime":
                return Column(column_name, DateTime)
            case "date":
                return Column(column_name, Date)
            case "bool":
                return Column(column_name, Boolean)
        return Column(column_name, String(255))

    def _process_model(self, model: Type[BaseModel], prefix: str, columns: List[Column]):
        """
        Processes the Pydantic data contract to extract columns for the SQL table.

        Parameters:
        - model (Type[BaseModel]): The Pydantic data contract.
        - prefix (str): The prefix for column names.
        - columns (List[Column]): List to append resulting SQLAlchemy Columns to.
        """
        fields = model.__fields__

        if self.only_payload_data and "data" in fields:
            fields = fields["data"].type_.__fields__

        for name, field in fields.items():
            if issubclass(field.type_, BaseModel):
                new_prefix = f"{prefix}{name}_"
                self._process_model(field.type_, new_prefix, columns)
            else:
                column = self._map_pydantic_field_to_column(prefix, name, field)
                if column is not None:
                    columns.append(column)

    def _create_table(self, model: Type[BaseModel]) -> Table:
        """
        Creates an SQL table based on the Pydantic data contract.

        Parameters:
        - model (Type[BaseModel]): The Pydantic model.

        Returns:
        Table: The created SQLAlchemy Table object.
        """
        columns = [Column("_id", Integer, primary_key=True, autoincrement=True)]
        self._process_model(model, "", columns)

        table_name = model.__name__
        if table_name in tables:
            table = Table(table_name, metadata, *columns, extend_existing=True)
        else:
            metadata.clear()
            table = Table(table_name, metadata, *columns)
        tables[table_name] = table
        return table

    def _drop_existing_table(self, table_name: str):
        """
        Drops an existing table from the database.

        Parameters:
        - table_name (str): The name of the table to drop.
        """
        inspector = inspect(self.engine)
        if table_name in inspector.get_table_names():
            table = Table(table_name, metadata)
            table.drop(self.engine)

    def create_sql_table(self):
        """Creates SQL tables using the specified Pydantic data contracts."""
        for contract in self.data_contract_batch:
            module = importlib.import_module(contract["data_contract"].replace(".py", "").replace("/", "."))
            pydantic_model = getattr(module, contract["class_name"])

            if self.drop_existing:
                self._drop_existing_table(pydantic_model.__name__)

            self._create_table(pydantic_model)

            metadata.create_all(self.engine)

    def _insert_data(self, session: Session, data: Dict):
        """
        Inserts data into the SQL table.

        Parameters:
        - session (Session): The SQLAlchemy Session object.
        - data (Dict): The data to insert.
        """
        ins = tables[self.class_name].insert().values(**data)
        session.execute(ins)

    def _update_data(self, session: Session, id_: int, data: Dict):
        """
        Updates a record in the SQL table.

        Parameters:
        - session (Session): The SQLAlchemy Session object.
        - id_ (int): The ID of the record to update.
        - data (Dict): The new data.
        """
        session.query(tables[self.class_name]).filter_by(_id=id_).update(data)

    def _delete_data(self, session: Session, id_: int):
        """
        Deletes a record from the SQL table.

        Parameters:
        - session (Session): The SQLAlchemy Session object.
        - id_ (int): The ID of the record to delete.
        """
        session.execute(tables[self.class_name].delete().where(tables[self.class_name].c._id == id_))

    def send_data(self, data: Dict[str, Any], session: Optional[Session] = None) -> None:
        """
        Simulates the next SQL transaction, which could be an insert, update, or delete operation.

        Parameters:
        - data (Dict): The data for insert or update operations.
        """
        external_session = True if session else False
        if not session:
            session_db = sessionmaker(bind=self.engine)
            session = session_db()

        try:
            if self.prob_update > 0 or self.prob_delete > 0:
                random_id = random.randint(1, self.number_of_items)  # NOSONAR
                #  https://rules.sonarsource.com/python/RSPEC-2245/
                existing_entry = session.query(tables[self.class_name]).filter_by(_id=random_id).first()

                if existing_entry:
                    action_choice = random.choices(  # NOSONAR
                        #  https://rules.sonarsource.com/python/RSPEC-2245/
                        ["update", "delete", "insert"],
                        weights=[self.prob_update, self.prob_delete, 1 - self.prob_update - self.prob_delete],
                        k=1,
                    )[0]

                    match action_choice:
                        case "update":
                            self._update_data(session, random_id, data)
                        case "delete":
                            self._delete_data(session, random_id)
                        case "insert":
                            self._insert_data(session, data)
                else:
                    self._insert_data(session, data)
            else:
                self._insert_data(session, data)

            if not external_session:
                session.commit()
        except Exception as e:
            if not external_session:
                session.rollback()
            print(f"Failed to handle data. Reason: {e}")

        if not external_session:
            session.close()

    def send_batch(self, batch: List[Dict[str, Any]]) -> None:
        """
        Sends a batch of data to the database.

        Parameters:
        - batch (List[Dict]): The list containing data to be sent.
        """
        session_db = sessionmaker(bind=self.engine)
        with session_db() as session:
            for item in batch:
                self.class_name = item["class_name"]
                self.send_data(item["payload"], session)
            session.commit()
