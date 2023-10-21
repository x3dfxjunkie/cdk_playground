"""Tests for ingestion pipelines configuration files
"""
import pytest
from pydantic import ValidationError
from app.infrastructure.ingestion.config.utils.load_pipelines import load_configurations
from app.infrastructure.ingestion.config.utils.validation_utils import ValidationConfigError
from app.infrastructure.ingestion.config.tests.models.pipelines_models.dms_merged_model import DmsMergedModel
from app.infrastructure.ingestion.config.tests.models.pipelines_models.messaging_merged_model import (
    MessagingMergedModel,
)
from app.infrastructure.ingestion.config.tests.models.pipelines_models.k2k_merged_model import (
    Kinesis2kinesisMergedModel,
)
from app.infrastructure.ingestion.ingestion import IngestionPattern


@pytest.mark.parametrize(
    "pattern, pipe_model",
    [
        (IngestionPattern.DMS, DmsMergedModel),
        (IngestionPattern.MESSAGING, MessagingMergedModel),
        (IngestionPattern.K2K, Kinesis2kinesisMergedModel),
    ],
)
def test_config_validation(pipe_model, pattern):
    for config in load_configurations(pattern):
        try:
            validated_config = pipe_model(**config)
            assert isinstance(validated_config, pipe_model)
        except ValidationError as err:
            error_msg = next(iter(err.errors()))
            raise ValidationConfigError(
                f"Error during {pattern} {config.get('stack_extension', None)} config validation process: {error_msg}"
            ) from err
