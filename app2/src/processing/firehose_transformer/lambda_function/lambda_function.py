""" Lambda Handler for Kinesis Firehose Transformer
    Used to obtain partitions and new line
"""

from app.src.processing.firehose_transformer.lambda_function.models.kinesis_firehose import (
    KinesisFirehoseEvent,
    KinesisFirehoseResponse,
)
from app.src.processing.firehose_transformer.lambda_function.utils.transformer import transformer


def lambda_handler(event, _):
    firehose_event: KinesisFirehoseEvent = KinesisFirehoseEvent.parse_obj(event)
    firehose_response: KinesisFirehoseResponse = KinesisFirehoseResponse(
        records=list(map(transformer, firehose_event.records))
    )
    return firehose_response.dict(by_alias=True)
