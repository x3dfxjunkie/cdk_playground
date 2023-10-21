"""
Construct file for Glue JOb
"""

import os
from typing import TypedDict

from app.guest360_constructs.construct_360 import Construct360
from app.guest360_constructs.iam_role import Guest360IamRole
from app.guest360_constructs.kms_key import Guest360KMSKey
from app.src.reliability.utils import GlueJobName, S3BucketName, StackName
from aws_cdk import aws_glue, aws_iam, aws_s3
from strongtyping.strong_typing import match_class_typing
from typing_extensions import NotRequired


@match_class_typing
class GlueProps(TypedDict):
    """
    Guest360 Glue Job properties
    """

    job_name: str
    bucket: str
    prefix: str
    artifact_name: str
    kms_key: NotRequired[Guest360KMSKey]


class Guest360Glue(Construct360):
    """
    Guest360 Glue Job Construct
    """

    @property
    def iam_role(self):
        return self.glue_job_role

    def __init__(self, scope: Construct360, construct_id: str, props: GlueProps, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Props check
        GlueProps(props)

        prefix = self.node.try_get_context("prefix")

        # Define Guest360 IAM Role
        iam_props = {"assumed_by": aws_iam.ServicePrincipal("glue.amazonaws.com"), "description": "Role for Glue job"}

        self.glue_job_role = Guest360IamRole(
            self,
            f"glue-job-role-{construct_id}",
            props=iam_props,
        )

        # Grant artifact bucket read access
        bucket_name = S3BucketName(prefix, props["bucket"]).name()
        bucket = aws_s3.Bucket.from_bucket_name(
            self, StackName(prefix=prefix, base_name="ArtifactBucket").name(), bucket_name
        )
        resource_s3_prefix = f'{props["prefix"]}*' if props["prefix"].endswith("/") else f'{props["prefix"]}/*'
        bucket.grant_read(self.glue_job_role.role, resource_s3_prefix)

        # Grant permissions to kms key
        if props.get("kms_key"):
            key = props["kms_key"]._key

            statements = aws_iam.PolicyStatement(
                actions=["kms:Encrypt", "kms:Decrypt", "kms:GenerateDataKey*", "kms:ReEncrypt*"],
                effect=aws_iam.Effect.ALLOW,
                resources=[key.key_arn],
            )

            iam_policy_to_role = aws_iam.Policy(self, f"{construct_id}-policy-kms_to_role", statements=[statements])
            self.glue_job_role.role.attach_inline_policy(iam_policy_to_role)

            kms_policy = aws_iam.PolicyStatement(
                actions=["kms:Encrypt", "kms:Decrypt", "kms:GenerateDataKey*", "kms:ReEncrypt*"],
                effect=aws_iam.Effect.ALLOW,
                principals=[self.glue_job_role.role],
                resources=["*"],
            )
            key.add_to_resource_policy(kms_policy)

        # Glue Job definition
        glue_job_command = aws_glue.CfnJob.JobCommandProperty(
            name="glueetl",
            script_location=f's3://{os.path.join(bucket_name, props["prefix"], props["artifact_name"])}',
            python_version="3",
        )

        self.glue_job = aws_glue.CfnJob(
            self,
            f"glue-job-{construct_id}",
            command=glue_job_command,
            name=GlueJobName(prefix, props["job_name"]).name(),
            role=self.glue_job_role.role.role_name,
            glue_version="4.0",
        )
