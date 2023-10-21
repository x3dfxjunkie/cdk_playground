"""Guest360MetricsLogger: Abstract class for logging load test metrics and test results"""
from abc import ABC, abstractmethod


class Guest360MetricsLogger(ABC):
    """
    An abstract class representing a logger for metrics. subclasses of this class should implement the publish method
    """

    @abstractmethod
    def publish(self) -> None:
        """
        optionally buffer and publishes metrics to a destination
        """
