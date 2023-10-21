import json
import os

import boto3
import botocore
from aws_lambda_powertools import Logger

logger = Logger()

stack_name = os.environ.get("GUEST360_STACK_NAME")

if stack_name is None:
    raise Exception(
        "missing stack name. Please set GUEST360_STACK_NAME environment variable"
    )

ssm_param_store_name = f"/{stack_name}/data-services/api-authorizer-lambda/api-config"
# ssm_param_store_name = "/Guest36020220914/data-services/api-authorizer-lambda/api-config"

api_auth_config = {
    "url": "https://stg.authorization.go.com/validate/",
    "scope_mapper_bucket": "s3bucket-490164644464",
    "scope_mapper_key": "/s3key/scope_map.json",
}

scope_map = json.loads(
    """
            {
              "authorization": [
                {
                  "authType": "pattern",
                  "urlPattern": "/api/v1/profile/*",
                  "id": 1,
                  "authToken": true,
                  "gdsEnabled": false,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-ia-roz-ccpa"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/minisite2/*",
                  "id": 2,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test",
                        "tpr-celia-other"
                      ]
                    }
                  ]
                },
                {
                  "authType": "pattern",
                  "urlPattern": "/api/v1/lightinglane/*",
                  "id": 3,
                  "authToken": true,
                  "gdsEnabled": true,
                  "scopes": [
                    {
                      "method": "GET",
                      "scopesRequired": [
                        "tpr-celia-test"
                      ]
                    }
                  ]
                }
              ]
            }
            """
)

#  AWS_REGION = "us-east-1"
#  ENDPOINT_URL = "http://host.docker.internal:4566"
#  os.environ["AWS_ACCESS_KEY_ID"] = "test"
#  os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
#  os.environ["AWS_DEFAULT_REGION"] = AWS_REGION
ENDPOINT_URL = None
AWS_REGION = os.environ["AWS_DEFAULT_REGION"]
ssm_client = boto3.client("ssm")
s3_resource = boto3.resource("s3")

sts = boto3.client("sts")
print(sts.get_caller_identity())
# Create SSM param store for testing:
try:
    ssm_client.put_parameter(
        Name=ssm_param_store_name,
        Value=json.dumps(api_auth_config),
        Type="SecureString",
        Overwrite=True,
    )
except Exception as error:
    # TODO - figure out class for botocore.errorfactory.ParameterAlreadyExists
    logger.info("Parameter store already exists, no need to create. error=%s", error)

s3_bucket = s3_resource.Bucket(api_auth_config["scope_mapper_bucket"])
s3_bucket.create()
s3_bucket.Versioning().enable()
s3_object = s3_bucket.put_object(
    Key=api_auth_config["scope_mapper_key"],
    Body=bytes(json.dumps(scope_map, indent=2), "utf-8"),
)
