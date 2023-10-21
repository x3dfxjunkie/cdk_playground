""" Lambda function of the Custom Resource to populate dynamodb table """
import os
import boto3
import botocore
from aws_lambda_powertools import Logger
from app.src.data_service.api_authorizers.api_authorizers.scope_map import SCOPE_MAP as SCOPE_MAP_DOCUMENT

logger = Logger(service=__name__)

SCOPE_MAP_TABLE_NAME = os.environ["SCOPE_MAP_TABLE_NAME"]
dynamodb_resource = boto3.resource("dynamodb")


def purge_scope_map_table():
    logger.info("Purging Scope Map Table: %s....", SCOPE_MAP_TABLE_NAME)
    try:
        scope_map_table = dynamodb_resource.Table(SCOPE_MAP_TABLE_NAME)
        scope_map_table_items = scope_map_table.scan()
        with scope_map_table.batch_writer() as purge_batch:
            for each in scope_map_table_items["Items"]:
                purge_batch.delete_item(Key={"id": each["id"]})
    except botocore.exceptions.ClientError as error:
        logger.error("An exception occurred while purging the scope map table.")
        logger.error(error)
        return False

    return True


def seed_scope_map_table(
    scope_map_document: dict,
):
    logger.info("Seeding Scope Map Table: %s....", SCOPE_MAP_TABLE_NAME)
    try:
        scope_map_table = dynamodb_resource.Table(SCOPE_MAP_TABLE_NAME)
        for scope_map_entry in scope_map_document["authorization"]:
            response = scope_map_table.put_item(Item=scope_map_entry)
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                logger.info("Item saved in DynamoDB.")
            else:
                logger.error("Could not save put item in DynamoDB.")
    except botocore.exceptions.ClientError as error:
        logger.error("An exception occurred while purging the scope map table.")
        logger.error(error)
        return False

    return True


# pylint: disable=unused-argument
def lambda_handler(
    event: dict,
    context,
):
    response = True
    request_type = event["RequestType"]
    if request_type in ("Create", "Update"):
        purge_scope_map_table()
        response = seed_scope_map_table(
            scope_map_document=SCOPE_MAP_DOCUMENT,
        )
    if request_type == "Delete":
        response = purge_scope_map_table()

    return response
