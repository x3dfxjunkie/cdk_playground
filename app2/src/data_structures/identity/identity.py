"""Module representing various aspects of identity.
"""
from datetime import datetime
from typing import Optional, List
from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True, eq=True)
class IdentityNode:
    """Class representing a node in the identity graph."""

    domain: str
    identifier: str
    atomic_id: Optional[str]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True, eq=True)
class IdentityEdge:
    """Class representing an edge in the identity graph."""

    source_node: str
    target_node: str
    active: bool
    created_date: datetime
    deactivated_date: Optional[datetime]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class IdentityGraph:
    nodes: List[IdentityNode]
    edges: List[IdentityEdge]
