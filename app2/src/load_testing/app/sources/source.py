"""
An abstract class representing a load test source (S3, local_file). Subclasses should implement the load_sample_data method
"""
from abc import ABC, abstractmethod


class Source(ABC):
    """
    An abstract class representing a load test source (S3, local_file). Subclasses should implement the load_sample_data method
    """

    @abstractmethod
    def get_sample_data(self) -> list:
        """
        load sample data
        """
        pass
