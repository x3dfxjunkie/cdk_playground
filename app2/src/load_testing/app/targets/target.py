"""abstract base class for a load test target"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Target(ABC):
    """
    An abstract class representing a load test target (or sink). Subclasses should implement the send_data method
    """

    @property
    @abstractmethod
    def target_type(self) -> str:
        pass

    @abstractmethod
    def send_data(self, data: Dict[str, Any]) -> None:
        """
        write/send a record to target

        Args:
            data (Dict[str, Any]): a single record
        """
        pass

    @abstractmethod
    def send_batch(self, batch: List[Dict[str, Any]]) -> None:
        """
        write/send a batch of records to target

        Args:
            batch (List[Dict[str, Any]]): A list of records or events
        """
        pass
