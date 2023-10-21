"""Onboarding Bootcamp Framework Stack"""
import logging
import sys

from aws_cdk import Stack, Tags

from app.infrastructure.workstream_stack import WorkstreamStack

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Load_testing | %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)


class BootcampStack(WorkstreamStack):
    """Class for building the Onboarding Bootcamp stack from the Onboarding Bootcamp Construct
    guest360_constructs/bootcamp/kinesis_construct.py
    all the configurations are loaded from ./config/environment/*.yaml
    """

    def __init__(
        self,
        scope: Stack,
        construct_id: str,
        environment_config: dict,  # pylint: disable=unused-argument
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        prefix = self.node.try_get_context("prefix")
        Tags.of(self).add("prefix", prefix)

        """
        These are needed for the Feature Flag section of the tutorial - disregard for previous sections
        """

        """
        Add the Kinesis Construct you created here. 
        NOTE: When creating the construct, notice there is a `scope` argument in the constructor, and there is a `scope` argument in this constructor as well. 
        The `scope` argument is the construct's parent or owner (https://docs.aws.amazon.com/cdk/v2/guide/constructs.html) - 
        meaning if same `scope` is supplied to the Kinesis construct here, our CF stack and Kinesis data stream will be in the same level in the construct hierarchy.
        We want the stack to own the data stream.
        """
