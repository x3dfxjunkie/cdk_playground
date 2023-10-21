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
                "iam_principal": "ServiceAccount/WDPR-guest360-datalake-prod",  # pragma: allowlist secret
                "snowflake_sqs_arn": "arn:aws:sqs:us-east-1:497075275374:sf-snowpipe-AIDAXHO76YZXIDMWSMBPH-RHPpbhJpyg74v-ZZdwrrrQ",
                "s3_bucket_keys": [
                    "f7a337c8-4316-4c8c-9baf-9c251538315d",
                    "109ffa91-9f70-4419-9149-c975224bb452",
                ],
            },
            "notification_integration": {
                "notification_name": "GUEST360_PROD_SNS_INTEGRATION",
                "iam_user_arn": "arn:aws:iam::497075275374:user/v74a0000-s",
                "arn_secret_iam_external_id": "arn:aws:secretsmanager:us-east-1:920268603720:secret:prd-use1-sns-snowflake-secret-Zw2cuG",
            },
        }
    ]
    return config
