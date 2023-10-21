"""dms_endpoint construct tests
"""
import logging
import os
import sys

import pytest
import yaml
from aws_cdk import App, Environment, Stack
from aws_cdk.assertions import Template

from app.guest360_constructs.ingestion.dms.dms_endpoint import Guest360DMSEndpoint, UnsupportedDMSEngineError

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {
    "prefix_global": "lst-pytest",
}

test_context = {
    "environment": "latest",
    "stack_name": "testStack",
    "prefix": "lst-TestStack-use1",
    "prefix_global": "lst-testStack",
}
stack_id = "TestStack"
dms_endpoint_id = "TestDMSEndpoint"
firehose_id = "TestDMSEndpoint"
bucket_id = "TestBucket"
directory = os.path.dirname(os.path.realpath(__file__))
AWS_DMS_PROPERTY = "AWS::DMS::Endpoint"


class TestDMSEndpoint:
    """Guest360 TestDMSEndpoint"""

    @pytest.mark.timeout(30, method="signal")
    @pytest.mark.parametrize("engine_name", ("mysql", "mariadb", "aurora"))
    def test_source_mysql_dms_endpoint(self, engine_name):
        test_app = App(context=test_context)
        test_stack = Stack(test_app, stack_id, env=Environment(account="123456789", region="us-east-1"))
        dms_endpoint_props = {
            "endpoint_type": "source",
            "engine_name": engine_name,
            "database_name": "TestInstance",
            "settings": {
                "events_poll_interval": 123,
                "server_timezone": "US/Pacific",
                "after_connect_script": "SHOW DATABASES",
                "clean_source_metadata_on_mismatch": False,
                "secrets_manager_access_role_arn": "arn:aws:secretsmanager:us-east-1:123456789:secret:TestSecret",  #'pragma: allowlist secret'
                "secrets_manager_secret_id": "TestSecretID",  #'pragma: allowlist secret'
            },
        }

        Guest360DMSEndpoint(test_stack, dms_endpoint_id, props=dms_endpoint_props)

        # render template.
        template = Template.from_stack(test_stack)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            AWS_DMS_PROPERTY,
            {
                "EndpointType": "source",
                "EngineName": engine_name,
                "MySqlSettings": {
                    "SecretsManagerAccessRoleArn": "arn:aws:secretsmanager:us-east-1:123456789:secret:TestSecret",  #'pragma: allowlist secret'
                    "SecretsManagerSecretId": "TestSecretID",  #'pragma: allowlist secret'
                },
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_target_mysql_dms_endpoint(self):
        test_app = App(context=test_context)
        test_stack = Stack(test_app, stack_id, env=Environment(account="123456789", region="us-east-1"))
        dms_endpoint_props = {
            "endpoint_type": "target",
            "engine_name": "mysql",
            "database_name": "TestInstance",
            "settings": {
                "max_file_size": 1024,
                "parallel_load_threads": 2,
                "target_db_type": "mysql",
                "clean_source_metadata_on_mismatch": False,
                "secrets_manager_access_role_arn": "arn:aws:secretsmanager:us-east-1:123456789:secret:TestSecret",  #'pragma: allowlist secret'
                "secrets_manager_secret_id": "TestSecretID",  #'pragma: allowlist secret'
            },
        }

        Guest360DMSEndpoint(test_stack, dms_endpoint_id, props=dms_endpoint_props)
        # render template.
        template = Template.from_stack(test_stack)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            AWS_DMS_PROPERTY,
            {
                "EndpointType": "target",
                "EngineName": "mysql",
                "MySqlSettings": {
                    "SecretsManagerAccessRoleArn": "arn:aws:secretsmanager:us-east-1:123456789:secret:TestSecret",  #'pragma: allowlist secret'
                    "SecretsManagerSecretId": "TestSecretID",  #'pragma: allowlist secret'
                },
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_source_oracle_dms_endpoint(self):
        test_app = App(context=test_context)
        test_stack = Stack(test_app, stack_id, env=Environment(account="123456789", region="us-east-1"))
        dms_endpoint_props = {
            "endpoint_type": "source",
            "engine_name": "oracle",
            "database_name": "TestInstance",
            "settings": {
                "access_alternate_directly": False,
                "additional_archived_log_dest_id": 123,
                "add_supplemental_logging": False,
                "allow_select_nested_tables": False,
                "archived_log_dest_id": 123,
                "archived_logs_only": False,
                "char_length_semantics": "charLengthSemantics",
                "direct_path_no_log": False,
                "direct_path_parallel_load": False,
                "enable_homogenous_tablespace": False,
                "extra_archived_log_dest_ids": [123],
                "fail_tasks_on_lob_truncation": False,
                "number_datatype_scale": 123,
                "oracle_path_prefix": "oraclePathPrefix",
                "parallel_asm_read_threads": 123,
                "read_ahead_blocks": 123,
                "read_table_space_name": False,
                "replace_path_prefix": False,
                "retry_interval": 123,
                "secrets_manager_access_role_arn": "arn:aws:secretsmanager:us-east-1:123456789:secret:TestSecret",  #'pragma: allowlist secret'
                "secrets_manager_oracle_asm_access_role_arn": "secretsManagerOracleAsmAccessRoleArn",  #'pragma: allowlist secret'
                "secrets_manager_oracle_asm_secret_id": "secretsManagerOracleAsmSecretId",
                "secrets_manager_secret_id": "TestSecretID",
                "security_db_encryption": "securityDbEncryption",
                "security_db_encryption_name": "securityDbEncryptionName",
                "spatial_data_option_to_geo_json_function_name": "spatialDataOptionToGeoJsonFunctionName",
                "standby_delay_time": 123,
                "use_alternate_folder_for_online": False,
                "use_b_file": False,
                "use_direct_path_full_load": False,
                "use_logminer_reader": False,
                "use_path_prefix": "usePathPrefix",
            },
        }

        Guest360DMSEndpoint(test_stack, dms_endpoint_id, props=dms_endpoint_props)
        # render template.
        template = Template.from_stack(test_stack)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            AWS_DMS_PROPERTY,
            {
                "EndpointType": "source",
                "EngineName": "oracle",
                "OracleSettings": {
                    "SecretsManagerAccessRoleArn": "arn:aws:secretsmanager:us-east-1:123456789:secret:TestSecret",  #'pragma: allowlist secret'
                    "SecretsManagerSecretId": "TestSecretID",  #'pragma: allowlist secret'
                },
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_target_oracle_dms_endpoint(self):
        test_app = App(context=test_context)
        test_stack = Stack(test_app, stack_id, env=Environment(account="123456789", region="us-east-1"))
        dms_endpoint_props = {
            "endpoint_type": "target",
            "engine_name": "oracle",
            "database_name": "TestInstance",
            "settings": {
                "access_alternate_directly": False,
                "additional_archived_log_dest_id": 123,
                "add_supplemental_logging": False,
                "allow_select_nested_tables": False,
                "archived_log_dest_id": 123,
                "archived_logs_only": False,
                "char_length_semantics": "charLengthSemantics",
                "direct_path_no_log": False,
                "direct_path_parallel_load": False,
                "enable_homogenous_tablespace": False,
                "extra_archived_log_dest_ids": [123],
                "fail_tasks_on_lob_truncation": False,
                "number_datatype_scale": 123,
                "oracle_path_prefix": "oraclePathPrefix",
                "parallel_asm_read_threads": 123,
                "read_ahead_blocks": 123,
                "read_table_space_name": False,
                "replace_path_prefix": False,
                "retry_interval": 123,
                "secrets_manager_access_role_arn": "arn:aws:secretsmanager:us-east-1:123456789:secret:TestSecret",  #'pragma: allowlist secret'
                "secrets_manager_oracle_asm_access_role_arn": "secretsManagerOracleAsmAccessRoleArn",  #'pragma: allowlist secret'
                "secrets_manager_oracle_asm_secret_id": "secretsManagerOracleAsmSecretId",
                "secrets_manager_secret_id": "TestSecretID",
                "security_db_encryption": "securityDbEncryption",
                "security_db_encryption_name": "securityDbEncryptionName",
                "spatial_data_option_to_geo_json_function_name": "spatialDataOptionToGeoJsonFunctionName",
                "standby_delay_time": 123,
                "use_alternate_folder_for_online": False,
                "use_b_file": False,
                "use_direct_path_full_load": False,
                "use_logminer_reader": False,
                "use_path_prefix": "usePathPrefix",
            },
        }

        Guest360DMSEndpoint(test_stack, dms_endpoint_id, props=dms_endpoint_props)
        # render template.
        template = Template.from_stack(test_stack)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            AWS_DMS_PROPERTY,
            {
                "EndpointType": "target",
                "EngineName": "oracle",
                "OracleSettings": {
                    "SecretsManagerAccessRoleArn": "arn:aws:secretsmanager:us-east-1:123456789:secret:TestSecret",  #'pragma: allowlist secret'
                    "SecretsManagerSecretId": "TestSecretID",  #'pragma: allowlist secret'
                },
            },
        )

    @pytest.mark.timeout(30, method="signal")
    def test_target_kinesis_dms_endpoint(self):
        test_app = App(context=test_context)
        test_stack = Stack(test_app, stack_id, env=Environment(account="123456789", region="us-east-1"))
        dms_endpoint_props = {
            "endpoint_type": "target",
            "engine_name": "kinesis",
            "database_name": "TestInstance",
            "settings": {
                "service_access_role_arn": "arn:aws:iam::123456789:role/kinesis-access-role",  #'pragma: allowlist secret'
                "stream_arn": "arn:aws:kinesis:us-east-1:123456789:secret:TestKinesis",
                "include_control_details": False,
                "include_null_and_empty": False,
                "include_partition_value": False,
                "include_table_alter_operations": False,
                "include_transaction_details": False,
                "message_format": "JSON",
                "no_hex_prefix": False,
                "partition_include_schema_table": False,
            },
        }

        Guest360DMSEndpoint(test_stack, dms_endpoint_id, props=dms_endpoint_props)

        # render template.
        template = Template.from_stack(test_stack)
        logger.debug(yaml.dump(template.to_json()))

        template.has_resource_properties(
            AWS_DMS_PROPERTY,
            {
                "EndpointType": "target",
                "EngineName": "kinesis",
                "KinesisSettings": {
                    "ServiceAccessRoleArn": "arn:aws:iam::123456789:role/kinesis-access-role",
                    "StreamArn": "arn:aws:kinesis:us-east-1:123456789:secret:TestKinesis",
                },
            },
        )

    def test_unsupported_dms_engine(self):
        test_app = App(context=test_context)
        test_stack = Stack(test_app, stack_id, env=Environment(account="123456789", region="us-east-1"))
        dms_endpoint_props = {"endpoint_type": "target", "engine_name": "some_unsupported_engine", "settings": {}}
        with pytest.raises(UnsupportedDMSEngineError):
            Guest360DMSEndpoint(test_stack, dms_endpoint_id, props=dms_endpoint_props)
