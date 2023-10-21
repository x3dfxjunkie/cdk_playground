"""Guest360LambdaFunction construct
"""
from typing import Any, Dict, TypedDict, Union

from aws_cdk import aws_pipes
from constructs import Construct
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import EventBridgePipeName
from app.guest360_constructs.cloudwatch_alarm import Guest360Alarm
from app.guest360_constructs.enums.event_bridge_pipe_states import EventBridgePipeState


class InvalidPipePropertyParameterError(Exception):
    """Exception for invalid event bridge source/target params supplied from config"""


@match_class_typing
class EventBridgePipeProps(TypedDict):
    """event bridge pipe properties"""

    name: str
    pipe_source_parameters: Dict[str, Any]
    pipe_target_parameters: Dict[str, Any]
    role_arn: str
    source_arn: str
    target_arn: str
    enrichment: NotRequired[str]
    enrichment_parameters: NotRequired[Dict[str, Any]]
    tags: NotRequired[Dict[str, str]]


class Guest360EventBridgePipe(Construct360):
    """Guest360 Construct for event bridge pipes"""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        props: Union[EventBridgePipeProps, dict],
        **kwargs,
    ) -> None:
        """__init__.
        Guest360EventBridgePipe
        """
        super().__init__(scope, construct_id, **kwargs)

        prefix = self.node.try_get_context("prefix")
        event_bridge_pipe_name = EventBridgePipeName(prefix, props["name"]).name()
        try:
            # TODO: should we have a resolution step here? Currently pipe source and target params don't validate the supplied params are valid
            # e.g; if `kinesis_stream_parameters` are given as a dict for target, the dict may not actually conform to aws_pipes.CfnPipe.PipeTargetKinesisStreamParametersProperty
            pipe_source_parameter = aws_pipes.CfnPipe.PipeSourceParametersProperty(**props["pipe_source_parameters"])
            pipe_target_parameters = aws_pipes.CfnPipe.PipeTargetParametersProperty(**props["pipe_target_parameters"])
        except TypeError as e:
            # NOTE: should we be more granular and do this per pipe param so we can log the specific problem? The TypeError message should be detailed enough
            raise InvalidPipePropertyParameterError(
                "Invalid source and/or target event bridge pipe parameters supplied in configuration"
            ) from e
        EventBridgePipeProps(props)
        aws_pipes.CfnPipe(
            self,
            id=event_bridge_pipe_name,  # TODO: is this okay we just reuse the name?
            role_arn=props["role_arn"],
            source=props["source_arn"],
            target=props["target_arn"],
            desired_state=EventBridgePipeState.RUNNING,
            name=event_bridge_pipe_name,
            source_parameters=pipe_source_parameter,
            tags=props.get("tags"),
            target_parameters=pipe_target_parameters,
            enrichment=props.get("enrichment"),
        )

        default_alarms = []  # TODO: what are good default alarms here?

        for cw_alarm in default_alarms:
            Guest360Alarm(
                self,
                f"{event_bridge_pipe_name}-{cw_alarm['metric'].metric_name}-cw-alarm",
                props=cw_alarm,
            )
