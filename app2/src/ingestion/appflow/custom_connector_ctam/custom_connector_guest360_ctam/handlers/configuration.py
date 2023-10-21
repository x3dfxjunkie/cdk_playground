"""CTAM CONFIG HANDLER"""
from app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam import constants
from app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam.handlers import validation
from app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam.handlers.client import HttpsClient
from custom_connector_sdk.connector import settings
from custom_connector_sdk.connector import configuration as config
from custom_connector_sdk.connector import auth
from custom_connector_sdk.lambda_handler import requests
from custom_connector_sdk.lambda_handler import responses
from custom_connector_sdk.lambda_handler.handlers import ConfigurationHandler


CONNECTOR_OWNER = "Disney CTAM Connector"
CONNECTOR_NAME = "PythonCTAMConnector"
CONNECTOR_VERSION = "1.0"

API_VERSION = "v5"
API_VERSION_KEY = "api_version"
ENTITY_ID = "title"

TRUE = "true"


def get_ctam_client() -> HttpsClient:
    return HttpsClient()


class CTAMConfigurationHandler(ConfigurationHandler):
    """CTAM Configuration Handler."""

    def validate_connector_runtime_settings(
        self, request: requests.ValidateConnectorRuntimeSettingsRequest
    ) -> responses.ValidateConnectorRuntimeSettingsResponse:
        errors = validation.validate_connector_runtime_settings(request)
        if errors:
            return responses.ValidateConnectorRuntimeSettingsResponse(is_success=False, error_details=errors)
        return responses.ValidateConnectorRuntimeSettingsResponse(is_success=True)

    # pylint: disable=unused-argument
    def validate_credentials(
        self, request: requests.ValidateCredentialsRequest
    ) -> responses.ValidateCredentialsResponse:
        return responses.ValidateCredentialsResponse(is_success=True)

    # pylint: disable=unused-argument
    def describe_connector_configuration(
        self, request: requests.DescribeConnectorConfigurationRequest
    ) -> responses.DescribeConnectorConfigurationResponse:
        connector_modes = [config.ConnectorModes.SOURCE]

        instance_url_setting = settings.ConnectorRuntimeSetting(
            key=constants.INSTANCE_URL_KEY,
            data_type=settings.ConnectorRuntimeSettingDataType.String,
            required=True,
            label="CTAM Instance URL",
            description="URL of the instance where user wants to " + "run the operations",
            scope=settings.ConnectorRuntimeSettingScope.CONNECTOR_PROFILE,
        )
        entity_id = settings.ConnectorRuntimeSetting(
            key=ENTITY_ID,
            data_type=settings.ConnectorRuntimeSettingDataType.String,
            required=True,
            label="Type of ctam entity",
            description="CTAM Entity to look up",
            scope=settings.ConnectorRuntimeSettingScope.CONNECTOR_PROFILE,
        )
        connector_runtime_settings = [instance_url_setting, entity_id]

        authentication_config = auth.AuthenticationConfig(is_basic_auth_supported=True)

        return responses.DescribeConnectorConfigurationResponse(
            is_success=True,
            connector_owner=CONNECTOR_OWNER,
            connector_name=CONNECTOR_NAME,
            connector_version=CONNECTOR_VERSION,
            connector_modes=connector_modes,
            connector_runtime_setting=connector_runtime_settings,
            authentication_config=authentication_config,
            supported_api_versions=[API_VERSION],
            supported_write_operations=constants.SUPPORTED_WRITE_OPERATIONS,
        )
