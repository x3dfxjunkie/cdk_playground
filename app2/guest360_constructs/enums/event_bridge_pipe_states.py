"""Event Bridge Pipe State"""
from enum import Enum


class EventBridgePipeState(str, Enum):
    # Only two states supported according to: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/update-pipe.html
    RUNNING: str = "RUNNING"
    STOPPED: str = "STOPPED"
