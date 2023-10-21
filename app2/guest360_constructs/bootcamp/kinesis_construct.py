from typing import TypedDict, Union

import aws_cdk
from aws_cdk import Duration, aws_kinesis
from cdk_nag import NagSuppressions
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired

from app.guest360_constructs.construct_360 import Construct360
from app.src.reliability.utils import KinesisStreamName

"""
START HERE! Create a class that inherits from `TypedDict` which defines various properties required for aws_cdk.aws_kinesis.Stream. 
To enforce proper typing,be sure to apply the match_class_typing decorator from the strongtyping package to the class.

"""


class BootcampKinesisProps(TypedDict):
    """FILL ME OUT: The props should reflect the bare minimum needed to get
    a Kinesis Stream created"""


"""
NEXT, fill out the __init__ of this new construct, which will use the properties defined above in the `BootcampKinesisProps`.
"""


class Guest360BootcampKinesisDatastream(Construct360):
    def __init__(self, scope: Construct360, construct_id: str, props: BootcampKinesisProps, **kwargs) -> None:
        """FILL ME OUT: it should instantiate the aws_kinesis.Stream method.
        aws_kinesis.Stream(scope=self, id=<unique string id>, props=???)
        """
        super().__init__(scope, construct_id, **kwargs)
        BootcampKinesisProps(props)
