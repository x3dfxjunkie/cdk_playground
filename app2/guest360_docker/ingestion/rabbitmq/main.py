"""
Script for asynchronously reading from rabbitmq and publishing to kinesis
Documentation for this code can be found here: docs/workstreams/sourcing/rabbitmq_consumer.md
"""
# pylint: disable=W0703
import asyncio
import json
import logging
import os
import time
from typing import Any, Dict, AsyncGenerator
import uuid
import aio_pika
from functools import partial
import aioboto3
from pythonjsonlogger import jsonlogger
from contextlib import asynccontextmanager
from botocore.exceptions import ClientError
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type, after_log, before_sleep_log


LOCAL = os.environ.get("LOCAL", default=False)
MAX_RETRIES = int(os.environ.get("MAX_RETRY_ATTEMPT", "3"))


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


class TaskTracker:
    """Class to track which asyncio process message tasks are being worked on currently.
    The purpose of tracking them is to make sure errors are tracked and escalated,
    this has no effect on whether or not asyncio is actually working on them."""

    def __init__(self):
        """Initialization method for TaskTracker class"""
        self.tasks = set()

    def add(self, task: asyncio.Task):
        """Add a task to the tracked set.

        Args:
            task (asyncio.Task): _description_
        """
        self.tasks.add(task)

    def cancel(self):
        """Cancel all currently processing tasks in the event of an exception"""
        for task in self.tasks:
            if not task.cancelled():
                task.cancel()
        self.tasks = set()

    def has_tasks(self):
        """Determines if we have any tasks"""
        return len(self.tasks) > 0

    async def check_tasks(self):
        if self.has_tasks():
            done, pending = await asyncio.wait(self.tasks, timeout=30)
            self.tasks = pending
            logger.info("Successfully processed %s messages", len(done))
            for task in done:
                exception = task.exception()
                if exception is not None:
                    self.cancel()
                    raise exception


async def get_secret(secret_name: str, aiosession: aioboto3.Session) -> Dict[str, Any]:
    """Function to get secret from AWS Secrets Managers
    Args:
        secret_name (str): Name of secret in secrets manager
        aiosession (aioboto3.Session): aioboto3 session
    Returns:
        Dict[str, Any]: _description_
    """
    async with aiosession.client("secretsmanager") as sm_client:
        response = await sm_client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])


@asynccontextmanager
async def rabbitmq_connect(
    rabbit_config: Dict[str, str]
) -> AsyncGenerator[aio_pika.abc.AbstractRobustConnection, None]:
    """Function to connect to rabbitmq
    Args:
        rabbit_usr (str): Rabbitmq username
        rabbit_pwd (str): rabbitmq password
        hostname (str): rabbitmq hostname
        port (str): rabbitmq port
        virtual_host (str): rabbitmq virtual host
    Returns:
        aio_pika.Connection: rabbitmq connection
    """
    # TLS Port
    use_ssl = os.environ.get("USE_SSL", default="true")
    use_ssl = True if use_ssl.lower() == "true" else False
    connection = await aio_pika.connect_robust(
        host=rabbit_config["hostname"],
        port=int(rabbit_config["port"]),
        login=rabbit_config["rabbit_usr"],
        password=rabbit_config["rabbit_pwd"],
        virtualhost=rabbit_config["virtual_host"],
        ssl=use_ssl,
    )
    logger.info("Successfully connected rabbitmq host.", exc_info=True)

    try:
        yield connection
    finally:
        await connection.close()


async def s3_upload_failed_message(bucket_name: str, key: str, data: bytes, aiosession: aioboto3.Session) -> None:
    """Function to upload failed messages to AWS s3
    Args:
        bucket_name (str): Name of AWS S3 Bucket
        key (str): Key for AWS S3 Bucket
        data (bytes): Data to upload to S3
        aiosession (aioboto3.Session): aioboto3 session

    """
    try:
        async with aiosession.client("s3") as s3_client:
            # Since we are running s3 boto client, which by default is synchronous, we must instead add it manually to the running event loop.
            # This event loop is created when async.run() is called on main, and the loop is maintained by asyncio.
            await s3_client.put_object(**{"Bucket": bucket_name, "Key": key, "Body": data})
            logger.info("Failed message uploaded to S3", extra={"s3_key": key})
    except Exception:
        logger.error("Failed to upload message to S3", exc_info=True, extra={"s3_key": key})
        raise


@retry(
    wait=wait_exponential(multiplier=1, min=2, max=60),
    stop=stop_after_attempt(5),
    retry=retry_if_exception_type(ClientError),
    reraise=True,
)
async def publish_to_kinesis(
    message: aio_pika.IncomingMessage,
    aiosession: aioboto3.Session,
    kinesis_stream_name: str,
) -> None:
    """Asynchronous function to publish message to kinesis. This function has retry logic to retry common Kinesis exceptions
        that may be successful on subsequent attempts. It implements exponential backoff.

    Args:
        message (aio_pika.IncomingMessage): Rabbitmq message to publish to kinesis
        aiosession (aioboto3.Session): aioboto3 session
        kinesis_stream_name (str): Stream name to publish to

    Raises:
        Exception: Raises an exception if ClientError is not retriable.
    """
    try:
        async with aiosession.client("kinesis") as kinesis_client:
            await kinesis_client.put_record(
                StreamName=kinesis_stream_name, Data=message.body, PartitionKey=uuid.uuid4().hex
            )
    except ClientError as e:
        if e.response["Error"]["Code"] in (
            "InternalFailureException",
            "ProvisionedThroughputExceededException",
            "LimitExceededException",
            "KMSThrottlingException",
        ):
            raise
        else:
            logger.error("Failed to publish message to kinesis due to %s", e.response["Error"]["Code"])
            raise Exception(f"Error: Failed to publish message to kinesis due to {e.response['Error']['Code']}") from e


async def process_message(
    message: aio_pika.IncomingMessage,
    aiosession: aioboto3.Session,
    kinesis_stream_name: str,
    s3_bucket: str,
) -> None:
    """Function to process a rabbitmq message and publish it to Kinesis
    Args:
        message (aio_pika.IncomingMessage): Incoming RabbitMQ Message to Publish
        aiosession (aioboto3.Session): aioboto3 session
        kinesis_stream_name (str): Stream name to publish to
        s3_bucket (str): S3 Bucket to upload failed objects to
    """
    async with message.process(ignore_processed=True):
        try:
            await publish_to_kinesis(message, aiosession, kinesis_stream_name)
            await message.ack()
            logger.debug("Message processed", extra={"message_body": message.body.decode("utf-8")})

        except Exception:
            logger.error("Failed to process message", exc_info=True)

            # Upload the failed message to the specified S3 bucket
            await message.reject()
            key = f"failed_messages/{message.message_id}"
            await s3_upload_failed_message(s3_bucket, key, message.body, aiosession)
            raise


async def process_message_wrapper(
    message: aio_pika.IncomingMessage,
    aiosession: Any,
    kinesis_stream_name: str,
    s3_bucket: str,
    tasks: TaskTracker,
) -> None:
    """Function that serves as a middleman between consume and process message for the purpose of adding a new, trackable asyncio task
        so that we can track Exceptions raised by the tasks.

    Args:
        message (aio_pika.IncomingMessage): Rabbitmq message to process
        aiosession (aioboto3.Session): aioboto3 session
        kinesis_stream_name (str): Name of the kinesis stream to publish to
        s3_bucket (str): name of the s3 bucket to upload to upon failure
        tasks (TaskTracker): TaskTracker instance to track tasks for the purpose of raising exceptions
    """
    task = asyncio.create_task(process_message(message, aiosession, kinesis_stream_name, s3_bucket))
    tasks.add(task)


@retry(
    wait=wait_exponential(multiplier=1, min=2, max=60),
    stop=stop_after_attempt(MAX_RETRIES),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    after=after_log(logger, logging.WARNING),
    retry=retry_if_exception_type(BaseException),
    reraise=True,
)
async def consume(
    rabbit_config: Dict[str, str],
    prefetch_count: int,
    rabbit_queue_name: str,
    aiosession: Any,
    kinesis_stream_name: str,
    s3_bucket: str,
    tasks: TaskTracker,
) -> None:
    async with rabbitmq_connect(rabbit_config) as rabbitmq_connection:
        async with rabbitmq_connection.channel(channel_number=1) as channel:
            await channel.set_qos(prefetch_count=prefetch_count, timeout=240)  # Make configuration driven
            queue = await channel.get_queue(rabbit_queue_name)
            process_message_func = partial(
                process_message_wrapper,
                aiosession=aiosession,
                kinesis_stream_name=kinesis_stream_name,
                s3_bucket=s3_bucket,
                tasks=tasks,
            )
            await queue.consume(process_message_func)
            logger.info("Listening for messages...")
            while True:
                await asyncio.sleep(30)
                await tasks.check_tasks()


async def orchestrate() -> None:
    """Main function which controls asynchronous execution.
    To use, run asyncio.run(orchestrate())
    """
    # Environment variables with defaults
    prefetch_count = int(os.environ.get("PREFETCH_COUNT", "100"))
    # Required Environment Variables / No Defaults
    try:
        secret_name = os.environ["RABBITMQ_SECRET_PATH"]
        rabbitmq_queue_name = os.environ["RABBITMQ_QUEUE"]
        kinesis_stream_name = os.environ["KINESIS_STREAM"]
        hostname = os.environ["RABBITMQ_HOST"]
        port = os.environ["RABBITMQ_PORT"]
        virtual_host = os.environ["RABBITMQ_VHOST"]
        s3_bucket = os.environ["FAILED_MSG_BUCKET_NAME"]
    except KeyError:
        logger.error("Missing environment variables")
        raise

    try:
        if not LOCAL:
            aiosession = aioboto3.Session()
            rabbitmq_credentials = await get_secret(secret_name, aiosession)
            rabbit_usr = rabbitmq_credentials["RABBIT_USR"]
            rabbit_pwd = rabbitmq_credentials["RABBIT_PWD"]
        else:
            aiosession = None
            rabbit_usr = os.environ.get("RABBIT_USR")
            rabbit_pwd = os.environ.get("RABBIT_PWD")

    except KeyError:
        logger.error("Missing rabbitmq credentials in AWS Secrets Manager.")
        raise

    rabbit_config = {
        "rabbit_usr": rabbit_usr,
        "rabbit_pwd": rabbit_pwd,
        "hostname": hostname,
        "virtual_host": virtual_host,
        "port": port,
    }
    # create tasks before consume so we keep the same reference between retries.
    tasks = TaskTracker()
    await consume(
        rabbit_config=rabbit_config,
        prefetch_count=prefetch_count,
        rabbit_queue_name=rabbitmq_queue_name,
        aiosession=aiosession,
        kinesis_stream_name=kinesis_stream_name,
        s3_bucket=s3_bucket,
        tasks=tasks,
    )
    logger.info("Exiting the consume coroutine")


if __name__ == "__main__":
    if LOCAL:
        # wait some time for rabbit infrastructure to be set up
        time.sleep(35)
    asyncio.run(orchestrate())
