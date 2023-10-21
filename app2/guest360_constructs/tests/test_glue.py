"""Tests for Guest360S3Bucket"""
# pylint: disable=redefined-outer-name pytest fixtures are exceptions to this rule
# pylint: disable=import-outside-toplevel need to import within the boto mocks due to lambda global boto resources
# pylint: disable=logging-fstring-interpolation for testing files lazy logging is not needed

import pytest
from app.guest360_constructs.glue import Guest360Glue
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from aws_cdk import App, Stack, assertions

TEST_CONTEXT = {"prefix": "lst-use1-pytest", "environment": "latest", "stack": "test_stack"}


@pytest.fixture
def test_props():
    return {"job_name": "test_name", "bucket": "test_bucket", "prefix": "prefix/", "artifact_name": "test.py"}


@pytest.mark.unit
def test_glue(test_props):
    app = App(context=TEST_CONTEXT)
    stack = Stack(app)

    test_g360_bucket = Guest360S3Bucket(stack, "TestBucket", region="us-east-1", props={"bucket_name": "test-bucket"})

    test_bucket_name = test_g360_bucket.bucket_name
    test_props["bucket"] = test_bucket_name

    Guest360Glue(stack, "TestGlue", props=test_props)

    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::Glue::Job",
        {
            "Command": {
                "Name": "glueetl",
                "PythonVersion": "3",
                "ScriptLocation": "s3://lst-use1-pytest-lst-use1-pytest-test-bucket/prefix/test.py",
            },
            "GlueVersion": "4.0",
        },
    )
