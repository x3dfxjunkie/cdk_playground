import json

# doesn't appear to be supported by localstack 2022-08-08
import aws_cdk.aws_rds as rds  # this requires localstack pro!
from typing import Union


class Guest360ConfigRDSValidation():
    """RDS Validation Module
    """

    def getRDSEngine(stack_config: dict)->  Union[rds.IInstanceEngine, rds.IClusterEngine, None]:
        """Based on the RDS engine type, it will return the IInstanceEngine or IClusterEngine based on the major and full version provided

        Args:
            stack_config (dict): based on the rds_engine_type, it will generate the DB Engine for the major and full version of the database.

        Returns:
            rds.IInstanceEngine | rds.IClusterEngine | None: IInstanceEngine or IClusterEngine (Aurora) or None if invalid
        """
        major_version = str(stack_config['rds']['rds_engine_major_version'])
        if stack_config['rds']['rds_engine_full_version']:
            full_version = str(stack_config['rds']['rds_engine_full_version'])
        else:
            full_version = None

        if stack_config['rds']['rds_engine_type'] == "mysql":
            return rds.DatabaseInstanceEngine.mysql(version=rds.MysqlEngineVersion.of(
                mysql_major_version=major_version,
                mysql_full_version=full_version
            ))
        elif stack_config['rds']['rds_engine_type'] == "mariadb":
            return rds.DatabaseInstanceEngine.maria_db(version=rds.MariaDbEngineVersion.of(
                maria_db_major_version=major_version,
                maria_db_full_version=full_version
            ))
        elif stack_config['rds']['rds_engine_type'] == "oracle":
            return rds.DatabaseInstanceEngine.oracle_ee(version=rds.OracleEngineVersion.of(
                oracle_major_version=major_version,
                oracle_full_version=full_version
            ))
        elif stack_config['rds']['rds_engine_type'] == "postgres":
            return rds.DatabaseInstanceEngine.postgres(version=rds.PostgresEngineVersion.of(
                postgres_major_version=major_version,
                postgres_full_version=full_version
            ))
        elif stack_config['rds']['rds_engine_type'] == "sql_server":
            return rds.DatabaseInstanceEngine.sql_server_se(version=rds.SqlServerEngineVersion.of(
                sql_server_major_version=major_version,
                sql_server_full_version=full_version
            ))
        elif stack_config['rds']['rds_engine_type'] == "aurora_mysql":
            return rds.DatabaseClusterEngine.aurora_mysql(version=rds.AuroraMysqlEngineVersion.of(
                aurora_mysql_major_version=major_version,
                aurora_mysql_full_version=full_version
            ))
        elif stack_config['rds']['rds_engine_type'] == "aurora_postgres":
            return rds.DatabaseClusterEngine.aurora_postgres(version=rds.AuroraPostgresEngineVersion.of(
                aurora_postgres_major_version=major_version,
                aurora_postgres_full_version=full_version
            ))

    def getRDSParameters(stack_config: dict) ->  Union[dict, None]:
        """Return JSON object with RDS Parameters defined

        Args:
            stack_config (dict): config item 'rds_parameters' defines the JSON format for additional RDS parameters to create

        Returns:
            dict | None: validates the JSON string and returns a JSON (dict) object or None if it fails or isn't available
        """
        if stack_config['rds']['rds_parameters']:
            return json.loads(stack_config['rds']['rds_parameters'])
        else:
            return None

    def getRDSStorage(stack_config:dict) ->  Union[str, None]:
        """Returns the amount of storage to create for the RDS instance. Validates the value is an integer and that it is > 0

        Args:
            stack_config (dict): pulls the value from the 'rds_allocated_storage' and validates this as the size of the database

        Returns:
            str | None: string of the database size to create or None if invalid
        """
        # Check if integer
        if isinstance(stack_config['rds']['rds_allocated_storage'], int) and stack_config['rds']['rds_allocated_storage'] > 0:
            return stack_config['rds']['rds_allocated_storage']
        else:
            return None

    def getRDSLicenseModel(stack_config:str) ->  Union[rds.LicenseModel, None]:
        """Returns the RDS Licensing Model

        Args:
            stack_config (str): Validates one of the optional licensing models "LICENSE_INCLUDED",  "BRING_YOUR_OWN_LICENSE", or "GENERAL_PUBLIC_LICENSE"

        Returns:
            rds.LicenseModel | None: returns the Literal value from rds.LicenseModel.X or None if an incorrect entry is provided
        """
        if stack_config['rds']['rds_license_model'] == "LICENSE_INCLUDED":
            return rds.LicenseModel.LICENSE_INCLUDED
        elif stack_config['rds']['rds_license_model'] == "BRING_YOUR_OWN_LICENSE":
            return rds.LicenseModel.BRING_YOUR_OWN_LICENSE
        elif stack_config['rds']['rds_license_model'] == "GENERAL_PUBLIC_LICENSE":
            return rds.LicenseModel.GENERAL_PUBLIC_LICENSE
        else:
            return None
