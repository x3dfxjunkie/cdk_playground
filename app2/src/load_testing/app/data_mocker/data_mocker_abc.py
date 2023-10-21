"""abstract base class for a data mocker"""
from abc import ABC, abstractmethod


class DataMockerABC(ABC):
    """
    An Abstract Base Classes for data Mocker. Subclasses should implement the next method
    """

    @abstractmethod
    def next(self):
        """
        Generate Synthetic data
        """
        pass
