""" Pipelines config pattern instance model"""
from typing import Union
from pydantic import BaseModel, Field
from app.infrastructure.ingestion.config.tests.models.data_pipe_model import DataPipe


class PatternInstanceBaseModel(BaseModel):
    region: str = Field(
        ...,
        regex="^us-east-1$",
        alias="region",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    data_pipe: DataPipe = Field(
        ...,
        alias="data_pipe",
        name="",
        description="",
    )
