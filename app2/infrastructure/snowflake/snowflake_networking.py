"""This file contains the Snowflake Networking for the Infrastructure Stack"""
import logging, yaml, hashlib
from typing import TypedDict
from typing_extensions import NotRequired
from app.guest360_constructs import (
    security_group,
    interface_vpc_endpoint,
    route53_private_hosted_zone,
    route53_domain_record_types,
    route53_resolver_endpoint,
)
from app.guest360_constructs.construct_360 import Construct360
from app.infrastructure.workstream_stack import WorkstreamStack

logger = logging.getLogger(__name__)


class SnowflakeNetworkingMain(TypedDict):
    construct_name: str
    enabled: bool
    private_hosted_zone: route53_private_hosted_zone.PrivateHostedZoneProps
    security_group: security_group.SecurityGroupProps
    snowflake_urls: list[route53_domain_record_types.CnameRecordProps]
    vpc_endpoint: interface_vpc_endpoint.InterfaceVPCEndpointProps
    resolver: route53_resolver_endpoint.Route53ResolverEndpointProps


class SnowflakeNetworkingSetup(TypedDict):
    feature_flag_enabled: bool
    accounts: NotRequired[list[SnowflakeNetworkingMain]]


class SnowflakeNetworkingBase(TypedDict):
    networking: SnowflakeNetworkingSetup


class Guest360SnowflakeNetworking(WorkstreamStack):
    """Infrastructure Stack
    Contains the components for snowflake networking in an account
    """

    def __init__(self, scope: Construct360, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self._environment = self.node.try_get_context("environment")
        self.stack_path = f"{self.project_dir}/" if self.node.try_get_context("stack_path") is not None else ""
        if self.get_feature_flag:
            for network in self.get_config()["networking"]["accounts"]:
                if network["enabled"]:
                    vpc_sg = security_group.Guest360SecurityGroup(
                        scope, f"{construct_id}_vpcsg_{network['construct_name']}", network["security_group"]
                    )
                    vpc_endpoint = interface_vpc_endpoint.Guest360InterfaceVPCEndpoint(
                        scope,
                        f"{construct_id}_vpc_{network['construct_name']}",
                        props=network["vpc_endpoint"] | {"security_groups": [vpc_sg], "reachable_from_dgn": True},
                    )
                    hosted_zone = route53_private_hosted_zone.Guest360PrivateHostedZone(
                        scope, f"{construct_id}_phz_{network['construct_name']}", props=network["private_hosted_zone"]
                    )
                    resolver_sg = security_group.Guest360SecurityGroup(
                        scope,
                        f"{construct_id}_resolversg_{network['construct_name']}",
                        network["resolver"]["security_group"],
                    )
                    route53_resolver_endpoint.Guest360Route53ResolverEndpoint(
                        scope,
                        f"{construct_id}_resolver{network['construct_name']}",
                        props={
                            "name": network["resolver"]["name"],
                            "security_group_ids": [resolver_sg.security_group_id],
                        },
                    )
                    for record in network["snowflake_urls"]:
                        props = (
                            {"domain_name": vpc_endpoint.vpc_endpoint_url}
                            | {"zone": hosted_zone.get_hosted_zone}
                            | {"record_name": record["record_name"]}
                        )
                        route53_domain_record_types.Guest360Route53CnameRecord(
                            scope,
                            hashlib.md5(  # NOSONAR
                                f"{network['private_hosted_zone']['zone_name']}{record['record_name']}".encode("ascii")
                            ).hexdigest(),
                            props=props,
                        )

    def get_config(self):
        with open(
            f"{self.stack_path}app/infrastructure/snowflake/configs/{self._environment}-snowflake.yaml",
            "r",
            encoding="UTF-8",
        ) as file:
            val = yaml.safe_load(file)
            SnowflakeNetworkingBase(val)
            return val

    @property
    def get_feature_flag(self):
        return self.get_config()["networking"]["feature_flag_enabled"]
