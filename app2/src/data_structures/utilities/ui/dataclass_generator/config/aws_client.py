"""
AWS Client class script
Raises:
    AWSSessionException: AWS Session failure exception.
    SecretsManagerClientException: AWS Secretes Manager Client Exception.
"""

import os
import boto3
import json


class AWSClient:
    """AWS Client class"""

    def __init__(self) -> None:
        self.user_role_arn = os.getenv("USER_ROLE_ARN")

    def aws_auth(self) -> dict:
        """
        Generates AWS authentication using the default profile and a given Role.
        It is possible to chance the path where credentials exists.

        Returns:
            dict: Client response credentials with assumed role.
        """
        session = boto3.Session()
        sts = session.client("sts")
        return sts.assume_role(RoleArn=self.user_role_arn, RoleSessionName="sm-extractor")

    def get_secrets_client(self, secret_name: str) -> dict:
        """
        Gets secrets in AWS Secrets Manager in a given path.
        Args:
            secret_name (str): Secrets path in AWS Secrets Manager.

        Raises:
            client_error: Error on AWS client.

        Returns:
            dict: Secrets dictionary.
        """
        region_name = "us-east-1"
        response = self.aws_auth()

        new_session = boto3.Session(
            aws_access_key_id=response["Credentials"]["AccessKeyId"],
            aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
            aws_session_token=response["Credentials"]["SessionToken"],
        )

        client = new_session.client(service_name="secretsmanager", region_name=region_name)

        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response.get("SecretString")
        return json.loads(secret)
