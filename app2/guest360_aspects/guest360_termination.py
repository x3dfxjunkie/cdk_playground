import jsii
from aws_cdk import Annotations, CfnResource, IAspect, RemovalPolicy, Stack, Tag, CfnDeletionPolicy
from constructs import IConstruct

LOG_MAX_RETION = 90


@jsii.implements(IAspect)
class Guest360Termination:
    def visit(self, node: IConstruct):
        ENVIRONMENT = node.node.try_get_context("environment").lower()

        if isinstance(node, CfnResource):
            # Apply a destroy policy to everything, except in prod
            # if ENVIRONMENT != "prod":  # Keeping this code in because we'll turn it back on sometime near 10/31
            node.apply_removal_policy(RemovalPolicy.DESTROY)

        if isinstance(node, CfnResource) and node.cfn_resource_type == "AWS::AppConfig::HostedConfigurationVersion":
            # Persist hosted configuration versions throughout deployment updates
            if ENVIRONMENT == "prod":
                node.cfn_options.update_replace_policy = CfnDeletionPolicy.RETAIN

        if isinstance(node, CfnResource) and node.cfn_resource_type == "AWS::S3::Bucket":
            # Destroy all objects in buckets, except in prod
            # if ENVIRONMENT != "prod":  # Keeping this code in because we'll turn it back on sometime near 10/31
            Tag("aws-cdk:auto-delete-objects", "true").visit(node)

        if isinstance(node, CfnResource):
            # If termination_protection isn't defined, or isn't set correctly (enabled for prod, disabled for all others)
            if (Stack.of(node).termination_protection is None) or (
                Stack.of(node).termination_protection != (ENVIRONMENT == "prod")
            ):
                Annotations.of(Stack.of(node)).add_error(
                    f"Stack termination is not set correctly on: {Stack.of(node).stack_name}"
                )

        if isinstance(node, CfnResource) and node.cfn_resource_type == "AWS::Logs::LogGroup":
            if "retentionInDays" in node._cfn_properties:
                if node.retention_in_days > LOG_MAX_RETION:
                    node.retention_in_days = LOG_MAX_RETION
            if "retentionInDays" not in node._cfn_properties:
                node.retention_in_days = LOG_MAX_RETION
