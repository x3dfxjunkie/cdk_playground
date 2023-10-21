"""CTAM lambda handler"""
from app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam.handlers.record import (
    CTAMRecordHandler,
)
from app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam.handlers.metadata import (
    CTAMMetadataHandler,
)
from app.src.ingestion.appflow.custom_connector_ctam.custom_connector_guest360_ctam.handlers.configuration import (
    CTAMConfigurationHandler,
)
from custom_connector_sdk.lambda_handler.lambda_handler import BaseLambdaConnectorHandler


class CTAMLambdaHandler(BaseLambdaConnectorHandler):
    def __init__(self):
        super().__init__(CTAMMetadataHandler(), CTAMRecordHandler(), CTAMConfigurationHandler())


def ctam_lambda_handler(event, context):
    """Lambda entry point."""
    return CTAMLambdaHandler().lambda_handler(event, context)
