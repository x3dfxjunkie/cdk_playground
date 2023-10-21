from abc import ABC, abstractmethod
from typing import Any, Dict, List

class StreamProcessor(ABC):
    """
    Base interface for domain processors. This class should never be instatiated directly, and only subclassed.
    Each domain should subclass this processor and implement process_records_batch method
    """

    @abstractmethod
    def process_records_batch(self, records: List[Dict[str, Any]]) -> None:
        """
        Processes a batch of records from the stream for a given domain
        Args:
            records (List[Dict[str, Any]]): The records to process
        TODO: change implementation to return list of records successful vs failed
        Returns:
            None
        """
        return
