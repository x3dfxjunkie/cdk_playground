import jsii
from aws_cdk import CfnResource, IAspect, Tag
from constructs import IConstruct


@jsii.implements(IAspect)
class Guest360PathTagger:
    """CDK Aspect to add cdk path as a tag to each resource.

    This module will visit each resource and tag it with the path in the CDK application.
    """

    def visit(self, node: IConstruct):

        ENVIRONMENT = node.node.try_get_context("environment")
        STACK_NAME = node.node.try_get_context("stack_name")

        # Apply tags to help with troubleshooting and identification
        if isinstance(node, CfnResource):
            """
            Unless the current node is part of the pipeline stack
            shorten the path by removing the first two levels, plus
            trailing "Resource".
            """
            if node.stack.stack_name != f"{STACK_NAME.lower()}-{ENVIRONMENT.lower()}":
                short_path_list = node.node.path.split("/")
                short_path_list.pop()
                short_path_list = short_path_list[2:]
                short_path = "/".join(short_path_list)
            else:
                short_path = node.node.path
            Tag("aws-cdk-path", short_path[:255]).visit(node)
