""" GLUE ETL job for extracting data from an S3 bucket, computing counts, and loading to DynamoDB  """

import json
import sys
from operator import itemgetter
from typing import Dict, List, Tuple

import boto3
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job

# NOTE: these are dependencies that exist in AWS Glue notebook
from awsglue.utils import getResolvedOptions
from botocore.client import ClientError
from pyspark.context import SparkContext
from pyspark.sql import functions as SqlFuncs


class MetricRetrievalError(Exception):
    """Custom exception for handling issues when converting the DynamicFrame and retrieving metric results"""


class MetricWriteError(Exception):
    """Custom exception for handling issues when writing metric to DB"""


class MetricMetaDataParserError(Exception):
    """Custom exception for handling issues when parsing metric metadata payload"""


def get_system_test_metric_metadata(data: str):
    try:
        return json.loads(data)
    except MetricMetaDataParserError as error:
        print(f"Failed to parse matadata metric payload {error}")
        return {}


def spark_aggregate(
    glue_context: GlueContext,
    parent_frame: DynamicFrame,
    groups: Tuple[str],
    aggs: List[Tuple[str, str]],
    transformation_ctx: str,
) -> DynamicFrame:
    aggs_funcs = [getattr(SqlFuncs, func)(column) for column, func in aggs]
    result = (
        parent_frame.toDF().groupBy(*groups).agg(*aggs_funcs)
        if len(groups) > 0
        else parent_frame.toDF().agg(*aggs_funcs)
    )
    return DynamicFrame.fromDF(result, glue_context, transformation_ctx)


def save_to_dynamodb(dynamo_params: Dict[str, str], metric: int) -> None:
    (
        execution_id,
        scenario_name,
        metrics_table_name,
        trace_id,
        test_case_record_name,
        test_case_record_type,
        test_case_type,
        system_test_metric_metadata,
    ) = itemgetter(
        "execution_id",
        "scenario_name",
        "metrics_table_name",
        "trace_id_key_value",
        "test_case_record_name",
        "test_case_record_type",
        "test_case_type",
        "system_test_metric_metadata",
    )(
        dynamo_params
    )
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(metrics_table_name)

    # Note: should we just massage the input args and unpack them into `Item`, rather than unpacking with itemgetter then re-setting them here?
    try:
        table.put_item(
            Item={
                "execution_name": execution_id,
                "scenario_name": scenario_name,
                "trace_id": trace_id,
                "system_test_metric_value": metric,
                "test_case_record_name": test_case_record_name,
                "test_case_record_type": test_case_record_type,
                "test_case_type": test_case_type,
                "system_test_metric_metadata": get_system_test_metric_metadata(system_test_metric_metadata),
            }
        )
    except ClientError as e:
        raise MetricWriteError(f"Failed to write item to {metrics_table_name}", e.response) from e


def retrieve_metric_result_from_df(result_df: DynamicFrame) -> int:
    # TODO should we make this more flexible? Right now we assume we're assuming the schema and the columns we want to retrieve
    try:
        result_data = result_df.toDF().first().asDict()
        return result_data[f"count({args['trace_id_key_name']})"]
    except Exception as e:
        raise MetricRetrievalError("Failed to retrieve metric from dataframe") from e


args = getResolvedOptions(
    sys.argv,
    [
        "JOB_NAME",
        "execution_id",
        "trace_id_key_value",
        "bucket_name",
        "bucket_path",
        "trace_id_key_name",
        "test_case_record_name",
        "test_case_record_type",
        "test_case_type",
        "scenario_name",
        "metrics_table_name",
        "system_test_metric_metadata",
    ],
)

sc = SparkContext.getOrCreate()
glue_context_ = GlueContext(sc)
spark = glue_context_.spark_session
job = Job(glue_context_)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
firehose_s3_data_df = glue_context_.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": [
            f"s3://{args['bucket_name']}/{args['bucket_path']}"
        ],  # args[f"s3://{args['bucket_name']}/{args['bucket_path']}"]
        "recurse": True,
    },
    transformation_ctx="firehose_s3_data_df",
)


if firehose_s3_data_df.count() > 0:
    filtered_by_trace_id_data_df = firehose_s3_data_df.filter(
        f=lambda row: args["trace_id_key_value"] == row[args["trace_id_key_name"]],
        transformation_ctx="filtered_by_trace_id_data_df",
    )
    # Script generated for node Aggregate
    aggregate_result_df = spark_aggregate(
        glue_context_,
        parent_frame=filtered_by_trace_id_data_df,
        groups=(args["trace_id_key_name"],),
        aggs=[(args["trace_id_key_name"], "count")],
        transformation_ctx="aggregate_result_df",
    )

    aggregate_result_df.show()

    metric_result = retrieve_metric_result_from_df(aggregate_result_df)
    save_to_dynamodb(args, metric_result)
else:
    save_to_dynamodb(args, 0)

job.commit()
