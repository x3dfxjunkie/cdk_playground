"""
Defines base construct and defaults for Guest360's ECR Repositories
"""
from typing import TypedDict, List
from typing_extensions import NotRequired

import aws_cdk
from constructs import Construct
from aws_cdk import aws_ecr, Duration
from aws_cdk.aws_ecr import Repository
from strongtyping.strong_typing import match_class_typing


class ImageReplicationProps(TypedDict):
    destination_account_id: str
    destination_region: str
    source_environments: List[str]


@match_class_typing
class RepoProps(TypedDict):
    """
    Defines optional values to set when creating a new ECR Repo
    """

    dummy_field: None  # TypedDict can't handle case of only NotRequired fields
    auto_delete_images: NotRequired[bool]
    encryption: NotRequired[str]
    encryption_key: NotRequired[str]
    image_scan_on_push: NotRequired[bool]
    image_tag_mutability: NotRequired[aws_ecr.TagMutability]
    lifecycle_registry_id: NotRequired[str]
    lifecycle_rules: NotRequired[List[aws_ecr.LifecycleRule]]
    removal_policy: NotRequired[aws_cdk.RemovalPolicy]
    repository_name: NotRequired[str]
    image_replication_props: NotRequired[List[ImageReplicationProps]]


class Guest360ECRRepository(Repository):
    """
    Define a ECR Repo with Guest360 defaults.
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        props: dict = None,
        **kwargs,
    ):
        """
        :param scope: -
        :param id: -
        :prop encryption: The kind of server-side encryption to apply to this repository. If you choose KMS, you can specify a KMS key via ``encryptionKey``. If encryptionKey is not specified, an AWS managed KMS key is used. Default: - ``KMS`` if ``encryptionKey`` is specified, or ``AES256`` otherwise.
        :prop encryption_key: External KMS key to use for repository encryption. The 'encryption' property must be either not specified or set to "KMS". An error will be emitted if encryption is set to "AES256". Default: - If encryption is set to ``KMS`` and this property is undefined, an AWS managed KMS key is used.
        :prop image_scan_on_push: Enable the scan on push when creating the repository. Guest360 Default: true
        :prop image_tag_mutability: The tag mutability setting for the repository. If this prop is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten, except for prod environment. Default: TagMutability.MUTABLE
        :prop lifecycle_registry_id: The AWS account ID associated with the registry that contains the repository. Default: The default registry is assumed.
        :prop lifecycle_rules: Life cycle rules to apply to this registry. Default: No life cycle rules
        :prop removal_policy: Determine what happens to the repository when the resource/stack is deleted. Default: RemovalPolicy.Retain
        :prop repository_name: Name for this repository. Default: Automatically generated name.
        :prop image_replication_props: Set of props that when defined will copy an image to a new repo. Default: None
        """
        # Check that props matches proper input structure
        if props is None:
            props = {"dummy_field": None}  # Dummy field to make TypeDict work
        RepoProps(props)
        props.pop("dummy_field", None)

        replication_list = props.pop("image_replication_props", None)
        self.replication_rules = []

        # Get context
        environment = scope.node.try_get_context("environment")
        is_static_env = scope.node.try_get_context("is_static_env")

        # Static Analysis is always on
        props["image_scan_on_push"] = True

        # Lifecycle rules
        user_rules = props.get("lifecycle_rules") if props.get("lifecycle_rules") else []
        props["lifecycle_rules"] = [
            # Default 1
            aws_ecr.LifecycleRule(
                description="Expire untagged images older than 24 hours",
                rule_priority=1,
                tag_status=aws_ecr.TagStatus.UNTAGGED,
                max_image_age=Duration.days(1),
            ),
            # Default 2
            aws_ecr.LifecycleRule(
                description="Keep last 3 images",
                rule_priority=2,
                tag_status=aws_ecr.TagStatus.TAGGED,
                tag_prefix_list=["v"],
                max_image_count=3,
            ),
            # User provided
            *user_rules,
        ]

        # Tag mutability
        if is_static_env:
            # Then this is a static environment
            props["image_tag_mutability"] = aws_ecr.TagMutability.MUTABLE
        else:
            # Then this is an ephemeral environment
            props["image_tag_mutability"] = props.get("image_tag_mutability")  # If None, CDK defaults to MUTABLE

        # Removal Policy
        if is_static_env:
            props["removal_policy"] = aws_cdk.RemovalPolicy.RETAIN
        else:
            props["removal_policy"] = aws_cdk.RemovalPolicy.DESTROY
            props["auto_delete_images"] = True

        super().__init__(
            scope=scope,
            id=construct_id,
            **props,
            **kwargs,
        )

        # Special, Repo-specific replication rules
        # These rules are 1:1 with a single repo, as dictated by repository filter field below
        if (
            replication_list  # Special configuration to replicate
            and environment in ["latest", "stage"]  # Approved replication environments
            and is_static_env  # Guard against ephemeral environments
        ):
            destinations = []
            filters = []
            for replication_config in replication_list:
                if environment not in replication_config["source_environments"]:
                    # Controls which environments to replicate from
                    # Example: you may not want a stage repo replicating externally, but latest is fine
                    continue

                # Target Account/Region
                destinations.append(
                    aws_ecr.CfnReplicationConfiguration.ReplicationDestinationProperty(
                        region=replication_config["destination_region"],
                        registry_id=replication_config["destination_account_id"],
                    )
                )
                # Filter must match repo name, to make rule 1-to-1 with special replication prop
                filters.append(
                    aws_ecr.CfnReplicationConfiguration.RepositoryFilterProperty(
                        filter=props["repository_name"],
                        filter_type="PREFIX_MATCH",
                    )
                )

            if destinations:
                self.replication_rules = [
                    aws_ecr.CfnReplicationConfiguration.ReplicationRuleProperty(
                        destinations=destinations, repository_filters=filters
                    )
                ]
