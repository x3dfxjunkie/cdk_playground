"""Unit Test for SQL transaction Generator Class"""
import pytest
from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import text
from pydantic import BaseModel, Field
from datetime import datetime
from app.src.load_testing.app.targets.sql_transaction_generator import SqlTransactionGenerator, SqlTransactionConfig

Base = declarative_base()

data_contract_batch = [
    {
        "data_contract": "app.src.data_structures.data_contracts.source.dreams.charge_account.v0.dreams_charge_account_chrg_grp_source_data_contract",
        "class_name": "DREAMSChargeAccountChrgGrpModel",
    },
    {
        "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_inventory_product_source_data_contract",
        "class_name": "CMEDLRInventoryProductModel",
    },
]


class Data(BaseModel):
    """Class for DREAMS Charge Account Charge Group Data"""

    auth_pin_encrpt_hash_vl: str = Field(
        ...,
        alias="AUTH_PIN_ENCRPT_HASH_VL",
        name="",
        description="",
        example="AAAaaAAAAAAAAaaAAAAaaAAAaaAAAAAAAA+A",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
    chrg_grp_id: int = Field(
        ...,
        alias="CHRG_GRP_ID",
        name="",
        description="",
        example=983378339,
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


DB_CONFIG = {
    "db_user": "test_user",
    "db_password": "",  # pragma: allowlist secret
    "db_host": "test_host",
    "db_port": 3306,
    "db_name": "test_db",
}


@pytest.fixture
def transaction_generator():
    config = SqlTransactionConfig(**DB_CONFIG)
    return SqlTransactionGenerator(data_contract_batch=data_contract_batch, config=config)


@pytest.fixture
def mock_engine():
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def patched_sessionmaker():
    with patch("sqlalchemy.orm.sessionmaker") as mock:
        yield mock


@pytest.fixture
def setup_database_with_data(patched_sessionmaker, transaction_generator, mock_engine):
    patched_sessionmaker.return_value = sessionmaker(bind=mock_engine)
    transaction_generator.engine = mock_engine
    transaction_generator.create_sql_table()

    data = {
        "auth_pin_encrpt_hash_vl": "testteST1234Test45string",
        "chrg_grp_id": 57708333,
        "chrg_grp_sts_nm": "UnEarned",
        "chrg_grp_typ_nm": "From Booking",
        "chrg_grp_ds": "Root",
        "chrg_grp_strt_dts": datetime.fromisoformat("1996-04-22T08:21:14"),
        "chrg_grp_end_dts": datetime.fromisoformat("2022-05-30T22:59:45"),
        "txn_fac_id": 9112,
        "src_acct_ctr_id": 626,
        "grp_dlgt_sml_bal_wrtoff_in": "testteST1234Test45string",
        "create_usr_id_cd": "NGEONEVIEW",
        "create_dts": datetime.fromisoformat("2022-04-03T01:47:49"),
        "updt_usr_id_cd": "FREEDOM",
        "updt_dts": datetime.fromisoformat("2010-06-30T01:49:44"),
        "jdo_seq_nb": 8224,
        "chrg_grp_actv_in": "xNOTIFIER",
    }
    transaction_generator.send_data(data)

    return mock_engine, transaction_generator.data_contract_batch[0]["class_name"], transaction_generator


def test_initialization(transaction_generator):
    assert transaction_generator.data_contract_batch == data_contract_batch


def test_map_pydantic_field_to_column(transaction_generator):
    column = transaction_generator._map_pydantic_field_to_column(
        "", "auth_pin_encrpt_hash_vl", Data.__fields__["auth_pin_encrpt_hash_vl"]
    )
    assert column.name == "auth_pin_encrpt_hash_vl"
    assert str(column.type) == "VARCHAR(255)"


@patch("sqlalchemy.orm.sessionmaker")
def test_send_data(mocked_sessionmaker, transaction_generator):
    with patch.object(transaction_generator, "_insert_data") as mock_insert, patch.object(
        transaction_generator, "_update_data"
    ) as mock_update, patch.object(transaction_generator, "_delete_data") as mock_delete:
        transaction_generator.send_data(
            {
                "auth_pin_encrpt_hash_vl": "testteST1234Test45string",
                "chrg_grp_id": 57708333,
                "chrg_grp_sts_nm": "UnEarned",
                "chrg_grp_typ_nm": "other word",
                "chrg_grp_ds": "Root",
                "chrg_grp_strt_dts": datetime.fromisoformat("1996-04-22T08:21:14"),
                "chrg_grp_end_dts": datetime.fromisoformat("2022-05-30T22:59:45"),
                "txn_fac_id": 9112,
                "src_acct_ctr_id": 626,
                "grp_dlgt_sml_bal_wrtoff_in": "testteST1234Test45string",
                "create_usr_id_cd": "NGEONEVIEW",
                "create_dts": datetime.fromisoformat("2022-04-03T01:47:49"),
                "updt_usr_id_cd": "FREEDOM",
                "updt_dts": datetime.fromisoformat("2010-06-30T01:49:44"),
                "jdo_seq_nb": 8224,
                "chrg_grp_actv_in": "xNOTIFIER",
            }
        )
        mock_insert.assert_called()
        mock_update.assert_not_called()
        mock_delete.assert_not_called()


@patch("sqlalchemy.orm.sessionmaker")
def test_insert_data(patched_sessionmaker, setup_database_with_data):
    mock_engine, table_name, _ = setup_database_with_data
    print(f"{table_name}: {table_name}")
    session_db = sessionmaker(bind=mock_engine)
    session = session_db()
    result = session.execute(text(f"SELECT * FROM {table_name}")).fetchall()

    expected_row = (
        1,
        "testteST1234Test45string",
        57708333,
        "UnEarned",
        "From Booking",
        "Root",
        "1996-04-22 08:21:14.000000",
        "2022-05-30 22:59:45.000000",
        9112,
        626,
        "testteST1234Test45string",
        "NGEONEVIEW",
        "2022-04-03 01:47:49.000000",
        "FREEDOM",
        "2010-06-30 01:49:44.000000",
        8224,
        "xNOTIFIER",
    )

    assert len(result) == 1
    assert result[0] == expected_row


@patch("sqlalchemy.orm.sessionmaker")
def test_update_data(patched_sessionmaker, setup_database_with_data):
    mock_engine, table_name, transaction_generator = setup_database_with_data
    session_db = sessionmaker(bind=mock_engine)
    session = session_db()

    original_result = session.execute(text(f"SELECT * FROM {table_name}")).fetchall()
    print(f"original_result: {original_result}")
    assert len(original_result) == 1

    updated_data = {
        "auth_pin_encrpt_hash_vl": "updatedValue",
        "chrg_grp_id": 1111,
        "chrg_grp_sts_nm": "Created as merge process",
        "chrg_grp_typ_nm": "dreams",
        "chrg_grp_ds": "Root",
        "chrg_grp_strt_dts": datetime.fromisoformat("2023-04-22T08:21:14"),
        "chrg_grp_end_dts": datetime.fromisoformat("2024-05-30T22:30:45"),
        "txn_fac_id": 2222,
        "src_acct_ctr_id": 3333,
        "grp_dlgt_sml_bal_wrtoff_in": "testteST1234Test45string",
        "create_usr_id_cd": "OCONK015",
        "create_dts": datetime.fromisoformat("2025-04-03T01:47:49"),
        "updt_usr_id_cd": "FREEDOM",
        "updt_dts": datetime.fromisoformat("2027-06-30T01:49:44"),
        "jdo_seq_nb": 4444,
        "chrg_grp_actv_in": "xNOTIFIER",
    }
    transaction_generator.prob_update = 1.0
    transaction_generator.number_of_items = 1
    transaction_generator.send_data(updated_data)

    updated_result = session.execute(text(f"SELECT * FROM {table_name}")).fetchall()
    assert len(updated_result) == 1

    expected_row = (
        1,
        "updatedValue",
        1111,
        "Created as merge process",
        "dreams",
        "Root",
        "2023-04-22 08:21:14.000000",
        "2024-05-30 22:30:45.000000",
        2222,
        3333,
        "testteST1234Test45string",
        "OCONK015",
        "2025-04-03 01:47:49.000000",
        "FREEDOM",
        "2027-06-30 01:49:44.000000",
        4444,
        "xNOTIFIER",
    )
    assert updated_result[0] == expected_row


@patch("sqlalchemy.orm.sessionmaker")
def test_delete_data(patched_sessionmaker, setup_database_with_data):
    mock_engine, table_name, transaction_generator = setup_database_with_data
    session_db = sessionmaker(bind=mock_engine)
    session = session_db()

    original_result = session.execute(text(f"SELECT * FROM {table_name}")).fetchall()
    print(f"original_result: {original_result}")
    assert len(original_result) == 1

    transaction_generator.prob_update = 0.0
    transaction_generator.prob_delete = 1.0
    transaction_generator.number_of_items = 1
    transaction_generator.send_data("")

    updated_result = session.execute(text(f"SELECT * FROM {table_name}")).fetchall()
    assert len(updated_result) == 0


@patch("sqlalchemy.orm.sessionmaker")
def test_send_batch_success(patched_sessionmaker, transaction_generator, mock_engine):
    patched_sessionmaker.return_value = sessionmaker(bind=mock_engine)
    transaction_generator.engine = mock_engine

    batch_data = [
        {
            "class_name": "DREAMSChargeAccountChrgGrpModel",
            "payload": {"auth_pin_encrpt_hash_vl": "testVal", "chrg_grp_id": 12345},
        }
    ]
    with patch.object(transaction_generator, "send_data") as mock_send_data:
        transaction_generator.send_batch(batch_data)
        assert mock_send_data.called


@patch("sqlalchemy.orm.sessionmaker")
def test_send_batch_exception(patched_sessionmaker, transaction_generator, mock_engine):
    patched_sessionmaker.return_value = sessionmaker(bind=mock_engine)
    transaction_generator.engine = mock_engine

    batch_data = [
        {
            "class_name": "DREAMSChargeAccountChrgGrpModel",
            "payload": {"auth_pin_encrpt_hash_vl": "testVal", "chrg_grp_id": 12345},
        }
    ]
    with patch.object(transaction_generator, "send_data", side_effect=Exception("Forced Exception")):
        with pytest.raises(Exception) as e_info:
            transaction_generator.send_batch(batch_data)
        assert str(e_info.value) == "Forced Exception"


def test_session_commit(setup_database_with_data, patched_sessionmaker):
    _, _, transaction_generator = setup_database_with_data
    data = {"auth_pin_encrpt_hash_vl": "testData", "chrg_grp_id": 123456}
    transaction_generator.send_data(data)
