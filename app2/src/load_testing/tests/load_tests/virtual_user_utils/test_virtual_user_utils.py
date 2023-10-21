import pytest
from unittest.mock import patch
from mock import patch, mock_open
from app.src.load_testing.app.virtual_users.virtual_user_utils.utils import VirtualUserUtils

DB_NAME = "db_load_testing"
ENGINE = "mariadb"
PORT = 3306
DB_INSTANCE_IDENTIFIER = "lst-use1-g360-ingest-c-loadtestingrdse6b4aguest-udyjzyxpirhe"
HOST = "lst-use1-g360-ingest-loadtesting.us-east-1.rds.amazonaws.com"
BUILTINS_OPEN = "builtins.open"


class AWSError(Exception):
    pass


class MockClient:
    @staticmethod
    def _get_secure_string():
        return "simulated_generated_secret"

    @staticmethod
    def _get_user():
        return "simulated_user"

    def get_secret_value(self, SecretId):  # NOSONAR Check AWS syntax
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/get_secret_value.html
        if SecretId == "valid-secret":  # pragma: allowlist secret
            return {
                "SecretString": f'{{"password": "{self._get_secure_string()}",'
                f'"dbname": "{DB_NAME}",'
                f'"engine": "{ENGINE}", '
                f'"port": {PORT}, '
                f'"dbInstanceIdentifier": "{DB_INSTANCE_IDENTIFIER}",'
                f'"host": "{HOST}",'
                f'"username": "{self._get_user()}"}}'
            }

        elif SecretId == "no-secretstring":  # pragma: allowlist secret
            return {"NotSecureString": "irrelevant_data"}

        else:
            raise AWSError("Some AWS exception")

    def get_parameter(self, Name):  # NOSONAR Check AWS syntax
        if Name == "valid_parameter":
            return {"Parameter": {"Value": "valid_value"}}

        elif Name == "invalid_parameter":
            return None


@patch("boto3.client", return_value=MockClient())
def test_get_secret_valid(boto_client):
    result = VirtualUserUtils.get_secret("valid-secret")
    expected_output = {
        "password": MockClient._get_secure_string(),
        "dbname": DB_NAME,
        "engine": ENGINE,
        "port": PORT,
        "dbInstanceIdentifier": DB_INSTANCE_IDENTIFIER,
        "host": HOST,
        "username": MockClient._get_user(),
    }
    assert result == expected_output


@patch("boto3.client", return_value=MockClient())
def test_get_secret_no_secretstring(boto_client):
    with pytest.raises(ValueError, match="The secret does not have a SecretString field."):
        VirtualUserUtils.get_secret("no-secretstring")


@patch("boto3.client", return_value=MockClient())
def test_get_secret_exception(boto_client, capsys):
    result = VirtualUserUtils.get_secret("invalid-secret")
    captured = capsys.readouterr()
    assert "Error retrieving secret: Some AWS exception" in captured.out
    assert result == {}


@patch("boto3.client", return_value=MockClient())
def test_validate_secret_valid(boto_client):
    secret_data = {
        "password": MockClient._get_secure_string(),
        "dbname": DB_NAME,
        "engine": ENGINE,
        "port": PORT,
        "dbInstanceIdentifier": DB_INSTANCE_IDENTIFIER,
        "host": HOST,
        "username": MockClient._get_user(),
    }
    assert VirtualUserUtils.validate_secret(secret_data, "dms")


@patch("boto3.client", return_value=MockClient())
def test_validate_secret_invalid(boto_client):
    secret_data = {
        "password": MockClient._get_secure_string(),
        "dbname": DB_NAME,
        "engine": ENGINE,
        # Missing port
        "dbInstanceIdentifier": DB_INSTANCE_IDENTIFIER,
        "host": HOST,
        "username": MockClient._get_user(),
    }
    assert not VirtualUserUtils.validate_secret(secret_data, "dms")


@patch("boto3.client", return_value=MockClient())
def test_validate_secret_undefined_pattern(boto_client):
    with pytest.raises(ValueError, match=r"Pattern type undefined_pattern is not defined."):
        VirtualUserUtils.validate_secret({}, "undefined_pattern")


@patch("boto3.client", return_value=MockClient())
def test_validate_secret_extra_keys(boto_client):
    secret_data = {
        "password": MockClient._get_secure_string(),
        "dbname": DB_NAME,
        "engine": ENGINE,
        "port": PORT,
        "dbInstanceIdentifier": DB_INSTANCE_IDENTIFIER,
        "host": HOST,
        "username": MockClient._get_user(),
        "extra_key": "unexpected_key",
    }
    assert not VirtualUserUtils.validate_secret(secret_data, "dms")


@pytest.fixture
def mocked_yaml_content():
    return """
    system_test:
        name: SystemTestLatest
        description: System Test Latest
        test_mode: time_mode
    pattern:
        dms:
            data_mocker:
                active_injection: True
                data_contract_test_data_path: None
                only_payload_data: True
                change_fields: 0.0
                omit_fields: 0.0
                use_alias: False
                add_data_contract: True
    """


def test_get_config_valid_pattern_and_key(mocked_yaml_content):
    m = mock_open(read_data=mocked_yaml_content)
    with patch(BUILTINS_OPEN, m):
        config = VirtualUserUtils.get_config("dms", "data_mocker")
        assert config == {
            "active_injection": True,
            "data_contract_test_data_path": "None",
            "only_payload_data": True,
            "change_fields": 0.0,
            "omit_fields": 0.0,
            "use_alias": False,
            "add_data_contract": True,
        }


def test_get_config_invalid_pattern(mocked_yaml_content):
    m = mock_open(read_data=mocked_yaml_content)
    with patch(BUILTINS_OPEN, m):
        with pytest.raises(KeyError, match="No configuration found for pattern type: invalid_pattern"):
            VirtualUserUtils.get_config("invalid_pattern", "data_mocker")


def test_get_config_invalid_key(mocked_yaml_content):
    m = mock_open(read_data=mocked_yaml_content)
    with patch(BUILTINS_OPEN, m):
        with pytest.raises(
            KeyError, match="No configuration found for pattern type: dms and key config name: invalid_key"
        ):
            VirtualUserUtils.get_config("dms", "invalid_key")


@patch("boto3.client", return_value=MockClient())
def test_get_parameter_store(boto_client):
    result = VirtualUserUtils.get_parameter("valid_parameter")
    expected_result = "valid_value"
    assert result == expected_result


@patch("boto3.client", return_value=MockClient())
def test_get_parameter_store_invalid(boto_client):
    result = VirtualUserUtils.get_parameter("invalid_parameter")
    expected_result = None
    assert result == expected_result
