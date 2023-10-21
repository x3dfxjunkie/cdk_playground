"""
    Consumer Static
"""

import logging
from typing import Any
from app.src.load_testing.lambdas.evaluator_system_test.endpoint_consumer import EndPointConsumer

logger = logging.getLogger(__name__)


class StaticConsumer(EndPointConsumer):
    """
    Gets count of objects or records from S3
    """

    def __init__(self, value: int) -> None:
        self.value = value

    def validate_parameter(self) -> Any:
        return self.value
