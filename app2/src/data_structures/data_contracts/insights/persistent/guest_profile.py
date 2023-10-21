"""Source Data Contract for Orion EA Lightning Lane"""
from __future__ import annotations

from datetime import date, datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from app.src.data_structures.data_contracts.insights.persistent.base_persistent import BasePersistent


class ProfileModel(BasePersistent):
    atomic_id: str = Field(
        ...,
        alias="atomic_id",
        name="Atomic ID",
        description="Unique ID for guest in UCE platform",
        example="cb0a1fb0-4cf0-4b68-b3a1-9f02cac3983b",
    )
    attractions_ridden: List[AttractionRideHistory] = Field(
        ...,
        alias="attractions_ridden",
        name="Attractions Ridden",
        description="List of attractions ridden by guest",
        example='[{"name":"Thunder Mountain", "count_ridden":1}, {"name":"Splash Mountain", "count_ridden": 2}]',
    )

    class AttractionRideHistory:
        """Class for encapsulating the data associated with a single ride completed history."""

        attraction_id: str
        attraction_name: str
        attraction_ride_count: int
