"""RabbitMQ target"""

import json
import logging
import time
import pika
from typing import Any, Dict, List
from app.src.load_testing.app.targets.target import Target

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class RabbitMQTarget(Target):
    def __init__(self, host, port, vhost, username, password):
        self.host = host
        self.port = port
        self.vhost = vhost
        self.username = username
        self.password = password
        self.connection = self.connect()
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="default_queue")
        self._target_type = "Rabbit MQ"

    @property
    def target_type(self) -> str:
        return self._target_type

    def connect(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host,
                virtual_host=self.vhost,
                port=self.port,
                credentials=pika.PlainCredentials(self.username, self.password),
            )
        )
        return connection

    def send_data(self, data: Dict[str, Any]) -> None:
        try:
            self.channel.basic_publish(exchange="", routing_key="default_queue", body=json.dumps(data))
            logger.info(f"Message Published Successfully: {data}")

        except Exception as e:
            logger.error(f"Failure in rabbit producer: {e}", exc_info=True)
            time.sleep(5)

    def close(self):
        if self.connection:
            self.connection.close()

    def send_batch(self, batch: List[Dict[str, Any]]) -> None:
        raise NotImplementedError

    def __del__(self):
        self.close()
