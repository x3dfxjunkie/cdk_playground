"""Guest360 DMS model"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class TargetSettings(BaseModel):
    include_control_details: bool = Field(
        ...,
        alias="include_control_details",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    include_null_and_empty: bool = Field(
        ...,
        alias="include_null_and_empty",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    include_partition_value: bool = Field(
        ...,
        alias="include_partition_value",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    include_table_alter_operations: bool = Field(
        ...,
        alias="include_table_alter_operations",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    include_transaction_details: bool = Field(
        ...,
        alias="include_transaction_details",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    message_format: str = Field(
        ...,
        alias="message_format",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    no_hex_prefix: bool = Field(
        ...,
        alias="no_hex_prefix",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    partition_include_schema_table: bool = Field(
        ...,
        alias="partition_include_schema_table",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class TargetEndpoint(BaseModel):
    endpoint_type: str = Field(
        ...,
        alias="endpoint_type",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    engine_name: str = Field(
        ...,
        alias="engine_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    settings: TargetSettings = Field(
        ...,
        alias="settings",
        name="",
        description="",
    )


class SubnetProps(BaseModel):
    group_name: str = Field(
        ...,
        alias="group_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    description: str = Field(
        ...,
        alias="description",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    subnet_identifer: str = Field(
        ...,
        alias="subnet_identifer",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    subnet_list: List[str] = Field(
        ...,
        alias="subnet_list",
        name="",
        description="",
    )


class ObjectLocator(BaseModel):
    schema_name: str = Field(
        ...,
        alias="schema-name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_name: str = Field(
        ...,
        alias="table-name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class Rule(BaseModel):
    rule_type: str = Field(
        ...,
        alias="rule-type",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rule_id: str = Field(
        ...,
        alias="rule-id",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rule_name: str = Field(
        ...,
        alias="rule-name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    rule_action: str = Field(
        ...,
        alias="rule-action",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    object_locator: ObjectLocator = Field(
        ...,
        alias="object-locator",
        name="",
        description="",
    )


class TableMappings(BaseModel):
    rules: List[Rule] = Field(
        ...,
        alias="rules",
        name="",
        description="",
    )


class DmsReplTaskItem(BaseModel):
    replication_task_identifier: str = Field(
        ...,
        regex=r"^[a-zA-Z][a-zA-Z0-9-]*$",
        alias="replication_task_identifier",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    source_endpoint_arn: str = Field(
        ...,
        alias="source_endpoint_arn",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    target_endpoint_arn: str = Field(
        ...,
        alias="target_endpoint_arn",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    replication_instance_arn: str = Field(
        ...,
        alias="replication_instance_arn",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    replication_task_settings: str = Field(
        ...,
        alias="replication_task_settings",
        name="",
        description="",
    )

    migration_type: str = Field(
        ...,
        alias="migration_type",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    table_mappings: TableMappings = Field(
        ...,
        alias="table_mappings",
        name="",
        description="",
    )


class SourceSettings(BaseModel):
    events_poll_interval: Optional[int] = Field(
        None,
        alias="events_poll_interval",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    clean_source_metadata_on_mismatch: Optional[bool] = Field(
        None,
        alias="clean_source_metadata_on_mismatch",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    secrets_manager_access_role_arn: str = Field(
        ...,
        alias="secrets_manager_access_role_arn",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    secrets_manager_secret_id: str = Field(
        ...,
        alias="secrets_manager_secret_id",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class SourceEndpoint(BaseModel):
    endpoint_type: str = Field(
        ...,
        alias="endpoint_type",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    settings: SourceSettings = Field(
        ...,
        alias="settings",
        name="",
        description="",
    )

    database_name: Optional[str] = Field(
        None,
        alias="database_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    engine_name: str = Field(
        ...,
        alias="engine_name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    ssl_mode: Optional[str] = Field(
        None,
        alias="ssl_mode",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )


class DmsReplInstance(BaseModel):
    name: str = Field(
        ...,
        alias="name",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    instance_class: str = Field(
        ...,
        alias="instance_class",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    storage: int = Field(
        ...,
        alias="storage",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    engine_version: str = Field(
        ...,
        alias="engine_version",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    auto_minor_version_upgrade: bool = Field(
        ...,
        alias="auto_minor_version_upgrade",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    allow_major_version_upgrade: bool = Field(
        ...,
        alias="allow_major_version_upgrade",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    multi_az: bool = Field(
        ...,
        alias="multi_az",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    maint_window: str = Field(
        ...,
        alias="maint_window",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    instance_identifier: str = Field(
        ...,
        alias="instance_identifier",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    security_group_ids: Optional[list[str]] = Field(
        None,
        alias="security_group_ids",
        name="",
        description="",
        guest_identifier=False,
        transaction_identifier=False,
        identifier_tag="",
    )

    subnet_props: SubnetProps = Field(
        ...,
        alias="subnet_props",
        name="",
        description="",
    )
