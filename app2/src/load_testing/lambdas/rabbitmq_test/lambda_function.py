"""
RabbitMQ tester

WARNING:
This Lambda is only for testing purposes
It is not expected to use it in production

"""
import json
import logging
import time
import uuid
import os

import pika
from pythonjsonlogger import jsonlogger


def publish_message():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("RABBITMQ_SERVER", "localhost"),
                virtual_host="my_vhost",
                port=str(5672),
                credentials=pika.PlainCredentials("guest", "guest"),
            )
        )
        channel = connection.channel()
        channel.queue_declare(queue="default_queue")
        message = {"Metadata": "Hello", "body": str(uuid.uuid4())}
        channel.basic_publish(exchange="", routing_key="default_queue", body=json.dumps(message))
        connection.close()
        return True
    except Exception as e:
        time.sleep(5)
        raise e


def setup_logging() -> logging.Logger:
    """Sets up a json logger for rabbitmq consumer

    Returns:
        json_logger: python logger to log json - easily compatable with cloudwatch.
    """
    log_handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    new_logger = logging.getLogger()
    new_logger.addHandler(log_handler)
    new_logger.setLevel(logging.INFO)
    return new_logger


def lambda_handler(event, context):  # NOSONAR avoid not used parameters warning
    """
    RabbitMQ tester
    """
    try:
        result = publish_message()
        if result:
            logger.info("Message Published Successfully")
        return result
    except Exception as e:
        logger.error(f"Failure in rabbit producer: {e}", exc_info=True)
        return False


logger = setup_logging()
