"""Module to handle reconstructing identity graphs from dynamodb stream output to any point in time.

Raises:
    GraphImportException: Errors when attempting to import graph from dynamodb

Returns:
    graphframes.GraphFrame: A graph representing the state of the identity graph at a given point in time.
"""
import pyspark
import datetime
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, desc, from_json, col
import graphframes


def import_identity_graph_from_s3(
    spark_context: pyspark.sql.context, base_path: str, snapshot_datetime: datetime.datetime = datetime.datetime.now()
) -> graphframes.GraphFrame:
    try:
        raw_edges_dataframe = spark_context.read.json(base_path + "/edges")
    except pyspark.sql.utils.AnalysisException as e:
        raise GraphImportException("Node directory not found") from e

    try:
        raw_nodes_dataframe = spark_context.read.json(base_path + "/nodes")
    except pyspark.sql.utils.AnalysisException as e:
        raise GraphImportException("Edge directory not found.") from e

    graph = construct_graph_from_raw_dataframes(
        spark_context, raw_nodes_dataframe, raw_edges_dataframe, snapshot_datetime
    )
    return graph


def construct_graph_from_raw_dataframes(
    spark: pyspark.sql.context,
    nodes_df: pyspark.sql.DataFrame,
    edges_df: pyspark.sql.DataFrame,
    snapshot_datetime: datetime.datetime,
) -> graphframes.GraphFrame:
    nodes = dynamo_to_nodes(spark, nodes_df, snapshot_datetime)
    edges = dynamo_to_edges(spark, edges_df, snapshot_datetime)
    graph = graphframes.GraphFrame(nodes, edges)
    return graph


def dynamo_to_nodes(
    spark, raw_json_df: pyspark.sql.DataFrame, snapshot_datetime: datetime.datetime = datetime.datetime.now()
) -> pyspark.sql.DataFrame:
    dynamo_nodes_df = get_snapshot_dynamodb_rows(
        raw_json_df, keys=["dynamodb.Keys.node_id.S"], snapshot_datetime=snapshot_datetime
    )
    string_deserialized_df = string_json_deserialization(spark, dynamo_nodes_df, "identity_node")
    return_df = string_deserialized_df.select(
        string_deserialized_df.dynamodb.Keys.node_id.S.alias("id"), string_deserialized_df.attributes
    )
    return return_df


def dynamo_to_edges(
    spark, raw_json_df: pyspark.sql.DataFrame, snapshot_datetime: datetime.datetime = datetime.datetime.now()
) -> pyspark.sql.DataFrame:
    dynamo_edges_df = get_snapshot_dynamodb_rows(
        raw_json_df,
        keys=["dynamodb.Keys.source_node.S", "dynamodb.Keys.target_node.S"],
        snapshot_datetime=snapshot_datetime,
    )
    string_deserialized_df = string_json_deserialization(spark, dynamo_edges_df, "identity_edge")
    return_df = string_deserialized_df.select(
        string_deserialized_df.dynamodb.Keys.source_node.S.alias("src"),
        string_deserialized_df.dynamodb.Keys.target_node.S.alias("dst"),
        string_deserialized_df.attributes,
    )
    return return_df


def get_snapshot_dynamodb_rows(
    raw_json_df: pyspark.sql.DataFrame, keys: list, snapshot_datetime: datetime.datetime
) -> pyspark.sql.DataFrame:
    snapshot_timestamp = int(snapshot_datetime.timestamp())
    window_def = Window.partitionBy(*keys).orderBy(desc("dynamodb.ApproximateCreationDateTime"))
    ordered_df = raw_json_df.filter(raw_json_df.dynamodb.ApproximateCreationDateTime <= snapshot_timestamp).withColumn(
        "row_num", row_number().over(window_def)
    )
    latest_row_df = ordered_df.filter(ordered_df.row_num == 1).filter(ordered_df.eventName != "REMOVE")
    return latest_row_df


def string_json_deserialization(
    spark: pyspark.sql.context, df: pyspark.sql.DataFrame, column_name: str
) -> pyspark.sql.DataFrame:
    object_schema = spark.read.json(df.rdd.map(lambda row: row["dynamodb"]["NewImage"][column_name]["S"])).schema
    column_name_fully_qualified = f"dynamodb.NewImage.{column_name}.S"
    string_deserialized_df = df.withColumn("attributes", from_json(col(column_name_fully_qualified), object_schema))
    return string_deserialized_df


class GraphImportException(Exception):
    pass


class DynamoDBSchemaError(Exception):
    pass
