""" Guest360 AppConfig model"""
from typing import Optional
from pydantic import BaseModel, Field


class Deployment(BaseModel):
    configuration_version: str = Field(
        ...,
        alias="configuration_version",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class HostedConfiguration(BaseModel):
    content: None = Field(
        ...,
        alias="content",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class AppConfig(BaseModel):
    deployment: Optional[Deployment] = Field(
        None,
        alias="deployment",
        name="",
        description="",
    )

    hosted_configuration: HostedConfiguration = Field(
        ...,
        alias="hosted_configuration",
        name="",
        description="",
    )
