"""
Tests for dataclass_to_sql.py module
"""
import os
import re
import pytest
from pathlib import Path
from os import listdir
import boto3
from moto import mock_s3
from unittest.mock import mock_open, patch, MagicMock
from datetime import datetime

from app.src.data_service.marketplace.sql_generator.data_contract_to_sql import (
    contract_to_sql,
    generate_sql_files,
    generate_environment_sql_files,
    get_notification_integration,
    main,
    prepare_and_generate_files,
)
from app.src.data_service.marketplace.sql_generator.generator_config import (
    DataContractConfig,
    SnowflakeConfig,
    SnowflakeConfigLoader,
    CustomJSONEncoder,
    ContractTrackerFileHandler,
    ContractTrackerS3Handler,
)
from app.src.data_service.marketplace.sql_generator.helpers import (
    render_sql_template,
    to_snake_case,
    load_snowflake_config,
    write_sql_file,
    load_data_contracts_config,
    unblobbing_schema_name,
    raw_schema_name,
    create_folders_tree,
    load_schema_gen_conf,
)
from app.src.data_service.marketplace.sql_generator.table_field import (
    TableField,
    LANDING_TABLE_FIELDS,
)
from app.src.data_service.marketplace.sql_generator.table_parser import (
    TableParser,
)
from app.src.data_service.marketplace.sql_generator.table import Table, UnblobbedTable


@pytest.fixture(name="environment", scope="module")
def environment_fix():
    return {"name": "LATEST", "short_name": "LST"}


@pytest.fixture(name="recursive_depth", scope="module")
def recursive_depth_fix():
    return 3


@pytest.fixture(name="cli_variables", scope="module")
def cli_variables_fix():
    return {"s3_upload": True, "create_landing": True, "recursive_depth": 3}


@pytest.fixture(name="notification_integration_config", scope="module")
def notification_integration_config_fix(environment):
    return get_notification_integration(environment["name"].lower())


@pytest.fixture(name="data_contract_config", scope="module")
def data_contract_config_fix():
    return DataContractConfig(
        ingestion_config={
            "class_name": "DREAMSRoomsReservationsTcGrpModel",
            "data_contract": "app.src.data_structures.data_contracts.source.dreams.rooms_reservations.v0.dreams_rooms_reservations_tc_grp_source_data_contract",
            "data_contract_version": "v0.1",
            "router_database": "LATEST_LANDING",
            "router_schema": "LND_DREAMS_RESORT_RESERVATION",
            "router_table": "TC_GRP",
        }
    )


@pytest.fixture(name="ingestion_data_contracts_config", scope="module")
def ingestion_data_contracts_config_fix():
    return [
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_inventory_product_source_data_contract",
            "class_name": "CMEDLRInventoryProductModel",
            "data_contract_version": "0.0.1",
            "router_database": "LATEST_LANDING",
            "router_schema": "LND_CME_DLR",
            "router_table": "INVENTORY_PRODUCT",
        },
    ]


@pytest.fixture(name="table_parser_config", scope="module")
def parser_config_fix():
    return SnowflakeConfig(
        {
            "bronze_database": "DATAHUB",
            "bronze_schema_prefix": "BRZ",
            "managed_artifacts_database": "MA",
            "managed_artifacts_schema": "LND_GUEST360",
            "external_stage": "LANDING.WRK_GUEST360.EXT_GUEST360_STAGE_JSON",
            "recreate_if_exists": {
                "landing_table": True,
                "landing_table_pipe": True,
            },
            "environments": [
                {
                    "name": "LATEST",
                    "short_name": "LST",
                },
                {
                    "name": "STAGE",
                    "short_name": "STG",
                },
                {
                    "name": "LOAD",
                    "short_name": "LOD",
                },
                {
                    "name": "PROD",
                    "short_name": "PRD",
                },
            ],
            "timestamp_validation": {
                "self_validation": True,
                "function_definitions": {
                    "function_name": "CUSTOM_DATETIME_CASTER",
                    "database_name": "UTILITY_DB",
                    "schema_name": "UTILITY_SCHEMA",
                },
                "not_recognized_formats": [
                    "YYYY-MM-DDTHH24:MI:SS.FF TZHTZM",
                    'YYYY-MM-DD"T"HH24:MI:SS.FFTZH:TZM',
                    'YYYY-MM-DD"T"HH24:MI:SSTZH:TZM',
                ],
            },
        }
    )


@pytest.fixture(name="warehouse", scope="module")
def create_default_managed_artifact_warehouse(
    environment: dict[str, str],
    table_parser_config: SnowflakeConfig,
) -> str:
    return f'{table_parser_config.managed_artifacts_database}_{environment["short_name"]}_WH'


@pytest.fixture(name="snowflake_config_loader", scope="module")
def snowflake_config_loader_fix():
    return SnowflakeConfigLoader(
        {
            "type": "snowflake",
            "default_router_database": "default_router_database",
            "unblobbing_database": "DATAHUB",
            "unblobbing_schema_prefix": "BRZ",
            "managed_artifacts_database": "MA",
            "managed_artifacts_schema": "LND_GUEST360",
            "data_warehouse": None,
            "external_stage": "LANDING.WRK_GUEST360.EXT_GUEST360_STAGE_JSON",
            "environments": [
                {"name": "LATEST", "short_name": "LST"},
                {"name": "STAGE", "short_name": "STG"},
                {"name": "LOAD", "short_name": "LOD"},
                {"name": "PROD", "short_name": "PRD"},
            ],
            "data_contracts": [{"name": "CMEDLRDestinationModel"}, {"name": "CMEDLRInvBucketDateTimeModel"}],
        }
    )


@pytest.fixture(name="load_snowflake_config_fix", scope="module")
def load_snowflake_config_fix():
    return load_snowflake_config()


@pytest.fixture(name="module_name", scope="module")
def module_name_fix():
    return "app.src.data_structures.data_contracts.source.dreams.rooms_reservations.v0.dreams_rooms_reservations_tc_grp_source_data_contract"


@pytest.fixture(name="child_module_name", scope="module")
def child_module_name_fix():
    return "app.src.data_structures.data_contracts.source.ea_dlr.v0.ea_dlr_lightning_lane_source_data_contract"


@pytest.fixture(name="contract_tracker_directory", scope="module")
def contract_tracker_directory_fix():
    file_path = f"{os.path.dirname(__file__)}/../../contract_tracker"
    return os.path.dirname(file_path)


@pytest.fixture(name="table", scope="module")
def table_fix(
    module_name,
    data_contract_config,
    table_parser_config,
):
    class_name = "DREAMSRoomsReservationsTcGrpModel"
    parser = TableParser(
        data_contract_config=data_contract_config,
        table_parser_config=table_parser_config,
    )
    parser.parse_tables(
        module_name,
        class_name,
    )
    return parser.get_tables()[0]


# @pytest.fixture(name="child_table", scope="module")
# def child_table_fix(
#     child_module_name,
#     data_contract_config,
#     table_parser_config,
# ):
#     class_name = "EADLRLightningLaneModel"
#     parser = TableParser(
#         data_contract_config=data_contract_config,
#         table_parser_config=table_parser_config,
#     )
#     parser.parse_tables(
#         child_module_name,
#         class_name,
#     )
#     return parser.get_tables()[1]


@pytest.fixture(name="all_ddls", scope="module")
def all_ddls_fix(table_parser_config, environment):
    data_contract_config = DataContractConfig(
        ingestion_config={
            "class_name": "DREAMSRoomsReservationsTcGrpModel",
            "data_contract": "app.src.data_structures.data_contracts.source.dreams.rooms_reservations.v0.dreams_rooms_reservations_tc_grp_source_data_contract",
            "data_contract_version": "v0.1",
            "router_database": "LATEST_LANDING",
            "router_schema": "LND_DREAMS_RESORT_RESERVATION",
            "router_table": "TC_GRP",
        }
    )
    parser = TableParser(
        data_contract_config=data_contract_config,
        table_parser_config=table_parser_config,
    )
    # parser.parse_tables(module_name, class_name)
    all_ddls = contract_to_sql(
        table_parser_config=table_parser_config,
        data_contract_config=data_contract_config,
        environment=environment,
        parser=parser,
    )
    return all_ddls


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("name_Id_", "name_id_"),
        ("_name_Id", "name_id"),
        ("name-Id", "name_id"),
        ("nameId", "name_id"),
        ("ClassName", "class_name"),
        ("TTL_TIME", "ttl_time"),
        ("ttl_time", "ttl_time"),
        ("admissionEntitlement__tdssn_", "admission_entitlement__tdssn_"),
        ("rootTable__parentTable__childTable__fieldName", "root_table__parent_table__child_table__field_name"),
    ],
)
def test_to_snake_case(input_str, expected):
    assert to_snake_case(input_str) == expected


def test_create_folders_tree(tmp_path):
    create_folders_tree(tmp_path, "latest")
    assert os.path.exists(os.path.join(tmp_path, "latest"))


def test_write_sql_file(tmp_path):
    create_folders_tree(tmp_path, "latest")
    write_sql_file(file_name="test.txt", sql="SELECT 1 FROM DUAL", generated_sql_directory=tmp_path / "latest")
    assert os.path.exists(os.path.join(tmp_path, "latest", "test.txt"))


class TestTableField:
    """Tests for TableField"""

    def test_pad_name(self) -> None:
        expected = "object_type         "

        field = TableField(
            _name="object_type",
            title="object_type",
            _type="STRING",
            description="object type for lightning Lane Event based of Walt Disney World (Florida State)",
        )
        field.pad_name(20)
        assert field.padded_name == expected

    def test_pad_name_dot(self) -> None:
        expected = 'landing_data:data.experience.location_hierarchy.land."facility_id"'

        field = TableField(
            _name="experience__location_hierarchy__land__facility_id",
            title="experience__location_hierarchy__land__facility_id",
            _type="STRING",
            description="Id for facilities based of Walt Disney World (Florida State)",
        )
        field.pad_name_dot(20, is_landing=True)
        assert field.padded_name_dot == expected


class TestDataContractConfig:
    """Tests for DataContractConfigs"""

    def test_config_data_contract_init(self):
        expected = "table"
        config = {
            "class_name": "a_class_name",
            "data_contract": "a_data_contract",
            "data_contract_version": "0.0.1",
            "router_database": "database",
            "router_schema": "schema",
            "router_table": "table",
        }
        config = DataContractConfig(config)
        assert config.router_table == expected

    def test_get_notification_integration(self, notification_integration_config):
        assert notification_integration_config.get("notification_name", "NoKey") is not "NoKey"
        assert notification_integration_config.get("iam_user_arn", "NoKey") is not "NoKey"
        assert notification_integration_config.get("arn_secret_iam_external_id", "NoKey") is not "NoKey"


class TestGeneratorHelpers:
    def test_load_data_contracts_config(
        self,
        environment,
    ):
        data_contracts_config = load_data_contracts_config(
            environment_name=environment["name"],
        )
        assert len(data_contracts_config)

    def test_load_snowflake_config(
        self,
    ):
        snowflake_config = load_snowflake_config()
        assert snowflake_config.external_stage == "LANDING.WRK_GUEST360.EXT_GUEST360_STAGE_JSON"


class TestGenerateSQLFiles:
    def test_generate_environment_sql_files(
        self, environment, table_parser_config, ingestion_data_contracts_config, tmp_path, recursive_depth
    ):
        contract_tracker_directory = tmp_path / "contract_trackers"
        create_folders_tree(contract_tracker_directory)
        environment_path = tmp_path / "latest"
        generate_environment_sql_files(
            environment=environment,
            table_parser_config=table_parser_config,
            environment_path=environment_path,
            data_contracts_config=ingestion_data_contracts_config,
            contract_tracker_directory=contract_tracker_directory,
            unique_schemas=set(),
            s3_upload=False,
            recursive_depth=recursive_depth,
            create_landing=False,
        )
        assert os.path.exists(os.path.join(environment_path, "pipelines", "CMEDLRInventoryProductModel.sql"))

    def test_generate_sql_files(self, table_parser_config, tmp_path, recursive_depth):
        expected_folder_structure = {
            environment["name"].lower(): {"pipelines": {}, "schemas": {}, "functions": {}}
            for environment in table_parser_config.environments
        }
        expected_folder_structure["contract_tracker"] = {}
        environment_path = tmp_path / "latest"
        contract_tracker_directory = tmp_path / "contract_tracker"
        create_folders_tree(contract_tracker_directory)
        generate_sql_files(
            table_parser_config=table_parser_config,
            generated_sql_directory=tmp_path,
            contract_tracker_directory=contract_tracker_directory,
            s3_upload=False,
            recursive_depth=recursive_depth,
            create_landing=False,
        )

        folder_structure = self._get_folder_structure(tmp_path)

        # This will work only if the contract_tracker.yaml is empty or the version of the Data Contract is newer
        assert os.path.exists(os.path.join(environment_path, "pipelines", "CMEDLRInventoryProductModel.sql"))
        # asserts for schema file creation
        assert os.path.exists(os.path.join(environment_path, "schemas", "cme_dlr.sql"))
        # asserts folder structure
        assert expected_folder_structure == folder_structure

    def _get_folder_structure(self, root_folder):
        if not os.path.isdir(root_folder):
            return None
        return {
            name: self._get_folder_structure(os.path.join(root_folder, name))
            for name in os.listdir(root_folder)
            if os.path.isdir(os.path.join(root_folder, name))
        }


class TestRenderSQLTemplate:
    """Tests for contract_to_sql"""

    def test_raw_schema_name(
        self,
        data_contract_config,
    ):
        assert raw_schema_name(data_contract_config.router_schema) == "DREAMS_RESORT_RESERVATION"

    def test_name_delimiter(self, data_contract_config):
        with pytest.raises(ValueError) as exc:
            raw_schema_name("ValueWithoutUnderscore")
        assert str(exc.value) == f"The name delimiter _ was not found in the router_schema ValueWithoutUnderscore"

    def test_unblobbing_schema_name(self, data_contract_config):
        assert unblobbing_schema_name(data_contract_config.router_schema) == "BRZ_DREAMS_RESORT_RESERVATION"

    def test_create_landing_table_ddl(
        self,
        data_contract_config,
    ):
        landing_table_fields = [field for field in LANDING_TABLE_FIELDS if field["cloudevent"] == True]
        expected = """CREATE TABLE IF NOT EXISTS LATEST_LANDING.LND_DREAMS_RESORT_RESERVATION.TC_GRP(
    LANDING_ID                                  STRING,
    LANDING_DATA                                VARIANT,
    LANDING_FILE_NAME                           STRING,
    LANDING_FILE_ROW_NUMBER                     INT,
    LANDING_FILE_LAST_MODIFIED                  DATETIME,
    LANDING_TIMESTAMP                           DATETIME,
    LANDING_CLOUDEVENT_ID STRING,
    LANDING_CLOUDEVENT_SPECVERSION STRING,
    LANDING_CLOUDEVENT_TIME DATETIME,
    LANDING_CLOUDEVENT_SOURCE STRING,
    LANDING_CLOUDEVENT_SUBJECT STRING,
    LANDING_CLOUDEVENT_STREAM STRING,
    LANDING_CLOUDEVENT_TYPE STRING,
    LANDING_CLOUDEVENT_DATASCHEMA STRING,
    LANDING_CLOUDEVENT_TRACEPARENT STRING,
    LANDING_CLOUDEVENT_TRACESTATE STRING,
    LANDING_CLOUDEVENT_CHECK_SUM STRING,
    LANDING_CLOUDEVENT_ROUTER_DATABASE STRING,
    LANDING_CLOUDEVENT_ROUTER_SCHEMA STRING,
    LANDING_CLOUDEVENT_ROUTER_TABLE STRING,
    LANDING_CLOUDEVENT_VALIDATED BOOLEAN,
    LANDING_CLOUDEVENT_DATA_CONTRACT_VERSION STRING,
    LANDING_CLOUDEVENT_DATACONTENTTYPE STRING,
    LANDING_CLOUDEVENT_EXCEPTION_ERROR STRING

);"""

        ddl = render_sql_template(
            template_name="create_landing_table.sql",
            table={"name": data_contract_config.router_table},
            table_database=data_contract_config.router_database,
            cloud_event_fields=landing_table_fields,
            table_schema=data_contract_config.router_schema,
        )
        assert ddl == expected

    def test_create_pipe_ddl(
        self,
        table_parser_config,
        data_contract_config,
        environment,
    ):
        landing_table_fields = [field for field in LANDING_TABLE_FIELDS if field["cloudevent"] == True]
        expected = """CREATE OR REPLACE PIPE LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_PIPE
AUTO_INGEST = TRUE
AS COPY INTO LATEST_LANDING.LND_DREAMS_RESORT_RESERVATION.TC_GRP(
    LANDING_ID,
    LANDING_DATA,
    LANDING_FILE_NAME,
    LANDING_FILE_ROW_NUMBER,
    LANDING_FILE_LAST_MODIFIED,
    LANDING_TIMESTAMP,
    LANDING_CLOUDEVENT_ID, 
    LANDING_CLOUDEVENT_SPECVERSION, 
    LANDING_CLOUDEVENT_TIME, 
    LANDING_CLOUDEVENT_SOURCE, 
    LANDING_CLOUDEVENT_SUBJECT, 
    LANDING_CLOUDEVENT_STREAM, 
    LANDING_CLOUDEVENT_TYPE, 
    LANDING_CLOUDEVENT_DATASCHEMA, 
    LANDING_CLOUDEVENT_TRACEPARENT, 
    LANDING_CLOUDEVENT_TRACESTATE, 
    LANDING_CLOUDEVENT_CHECK_SUM, 
    LANDING_CLOUDEVENT_ROUTER_DATABASE, 
    LANDING_CLOUDEVENT_ROUTER_SCHEMA, 
    LANDING_CLOUDEVENT_ROUTER_TABLE, 
    LANDING_CLOUDEVENT_VALIDATED, 
    LANDING_CLOUDEVENT_DATA_CONTRACT_VERSION, 
    LANDING_CLOUDEVENT_DATACONTENTTYPE, 
    LANDING_CLOUDEVENT_EXCEPTION_ERROR
)
FROM(
SELECT
    LOWER(UUID_STRING('998bc5ba-a184-4144-8f97-d3b34526e37f', CONCAT(metadata$filename, ':', metadata$file_row_number))) AS LANDING_ID,
    $1                                                                 AS LANDING_DATA,
    metadata$filename                                                  AS LANDING_FILE_NAME,
    metadata$file_row_number                                           AS LANDING_FILE_ROW_NUMBER,
    metadata$file_last_modified                                        AS LANDING_FILE_LAST_MODIFIED,
    TO_TIMESTAMP_NTZ(CONVERT_TIMEZONE('UTC', CURRENT_TIMESTAMP()))     AS LANDING_TIMESTAMP,
    $1:id :: STRING AS LANDING_CLOUDEVENT_ID,
    $1:specversion :: STRING AS LANDING_CLOUDEVENT_SPECVERSION,
    $1:time :: DATETIME AS LANDING_CLOUDEVENT_TIME,
    $1:source :: STRING AS LANDING_CLOUDEVENT_SOURCE,
    $1:subject :: STRING AS LANDING_CLOUDEVENT_SUBJECT,
    $1:stream :: STRING AS LANDING_CLOUDEVENT_STREAM,
    $1:type :: STRING AS LANDING_CLOUDEVENT_TYPE,
    $1:dataschema :: STRING AS LANDING_CLOUDEVENT_DATASCHEMA,
    $1:traceparent :: STRING AS LANDING_CLOUDEVENT_TRACEPARENT,
    $1:tracestate :: STRING AS LANDING_CLOUDEVENT_TRACESTATE,
    $1:check_sum :: STRING AS LANDING_CLOUDEVENT_CHECK_SUM,
    $1:router_database :: STRING AS LANDING_CLOUDEVENT_ROUTER_DATABASE,
    $1:router_schema :: STRING AS LANDING_CLOUDEVENT_ROUTER_SCHEMA,
    $1:router_table :: STRING AS LANDING_CLOUDEVENT_ROUTER_TABLE,
    $1:validated :: BOOLEAN AS LANDING_CLOUDEVENT_VALIDATED,
    $1:data_contract_version :: STRING AS LANDING_CLOUDEVENT_DATA_CONTRACT_VERSION,
    $1:datacontenttype :: STRING AS LANDING_CLOUDEVENT_DATACONTENTTYPE,
    $1:exception_error :: STRING AS LANDING_CLOUDEVENT_EXCEPTION_ERROR
FROM @LATEST_LANDING.WRK_GUEST360.EXT_GUEST360_STAGE_JSON/database=LATEST_LANDING/schema=LND_DREAMS_RESORT_RESERVATION/table=TC_GRP/
)FILE_FORMAT = (TYPE = JSON);

ALTER PIPE LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_PIPE REFRESH;

--Helper query for pipe status:
-- SELECT SYSTEM$PIPE_STATUS('LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_PIPE');"""

        ddl = render_sql_template(
            template_name="create_landing_pipe.sql",
            table={"name": data_contract_config.router_table},
            landing_database=data_contract_config.router_database,
            landing_schema=data_contract_config.router_schema,
            pipe_database=table_parser_config.managed_artifacts_database,
            pipe_schema=table_parser_config.managed_artifacts_schema,
            environment=environment["name"],
            pipe_prefix=raw_schema_name(data_contract_config.router_schema),
            recreate_if_exists=True,
            cloud_event_fields=landing_table_fields,
            external_stage=table_parser_config.external_stage,
        )
        assert ddl == expected

    def test_create_table_ddl(
        self,
        table,
        table_parser_config,
        data_contract_config,
        environment,
    ):
        expected = """CREATE OR REPLACE TABLE LATEST_DATAHUB.BRZ_DREAMS_RESORT_RESERVATION.TC_GRP
    COPY GRANTS
    COMMENT="This table ties together the reservation/package components and it also ties to the reservation information"
(
    data                                       VARIANT,
    data_create_usr_id_cd                     STRING,
    data_create_dts                           DATETIME,
    data_updt_usr_id_cd                       STRING,
    data_updt_dts                             DATETIME,
    data_jdo_seq_nb                           INTEGER,
    data_tc_grp_nb                            INTEGER,
    data_tps_id                               INTEGER,
    data_comnctn_chan_id                      INTEGER,
    data_sls_chan_id                          INTEGER,
    data_tc_grp_typ_nm                        STRING,
    data_adv_internt_chkin_in                 STRING,
    data_add_on_tc_grp_nb                     INTEGER,
    data_prge_dts                             DATETIME,
    metadata                                   VARIANT,
    metadata_timestamp                        DATETIME,
    metadata_record_type                      STRING,
    metadata_operation                        STRING,
    metadata_partition_key_type               STRING,
    metadata_schema_name                      STRING,
    metadata_table_name                       STRING,
    metadata_transaction_id                   INTEGER,
    metadata_transaction_record_id            INTEGER,
    metadata_prev_transaction_id              INTEGER,
    metadata_prev_transaction_record_id       INTEGER,
    metadata_commit_timestamp                 DATETIME,
    metadata_stream_position                  STRING,
    landing_id                                 STRING,
    landing_file_name                          STRING,
    landing_file_row_number                    INTEGER,
    landing_file_last_modified                 DATETIME,
    landing_timestamp                          DATETIME,
    landing_cloudevent_id                      STRING,
    landing_cloudevent_specversion             STRING,
    landing_cloudevent_time                    DATETIME,
    landing_cloudevent_source                  STRING,
    landing_cloudevent_subject                 STRING,
    landing_cloudevent_stream                  STRING,
    landing_cloudevent_type                    STRING,
    landing_cloudevent_dataschema              STRING,
    landing_cloudevent_traceparent             STRING,
    landing_cloudevent_tracestate              STRING,
    landing_cloudevent_check_sum               STRING,
    landing_cloudevent_router_database         STRING,
    landing_cloudevent_router_schema           STRING,
    landing_cloudevent_router_table            STRING,
    landing_cloudevent_validated               BOOLEAN,
    landing_cloudevent_data_contract_version   STRING,
    landing_cloudevent_datacontenttype         STRING,
    landing_cloudevent_exception_error         STRING
    ,CONSTRAINT pk PRIMARY KEY (data_tc_grp_nb) NOT ENFORCED
    );"""

        ddl = render_sql_template(
            template_name="create_table.sql",
            table=table,
            table_database=table_parser_config.unblobbing_database,
            table_schema=unblobbing_schema_name(data_contract_config.router_schema),
            environment=environment["name"],
        )
        ddl = re.sub("_+", "_", ddl)
        assert ddl == expected

    def test_create_stream_ddl(
        self,
        table,
        table_parser_config,
        data_contract_config,
        environment,
    ):
        expected = """CREATE OR REPLACE STREAM LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_STREAM COPY GRANTS
ON TABLE LATEST_LANDING.LND_DREAMS_RESORT_RESERVATION.TC_GRP\nSHOW_INITIAL_ROWS = TRUE;"""
        ddl = render_sql_template(
            template_name="create_stream.sql",
            table=table,
            stream_database=table_parser_config.managed_artifacts_database,
            stream_schema=table_parser_config.managed_artifacts_schema,
            landing_database=data_contract_config.router_database,
            landing_schema=data_contract_config.router_schema,
            environment=environment["name"],
            stream_prefix=raw_schema_name(data_contract_config.router_schema),
        )
        assert ddl == expected

    def test_create_task_ddl(
        self,
        table,
        table_parser_config,
        warehouse,
        data_contract_config,
        environment,
        notification_integration_config,
    ):
        expected = """CREATE OR REPLACE TASK LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_TASK
    WAREHOUSE = 'MA_LST_WH'
    SCHEDULE = ''
    ERROR_INTEGRATION = GUEST360_LATEST_SNS_INTEGRATION
    WHEN SYSTEM$STREAM_HAS_DATA('LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_STREAM')  
    AS
MERGE INTO LATEST_DATAHUB.BRZ_DREAMS_RESORT_RESERVATION.TC_GRP AS T
    USING ( SELECT 
            ST.METADATA$ACTION AS METADATA$ACTION,
            ST.METADATA$ISUPDATE AS METADATA$ISUPDATE,
            ST.LANDING_DATA:data."data"::VARIANT AS DATA,
            ST.LANDING_DATA:data."data"."CREATE_USR_ID_CD"::STRING AS DATA__CREATE_USR_ID_CD,
            UTILITY_DB.UTILITY_SCHEMA.CUSTOM_DATETIME_CASTER( ST.LANDING_DATA:data."data"."CREATE_DTS"  ) AS DATA__CREATE_DTS,
            ST.LANDING_DATA:data."data"."UPDT_USR_ID_CD"::STRING AS DATA__UPDT_USR_ID_CD,
            UTILITY_DB.UTILITY_SCHEMA.CUSTOM_DATETIME_CASTER( ST.LANDING_DATA:data."data"."UPDT_DTS"  ) AS DATA__UPDT_DTS,
            ST.LANDING_DATA:data."data"."JDO_SEQ_NB"::INTEGER AS DATA__JDO_SEQ_NB,
            ST.LANDING_DATA:data."data"."TC_GRP_NB"::INTEGER AS DATA__TC_GRP_NB,
            ST.LANDING_DATA:data."data"."TPS_ID"::INTEGER AS DATA__TPS_ID,
            ST.LANDING_DATA:data."data"."COMNCTN_CHAN_ID"::INTEGER AS DATA__COMNCTN_CHAN_ID,
            ST.LANDING_DATA:data."data"."SLS_CHAN_ID"::INTEGER AS DATA__SLS_CHAN_ID,
            ST.LANDING_DATA:data."data"."TC_GRP_TYP_NM"::STRING AS DATA__TC_GRP_TYP_NM,
            ST.LANDING_DATA:data."data"."ADV_INTERNT_CHKIN_IN"::STRING AS DATA__ADV_INTERNT_CHKIN_IN,
            ST.LANDING_DATA:data."data"."ADD_ON_TC_GRP_NB"::INTEGER AS DATA__ADD_ON_TC_GRP_NB,
            UTILITY_DB.UTILITY_SCHEMA.CUSTOM_DATETIME_CASTER( ST.LANDING_DATA:data."data"."PRGE_DTS"  ) AS DATA__PRGE_DTS,
            ST.LANDING_DATA:data."metadata"::VARIANT AS METADATA,
            UTILITY_DB.UTILITY_SCHEMA.CUSTOM_DATETIME_CASTER( ST.LANDING_DATA:data."metadata"."timestamp"  ) AS METADATA__TIMESTAMP,
            ST.LANDING_DATA:data."metadata"."record-type"::STRING AS METADATA__RECORD_TYPE,
            ST.LANDING_DATA:data."metadata"."operation"::STRING AS METADATA__OPERATION,
            ST.LANDING_DATA:data."metadata"."partition-key-type"::STRING AS METADATA__PARTITION_KEY_TYPE,
            ST.LANDING_DATA:data."metadata"."schema-name"::STRING AS METADATA__SCHEMA_NAME,
            ST.LANDING_DATA:data."metadata"."table-name"::STRING AS METADATA__TABLE_NAME,
            ST.LANDING_DATA:data."metadata"."transaction-id"::INTEGER AS METADATA__TRANSACTION_ID,
            ST.LANDING_DATA:data."metadata"."transaction-record-id"::INTEGER AS METADATA__TRANSACTION_RECORD_ID,
            ST.LANDING_DATA:data."metadata"."prev-transaction-id"::INTEGER AS METADATA__PREV_TRANSACTION_ID,
            ST.LANDING_DATA:data."metadata"."prev-transaction-record-id"::INTEGER AS METADATA__PREV_TRANSACTION_RECORD_ID,
            UTILITY_DB.UTILITY_SCHEMA.CUSTOM_DATETIME_CASTER( ST.LANDING_DATA:data."metadata"."commit-timestamp"  ) AS METADATA__COMMIT_TIMESTAMP,
            ST.LANDING_DATA:data."metadata"."stream-position"::STRING AS METADATA__STREAM_POSITION,
            ST.landing_id AS LANDING_ID,
            ST.landing_file_name AS LANDING_FILE_NAME,
            ST.landing_file_row_number AS LANDING_FILE_ROW_NUMBER,
            ST.landing_file_last_modified AS LANDING_FILE_LAST_MODIFIED,
            ST.landing_timestamp AS LANDING_TIMESTAMP,
            ST.landing_cloudevent_id AS LANDING_CLOUDEVENT_ID,
            ST.landing_cloudevent_specversion AS LANDING_CLOUDEVENT_SPECVERSION,
            ST.landing_cloudevent_time AS LANDING_CLOUDEVENT_TIME,
            ST.landing_cloudevent_source AS LANDING_CLOUDEVENT_SOURCE,
            ST.landing_cloudevent_subject AS LANDING_CLOUDEVENT_SUBJECT,
            ST.landing_cloudevent_stream AS LANDING_CLOUDEVENT_STREAM,
            ST.landing_cloudevent_type AS LANDING_CLOUDEVENT_TYPE,
            ST.landing_cloudevent_dataschema AS LANDING_CLOUDEVENT_DATASCHEMA,
            ST.landing_cloudevent_traceparent AS LANDING_CLOUDEVENT_TRACEPARENT,
            ST.landing_cloudevent_tracestate AS LANDING_CLOUDEVENT_TRACESTATE,
            ST.landing_cloudevent_check_sum AS LANDING_CLOUDEVENT_CHECK_SUM,
            ST.landing_cloudevent_router_database AS LANDING_CLOUDEVENT_ROUTER_DATABASE,
            ST.landing_cloudevent_router_schema AS LANDING_CLOUDEVENT_ROUTER_SCHEMA,
            ST.landing_cloudevent_router_table AS LANDING_CLOUDEVENT_ROUTER_TABLE,
            ST.landing_cloudevent_validated AS LANDING_CLOUDEVENT_VALIDATED,
            ST.landing_cloudevent_data_contract_version AS LANDING_CLOUDEVENT_DATA_CONTRACT_VERSION,
            ST.landing_cloudevent_datacontenttype AS LANDING_CLOUDEVENT_DATACONTENTTYPE,
            ST.landing_cloudevent_exception_error AS LANDING_CLOUDEVENT_EXCEPTION_ERROR
            FROM LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_STREAM AS ST 
            WHERE ST.LANDING_CLOUDEVENT_VALIDATED = true )  AS S
    ON S.landing_id = T.landing_id
    WHEN MATCHED
        AND S.metadata$action = 'INSERT'
        AND S.metadata$isupdate
    THEN
        UPDATE SET
            T.data                                       = S.DATA,
            T.data__create_usr_id_cd                     = S.DATA__CREATE_USR_ID_CD,
            T.data__create_dts                           = S.DATA__CREATE_DTS,
            T.data__updt_usr_id_cd                       = S.DATA__UPDT_USR_ID_CD,
            T.data__updt_dts                             = S.DATA__UPDT_DTS,
            T.data__jdo_seq_nb                           = S.DATA__JDO_SEQ_NB,
            T.data__tc_grp_nb                            = S.DATA__TC_GRP_NB,
            T.data__tps_id                               = S.DATA__TPS_ID,
            T.data__comnctn_chan_id                      = S.DATA__COMNCTN_CHAN_ID,
            T.data__sls_chan_id                          = S.DATA__SLS_CHAN_ID,
            T.data__tc_grp_typ_nm                        = S.DATA__TC_GRP_TYP_NM,
            T.data__adv_internt_chkin_in                 = S.DATA__ADV_INTERNT_CHKIN_IN,
            T.data__add_on_tc_grp_nb                     = S.DATA__ADD_ON_TC_GRP_NB,
            T.data__prge_dts                             = S.DATA__PRGE_DTS,
            T.metadata                                   = S.METADATA,
            T.metadata__timestamp                        = S.METADATA__TIMESTAMP,
            T.metadata__record_type                      = S.METADATA__RECORD_TYPE,
            T.metadata__operation                        = S.METADATA__OPERATION,
            T.metadata__partition_key_type               = S.METADATA__PARTITION_KEY_TYPE,
            T.metadata__schema_name                      = S.METADATA__SCHEMA_NAME,
            T.metadata__table_name                       = S.METADATA__TABLE_NAME,
            T.metadata__transaction_id                   = S.METADATA__TRANSACTION_ID,
            T.metadata__transaction_record_id            = S.METADATA__TRANSACTION_RECORD_ID,
            T.metadata__prev_transaction_id              = S.METADATA__PREV_TRANSACTION_ID,
            T.metadata__prev_transaction_record_id       = S.METADATA__PREV_TRANSACTION_RECORD_ID,
            T.metadata__commit_timestamp                 = S.METADATA__COMMIT_TIMESTAMP,
            T.metadata__stream_position                  = S.METADATA__STREAM_POSITION,
            T.landing_id                                 = S.LANDING_ID,
            T.landing_file_name                          = S.LANDING_FILE_NAME,
            T.landing_file_row_number                    = S.LANDING_FILE_ROW_NUMBER,
            T.landing_file_last_modified                 = S.LANDING_FILE_LAST_MODIFIED,
            T.landing_timestamp                          = S.LANDING_TIMESTAMP,
            T.landing_cloudevent_id                      = S.LANDING_CLOUDEVENT_ID,
            T.landing_cloudevent_specversion             = S.LANDING_CLOUDEVENT_SPECVERSION,
            T.landing_cloudevent_time                    = S.LANDING_CLOUDEVENT_TIME,
            T.landing_cloudevent_source                  = S.LANDING_CLOUDEVENT_SOURCE,
            T.landing_cloudevent_subject                 = S.LANDING_CLOUDEVENT_SUBJECT,
            T.landing_cloudevent_stream                  = S.LANDING_CLOUDEVENT_STREAM,
            T.landing_cloudevent_type                    = S.LANDING_CLOUDEVENT_TYPE,
            T.landing_cloudevent_dataschema              = S.LANDING_CLOUDEVENT_DATASCHEMA,
            T.landing_cloudevent_traceparent             = S.LANDING_CLOUDEVENT_TRACEPARENT,
            T.landing_cloudevent_tracestate              = S.LANDING_CLOUDEVENT_TRACESTATE,
            T.landing_cloudevent_check_sum               = S.LANDING_CLOUDEVENT_CHECK_SUM,
            T.landing_cloudevent_router_database         = S.LANDING_CLOUDEVENT_ROUTER_DATABASE,
            T.landing_cloudevent_router_schema           = S.LANDING_CLOUDEVENT_ROUTER_SCHEMA,
            T.landing_cloudevent_router_table            = S.LANDING_CLOUDEVENT_ROUTER_TABLE,
            T.landing_cloudevent_validated               = S.LANDING_CLOUDEVENT_VALIDATED,
            T.landing_cloudevent_data_contract_version   = S.LANDING_CLOUDEVENT_DATA_CONTRACT_VERSION,
            T.landing_cloudevent_datacontenttype         = S.LANDING_CLOUDEVENT_DATACONTENTTYPE,
            T.landing_cloudevent_exception_error         = S.LANDING_CLOUDEVENT_EXCEPTION_ERROR"""
        ddl = render_sql_template(
            template_name="create_task.sql",
            table=table,
            stream_database=table_parser_config.managed_artifacts_database,
            stream_schema=table_parser_config.managed_artifacts_schema,
            stream_prefix=raw_schema_name(data_contract_config.router_schema),
            managed_artifacts_prefix=raw_schema_name(data_contract_config.router_schema),
            task_database=table_parser_config.managed_artifacts_database,
            task_schema=table_parser_config.managed_artifacts_schema,
            table_database=table_parser_config.unblobbing_database,
            table_schema=unblobbing_schema_name(data_contract_config.router_schema),
            warehouse=warehouse,
            environment=environment["name"],
            error_integration_name=notification_integration_config["notification_name"],
            timestamp_validation=table_parser_config.timestamp_validation,
        )
        assert expected in ddl

    #     def test_create_child_task_ddl(
    #         self,
    #         child_table,
    #         table_parser_config,
    #         warehouse,
    #         data_contract_config,
    #         environment,
    #         notification_integration_config,
    #     ):
    #         expected = """CREATE OR REPLACE TASK LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_ITEM_ENTITLEMENT_ACTIVITIES_TASK
    #     WAREHOUSE = 'MA_LST_WH'
    #     SCHEDULE = ''
    #     ERROR_INTEGRATION = GUEST360_LATEST_SNS_INTEGRATION
    #     WHEN SYSTEM$STREAM_HAS_DATA('LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_ITEM_ENTITLEMENT_ACTIVITIES_STREAM')
    #     AS
    # MERGE INTO LATEST_DATAHUB.BRZ_DREAMS_RESORT_RESERVATION.TC_GRP_ITEM_ENTITLEMENT_ACTIVITIES AS T
    #     USING (
    #         SELECT
    #         v.METADATA$ACTION AS METADATA$ACTION,
    #         v.METADATA$ISUPDATE AS METADATA$ISUPDATE,
    #         v.LANDING_CLOUDEVENT_VALIDATED as VALIDATED,"""
    #         ddl = render_sql_template(
    #             template_name="create_child_task.sql",
    #             table=child_table,
    #             stream_database=table_parser_config.managed_artifacts_database,
    #             stream_schema=table_parser_config.managed_artifacts_schema,
    #             stream_prefix=raw_schema_name(data_contract_config.router_schema),
    #             managed_artifacts_prefix=raw_schema_name(data_contract_config.router_schema),
    #             task_database=table_parser_config.managed_artifacts_database,
    #             task_schema=table_parser_config.managed_artifacts_schema,
    #             table_database=table_parser_config.unblobbing_database,
    #             table_schema=unblobbing_schema_name(data_contract_config.router_schema),
    #             warehouse=warehouse,
    #             environment=environment["name"],
    #             error_integration_name=notification_integration_config["notification_name"],
    #             timestamp_validation=table_parser_config.timestamp_validation,
    #         )
    #         ddl = re.sub("_+", "_", ddl)
    #         assert expected in ddl

    def test_create_child_table_ddl(
        self,
        table,
        table_parser_config,
        data_contract_config,
        environment,
    ):
        expected = """CREATE OR REPLACE TABLE LATEST_DATAHUB.BRZ_DREAMS_RESORT_RESERVATION.TC_GRP
(
    data                                       VARIANT,
    data_create_usr_id_cd                     STRING,
    data_create_dts                           DATETIME,
    data_updt_usr_id_cd                       STRING,
    data_updt_dts                             DATETIME,
    data_jdo_seq_nb                           INTEGER,
    data_tc_grp_nb                            INTEGER,
    data_tps_id                               INTEGER,
    data_comnctn_chan_id                      INTEGER,
    data_sls_chan_id                          INTEGER,
    data_tc_grp_typ_nm                        STRING,
    data_adv_internt_chkin_in                 STRING,
    data_add_on_tc_grp_nb                     INTEGER,
    data_prge_dts                             DATETIME,
    metadata                                   VARIANT,
    metadata_timestamp                        DATETIME,
    metadata_record_type                      STRING,
    metadata_operation                        STRING,
    metadata_partition_key_type               STRING,
    metadata_schema_name                      STRING,
    metadata_table_name                       STRING,
    metadata_transaction_id                   INTEGER,
    metadata_transaction_record_id            INTEGER,
    metadata_prev_transaction_id              INTEGER,
    metadata_prev_transaction_record_id       INTEGER,
    metadata_commit_timestamp                 DATETIME,
    metadata_stream_position                  STRING,
    landing_id                                 STRING,
    landing_file_name                          STRING,
    landing_file_row_number                    INTEGER,
    landing_file_last_modified                 DATETIME,
    landing_timestamp                          DATETIME,
    landing_cloudevent_id                      STRING,
    landing_cloudevent_specversion             STRING,
    landing_cloudevent_time                    DATETIME,
    landing_cloudevent_source                  STRING,
    landing_cloudevent_subject                 STRING,
    landing_cloudevent_stream                  STRING,
    landing_cloudevent_type                    STRING,
    landing_cloudevent_dataschema              STRING,
    landing_cloudevent_traceparent             STRING,
    landing_cloudevent_tracestate              STRING,
    landing_cloudevent_check_sum               STRING,
    landing_cloudevent_router_database         STRING,
    landing_cloudevent_router_schema           STRING,
    landing_cloudevent_router_table            STRING,
    landing_cloudevent_validated               BOOLEAN,
    landing_cloudevent_data_contract_version   STRING,
    landing_cloudevent_datacontenttype         STRING,
    landing_cloudevent_exception_error         STRING
);"""
        ddl = render_sql_template(
            template_name="create_child_table.sql",
            table=table,
            table_database=table_parser_config.unblobbing_database,
            table_schema=unblobbing_schema_name(data_contract_config.router_schema),
            environment=environment["name"],
        )
        ddl = re.sub("_+", "_", ddl)
        assert expected in ddl

    #     def test_create_child_stream_ddl(
    #         self,
    #         child_table,
    #         table_parser_config,
    #         data_contract_config,
    #         environment,
    #     ):
    #         expected = """CREATE OR REPLACE STREAM LATEST_MA.LND_GUEST360.DREAMS_RESORT_RESERVATION_TC_GRP_ITEM_ENTITLEMENT_ACTIVITIES_STREAM COPY GRANTS
    # ON TABLE LATEST_LANDING.LND_DREAMS_RESORT_RESERVATION.TC_GRP
    # SHOW_INITIAL_ROWS = TRUE;"""
    #         ddl = render_sql_template(
    #             template_name="create_child_stream.sql",
    #             table=child_table,
    #             stream_database=table_parser_config.managed_artifacts_database,
    #             stream_schema=table_parser_config.managed_artifacts_schema,
    #             stream_prefix=raw_schema_name(data_contract_config.router_schema),
    #             environment=environment["name"],
    #             landing_database=data_contract_config.router_database,
    #             landing_schema=data_contract_config.router_schema,
    #         )
    #         ddl = re.sub("_+", "_", ddl)
    #         assert expected in ddl

    def test_create_schema_ddl(self, data_contract_config):
        expected = """use warehouse GUEST360_WH;
use role GUEST360_L3;
use database LATEST_LANDING;

EXECUTE IMMEDIATE $$
DECLARE
    DB_NAME STRING;
    SCH_NAME STRING ;
    COMMENTS STRING;
    BU_UNIT STRING;
    BU_OWNER_EMAIL STRING;
    IA_UNIT STRING;
    IA_OWNER_EMAIL STRING;
    TYPE STRING ;
    ETL_USER_NAME STRING;
    ADD_ROLE_MASTER STRING;
    ENVIRONMENT STRING;
    SCHEMA_APPROVAL_IND STRING;
    BAPPID STRING;
    PROC_NAME STRING;

BEGIN
    DB_NAME :='LATEST_LANDING';
    SCH_NAME :='LND_DREAMS_RESORT_RESERVATION';
    COMMENTS  := 'Landing layer schema for DREAMS_RESORT_RESERVATION';
    BU_UNIT :='';
    BU_OWNER_EMAIL :='';
    IA_UNIT := 'DSNE PROJECTS';
    IA_OWNER_EMAIL := 'RENAN.PEREIRA@DISNEY.COM';
    TYPE := 'RW' ;
    ETL_USER_NAME :='';
    ADD_ROLE_MASTER := 'Y';
    ENVIRONMENT := 'latest';
    SCHEMA_APPROVAL_IND := 'Y';
    BAPPID := '';
    PROC_NAME := '';

    EXECUTE IMMEDIATE 'DESCRIBE SCHEMA  LND_DREAMS_RESORT_RESERVATION';
    RETURN 'SCHEMA ' || SCH_NAME || ' ALREADY EXISTS.';

EXCEPTION
    WHEN OTHER THEN
        EXECUTE IMMEDIATE 'CALL UTILITY_DB.UTILITY_SCHEMA.SP_CREATE_SCHEMA(
                            ''' || DB_NAME || ''',
                            ''' || SCH_NAME || ''',
                            ''' || BU_UNIT || ''',
                            ''' || BU_OWNER_EMAIL || ''',
                            ''' || IA_UNIT || ''',
                            ''' || IA_OWNER_EMAIL || ''',
                            ''' || COMMENTS || ''',
                            ''' || TYPE || ''',
                            ''' || ETL_USER_NAME || ''',
                            ''' || ADD_ROLE_MASTER || ''',
                            ''' || ENVIRONMENT || ''',
                            ''' || SCHEMA_APPROVAL_IND || ''',
                            ''' || BAPPID || ''',
                            ''' || PROC_NAME || ''')';
        RETURN 'SCHEMA ' || SCH_NAME || ' CREATED SUCCESFULLY.';
END$$;"""

        static_schema_info = vars(load_schema_gen_conf())
        ddl = render_sql_template(
            template_name="create_schema.sql",
            environment_name="latest",
            database_name=data_contract_config.router_database,
            schema_name=data_contract_config.router_schema,
            comments=f'Landing layer schema for {data_contract_config.router_schema.replace("LND_", "")}',
            **static_schema_info,
        )
        assert expected == ddl

    def test_timestamp_validation_function(self, table_parser_config):
        expected = """CREATE OR REPLACE FUNCTION UTILITY_DB.UTILITY_SCHEMA.CUSTOM_DATETIME_CASTER(input_string STRING)
RETURNS TIMESTAMP
LANGUAGE SQL
AS
$$
    CASE
       WHEN TRY_TO_TIMESTAMP(input_string, 'YYYY-MM-DDTHH24:MI:SS.FF TZHTZM') IS NOT NULL
        THEN TRY_TO_TIMESTAMP(input_string, 'YYYY-MM-DDTHH24:MI:SS.FF TZHTZM')
       WHEN TRY_TO_TIMESTAMP(input_string, 'YYYY-MM-DD"T"HH24:MI:SS.FFTZH:TZM') IS NOT NULL
        THEN TRY_TO_TIMESTAMP(input_string, 'YYYY-MM-DD"T"HH24:MI:SS.FFTZH:TZM')
       WHEN TRY_TO_TIMESTAMP(input_string, 'YYYY-MM-DD"T"HH24:MI:SSTZH:TZM') IS NOT NULL
        THEN TRY_TO_TIMESTAMP(input_string, 'YYYY-MM-DD"T"HH24:MI:SSTZH:TZM')
       ELSE input_string::DATETIME
    END
$$
;"""
        ddl = render_sql_template(
            template_name="validation_dts_function.sql",
            timestamp_validation=table_parser_config.timestamp_validation,
        )

        assert ddl == expected


class TestLandingTable:
    """Tests for LandingTable"""

    def test_name(self, table):
        expected = "tc_grp"
        assert table.name == expected


# class TestChildTable:
#     """Tests for ChildTable"""

#     def test_name(self, child_table):
#         expected = "tc_grp____item__entitlement__activities"
#         assert child_table.name == expected


class TestDataContractToSQL:
    """Tests for DataContractToSQL"""

    def test_contract_to_sql_create_task(self, all_ddls):
        assert "TASK" in all_ddls


class TestTableParser:
    """Tests for TableParser"""

    def test_dataclass_to_dict_no_module(self, module_name, table_parser_config, data_contract_config) -> None:
        class_name = "SomeContractWithoutAModule"

        with pytest.raises(AttributeError, match=r".*has no attribute.*"):
            TableParser(
                data_contract_config=data_contract_config,
                table_parser_config=table_parser_config,
            ).parse_tables(module_name, class_name)

    def test_table_all_tag_names(self):
        Table.all_tag_names
        assert hasattr(Table, "all_tag_names")

    @pytest.mark.parametrize(
        "key,expected",
        [
            ("title", "Travel Component Group"),
            (
                "description",
                "Payload class for DREAMSRoomsReservationTcGrpModel",
            ),
        ],
    )
    def test_dataclass_to_dict(self, key, expected, module_name, table_parser_config, data_contract_config) -> None:
        class_name = "DREAMSRoomsReservationsTcGrpModel"

        parser = TableParser(
            data_contract_config=data_contract_config,
            table_parser_config=table_parser_config,
        )
        parser.parse_tables(module_name, class_name)
        assert parser.parsed_schema[key] == expected

    def test_dataclass_to_dict_config(
        self,
        module_name,
        data_contract_config,
        table_parser_config,
    ) -> None:
        class_name = "DREAMSRoomsReservationsTcGrpModel"
        expected = "This table ties together the reservation/package components and it also ties to the reservation information"

        parser = TableParser(
            data_contract_config=data_contract_config,
            table_parser_config=table_parser_config,
        )
        parser.parse_tables(module_name, class_name)
        assert parser.landing_config["description"] == expected

    def test_parse_dataclass_fields(self, table) -> None:
        expected = TableField(
            _name="data__CREATE_DTS",
            title="Create Dts",
            _type="string",
            format="date-time",
            description="The month day century year hour minute and second when a row was created in this table.",
            example="2023-03-29T11:30:10.669000Z",
            guest_identifier=False,
            transaction_identifier=False,
            identifier_tag="",
            is_primary_key=False,
            nullable=True,
            _tags=[],
        )
        assert table.fields[2] == expected


class TestTable:
    @pytest.mark.parametrize(
        "initial_route_elements,route,expected_result",
        [
            ({}, [], {}),
            ({}, ["ele1"], {"ele1": {}}),
            ({}, ["ele1", "ele2"], {"ele1": {"ele2": {}}}),
            ({}, ["ele1", "ele2", "sub1", "sub2", "ele3"], {"ele1": {"ele2": {"sub1": {"sub2": {"ele3": {}}}}}}),
        ],
    )
    def test_insert_route(self, initial_route_elements, route, expected_result):
        UnblobbedTable("test").insert_route(initial_route_elements, route)

        assert initial_route_elements == expected_result

    @pytest.mark.parametrize(
        "route_elements,expected_result",
        [
            ({}, []),
            ({"ele1": {}}, ['LATERAL FLATTEN (input => ST.LANDING_DATA:data."ele1" , outer => true ) as ele1']),
            (
                {"ele1": {"ele1_1": {}}},
                [
                    'LATERAL FLATTEN (input => ST.LANDING_DATA:data."ele1" , outer => true ) as ele1',
                    'LATERAL FLATTEN (input => ele1.value:"ele1_1" , outer => true ) as ele1_ele1_1',
                ],
            ),
            (
                {"ele1": {"ele1_1__ele1_2": {}}},
                [
                    'LATERAL FLATTEN (input => ST.LANDING_DATA:data."ele1" , outer => true ) as ele1',
                    'LATERAL FLATTEN (input => ele1.value:"ele1_1"."ele1_2" , outer => true ) as ele1_ele1_1__ele1_2',
                ],
            ),
            (
                {"ele1": {"ele1_1-ele1_2": {}}},
                [
                    'LATERAL FLATTEN (input => ST.LANDING_DATA:data."ele1" , outer => true ) as ele1',
                    'LATERAL FLATTEN (input => ele1.value:"ele1_1-ele1_2" , outer => true ) as ele1_ele1_1_ele1_2',
                ],
            ),
        ],
    )
    def test_generate_flatten_str(self, route_elements, expected_result):
        compute_result = UnblobbedTable("test").generate_flatten_str(route_elements)
        assert compute_result == expected_result


@pytest.fixture(name="mock_s3_bucket", scope="module")
def mock_s3_bucket():
    with mock_s3():
        s3 = boto3.resource("s3", region_name="us-east-1")
        s3.create_bucket(Bucket="lst-use1-guest360-build-pipeline-bucket")
        yield s3


class TestContractTrackerS3Handler:
    def test_load_nonexistent_contract(self, mock_s3_bucket):
        tracker = ContractTrackerS3Handler(None, "LST")
        result = tracker.load_existing_contracts()
        assert result == {"contracts": []}

    def test_save_and_load_contract(self, mock_s3_bucket):
        tracker = ContractTrackerS3Handler(None, "LST")
        contracts = {"contracts": [{"name": "Contract1"}]}
        tracker.save_contracts(contracts)

        loaded_contracts = tracker.load_existing_contracts()
        assert loaded_contracts == contracts


class TestContractTrackerFileHandler:
    def test_init(self):
        handler = ContractTrackerFileHandler(Path("/base/directory"), "PROD")
        assert handler.file_path == Path("/base/directory/prod.yaml")

    @patch("builtins.open", new_callable=mock_open, read_data="contracts: []")
    def test_load_existing_contracts_file_exists(self, mock_file):
        handler = ContractTrackerFileHandler(Path("/base/directory"), "PROD")
        result = handler.load_existing_contracts()
        assert result == {"contracts": []}

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("os.path.exists", return_value=False)
    def test_load_existing_contracts_file_not_exists(self, mock_exists, mock_file):
        handler = ContractTrackerFileHandler(Path("/base/directory"), "PROD")
        result = handler.load_existing_contracts()
        assert result == {"contracts": []}

    @patch("builtins.open", new_callable=mock_open)
    @patch("yaml.dump")
    def test_save_contracts(self, mock_yaml_dump, mock_file):
        handler = ContractTrackerFileHandler(Path("/base/directory"), "PROD")
        contracts = {"contracts": ["contract1", "contract2"]}
        handler.save_contracts(contracts)
        mock_yaml_dump.assert_called_once_with(contracts, mock_file())


def test_custom_json_encoder_datetime():
    encoder = CustomJSONEncoder()
    now = datetime.now()
    result = encoder.default(now)
    assert result == now.isoformat()


def test_custom_json_encoder_set():
    encoder = CustomJSONEncoder()
    items = {1, 2, 3}
    result = encoder.default(items)
    assert result == [1, 2, 3]


def test_custom_json_encoder_default():
    encoder = CustomJSONEncoder()
    with pytest.raises(TypeError):
        encoder.default(object())


# Mock for the load_snowflake_config function
mocked_config = {"key": "value"}


# Mock for the generate_sql_files function
def mock_generate_sql_files(*args, **kwargs):
    pass


@pytest.mark.parametrize(
    "cli_args, expected_local, expected_create_landing",
    [
        (["--s3_upload"], True, False),
        (["--create_landing"], False, True),
        (["--s3_upload", "--create_landing"], True, True),
        ([], False, False),
    ],
)
def test_main(cli_args, expected_local, expected_create_landing, recursive_depth):
    with patch(
        "argparse.ArgumentParser.parse_args",
        return_value=MagicMock(
            s3_upload=expected_local, create_landing=expected_create_landing, recursive_depth=recursive_depth
        ),
    ):
        with patch(
            "app.src.data_service.marketplace.sql_generator.data_contract_to_sql.prepare_and_generate_files"
        ) as mock_prepare:
            main()
            mock_prepare.assert_called_once_with(
                s3_upload=expected_local, create_landing=expected_create_landing, recursive_depth=recursive_depth
            )


def test_prepare_and_generate_files(cli_variables):
    args = MagicMock(
        is_local=cli_variables["s3_upload"],
        create_landing=cli_variables["create_landing"],
        recursive_depth=cli_variables["recursive_depth"],
    )

    with patch("os.makedirs"):
        with patch("os.path.exists", return_value=True):
            with patch("shutil.rmtree"):
                with patch(
                    "app.src.data_service.marketplace.sql_generator.helpers.load_snowflake_config",
                    return_value=mocked_config,
                ):
                    with patch(
                        "app.src.data_service.marketplace.sql_generator.data_contract_to_sql.generate_sql_files",
                        side_effect=mock_generate_sql_files,
                    ):
                        prepare_and_generate_files(
                            s3_upload=args.s3_upload,
                            create_landing=args.create_landing,
                            recursive_depth=args.recursive_depth,
                        )
