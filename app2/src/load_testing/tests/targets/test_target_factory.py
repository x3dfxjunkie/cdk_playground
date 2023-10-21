"""Target Factory tests"""


import pytest
from unittest.mock import patch
from app.src.load_testing.app.targets.target_factory import (
    TargetFactory,
    PatternType,
    KinesisStreamTarget,
    RabbitMQTarget,
    SqlTransactionGenerator,
)

CONFIG_REGION_NAME = "region"
CONFIG_STREAM_NAME = "stream_name"
CONFIG_MESSAGING_HOST = "host"
CONFIG_MESSAGING_PORT = "port"
CONFIG_MESSAGING_VHOST = "vhost"
CONFIG_MESSAGING_USERNAME = "username"
CONFIG_MESSAGING_SECUREPASS = "secure"

kinesis_config = {CONFIG_REGION_NAME: "us-east-1", CONFIG_STREAM_NAME: "cme-dlr-kinesis-dm"}

messaging_config = {
    CONFIG_MESSAGING_HOST: "rabbitmq.lst-use1-pr-3400-load-testing-static",
    CONFIG_MESSAGING_PORT: 5672,
    CONFIG_MESSAGING_VHOST: "/",
    CONFIG_MESSAGING_USERNAME: "guest",
    CONFIG_MESSAGING_SECUREPASS: "guest",
}


# Mocked Constructors
def mock_kinesis_constructor(self, stream_name, region):
    self.region = region
    self.stream_name = stream_name
    self.send_count = 0


def mock_rabbitmq_constructor(self, host, port, vhost, username, secure_string):
    self.host = host
    self.port = port
    self.vhost = vhost
    self.username = username
    self.password = secure_string
    self.connection = None


# Test functions
@patch.object(KinesisStreamTarget, "__init__", mock_kinesis_constructor)
def test_get_target_kinesis():
    target = TargetFactory.get_target(
        PatternType.PATTERN_TYPE_KINESIS, config=kinesis_config, prefix="lst-use1-guest360"
    )
    assert isinstance(target, KinesisStreamTarget)
    assert target.stream_name == "lst-use1-guest360-cme-dlr-kinesis-dm"


@patch.object(RabbitMQTarget, "__init__", mock_rabbitmq_constructor)
def test_get_target_rabbitmq():
    target = TargetFactory.get_target(PatternType.PATTERN_TYPE_MESSAGING, config=messaging_config)
    assert isinstance(target, RabbitMQTarget)
    assert target.host == "rabbitmq.lst-use1-pr-3400-load-testing-static"


def mock_sql_transaction_generator_constructor(self, data_contract_batch, config):
    self.data_contract_batch = data_contract_batch
    self.db_user = config.db_user
    self.db_password = config.db_password
    self.db_host = config.db_host
    self.db_port = config.db_port
    self.db_name = config.db_name
    self.add_prefix = config.add_prefix
    self.drop_existing = config.drop_existing
    self.only_payload_data = config.only_payload_data
    self.all_columns_as_varchar = config.all_columns_as_varchar
    self.number_of_items = config.number_of_items
    self.prob_update = config.prob_update
    self.prob_delete = config.prob_delete


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

dms_config = {
    "username": "guest",
    "host": "lst-use1-pr-4074-ingest-c-loadtestingrdse6b4aguest-udyjzyxpirhe.c5rhzyl2py8d.us-east-1.rds.amazonaws.com",
    "port": 3306,
    "dbname": "db_load_testing",
    "add_prefix": True,
    "drop_existing": False,
    "only_payload_data": True,
    "all_columns_as_varchar": True,
    "number_of_items": 200,
    "prob_update": 0.5,
    "prob_delete": 0.3,
}


@patch.object(SqlTransactionGenerator, "__init__", mock_sql_transaction_generator_constructor)
def test_get_target_dms():
    target = TargetFactory.get_target(
        PatternType.PATTERN_TYPE_DMS, data_contract_batch=data_contract_batch, **dms_config
    )

    assert isinstance(target, SqlTransactionGenerator)
    assert target.db_user == "guest"
    assert (
        target.db_host
        == "lst-use1-pr-4074-ingest-c-loadtestingrdse6b4aguest-udyjzyxpirhe.c5rhzyl2py8d.us-east-1.rds.amazonaws.com"
    )
    assert target.db_port == 3306
    assert target.db_name == "db_load_testing"
    assert target.add_prefix == True
    assert target.drop_existing == False
    assert target.only_payload_data == True
    assert target.all_columns_as_varchar == True
    assert target.number_of_items == 200
    assert target.prob_update == 0.5
    assert target.prob_delete == 0.3
