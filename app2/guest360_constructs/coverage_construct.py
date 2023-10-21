from constructs import Construct

from aws_cdk import aws_s3
from cdk_nag import NagSuppressions


class CoverageConstruct(Construct):
    """
    Dummy construct to testing code coverage.
    """
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id)
        logging_bucket = aws_s3.Bucket(
            self,
            "coverage-test-bucket",
            bucket_name="coverage-test-bucket",
        )
        NagSuppressions.add_resource_suppressions(
            logging_bucket,
            [
                {
                    "id": "AwsSolutions-S1",
                    "reason": "This is a dummy construct/bucket for testing code coverage so won't have log bucket.",
                }
            ],
        )
