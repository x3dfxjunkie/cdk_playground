""" Pipelines config data pipe model"""
from typing import Optional, List, ClassVar
from pydantic import BaseModel, Field, validator


class Error(BaseModel):
    namespace: str = Field(
        ...,
        alias="namespace",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value: int = Field(
        ...,
        alias="value",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    unit: str = Field(
        ...,
        alias="unit",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Metrics(BaseModel):
    error: Error = Field(
        ...,
        alias="error",
        name="",
        description="",
    )


class KeyPathItem(BaseModel):
    name: Optional[str] = Field(
        None,
        alias="name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    value: Optional[str] = Field(
        None,
        alias="value",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DataContract(BaseModel):
    data_contract: str = Field(
        ...,
        alias="data_contract",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    class_name: str = Field(
        ...,
        alias="class_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    data_contract_version: str = Field(
        ...,
        alias="data_contract_version",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    key_path: Optional[List[KeyPathItem]] = Field(
        None,
        alias="key_path",
        name="",
        description="",
    )

    router_database: str = Field(
        ...,
        alias="router_database",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    router_schema: str = Field(
        ...,
        alias="router_schema",
        regex=r"^(LND_.+)$",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    router_table: str = Field(
        ...,
        alias="router_table",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DataPipe(BaseModel):
    default_router_database: str = Field(
        ...,
        alias="default_router_database",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    default_table: str = Field(
        ...,
        regex=r"^DEFAULT_ROUTER_TABLE$",
        alias="default_table",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    default_schema: str = Field(
        ...,
        regex=r"^(LND_.*|DEFAULT_ROUTER_SCHEMA)$",
        alias="default_schema",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_path: Optional[str] = Field(
        None,
        alias="table_path",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    schema_path: Optional[str] = Field(
        None,
        alias="schema_path",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    key_to_load: Optional[str] = Field(
        None,
        alias="key_to_load",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    metrics: Metrics = Field(
        ...,
        alias="metrics",
        name="",
        description="",
    )

    data_contracts: Optional[List[DataContract]] = Field(
        None,
        alias="data_contracts",
        name="",
        description="",
    )

    # TODO: eventually this is should be required
    data_mapper_type: Optional[str] = Field(
        None,
        alias="data_mapper_type",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ROUTER_DATABASE_DEFAULTS: ClassVar = [
        "DEFAULT_ROUTER_DATABASE_LANDING",
        "DEFAULT_ROUTER_LATEST_LANDING",
        "DEFAULT_ROUTER_STAGE_LANDING",
        "DEFAULT_ROUTER_LOAD_LANDING",
        "DEFAULT_ROUTER_PROD_LANDING",
    ]

    @validator("default_router_database")
    def validate_default_router_database(cls, value):  # pylint: disable=E0213
        try:
            assert value in cls.ROUTER_DATABASE_DEFAULTS
        except AssertionError as err:
            raise ValueError(f"Incorrect default_router_database value: {value}") from err
