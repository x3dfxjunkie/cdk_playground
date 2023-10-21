"""
This is a rabbitmq producer for local testing.
This should be sufficient to test changes to the consumer,
though not for producing messages to kinesis
"""
# pylint: disable=W0703
import logging
import time
import random
import json
import uuid

import pika
from pythonjsonlogger import jsonlogger

time.sleep(30)


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


logger = setup_logging()
# Connect to RabbitMQ
while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="rabbitmq",
                virtual_host="my_vhost",
                port=str(5672),
                credentials=pika.PlainCredentials("guest", "guest"),
            )
        )
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue="default_queue")

        # Produce messages
        logger.info("Producing messages")
        n = 0
        while True:
            message = {"Metadata": "Hello", "body": str(uuid.uuid4())}
            channel.basic_publish(exchange="", routing_key="default_queue", body=json.dumps(message))
            n += 1
            if n % 1000 == 0:
                logger.info("Produced 1000 messages")
            time.sleep(0.01)
    except Exception as e:
        logger.error("Failure in rabbit producer", exc_info=True)
        time.sleep(5)
    else:
        time.sleep(5)
