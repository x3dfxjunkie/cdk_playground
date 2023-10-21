"""
An abstract class representing a endpoint consumer (S3, Cloudwatch). Subclasses should implement the validate_parameter method
"""
from abc import ABC, abstractmethod
from typing import Any


class EndPointConsumer(ABC):
    """
    An abstract class representing a endpoint consumer (S3, Cloudwatch). Subclasses should implement the validate_parameter method
    """

    @abstractmethod
    def validate_parameter(self) -> Any:
        """
        validate parameter
        """
        pass
