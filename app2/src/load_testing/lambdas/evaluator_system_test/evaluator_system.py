"""class EvaluatorSystemTest"""
from app.src.load_testing.lambdas.evaluator_system_test.endpoint_consumer_factory import EndpointConsumerFactory

CONFIG_ENDPOINT_TYPE = "type"
CONFIG_ENDPOINT = "endpoint"
CONFIG_LABEL = "label"


class EvaluatorSystemTest:
    """class EvaluatorSystemTest"""

    def __init__(self, start_time, prefix, execution_id):
        self.start_time = start_time
        self.prefix = prefix
        self.execution_id = execution_id

    def get_parameter_value(self, parameter):
        endpoint_consumer = EndpointConsumerFactory.get_endpoint_consumer(
            parameter.get(CONFIG_ENDPOINT).get(CONFIG_ENDPOINT_TYPE),
            config=parameter.get(CONFIG_ENDPOINT),
            prefix=self.prefix,
            start_time=self.start_time,
            execution_id=self.execution_id,
            label=parameter.get(CONFIG_LABEL),
        )
        try:
            value = endpoint_consumer.validate_parameter()
        except AttributeError:
            value = 0
        return {"name": parameter.get("label"), "value": value, "metadata": parameter}
