"""test for lambda shredder construct
"""
import logging
import sys
from aws_cdk import assertions
from app.guest360_constructs.ingestion.data_pipeline_dashboard import Guest360IngestionPipelineDashboard
from test_helpers.print_template import print_template_on_debug

# set log levels for noisy boto calls to info
logging.getLogger("faker").setLevel(logging.INFO)
logging.getLogger("boto3").setLevel(logging.INFO)
logging.getLogger("botocore").setLevel(logging.INFO)
logging.getLogger("s3transfer").setLevel(logging.INFO)

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


def test_ingestion_data_pipeline_add_function_enrichment(test_stack):  # pylint: disable=redefined-outer-name
    dashboard = Guest360IngestionPipelineDashboard(test_stack, "test_ingestion_dashboard", "test_ingestion_dashboard")
    dashboard.add_function_enrichment(
        namespace="test_namespace", subject="test_subject", function_name="test_function_name"
    )
    # render template
    template = assertions.Template.from_stack(test_stack)

    print_template_on_debug(template, logger)
    template.resource_count_is(type="AWS::CloudWatch::Dashboard", count=1)
