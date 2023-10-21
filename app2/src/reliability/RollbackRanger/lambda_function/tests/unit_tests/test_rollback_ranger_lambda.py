"""
    This tests the Lambda function from a mock event
"""
# pylint: disable=C0415
from io import BytesIO
import boto3
import os
import pytest
import time

from moto import mock_s3

from app.src.reliability.RollbackRanger.lambda_function.lambda_function import lambda_handler

os.environ["REGION"] = "use1"
os.environ["ENVIRONMENT"] = "testenv"
BUCKET_NAME = "TEST"


@mock_s3
def test_s3copy_rollback_ranger_function():
    """Test s3 copy functionality"""
    # instantiate s3 client
    s3_client = boto3.client("s3")

    # create test bucket
    s3_client.create_bucket(Bucket=BUCKET_NAME)
    # create wrapper for byte objects so it works with boto3
    fileobj1 = BytesIO(b"app_deployed.zip")
    fileobj2 = BytesIO(b"app.zip")
    # create mock app_deployed and app.zip files
    s3_client.upload_fileobj(fileobj1, BUCKET_NAME, "app_deployed.zip")
    s3_client.upload_fileobj(fileobj2, BUCKET_NAME, "app.zip")

    # capture app.zip file description before copy call in lambda
    listobj1 = s3_client.list_objects(Bucket=BUCKET_NAME)
    file_before_copy = listobj1["Contents"][0]

    # call copy function in rollback ranger lambda
    response = lambda_handler({"EnableRollback": "True"}, None, BUCKET_NAME)

    # capture file description after copy call. Should be different
    listobj2 = s3_client.list_objects(Bucket=BUCKET_NAME)
    file_after_copy = listobj2["Contents"][0]

    assert response == "Successful Rollback" and file_before_copy != file_after_copy


@mock_s3
def test_s3copy_failure_rollback_ranger_function():
    """Test s3 copy functionality"""
    with pytest.raises(Exception) as excinfo:
        s3_client = boto3.client("s3")
        s3_client.create_bucket(Bucket=BUCKET_NAME)

        fileobj1 = BytesIO(b"app_deployed.zip")
        fileobj2 = BytesIO(b"app.zip")
        # purposely introduce typo in name to make sure call fails if file DNE
        s3_client.upload_fileobj(fileobj1, BUCKET_NAME, "app_deployed_fail.zip")
        s3_client.upload_fileobj(fileobj2, BUCKET_NAME, "app.zip")

        lambda_handler({"EnableRollback": "True"}, None, BUCKET_NAME)

    assert str(excinfo.value) == "An error occurred (404) when calling the HeadObject operation: Not Found"


def test_basic_rollback_ranger_function():
    """Test False Payload"""
    # Test to make sure lambda can accept input
    response = lambda_handler({"EnableRollback": "False"}, None)
    assert response == 'Did not rollback. To rollback, pass {"EnableRollback": "True"} to lambda'
