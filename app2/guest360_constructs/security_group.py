"""
Defines base construct and defaults for security group
"""
import aws_cdk, os, yaml
from typing import TypedDict, Dict, Any
from typing_extensions import NotRequired
from app.guest360_constructs.construct_360 import Construct360
from aws_cdk import aws_ec2 as ec2
from strongtyping.strong_typing import match_class_typing
from aws_cdk.aws_ec2 import SecurityGroup
from app.src.reliability.utils import StackName


@match_class_typing
class SecurityGroupRule(TypedDict):
    """
    :prop protocol => (TCP/UDP/ICMP) Huge List of allowed protocols, there is something more than TCP?  https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/Protocol.html#aws_cdk.aws_ec2.Protocol
    :prop from_port => starting port - please note that ports below 1024 may have nacls assigned
    :prop to_Port => finishing port - please note that ports below 1024 may have nacls assigned
    ###Note one of the next 3 are required, if none provided defaults to vpc
    :prop cidr_block => specific cidr block in x.x.x.x/x format
    :prop vpc_only => helper flag to add the cidr for the vpc
    :prop all_internal => helper flag to add all disney internal ips (which includes some external)
    """

    protocol: str
    from_port: int
    to_port: int
    cidr_block: NotRequired[str]
    vpc_only: NotRequired[bool]
    all_internal: NotRequired[bool]


@match_class_typing
class SecurityGroupProps(TypedDict):
    """
    :prop security_group_name - The name of the security group. For valid values, see the GroupName parameter of the CreateSecurityGroup action in the Amazon EC2 API Reference. It is not recommended to use an explicit group name. Default: If you don’t specify a GroupName, AWS CloudFormation generates a unique physical ID and uses that ID for the group name.
    :prop ingress_rules - Rules that determine allowed inbound traffic to the security group.  no rules equals no traffic
    :prop egress_rules - Rules that determine allowed outbound traffic to the security group.  no rules equals no traffic
    """

    security_group_name: str
    ingress_rules: NotRequired[list[Dict[Any, Any]]]
    egress_rules: NotRequired[list[Dict[Any, Any]]]


class Guest360SecurityGroup(Construct360):
    """
    Example:
        obj = {
            "security_group_name": "Foo",
            "ingress_rules: [{
                "protocol": "TCP",
                "from_port": "443",
                "to_port":
            }]
        }
        Guest360SecurityGroup(stack,  ", "TheQueueName")
    Args:
        scope (Construct): scope
        id (str): id
        props (SecurityGroupProps): properties to use for the Security Group.
        kwargs (dict): kwargs dict to pass to construct init.

    Returns:
        None
    """

    def __init__(self, scope: Construct360, construct_id: str, props: SecurityGroupProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        SecurityGroupProps(props)
        stack = aws_cdk.Stack.of(self)
        prefix = self.node.try_get_context("prefix")
        self.naming_prefix = f"{prefix}-{construct_id}"
        props["security_group_name"] = f'{self.naming_prefix}-{props["security_group_name"]}'
        environment = self.node.try_get_context("environment")
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/../configs/{environment}-environment.yaml",
            mode="r",
            encoding="utf-8",
        ) as file:
            vpc = yaml.safe_load(file)["networking"][stack.region]["vpc"]

        self.vpc_cidr_blocks = vpc["cidr"]
        self._vpc = aws_cdk.aws_ec2.Vpc.from_lookup(self, StackName(self.naming_prefix, "vpc").name(), vpc_id=vpc["id"])
        self.props_default = {"allow_all_ipv6_outbound": False, "allow_all_outbound": False, "vpc": self._vpc}
        self.props_merged = self.props_default | props
        self._ingress_rules = self.props_merged.pop("ingress_rules", [])
        self._egress_rules = self.props_merged.pop("egress_rules", [])
        self._security_group = SecurityGroup(self, construct_id, **self.props_merged)
        self._create_rules(self._ingress_rules, self._security_group.add_ingress_rule)
        self._create_rules(self._egress_rules, self._security_group.add_egress_rule)

    def _create_rules(self, rules, add_rule):
        for rule in rules:
            self._validate_rule(rule)
            if (
                not rule.keys() & {"vpc_only", "all_internal", "cidr_block"}
                or "vpc_only" in rule.keys()
                and rule["vpc_only"]
            ):
                for peer in self._get_vpc_cidr_blocks():
                    add_rule(peer, self._get_protocol(rule))
            elif "all_internal" in rule.keys() and rule["all_internal"]:
                for peer in self._get_internal_cidr_blocks():
                    add_rule(peer, self._get_protocol(rule))
            else:
                add_rule(ec2.Peer.ipv4(rule["cidr_block"]), self._get_protocol(rule))

    def _get_protocol(self, rule):
        match rule["protocol"]:
            case "TCP":
                return ec2.Port.tcp_range(start_port=rule["from_port"], end_port=rule["to_port"])
            case "UDP":
                return ec2.Port.udp_range(start_port=rule["from_port"], end_port=rule["to_port"])
            case "ICMP":
                return ec2.Port.icmp_ping()
            case other:
                raise ValueError("Protocol not supported.")

    def _get_vpc_cidr_blocks(self):
        return [ec2.Peer.ipv4(cidr) for cidr in self.vpc_cidr_blocks]

    def _get_internal_cidr_blocks(self):
        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/../configs/constants.yaml",
            mode="r",
            encoding="utf-8",
        ) as file:
            return [ec2.Peer.ipv4(cidr) for cidr in yaml.safe_load(file)["disney_internal_cidr_blocks"]["ipv4"]]

    def _validate_rule(self, rule):
        SecurityGroupRule(rule)
        if rule["from_port"] > 65535 or rule["to_port"] > 65535:
            raise ValueError("Ports out of range.")

    @property
    def security_group_id(self):
        return self._security_group.security_group_id

    @property
    def security_group(self):
        return self._security_group

    @classmethod
    def from_lookup_by_name(cls, *args, **kwargs) -> aws_cdk.aws_ec2.SecurityGroup:
        return aws_cdk.aws_ec2.SecurityGroup.from_lookup_by_name(*args, **kwargs)

    @classmethod
    def from_lookup_by_id(cls, *args, **kwargs) -> aws_cdk.aws_ec2.SecurityGroup:
        return aws_cdk.aws_ec2.SecurityGroup.from_lookup_by_id(*args, **kwargs)
