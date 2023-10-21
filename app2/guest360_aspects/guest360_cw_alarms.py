import jsii
from aws_cdk import CfnResource, IAspect
from constructs import IConstruct


@jsii.implements(IAspect)
class Guest360CWAlarms:
    """CDK Aspect to standardize the names of CW alarms.

    This module will visit each resource and rename it with the path in the CDK application.
    """

    def visit(self, node: IConstruct):
        if isinstance(node, CfnResource) and node.cfn_resource_type == "AWS::CloudWatch::Alarm":
            if len(node.alarm_name) > 255:
                """Shorten some CloudWatch alarm names

                Some alarm names are over the 255 character limit, and need to be shortened.

                Example long name:
                    cw-Guest360Pipeline/latest-guest360-pipeline-us-east-1/Guest360Stack/ingestion/gam/lst-use1-guest360-lst-use1-guest360-lst-use1-guest360-lst-use1-guest360-gam-kinesis-GAM-MAGICBAND-GUEST360/lst-use1-guest360-lst-use1-guest360-lst-use1-guest360-lst-use1-guest360-lst-use1-guest360-gam-kinesis-GAM-MAGICBAND-GUEST360-KinesisStream/Resource-Iterator-Age-Max-Warning

                This will:
                    split the name on '/'                                 node.alarm_name.split("/")
                    create a slice starting at len() -2                   [len(node.alarm_name.split("/")) - 2]
                    end the slice at the last field                       node.alarm_name.split("/")[-1]
                    join the slice, and limit output to 255 characters    join([])[:255]

                Example short_name:
                    lst-use1-guest360-lst-use1-guest360-lst-use1-guest360-lst-use1-guest360-lst-use1-guest360-gam-kinesis-GAM-MAGICBAND-GUEST360-KinesisStream/Resource-Iterator-Age-Max-Warning
                """
                short_name = "/".join([node.alarm_name.split("/")[len(node.alarm_name.split("/")) - 2], node.alarm_name.split("/")[-1]])[:255]
                node._cfn_properties["alarmName"] = short_name
                node.alarm_name = short_name
