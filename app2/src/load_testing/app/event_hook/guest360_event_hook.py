"""
    Class Guest360EventHook
"""

import threading

from locust import events


# pylint: disable=E1120
class Guest360EventHook:
    """
    SubClass that handles the events and their corresponding listener
    """

    _handlers = []
    _instance = None
    _lock = threading.Lock()

    # pylint: disable=W0613, E1120
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def fire(self, **kwargs):
        """
        fire and request event of locust
        """
        events.request.fire(**kwargs)

    def get_handlers(self):
        """
        Return list of handlers
        """
        return self._handlers

    def add_listener(self, request):
        """
        Validates if no exist a same handler in the listeners list and added it
        """

        if f"{request.__module__}.{request.__name__}" not in [
            f"{handler.__module__}.{handler.__name__}" for handler in self.get_handlers()
        ]:
            self._handlers.append(request)
            return events.request.add_listener(request)
