"""DMS Endpoint Guest360 Construct"""
from enum import Enum
from typing import TypedDict

from aws_cdk import aws_dms
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360


class MysqlSettingsProps(TypedDict):
    """
    MySQL settings properties
    """

    secrets_manager_access_role_arn: str  # The full Amazon Resource Name (ARN) of the IAM role that grant access to get secret value and decrypt kms key. f you use the default encryption key created by AWS Secrets Manager, you do not have to specify the AWS KMS permissions for kms_key_arn.
    secrets_manager_secret_id: str  # The full ARN, partial ARN, or display name of the SecretsManagerSecret that contains the MySQL endpoint connection details

    events_poll_interval: NotRequired[
        int
    ]  # Source Attribute - Specifies how often to check the binary log for new changes/events when the database is idle.
    server_timezone: NotRequired[str]  # Source Attribute - Specifies the time zone for the source MySQL database
    after_connect_script: NotRequired[
        str
    ]  # Source Attribute - Specifies a script to run immediately after AWS DMS connects to the endpoint

    target_db_type: NotRequired[
        str
    ]  # Target Attribute - Specifies where to migrate source tables on the target, either to a single database or multiple databases
    parallel_load_threads: NotRequired[
        int
    ]  # Target Attribute - Improves performance when loading data into the MySQL-compatible target database
    max_file_size: NotRequired[
        int
    ]  # Target Attribute - Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database

    clean_source_metadata_on_mismatch: NotRequired[
        bool
    ]  # Cleans and recreates table metadata information on the replication instance when a mismatch occurs.


class OracleSettingsProps(TypedDict):
    """
    Oracle settings properties
    """

    secrets_manager_access_role_arn: str  # # The full Amazon Resource Name (ARN) of the IAM role that grant access to get secret value and decrypt kms key. f you use the default encryption key created by AWS Secrets Manager, you do not have to specify the AWS KMS permissions for kms_key_arn.
    secrets_manager_secret_id: str  # The full ARN, partial ARN, or display name of the SecretsManagerSecret that contains the Oracle endpoint connection details.

    access_alternate_directly: NotRequired[
        bool
    ]  # Set this attribute to false in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.
    additional_archived_log_dest_id: NotRequired[
        int
    ]  # Set this attribute with ArchivedLogDestId in a primary/ standby setupp. This attribute is useful in the case of a switchover. In this case, AWS DMS needs to know which destination to get archive redo logs from to read changes.
    add_supplemental_logging: NotRequired[
        bool
    ]  # Set this attribute to set up table-level supplemental logging for the Oracle database
    allow_select_nested_tables: NotRequired[
        bool
    ]  # Set this attribute to true to enable replication of Oracle tables containing columns that are nested tables or defined types.
    archived_log_dest_id: NotRequired[
        int
    ]  # Specifies the ID of the destination for the archived redo logs. This value should be the same as a number in the dest_id column of the v$archived_log view
    archived_logs_only: NotRequired[bool]  # When this field is set to Y , AWS DMS only accesses the archived redo logs
    char_length_semantics: NotRequired[
        str
    ]  # Specifies whether the length of a character column is in bytes or in characters
    direct_path_no_log: NotRequired[
        bool
    ]  # When set to true, this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs
    direct_path_parallel_load: NotRequired[
        bool
    ]  # When set to true , this attribute specifies a parallel load when useDirectPathFullLoad is set to Y
    enable_homogenous_tablespace: NotRequired[
        bool
    ]  # Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target
    extra_archived_log_dest_ids: NotRequired[
        list[int]
    ]  # Specifies the IDs of one more destinations for one or more archived redo logs.
    fail_tasks_on_lob_truncation: NotRequired[
        bool
    ]  # When set to true, this attribute causes a task to fail if the actual size of an LOB column is greater than the specified LobMaxSize
    number_datatype_scale: NotRequired[int]  # Specifies the number scale. You can select a scale up to 38
    oracle_path_prefix: NotRequired[
        str
    ]  # Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source
    parallel_asm_read_threads: NotRequired[
        int
    ]  # Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM).
    read_ahead_blocks: NotRequired[
        int
    ]  #  Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM)
    read_table_space_name: NotRequired[bool]  # When set to true, this attribute supports tablespace replication.
    replace_path_prefix: NotRequired[
        bool
    ]  # Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source
    retry_interval: NotRequired[int]  # Specifies the number of seconds that the system waits before resending a query
    secrets_manager_oracle_asm_access_role_arn: NotRequired[
        str
    ]  # Required only if your Oracle endpoint uses Advanced Storage Manager (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret
    secrets_manager_oracle_asm_secret_id: NotRequired[
        str
    ]  # Required only if your Oracle endpoint uses Advanced Storage Manager (ASM)
    security_db_encryption: NotRequired[
        str
    ]  # For an Oracle source endpoint, the transparent data encryption (TDE) password required by AWM DMS to access Oracle redo logs encrypted by TDE using Binary Reader
    security_db_encryption_name: NotRequired[
        str
    ]  # For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE
    spatial_data_option_to_geo_json_function_name: NotRequired[
        str
    ]  # Use this attribute to convert SDO_GEOMETRY to GEOJSON format
    standby_delay_time: NotRequired[
        int
    ]  # Use this attribute to specify a time in minutes for the delay in standby sync
    use_alternate_folder_for_online: NotRequired[
        bool
    ]  # Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source
    use_b_file: NotRequired[
        bool
    ]  # Set this attribute to Y to capture change data using the Binary Reader utility. Set UseLogminerReader to N to set this attribute to Y.
    use_direct_path_full_load: NotRequired[
        bool
    ]  # Set this attribute to Y to have AWS DMS use a direct path full load. Specify this value to use the direct path protocol in the Oracle Call Interface (OCI)
    use_logminer_reader: NotRequired[
        bool
    ]  # Set this attribute to Y to capture change data using the Oracle LogMiner utility (the default)
    use_path_prefix: NotRequired[
        str
    ]  # Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source


class KinesisSettingsProps(TypedDict):
    """
    Kinesis settings properties
    """

    service_access_role_arn: str  # The Amazon Resource Name (ARN) for the IAM role that AWS DMS uses to write to the Kinesis data stream
    stream_arn: str  # The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint
    include_control_details: NotRequired[
        bool
    ]  # Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output
    include_null_and_empty: NotRequired[bool]  # Include NULL and empty columns for records migrated to the endpoint
    include_partition_value: NotRequired[
        bool
    ]  # hows the partition value within the Kinesis message output, unless the partition type is schema-table-type
    include_table_alter_operations: NotRequired[
        bool
    ]  # Includes any data definition language (DDL) operations that change the table in the control data, such as rename-table , drop-table , add-column , drop-column , and rename-column
    include_transaction_details: NotRequired[
        bool
    ]  # Provides detailed transaction information from the source database.
    message_format: str  # The output format for the records created on the endpoint. The message format is JSON (default) or JSON_UNFORMATTED (a single line with no tab)
    no_hex_prefix: NotRequired[
        bool
    ]  # Set this optional parameter to true to avoid adding a ‘0x’ prefix to raw data in hexadecimal format
    partition_include_schema_table: NotRequired[
        bool
    ]  # Prefixes schema and table names to partition values, when the partition type is primary-key-type . Doing this increases data distribution among Kinesis shards.


@match_class_typing
class DMSEndpointProps(TypedDict):
    """
    DMS Endpoint properties
    """

    endpoint_type: str  # Endpoint type, allowed values source or target
    engine_name: str  # The type of engine for the endpoint, depending on the EndpointType value. Valid values : mysql | oracle | mariadb | kinesis
    settings: dict  #  Props for Oracle, Kinesis and MySQL - these should be OracleSettingsProps, KinesisSettingsProps, MysqlSettingsProps, just FYI.
    database_name: NotRequired[str]  # DB instance name


class DMSEngineType(str, Enum):
    ORACLE: str = "oracle"
    MYSQL: str = "mysql"
    MARIADB: str = "mariadb"
    KINESIS: str = "kinesis"
    AURORA: str = "aurora"


class UnsupportedDMSEngineError(Exception):
    pass


class Guest360DMSEndpoint(Construct360):
    """
    Class definition Guest360's base construct for DMS Endpoint
    """

    def __init__(self, scope: Construct360, construct_id: str, props: DMSEndpointProps, **kwargs) -> None:
        """Construct to create database migration services endpoint resources
        Args:
            scope (Construct360)
            construct_id (str): Construct ID
            props (dict) : Configuration for DMS Endpoint - See DMSEndpointProps
            **kwargs: Description
        """
        super().__init__(scope, construct_id, **kwargs)

        # Check dms endpoint props
        DMSEndpointProps(props)

        prefix = self.node.try_get_context("prefix")
        self.naming_prefix = f"{prefix}-{construct_id}"
        endpoint_props: dict = props

        if props["engine_name"] in [DMSEngineType.MYSQL, DMSEngineType.MARIADB, DMSEngineType.AURORA]:
            # Check MySQL props
            MysqlSettingsProps(props["settings"])

            # Define MySQL settings property
            my_sql_settings = aws_dms.CfnEndpoint.MySqlSettingsProperty(**props["settings"])
            endpoint_props["my_sql_settings"] = my_sql_settings

        elif props["engine_name"] == DMSEngineType.ORACLE:
            # Check oracle props
            OracleSettingsProps(props["settings"])

            # Define Oracle settings property
            oracle_settings = aws_dms.CfnEndpoint.OracleSettingsProperty(**props["settings"])
            endpoint_props["oracle_settings"] = oracle_settings

        elif props["engine_name"] == DMSEngineType.KINESIS:
            # Check kinesis props
            KinesisSettingsProps(props["settings"])

            # Define kinesis settings property
            kinesis_settings = aws_dms.CfnEndpoint.KinesisSettingsProperty(**props["settings"])
            endpoint_props["kinesis_settings"] = kinesis_settings
        else:
            raise UnsupportedDMSEngineError(
                f'Unsupported DMS Engine: {props["engine_name"]}. Supported engine types: {[e.value for e in DMSEngineType]}'
            )

        # Clear settings key argument
        endpoint_props.pop("settings")

        self.dms_endpoint = aws_dms.CfnEndpoint(
            self,
            self.naming_prefix,
            **endpoint_props,
        )
