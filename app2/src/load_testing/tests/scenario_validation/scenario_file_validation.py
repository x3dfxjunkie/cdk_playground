"""
Validating System Test Scenario file
"""
from typing import List, Optional
from pydantic import BaseModel, ValidationError, Field
import yaml
import os
import pytest

NAME_REGEX = r"^[^\s]*$"  # Fixing Code smells
SCHEMA_DESCRIPTION = "The name of the schema."  # Fixing Code smells


class SystemTest(BaseModel):
    """Class SystemTest for System Test Model"""

    name: str = Field(
        ...,
        description="The name of the system test.",
        example="OrionEASystemTest",
        regex=NAME_REGEX,
    )
    description: Optional[str] = Field(
        None,
        description="The description of the system test.",
        example="OrionEA System test",
        max_length=100,
    )


class InputEndpoint(BaseModel):
    """Class InputEndpoint for Input"""

    type: str = Field(
        ...,
        description="The path to the schema of the data.",
        example="kinesis",
        regex="^(kinesis|s3|glue)$",
    )
    stream_name: Optional[str] = Field(
        None,
        description="The name of the Kinesis stream from which the data will be ingested.",
        example="dlr-lightning-lane-stream",
        regex=NAME_REGEX,
    )
    region: Optional[str] = Field(
        None,
        description="The AWS region where the resource is located.",
        example="us-east-1",
        regex="^(us-east-1|us-west-2)$",
    )


class Samples(BaseModel):
    """Class Samples for Class Data"""

    source: str = Field(
        ...,
        description="The source of the sample data",
        example="s3",
        regex="^(kinesis|s3|glue)$",
    )
    bucket_name: str = Field(
        ...,
        description="The name of the S3 bucket containing the sample data.",
        example="load-testing",
        regex=r"^(?![\.-])[a-z0-9\.-]{3,63}(?<![.-])$",
    )
    path: str = Field(
        ...,
        description="The path in the S3 bucket where the sample data is located.",
        example="orion_ea_normal/",
    )


class Data(BaseModel):
    """Class Data for Inputs"""

    schema_path: str = Field(
        ...,
        alias="schema",
        description="The path to the schema of the data.",
        example="path/to/dataclass/schema",
    )
    schema_name: str = Field(
        ...,
        description="NAME_REGEX",
        example="orion_ea",
        regex=NAME_REGEX,
    )
    active_injection: bool = Field(
        ...,
        description="The flag to activate injection. If false, injection won't take place.",
        example="false",
    )
    limit_records: int = Field(
        ...,
        description="The limit on the number of records for the test.",
        example="100",
        ge=0,
        le=65535,
    )
    duration_minutes: Optional[int] = Field(
        None,
        description="The time to wait",
        example="2",
        ge=0,
        le=60,
    )
    arrival_rate: Optional[int] = Field(
        None,
        description="Event arrival rate",
        example="2",
        ge=0,
        le=400,
    )
    samples: Optional[Samples]


class Input(BaseModel):
    """Input Class for Base model"""

    endpoint: InputEndpoint
    data: Data


class Dimensions(BaseModel):
    """Dimensions Class - Field for Metrics"""

    name: str = Field(
        ...,
        description="The name of the dimension",
        example="Source",
        regex="^[a-zA-Z-_]*$",
    )
    value: str = Field(
        ...,
        description="The value for the dimension.",
        example="Orion_EA",
        regex="^[a-zA-Z-_]*$",
    )


class Metrics(BaseModel):
    """Class Metrics Base Model"""

    namespace_name: str = Field(
        ...,
        description="NAME_REGEX",
        example="orion_ea",
        regex=NAME_REGEX,
    )
    cw_log_group_name: str = Field(
        ...,
        description="NAME_REGEX",
        example="orion_ea",
        regex=NAME_REGEX,
    )
    dimensions: List[Dimensions]


class Endpoint(BaseModel):
    """Class Endpoint - Parameters"""

    type: str = Field(
        ...,
        description="The source of the sample data",
        example="s3",
        regex="^(static|s3|kinesis|firehose|glue|snowflake|cloudwatch)$",
    )
    account: Optional[str] = Field(
        None,
        description="Provide details for the account",
        example="disneyparksandresorts.us-east-1.privatelink",
        regex=NAME_REGEX,
    )
    bucket_name: Optional[str] = Field(
        None,
        description="The name of the S3 bucket",
        example="ingestion-raw",
        regex=r"^(?![\.-])[a-z0-9\.-]{3,63}(?<![.-])$",
    )
    bucket_path: Optional[str] = Field(
        None,
        description="The path in the S3 bucket",
        example="snowpipe/database=LATEST_LANDING/",
    )
    database: Optional[str] = Field(
        None,
        description="The Database name",
        example="LATEST_LANDING",
    )
    prefix: Optional[str] = Field(
        None,
        description="The Prefix for the file in the S3",
        example="snowpipe/database=LATEST_LANDING",
    )
    role: Optional[str] = Field(
        None,
        description="The role user name",
        example="F_HELIX_EVAL_LATEST_LANDING_ROLE",
    )
    schema_path: Optional[str] = Field(
        None,
        alias="schema",
        description="The schema fot the DB",
        example="LND__EA",
    )
    snowflake_secret_name: Optional[str] = Field(
        None,
        description="The snowflake secret name",
        example="lst-use1-snowflake-cred-secret",
    )
    statistic: Optional[str] = Field(
        None,
        description="The statistic name",
        example="CountOfRecords",
    )
    table: Optional[str] = Field(
        None,
        description="The table name",
        example="DLR_LIGHTNING_LANE_LANDING",
    )
    trace_id_key_name: Optional[str] = Field(
        None,
        description="The trace ID key name",
        example="trace_id",
    )
    user: Optional[str] = Field(
        None,
        description="The user name",
        example="f-helix-eval-lst",
    )
    value: Optional[int] = Field(
        None,
        description="The value",
        example="100",
    )
    warehouse: Optional[str] = Field(
        None,
        description="The warehouse name",
        example="LANDING_LST_WH",
    )


class Destination(BaseModel):
    """Class Destination For Base model"""

    database: Optional[str] = Field(
        None,
        description="The name of the database where the test results will be stored",
        example="LATEST_LANDING",
        regex=NAME_REGEX,
    )
    schema_path: Optional[str] = Field(
        None,
        alias="schema",
        description="The name of the schema where the test results will be stored",
        example="LND__EA",
    )
    table: Optional[str] = Field(
        None,
        description="The name of the table where the test results will be stored",
        example="WDW_LIGHTNING_LANE",
        regex=NAME_REGEX,
    )


class Parameters(BaseModel):
    """Class Test For Output"""

    label: str = Field(
        ...,
        description="The name label of the parameter",
        example="RecordsPublished",
        regex=NAME_REGEX,
    )
    endpoint: Endpoint


class ConditionTest(BaseModel):
    """Class Test For Output"""

    name: Optional[str] = Field(
        None,
        description="The name of the condition",
        example="check_records_snowflake",
        regex=NAME_REGEX,
    )
    condition: Optional[str] = Field(
        None,
        description="The condition to evaluate",
        example="RecordsPublished == CountRecordByTraceSnowFlake",
    )


class Output(BaseModel):
    """Class Output for System Test Model"""

    destination: Optional[Destination]
    parameters: List[Parameters]
    tests: List[ConditionTest]


class SystemTestModel(BaseModel):
    """Class System Test Base Model"""

    system_test: SystemTest
    input: Input
    metrics: Metrics
    output: Output


def test_system_scenario_validation_files():
    directory = "app/src/load_testing/app/virtual_users/system_tests/latest/"
    for filename in os.listdir(directory):
        if filename.endswith(".yaml"):
            with open(os.path.join(directory, filename), encoding="utf-8") as f:
                data = yaml.safe_load(f)
                print(data)
                if data is None:
                    pytest.fail(f"Unable to parse {filename}: file may be empty or malformed")
                try:
                    SystemTestModel(**data)
                except ValidationError as e:
                    print(f"Validation error in {filename}: {e}")
                    pytest.fail(f"Validation error in {filename}: {e}")
