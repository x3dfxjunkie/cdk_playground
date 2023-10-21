"""Feature flag interface"""
from abc import ABC, abstractmethod
from typing import Any, Dict


class FeatureFlagInterface(ABC):
    """
    Base interface for feature flags. This class should never be instatiated directly, and only subclassed.
    Each domain should subclass this interface and implement get_config and get_dependences method
    """

    @abstractmethod
    def get_config(self, environment: str) -> Dict[str, Any]:
        raise NotImplementedError("This method must be implemented")

    @abstractmethod
    def resolve_dependences(self, config: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError("This method must be implemented")

    @abstractmethod
    def is_feature_enabled(self, environment: str, key_path: str) -> bool:
        raise NotImplementedError("This method must be implemented")
