"""
    Endpoint Consumer Factory    
"""


from app.src.load_testing.lambdas.evaluator_system_test.cloudwatch_consumer import CloudWatchConsumer
from app.src.load_testing.lambdas.evaluator_system_test.endpoint_consumer import EndPointConsumer
from app.src.load_testing.lambdas.evaluator_system_test.s3_consumer import S3Consumer
from app.src.load_testing.lambdas.evaluator_system_test.static_consumer import StaticConsumer

# config names
CONFIG_BUCKET_NAME = "bucket_name"
CONFIG_BUCKET_PREFIX = "prefix"
CONFIG_STATISTIC = "statistic"
CONFIG_START_TIME = "start_time"
CONFIG_NAMESPACE = "namespace"
CONFIG_METRIC_NAME = "metric_name"
CONFIG_DIMENSIONS = "dimensions"
CONFIG_PERIOD = "period"
CONFIG_STATIC_VALUE = "value"

CONFIG_SNOWFLAKE_SECRET_NAME = "snowflake_secret_name"  # pragma: allowlist secret
CONFIG_USER = "user"
CONFIG_ROLE = "role"
CONFIG_ACCOUNT = "account"
CONFIG_WAREHOUSE = "warehouse"
CONFIG_DATABASE = "database"
CONFIG_SCHEMA = "schema"
CONFIG_TABLE = "table"


# source types
class EndPointConsumerType:
    ENDPOINT_CONSUMER_TYPE_S3 = "s3"
    ENDPOINT_CONSUMER_TYPE_CLOUDWATCH = "cloudwatch"
    ENDPOINT_CONSUMER_TYPE_STATIC = "static"


# pylint: disable=C0103,W0621,W0612,W0613
class EndpointConsumerFactory:
    """
    Class that return an instance of a Object EndPointConsumer according to the EndPointConsumerType
    """

    @staticmethod
    def get_endpoint_consumer(endpoint_consumer_type, **kwargs) -> EndPointConsumer:
        endpoint_consumer = None

        if endpoint_consumer_type == EndPointConsumerType.ENDPOINT_CONSUMER_TYPE_S3:
            endpoint_consumer = EndpointConsumerFactory.get_endpoint_consumer_s3(**kwargs)
        elif endpoint_consumer_type == EndPointConsumerType.ENDPOINT_CONSUMER_TYPE_CLOUDWATCH:
            endpoint_consumer = EndpointConsumerFactory.get_endpoint_consumer_cloudwatch(**kwargs)
        elif endpoint_consumer_type == EndPointConsumerType.ENDPOINT_CONSUMER_TYPE_STATIC:
            endpoint_consumer = EndpointConsumerFactory.get_endpoint_consumer_static(**kwargs)
        else:
            pass
        return endpoint_consumer

    @staticmethod
    def get_endpoint_consumer_s3(config, prefix, start_time, label, execution_id=None):
        bucket_name = f"{prefix}-{config[CONFIG_BUCKET_NAME]}"
        bucket_path = config[CONFIG_BUCKET_PREFIX]
        statistic = config[CONFIG_STATISTIC]

        print(bucket_name, bucket_path, statistic)

        return S3Consumer(bucket_name, bucket_path, start_time, statistic, execution_id)

    @staticmethod
    def get_endpoint_consumer_static(config, start_time=None, execution_id=None, label=None, prefix=None):
        value = int(config[CONFIG_STATIC_VALUE])
        return StaticConsumer(value)

    @staticmethod
    def get_endpoint_consumer_cloudwatch(config, start_time, execution_id, label, prefix=None):
        namespace = config[CONFIG_NAMESPACE]
        metric_name = config[CONFIG_METRIC_NAME]
        statistic = config[CONFIG_STATISTIC]
        dimensions = config[CONFIG_DIMENSIONS]
        period = config.get(CONFIG_PERIOD, None)

        return CloudWatchConsumer(
            label, namespace, metric_name, statistic, dimensions, start_time, period, execution_id
        )
