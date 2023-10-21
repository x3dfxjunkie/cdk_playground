"""
Defines base construct and defaults for route53 private hosted zone
"""
import aws_cdk, re
from typing import TypedDict
from typing_extensions import NotRequired
from app.guest360_constructs.construct_360 import Construct360
from aws_cdk import Duration
from strongtyping.strong_typing import match_class_typing
from aws_cdk.aws_route53 import RecordTarget, CnameRecord, ARecord, PrivateHostedZone

ip_address_validator = re.compile(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$")


@match_class_typing
class CnameRecordProps(TypedDict):
    """
    Important Note for CName Records
    <dns name> -> <other dns name> but the record keeps the original name
    This allows for the following situation
    foo.snowflakecomputing.com => vpcexxxx.amazonaws.com to be received by the vpcendpoint as foo.snowflakecomputing.com for TLS cert purposes

    :prop domain_name -  The domain name of the target that this record should point to.
    :prop zone -  The hosted zone in which to define the new record

    :prop record_name - The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify “acme”. You can also specify the fully qualified domain name which terminates with a “.”. For example, “acme.example.com.”. Default: zone root
    :prop delete_existing - Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids “manual” actions to delete existing record sets. .. epigraph:: N.B.: this feature is dangerous, use with caution! It can only be used safely when deleteExisting is set to true as soon as the resource is added to the stack. Changing an existing Record Set’s deleteExisting property from false -> true after deployment will delete the record! Default: false
    :prop ttl -  The resource record cache time to live (TTL). Default: Duration.minutes(30)
    """

    domain_name: str
    zone: PrivateHostedZone

    record_name: NotRequired[str]
    delete_existing: NotRequired[bool]
    ttl: NotRequired[Duration]


class Guest360Route53CnameRecord(Construct360):
    """
    A CName record points to another DNS name.  This is useful whne you want to keep the origin domain name even though the intermediate hops
    may use other DNS names.
    """

    def __init__(self, scope: Construct360, construct_id: str, props: CnameRecordProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        CnameRecordProps(props)
        if ip_address_validator.match(props["domain_name"]) is not None:
            raise ValueError("CNAME records require a FQDN not an ip address")
        self.props_default = {"ttl": Duration.minutes(30)}
        self.props_merged = self.props_default | props
        self._domain_record = CnameRecord(self, construct_id, **self.props_merged)


@match_class_typing
class Guest360ARecordProps(TypedDict):
    """
    Important Note for A Records
    <dns name> -> <IP Address> (but allows lookups of load balancers and cloudfront distribution though aliases)
    This allows for the following situation
    foo.snowflakecomputing.com => 1.1.1.1

    :prop target -  The target, needs to implement the target class
    :prop zone -  The hosted zone in which to define the new record

    :prop record_name - The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify “acme”. You can also specify the fully qualified domain name which terminates with a “.”. For example, “acme.example.com.”. Default: zone root
    :prop delete_existing - Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids “manual” actions to delete existing record sets. .. epigraph:: N.B.: this feature is dangerous, use with caution! It can only be used safely when deleteExisting is set to true as soon as the resource is added to the stack. Changing an existing Record Set’s deleteExisting property from false -> true after deployment will delete the record! Default: false
    :prop ttl -  The resource record cache time to live (TTL). Default: Duration.minutes(30)
    """

    target: RecordTarget
    zone: PrivateHostedZone

    record_name: NotRequired[str]
    delete_existing: NotRequired[bool]
    ttl: NotRequired[Duration]


class Guest360Route53ARecord(Construct360):
    """
    A CName record points to another DNS name.  This is useful whne you want to keep the origin domain name even though the intermediate hops
    may use other DNS names.
    """

    def __init__(self, scope: Construct360, construct_id: str, props: Guest360ARecordProps, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        Guest360ARecordProps(props)
        self.props_default = {"ttl": Duration.minutes(30)}
        self.props_merged = self.props_default | props
        self._domain_record = ARecord(self, construct_id, **self.props_merged)
