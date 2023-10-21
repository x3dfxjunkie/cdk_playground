"""test for messaging instance construct
"""
# pylint: disable=redefined-outer-name
import json
import logging
import sys
import os
import yaml

from mock import patch
import pytest
from aws_cdk import assertions, aws_lambda
from app.guest360_constructs.ingestion.messaging_ingest import Guest360MessagingIngest
from app.guest360_constructs.app_config_base import Guest360AppConfigBase
from app.guest360_constructs.s3_bucket import Guest360S3Bucket
from app.guest360_constructs.ingestion.tests.assertion_utils import (
    assert_template_contains_common_ingestion_resources,
    assert_template_contains_dashboard_resources,
)


logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


@pytest.fixture
def test_props():
    with open(f"{os.path.dirname(__file__)}/config/messaging_pipeline.yaml", encoding="utf-8") as fp:
        pipeline_config = yaml.unsafe_load(fp.read())
        props = pipeline_config["pattern_instances"][0]["resources"]
    yield props


@pytest.mark.timeout(30, method="signal")
def test_messaging_ingest_created(test_props, test_stack):
    bucket = Guest360S3Bucket(test_stack, "test", region="us-east-1", props={"bucket_name": "test"}).bucket
    test_props["static_buckets"] = [{"bucket_name": "test", "bucket": bucket}]
    test_props["app_config_base"] = Guest360AppConfigBase(
        test_stack,
        construct_id="test-dms-ingest",
        props={
            "deployment_strategy": {
                "deployment_duration_in_minutes": 0,
                "growth_factor": 100,
                "replicate_to": "NONE",
            },
        },
    )
    with patch(
        "app.guest360_constructs.lambda_function.aws_lambda.Code.from_asset",
        lambda *args: aws_lambda.Code.from_inline("""mytestcode"""),
    ):
        Guest360MessagingIngest(test_stack, "test-messaging-ingest", test_props)

    template = assertions.Template.from_stack(test_stack)

    logger.debug(json.dumps(template.to_json(), indent=2))

    assert_template_contains_common_ingestion_resources(template)
    assert_template_contains_dashboard_resources(template)
    template.resource_count_is("AWS::S3::Bucket", 2)
    template.resource_count_is("AWS::ECS::Cluster", 1)
    template.resource_count_is("AWS::IAM::Role", 9)
