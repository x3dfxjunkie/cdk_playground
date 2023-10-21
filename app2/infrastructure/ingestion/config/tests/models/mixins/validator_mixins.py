"""Module for containing Mixins that include common validator methods which may be re-used"""
from pydantic import validator
from app.infrastructure.ingestion.config.utils.validation_utils import type_validator


class EncryptionKeyValidatorMixin:
    @validator("encryption_key")
    def validate_encryption_key(cls, v):  # pylint: disable=E0213
        return type_validator(
            value=v,
            lib_path="aws_cdk.aws_kms",
            attr_path="Key",
        )
