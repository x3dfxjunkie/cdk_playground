import datetime as dt
import json
import logging
import os
import urllib
from itertools import zip_longest

import boto3
import shredder_utils
import smart_open as so
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
aws_batch = boto3.client('batch')


def handler(event, context):

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:

        for record in event["Records"]:

            # logger.info(record)
            nw = str(dt.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))

            # variables
            batch_job_region = aws_batch.meta.region_name
            s3_bucket_landing = os.environ["S3_BUCKET_NAME_LANDING"]
            stream_name = os.environ['KINESIS_STREAM_NAME']
            stack_name = os.environ['STACK_NAME']
            max_file_size = os.environ['MAX_FILE_SIZE']

            key = urllib.parse.unquote(record["s3"]["object"]["key"])

            container_overrides = {
                "environment": [{
                    "name": "S3_BUCKET_NAME_LANDING",
                    "value": s3_bucket_landing
                }, {
                    "name": "S3_OBJECT_KEY",
                    "value": key
                }, {
                    "name": "REGION",
                    "value": batch_job_region
                }, {
                    "name": "KINESIS_STREAM_NAME",
                    "value": stream_name
                }]
            }

            head_response = s3.head_object(
                Bucket=s3_bucket_landing,
                Key=key
            )

            file_size = head_response['ResponseMetadata']['HTTPHeaders']['content-length']

            if int(file_size) > int(max_file_size):
                # Currently passing this if file exceeds 250mb as this initial construct is only utilizing lambdas, batch/ECS approach will come in a future iteration
                logger.info(
                    f'{key} file exceeds 250mb, skipping lambda processing')
                pass
                # batch_job_name = f"batch-job".lower().replace(
                #     " ", "").replace(".", "")
                # response = aws_batch.submit_job(jobName=batch_job_name,
                #                                 jobQueue=batch_job_queue,
                #                                 jobDefinition=batch_job_definition,
                #                                 containerOverrides=container_overrides)
            else:

                delim = '.'
                s3_seperated = key.rsplit(delim, 1)
                file_type = s3_seperated[1]

                s3_path_landing = f"s3://{s3_bucket_landing}/{key}"
                path_like_object = so.open(s3_path_landing, 'rb')
                iterations = shredder_utils.shredder(
                    file_type, path_like_object, key, stream_name)

            logger.info(
                f'Lambda Shredder {iterations} Iterations Completed...')
            return None

    except Exception as e:
        logger.error(e)
        raise e
