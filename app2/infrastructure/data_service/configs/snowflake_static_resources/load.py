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
                "snowflake_sqs_arn": "arn:aws:sqs:us-east-1:409709704790:sf-snowpipe-AIDAV6ZEZ6ZLI6KH5NWGZ-7lhGYOpBH4BQ9qCvvatGiw",
                "s3_bucket_keys": [
                    "94aae997-6e4e-46f9-82a5-c5f0b60a336e",
                    "8fd61660-efe7-480c-9c0a-65aa41141588",
                ],
            },
            "notification_integration": {
                "notification_name": "GUEST360_LOAD_SNS_INTEGRATION",
                "iam_user_arn": "arn:aws:iam::409709704790:user/oql90000-s",
                "arn_secret_iam_external_id": "arn:aws:secretsmanager:us-east-1:863175788676:secret:lod-use1-sns-snowflake-secret-MkUtDj",
            },
        }
    ]
    return config
