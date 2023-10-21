""" Guest360 SQS Model """
from __future__ import annotations
from typing import Optional, Any
from pydantic import BaseModel, Field
from app.infrastructure.ingestion.config.tests.models.mixins.validator_mixins import EncryptionKeyValidatorMixin


class Sqs(BaseModel, EncryptionKeyValidatorMixin):
    queue_name: str = Field(
        ...,
        alias="queue_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    encryption_key: Optional[Any] = Field(
        ...,
        alias="encryption_key",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )
