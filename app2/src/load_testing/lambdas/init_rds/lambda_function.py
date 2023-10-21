"""
 init RDS lambda function
"""
import json
import logging
import os

import boto3
import pymysql

ENDPOINT = os.getenv("ENDPOINT")
PORT = int(os.getenv("PORT"))
USER = os.getenv("USER")
REGION = os.getenv("REGION")
DBNAME = os.getenv("DBNAME")
SECRET_NAME = os.getenv("SECRET_NAME")

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# pylint: disable=W0613, W0718
def lambda_handler(event, context):
    admin_pass = get_secret_value("password")
    try:
        conn = pymysql.connect(
            host=ENDPOINT,
            user=USER,
            passwd=admin_pass,
            port=PORT,
            database=DBNAME,
        )
        cur = conn.cursor()
        cur.execute("""SELECT now()""")
        query_results = cur.fetchall()
        return query_results
    except pymysql.Error as error:  # pylint
        logger.error("Database connection failed due to %s", str(error))
        raise error


def get_secret_value(key):
    # Create a Secrets Manager client
    session = boto3.Session()
    client = session.client(service_name="secretsmanager", region_name=REGION)
    secret_value_response = client.get_secret_value(SecretId=SECRET_NAME)
    return json.loads(secret_value_response["SecretString"])[key]
