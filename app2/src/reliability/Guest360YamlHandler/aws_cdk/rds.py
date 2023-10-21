"""Engine: create a IInstanceEngine from engine_name and version. """
import aws_cdk
from aws_cdk import aws_rds as RDS
from aws_cdk.aws_rds import DatabaseInstanceEngine as DBI

MAP_ENGINE: dict[str, aws_cdk.aws_rds.IInstanceEngine] = {
    "MARIADB": DBI.MARIADB,
    "MYSQL": DBI.MYSQL,
    "ORACLE_EE": DBI.ORACLE_EE,
    "ORACLE_EE_CDB": DBI.ORACLE_EE_CDB,
    "ORACLE_SE2": DBI.ORACLE_SE2,
    "ORACLE_SE2_CDB": DBI.ORACLE_SE2_CDB,
    "POSTGRES": DBI.POSTGRES,
    "SQL_SERVER_EE": DBI.SQL_SERVER_EE,
    "SQL_SERVER_EX": DBI.SQL_SERVER_EX,
    "SQL_SERVER_SE": DBI.SQL_SERVER_SE,
    "SQL_SERVER_WEB": DBI.SQL_SERVER_SE,
}


def instance_engine(engine_name: str, version=None) -> RDS.IInstanceEngine:
    """Engine: create a IInstanceEngine from engine_name and version.

    Args:
        engine_name (str): Engine name (mariadb,postgresql,oracle,mysql,sqlserver)
        version (str - Optional): version of engine

    Returns:
        aws_cdk.aws_rds.IInstanceEngine:
    """
    engine = None
    if version is None:
        engine = MAP_ENGINE.get(engine_name)
    else:
        engine = map_engine_with_version(engine_name, version)

    if engine is None:
        raise ValueError("Engine name or version is not valid")
    return engine


def map_engine_with_version(engine_name, version):
    """
    Return Engine using name and version

    Args:
        engine_name (_type_): engine name
        version (_type_): engine version

    Raises:
        ValueError: Engine name is not valid

    Returns:
        IEngine: Engine
    """
    match engine_name:
        case "MARIADB":
            return DBI.maria_db(version=RDS.MariaDbEngineVersion.of(version, version))
        case "MYSQL":
            return DBI.mysql(version=RDS.MysqlEngineVersion.of(version, version))
        case "ORACLE_EE":
            return DBI.oracle_ee(version=RDS.OracleEngineVersion.of(version, version))
        case "ORACLE_EE_CDB":
            return DBI.oracle_ee_cdb(version=RDS.OracleEngineVersion.of(version, version))
        case "ORACLE_SE2":
            return DBI.oracle_se2(version=RDS.OracleEngineVersion.of(version, version))
        case "ORACLE_SE2_CDB":
            return DBI.oracle_se2_cdb(version=RDS.OracleEngineVersion.of(version, version))
        case "POSTGRES":
            return DBI.postgres(version=RDS.PostgresEngineVersion.of(version, version))
        case "SQL_SERVER_EE":
            return DBI.sql_server_ee(version=RDS.SqlServerEngineVersion.of(version, version))
        case "SQL_SERVER_EX":
            return DBI.sql_server_ex(version=RDS.SqlServerEngineVersion.of(version, version))
        case "SQL_SERVER_SE":
            return DBI.sql_server_se(version=RDS.SqlServerEngineVersion.of(version, version))
        case "SQL_SERVER_WEB":
            return DBI.sql_server_web(version=RDS.SqlServerEngineVersion.of(version, version))
        case _:
            raise ValueError("Engine name is not valid")
