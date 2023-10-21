""" Stack for DMS Certificates to support DMS Ingest infrastructure."""
import logging
import sys

import aws_cdk
from aws_cdk import aws_dms, Stack
import requests
from retry import retry

from app.guest360_constructs.construct_360 import Construct360
from app.infrastructure.workstream_stack import WorkstreamStack
from app.src.reliability.utils import StackName


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - DMS Ingestion Certificates | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class FetchCertificateError(Exception):
    "Failed to get the requested certificate"


@retry(FetchCertificateError, delay=5, tries=6)
def get_dms_certificate(cert_url_path: str, timeout: int = 30) -> str:
    """
    TODO: Validate that we are getting a valid certificate
    Take a url path and return pem certificate
    Args:
        cert_url_path (str): url path to the requested cert
    Returns:
        str: pem formatted cert
    test pulling RDS CA cert chain (simple test - just verify it runs and we get a result)
    >>> '-----BEGIN CERTIFICATE-----' in get_dms_certificate("https://truststore.pki.rds.amazonaws.com/us-east-1/us-east-1-bundle.pem")
    True
    """
    try:
        response = requests.get(cert_url_path, timeout=timeout)
        response.raise_for_status()
        return response.content.decode()
    except Exception as err:
        logger.error(err)
        raise FetchCertificateError(f"Failed to get the requested certificate using {cert_url_path}") from err


class DMSIngestionCerts(WorkstreamStack):
    """
    Stack definition for the dms certificates. Creates rds certificates for DMS sources that require SSL.
    """

    @property
    def certificates(self) -> list[aws_cdk.CfnOutput.import_value]:
        """Property to return kinesis streams"""
        return self.dms_certificates

    def __init__(self, scope: Construct360, construct_id: str, config: dict, **kwargs) -> None:
        """Initialization method for ingestion certificates class
        Args:
            scope (Construct360): scope for stack
            construct_id (str): ID of construct for naming purposes
            environment_config (dict): environment configuration details
        """
        super().__init__(scope, construct_id, **kwargs)

        prefix = self.node.try_get_context("prefix")
        is_static_env = self.node.try_get_context("is_static_env")
        stack_name = Stack.of(self).stack_name

        self.dms_certificates = []

        # create RDS DMS certificate
        for instance in config["instances"]:
            props = instance["certificate"]
            certificate_name = StackName(prefix, props["cert_name"]).name()

            cert_file = get_dms_certificate(props["cert_url"])
            self.cfn_certificate = aws_dms.CfnCertificate(
                self,
                StackName(prefix, props["cert_name"]).name(),
                certificate_pem=cert_file,
            )

            resource_name = f"dms_cert_{props['cert_name']}"
            cert_name = StackName(prefix, f"{props['cert_name']}-cert-output").name()

            self.ssm_export(resource_name, self.cfn_certificate.ref, cert_name)

            self.dms_certificates.append(
                {
                    "parameter_name": f"/{prefix}/{stack_name}/{cert_name}/{resource_name}",
                    "certificate_name": certificate_name,
                }
            )
