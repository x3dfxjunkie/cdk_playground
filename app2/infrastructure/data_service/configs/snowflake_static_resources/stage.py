"""
AWS Snow pipe configuration parameters
"""


def get_configs():
    config = [
        {
            "static_resources_name": "ingestion_raw",
            "external_stage": {
                "external_stage_name": "ingestion_raw_external_stage",
                "s3_bucket": None,
                "s3_bucket_name": "ingestion-raw",
                "s3_bucket_prefix": "snowpipe",
                "iam_principal": "ServiceAccount/WDPR-guest360-datalake-test",  # pragma: allowlist secret
                "snowflake_sqs_arn": "arn:aws:sqs:us-east-1:409709704790:sf-snowpipe-AIDAV6ZEZ6ZLI6KH5NWGZ-7lhGYOpBH4BQ9qCvvatGiw",  # updated to new sf dev account arn
                "s3_bucket_keys": [
                    "4702e56b-9611-4624-983b-13abfe3f3b58",
                    "b17bece6-19f6-412e-895a-8910457c85f0",
                ],
            },
            "notification_integration": {
                "notification_name": "GUEST360_STAGE_SNS_INTEGRATION",
                "iam_user_arn": "arn:aws:iam::409709704790:user/oql90000-s",
                "arn_secret_iam_external_id": "arn:aws:secretsmanager:us-east-1:863175788676:secret:stg-use1-sns-snowflake-secret-3yX5Sh",
            },
        }
    ]
    return config
