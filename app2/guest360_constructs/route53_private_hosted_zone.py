"""
Defines base construct and defaults for route53 private hosted zone
"""
import aws_cdk, os, yaml, re
from typing import TypedDict
from typing_extensions import NotRequired
from app.guest360_constructs.construct_360 import Construct360
from constructs import Construct
from strongtyping.strong_typing import match_class_typing
from aws_cdk.aws_route53 import PrivateHostedZone
from app.src.reliability.utils import (
    StackName,
)


@match_class_typing
class PrivateHostedZoneProps(TypedDict):
    """
    :prop domain_name -  The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
    :prop zone -   Whether to add a trailing dot to the zone name. Default: true
    Not Implemented
    :prop comment - Any comments that you want to include about the hosted zone. Default: none
    :prop query_logs_log_group_arn - The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
    """

    zone_name: str
    add_trailing_dot: NotRequired[bool]
    extra_vpcs: NotRequired[list[str]]


class Guest360PrivateHostedZone(Construct360):
    """ """

    def __init__(self, scope: Construct360, construct_id: str, props: PrivateHostedZoneProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        PrivateHostedZoneProps(props)
        self.naming_prefix = f"{self._prefix}-{construct_id}"
        self.props_default = {"vpc": self._return_vpc(self._vpc_id)}
        self.props_merged = self.props_default | props
        self.extra_vpcs = self.props_merged.pop("extra_vpcs", [])
        self._private_hosted_zone = PrivateHostedZone(self, construct_id, **self.props_merged)
        for vpc in self.extra_vpcs:
            self._private_hosted_zone.add_vpc(self._return_vpc(vpc))

    def _return_vpc(self, vpc_id):
        return aws_cdk.aws_ec2.Vpc.from_lookup(self, StackName(self.naming_prefix, vpc_id).name(), vpc_id=vpc_id)

    @property
    def get_hosted_zone_arn(self):
        return self._private_hosted_zone.hosted_zone_arn

    @property
    def get_hosted_zone_id(self):
        return self._private_hosted_zone.hosted_zone_id

    @property
    def get_hosted_zone(self):
        return self._private_hosted_zone

    @classmethod
    def get_from_hosted_zone_attributes(cls, *args, **kwargs) -> PrivateHostedZone:
        """
        Imports from another stack
        stack, "test", **{"hosted_zone_id": "foo", "zone_name": "foo"}
        """
        return PrivateHostedZone.from_hosted_zone_attributes(*args, **kwargs)

    @classmethod
    def get_from_hosted_zone_id(cls, *args, **kwargs):
        """
        Imports from outside of cdk or another stack
        stack, "test", **{"hosted_zone_id": "foo"}
        """
        return PrivateHostedZone.from_hosted_zone_id(*args, **kwargs)

    @classmethod
    def get_from_lookup(cls, *args, **kwargs):
        """
        Lookup a hosted zone in the current account/region based on query parameters.
        Requires environment, you must specify env for the stack.
        Use to easily query hosted zones.
        """
        return PrivateHostedZone.from_hosted_zone_id(*args, **kwargs)
