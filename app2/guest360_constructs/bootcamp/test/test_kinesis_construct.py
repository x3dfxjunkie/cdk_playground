import pytest
import logging
import sys
import yaml

from app.guest360_constructs.bootcamp.kinesis_construct import Guest360BootcampKinesisDatastream

from aws_cdk import App, Stack, assertions

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

TEST_CONTEXT = {"prefix": "lst-test_kinesis-use1", "environment": "local"}


class TestBootcampKinesis:
    @pytest.mark.timeout(30, method="signal")
    def test_instantiate_construct_default_params(self):
        """
        SHOW TIME! Time to test that your construct (Guest360BootcampKinesisDatastream) creates a kinesis stream correctly.
        """

        """A construct which represents an entire CDK app.
        This construct is normally the root of the construct tree.
        From: https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_core.App.html"""
        app = App(context=TEST_CONTEXT)

        """A root construct which represents a single CloudFormation stack.
        From: https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_core.Stack.html"""
        stack = Stack(app)

        """Instantiate the Guest360BootcampKinesisDatastream(<STACK VAR>, <ID (can be any unique string of your choosing)>, <BootcampKinesisProps>)"""

        """Cloudformation Template"""
        template = assertions.Template.from_stack(stack)
        """ Print the Cloudformation template as a yaml and json """
        logger.debug(yaml.dump(template.to_json()))
