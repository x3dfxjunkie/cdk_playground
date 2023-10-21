"""
    Target Factory
"""
from app.src.load_testing.app.targets.kinesis_stream_target import KinesisStreamTarget
from app.src.load_testing.app.targets.rabbitmq_target import RabbitMQTarget
from app.src.load_testing.app.targets.sql_transaction_generator import SqlTransactionGenerator, SqlTransactionConfig
from app.src.load_testing.app.targets.target import Target


# Endpoint types
class PatternType:
    PATTERN_TYPE_KINESIS = "kinesis"
    PATTERN_TYPE_MESSAGING = "messaging"
    PATTERN_TYPE_DMS = "dms"


CONFIG_REGION_NAME = "region"
CONFIG_STREAM_NAME = "stream_name"
CONFIG_MESSAGING_HOST = "host"
CONFIG_MESSAGING_PORT = "port"
CONFIG_MESSAGING_VHOST = "vhost"
CONFIG_MESSAGING_USERNAME = "username"
CONFIG_MESSAGING_SECUREPASS = "secure"
CONFIG_DMS_DB_USER = "username"
CONFIG_DMS_DB_PASSWORD = "password"  # pragma: allowlist secret
CONFIG_DMS_DB_HOST = "host"
CONFIG_DMS_DB_PORT = "port"
CONFIG_DMS_DB_NAME = "dbname"
CONFIG_DMS_ADD_PREFIX = "add_prefix"
CONFIG_DMS_DROP_EXISTING = "drop_existing"
CONFIG_DMS_ONLY_PAYLOAD_DATA = "only_payload_data"
CONFIG_DMS_ALL_COLUMNS_AS_VARCHAR = "all_columns_as_varchar"
CONFIG_DMS_NUMBER_OF_ITEMS = "number_of_items"
CONFIG_DMS_PROB_UPDATE = "prob_update"
CONFIG_DMS_PROB_DELETE = "prob_delete"


# pylint: disable=C0103,W0621,W0612
class TargetFactory:
    """
    Class that return an instance of object Target according to the target_type
    """

    @staticmethod
    def get_target(endpoint_type, **kwargs) -> Target:
        target = None
        match endpoint_type:
            case PatternType.PATTERN_TYPE_KINESIS:
                target = TargetFactory.get_target_kinesis(**kwargs)
            case PatternType.PATTERN_TYPE_MESSAGING:
                target = TargetFactory.get_target_messaging(**kwargs)
            case PatternType.PATTERN_TYPE_DMS:
                target = TargetFactory.get_target_dms(**kwargs)
        return target

    @staticmethod
    def get_target_kinesis(config, prefix):
        stream_name = f"{prefix}-{config[CONFIG_STREAM_NAME]}"
        region = config[CONFIG_REGION_NAME]
        return KinesisStreamTarget(stream_name, region)

    @staticmethod
    def get_target_messaging(config):
        host = config[CONFIG_MESSAGING_HOST]
        port = config[CONFIG_MESSAGING_PORT]
        vhost = config[CONFIG_MESSAGING_VHOST]
        username = config[CONFIG_MESSAGING_USERNAME]
        password = config[CONFIG_MESSAGING_SECUREPASS]
        return RabbitMQTarget(host, port, vhost, username, password)

    @staticmethod
    def get_target_dms(data_contract_batch, **config):
        dms_config = SqlTransactionConfig(
            db_user=config[CONFIG_DMS_DB_USER],
            db_password=config.get(CONFIG_DMS_DB_PASSWORD, "secure"),
            db_host=config[CONFIG_DMS_DB_HOST],
            db_port=config[CONFIG_DMS_DB_PORT],
            db_name=config[CONFIG_DMS_DB_NAME],
            add_prefix=config.get(CONFIG_DMS_ADD_PREFIX, False),
            drop_existing=config.get(CONFIG_DMS_DROP_EXISTING, True),
            only_payload_data=config.get(CONFIG_DMS_ONLY_PAYLOAD_DATA, True),
            all_columns_as_varchar=config.get(CONFIG_DMS_ALL_COLUMNS_AS_VARCHAR, False),
            number_of_items=config.get(CONFIG_DMS_NUMBER_OF_ITEMS, 100),
            prob_update=config.get(CONFIG_DMS_PROB_UPDATE, 0.0),
            prob_delete=config.get(CONFIG_DMS_PROB_DELETE, 0.0),
        )
        return SqlTransactionGenerator(data_contract_batch=data_contract_batch, config=dms_config)
