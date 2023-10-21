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
            },
            "notification_integration": {
                "notification_name": "GUEST360_LATEST_SNS_INTEGRATION",
                "iam_user_arn": "arn:aws:iam::409709704790:user/oql90000-s",
                "arn_secret_iam_external_id": "arn:aws:secretsmanager:us-east-1:543276908693:secret:lst-use1-sns-snowflake-secret-PdJGUz",
            },
        }
    ]
    return config
