"""
This Function is the handler function for the rollback ranger lambda
This will simply replace app.zip with app_deployment.zip. It rollbacks
the deployment to the last successful one.

Payload to run lambda:
```json
{"EnableRollback": "True"}
```
"""
import boto3
import json
import os


def lambda_handler(event: dict, _, bucket_name=None, key_prefix=""):
    """Replaces app.zip with app_deployed.zip"""
    # this conditional accounts for pytest calls to lambda
    if bucket_name is None:
        prefix = os.getenv("PREFIX")
        bucket_name = f"{prefix}-build-pipeline-bucket"
        key_prefix = "CodeBuild/Guest360/"

    if event.get("EnableRollback") == "True":
        s3 = boto3.resource("s3")
        copy_source = {
            "Bucket": bucket_name,
            "Key": f"{key_prefix}app_deployed.zip",
        }
        target_bucket = s3.Bucket(bucket_name)
        # This param is needed to avoid kms:GenerateKmsKey errors
        kms_bypass = {"ServerSideEncryption": "aws:kms"}
        # overwrite app.zip with app_deployed.zip
        target_bucket.copy(copy_source, f"{key_prefix}app.zip", kms_bypass)
        # this copy command does not return a response. If an error occurs, "successful rollback"
        # message is not returned and the exception/error is raised in AWS Lambda.
        response = "Successful Rollback"
        return json.loads(json.dumps(response, default=str))

    else:
        response = 'Did not rollback. To rollback, pass {"EnableRollback": "True"} to lambda'
        return json.loads(json.dumps(response, default=str))
