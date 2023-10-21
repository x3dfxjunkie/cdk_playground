"""This Function Transforms a Kinesis Firehose Record To the Desired Output

Returns:
    KinesisFirehoseResponseRecord
"""
from app.src.processing.firehose_transformer.lambda_function.models.kinesis_firehose import (
    KinesisFirehoseRecord,
    KinesisFirehoseResponseRecord,
)
from app.src.processing.firehose_transformer.lambda_function.utils.newline_appender import append_new_line
from app.src.processing.firehose_transformer.lambda_function.utils.partition_extractor import extract_partition


def transformer(kinesis_firehose_event: KinesisFirehoseRecord) -> KinesisFirehoseResponseRecord:
    return KinesisFirehoseResponseRecord(
        record_id=kinesis_firehose_event.record_id,
        approximate_arrival_timestamp=kinesis_firehose_event.approximate_arrival_timestamp,
        data=append_new_line(kinesis_firehose_event.data),
        result="Ok",
        metadata={"partitionKeys": extract_partition(kinesis_firehose_event)},
    )
