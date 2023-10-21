import app.src.processing.realtime.module.domains.gam.identity_processor as identity_processor
import snowflake.connector
import json
import boto3
import os
import sys

from opentelemetry import trace
from opentelemetry.metrics import get_meter
from aws_lambda_powertools import Logger

logging = Logger(service=__name__)
trace.get_tracer_provider()
tracer = trace.get_tracer(__name__)

batch_meter = get_meter("batches")
batch_counter = batch_meter.create_counter("batch_count")

records = 0

def main(snowflake_user_name, snowflake_role_name):
        
        with tracer.start_as_current_span("historical_load_main"):
            endpoint_url = os.environ.get("ENDPOINT_URL")
            event_table_name = os.environ.get("EXPERIENCE_EVENT_TABLE_NAME")
            identity_table_name = os.environ.get("IDENTITY_TABLE_NAME")
            identity_nodes_table_name = os.environ.get("IDENTITY_NODES_TABLE_NAME")
            identity_edges_table_name = os.environ.get("IDENTITY_EDGES_TABLE_NAME")
            profile_table_name = os.environ.get("PROFILE_TABLENAME")
            identity_notification_stream_name = os.environ.get("IDENTITY_NOTIFICATION_STREAM_NAME")
            snowflake_warehouse_name = os.environ.get("SNOWFLAKE_WAREHOUSE_NAME")
            snowflake_db_name = os.environ.get("SNOWFLAKE_DB_NAME")
            snowflake_schema_name = os.environ.get("SNOWFLAKE_SCHEMA_NAME")
            snowflake_table_name = os.environ.get("SNOWFLAKE_TABLE_NAME")
            source_ll_kinesis_stream_name = os.environ.get("RAW_LL_STREAM_NAME", "guest360-ea-test")
            source_gam_kinesis_stream_name = os.environ.get("RAW_GAM_STREAM_NAME", "gam")
            aws_profile_name = os.environ.get("AWS_PROFILE_NAME")
            session = boto3.Session(profile_name=aws_profile_name)
            dynamodb_resource = session.resource("dynamodb", endpoint_url=endpoint_url)
            kinesis_client = session.client("kinesis", endpoint_url=endpoint_url)
            processor = identity_processor.IdentityProcessor(dynamo_resource=dynamodb_resource,
                                                                kinesis_client=kinesis_client,
                                                                event_table_name=event_table_name,
                                                                identity_table_name=identity_table_name,
                                                                identity_nodes_table_name=identity_nodes_table_name,
                                                                identity_edges_table_name=identity_edges_table_name,
                                                                profile_table_name=profile_table_name,
                                                                identity_notification_stream_name=identity_notification_stream_name)
            loader = HistoricalGAMLoader(processor=processor, snowflake_warehouse_name=snowflake_warehouse_name, snowflake_user_name=snowflake_user_name, snowflake_role_name=snowflake_role_name, snowflake_db_name=snowflake_db_name, snowflake_schema_name=snowflake_schema_name, snowflake_table_name=snowflake_table_name)
            loader.work()


class HistoricalGAMLoader:

    def __init__(self, processor, snowflake_warehouse_name, snowflake_user_name, snowflake_role_name, snowflake_db_name, snowflake_schema_name, snowflake_table_name): 
   
        self.processor = processor
        self.snowflake_warehouse_name = snowflake_warehouse_name
        self.snowflake_user_name = snowflake_user_name
        self.snowflake_role_name = snowflake_role_name
        self.snowflake_db_name = snowflake_db_name
        self.snowflake_schema_name = snowflake_schema_name
        self.snowflake_table_name = snowflake_table_name

    def fetch_historical_data_records(self):
        dlr_gam_historical_records_query = f"select * from {self.snowflake_table_name}"
        with tracer.start_as_current_span("get_batches_from_snowflake"):
            con = snowflake.connector.connect(
                user=self.snowflake_user_name,
                role=self.snowflake_role_name,
                account='disneyparksandresorts.us-east-1.privatelink',
                authenticator='externalbrowser',
                warehouse=self.snowflake_warehouse_name,
                database=self.snowflake_db_name,
                schema=self.snowflake_schema_name,
            )
            cur = con.cursor()
            cur.execute(dlr_gam_historical_records_query)
            batches = cur.get_result_batches()
            return batches


    def get_dict(self, record):
        global records
        json_record = record[0]
        dict_record = json.loads(json_record)
        records = records + 1
        return dict_record


    def process_batch_into_list(self, batch):
        return list(map(self.get_dict, batch))
    
    def work(self):
         batches = self.fetch_historical_data_records()
         for batch in batches:
            with tracer.start_as_current_span("process_batch_into_list"):
                list_of_dicts = self.process_batch_into_list(batch)
            with tracer.start_as_current_span("process_records_batch"):
                self.processor.process_records_batch(list_of_dicts)
                batch_counter.add(1)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        snowflake_user_name = sys.argv[1]
        snowflake_role_name = sys.argv[2]
    else:
        snowflake_user_name = os.environ.get("SNOWFLAKE_USERNAME")
        snowflake_role_name = os.environ.get("SNOWFLAKE_ROLE_NAME")
    main(snowflake_user_name, snowflake_role_name)
