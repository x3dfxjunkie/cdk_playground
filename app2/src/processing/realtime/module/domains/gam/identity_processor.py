from app.src.processing.realtime.module.domains.stream_processor import StreamProcessor
from typing import List, Dict, Any
import json
from aws_lambda_powertools import Logger
from opentelemetry import trace, context
from opentelemetry.metrics import get_meter
import concurrent.futures

logging = Logger(service=__name__)
trace.get_tracer_provider()
tracer = trace.get_tracer(__name__)

record_meter = get_meter("records")
record_counter = record_meter.create_counter("record_count")
bad_record_counter = record_meter.create_counter("bad_record_count")

import app.src.data_structures.object_lookup.lookup as lookup
from app.src.data_structures.identity.identity import IdentityNode, IdentityEdge


class IdentityProcessor(StreamProcessor):
    def __init__(self, dynamo_resource, kinesis_client, event_table_name: str, identity_table_name: str, identity_nodes_table_name: str, identity_edges_table_name: str, profile_table_name: str, identity_notification_stream_name: str) -> None:
        with tracer.start_as_current_span("init_identity_processor"):
            super().__init__()
            self.event_table_name = event_table_name
            self.identity_table_name = identity_table_name
            self.identity_nodes_table_name = identity_nodes_table_name
            self.identity_edges_table_name = identity_edges_table_name
            self.profile_table_name = profile_table_name
            self.dynamo_resource = dynamo_resource
            self.kinesis_client = kinesis_client
            self.identity_notification_stream_name = identity_notification_stream_name
            self.lookup = lookup.DynamoDBLookupFactory.get_dynamodb_lookup(dynamo_resource, kinesis_client, profile_table_name=profile_table_name, identity_table_name=identity_table_name, identity_nodes_table_name=identity_nodes_table_name, identity_edges_table_name=identity_edges_table_name, events_table_name=event_table_name, identity_notification_stream_name=identity_notification_stream_name)

    def process_records_batch(self, records: List[Dict[str, Any]]) -> None:
        """
        Process all records in a batch as a list of dictionary elements
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=8, initializer=tracer.start_as_current_span, initargs=("process_records_concurrently",)) as executor:
            ctx = context.get_current()
            executor.map(self.process_record, len(records) * [ctx], records)

    def process_record(self, ctx, record):
        record_counter.add(1)
        try:
            with tracer.start_as_current_span("process_record", ctx):
                action = record["action"].lower()
                if action == "add":
                    self.process_add(record)
                if action == "snapshot":
                    self.process_snapshot(record)
                if action == "merge":
                    self.process_merge(record)
                if action == "remove":
                    self.process_remove(record)
        except Exception as e:
            bad_record_counter.add(1)
            raise e

    def process_add(self, record: Dict):
        """Iterate through all of the new identifiers and add to existing identifiers.

        Args:
            record (Dict): Add record from GAM.
        """
        with tracer.start_as_current_span("process_add"):
            for new_identifier in record["addedGuestIdentifiers"]:
                for existing_identifier in record["resultingGuestIdentifiers"]:
                    # Do not create any self connected nodes.
                    if new_identifier["type"] == existing_identifier["type"] and new_identifier["value"] == existing_identifier["value"]:
                        continue
                    self.lookup.link_identity(existing_identifier["type"], existing_identifier["value"], new_identifier["type"], new_identifier["value"])

    def process_snapshot(self, record: Dict):
        """Iterate through the entire list and connect every identifier from the snapshot to ensure they all have the same atomic_id

        Args:
            record (Dict): Snapshot record from GAM.
        """
        # HACK: We don't need to iterate over the entire inner records, since a connection is bi-directional.
        with tracer.start_as_current_span("process_snapshot"):
            for outer_new_identifier in record["resultingGuestIdentifiers"]:
                for inner_new_identifier in record["resultingGuestIdentifiers"]:
                    # Do not create any self connected nodes.
                    if inner_new_identifier["type"] == outer_new_identifier["type"] and inner_new_identifier["value"] == outer_new_identifier["value"]:
                        continue
                    self.lookup.link_identity(inner_new_identifier["type"], inner_new_identifier["value"], outer_new_identifier["type"], outer_new_identifier["value"])

    def process_merge(self, record: Dict):
        """Combine both identity lists together and link them all together, including decommissioned xids and swids.

        Args:
            record (Dict): Merge record from GAM.
        """
        with tracer.start_as_current_span("process_merge"):
            all_identifiers = record["previousGuestIdentifiers1"] + record["previousGuestIdentifiers2"]
            xids, other_identifiers = _split_xids_from_other_identifiers(all_identifiers)
            # HACK: We don't need to iterate over the entire inner records, since a connection is bi-directional.
            for xid in xids:
                xid_node = self.lookup.get_identity_node(xid["type"], xid["value"])
                if xid_node is None:
                    new_atomic_id = self.lookup._datastore._create_atomic_id(xid["type"], xid["value"], connection_type="explicit")
                    self.lookup._datastore.create_identity_node(domain=xid["type"], identifier=xid["value"], atomic_id=new_atomic_id)
                    xid_node = self.lookup.get_identity_node(xid["type"], xid["value"])
                existing_edges = self.lookup.get_identity_edges(xid_node)
                new_edges = _get_new_edges(existing_edges, other_identifiers + xids)
                for new_edge in new_edges:
                    # Do not create any self connected nodes.
                    if f"{xid['type']}#{xid['value']}" == new_edge:
                        continue
                    #TODO: Refactor to remove string parsing - it's possible for hashes to be used in keys, not a reliable char to split on.
                    self.lookup.link_identity(xid["type"], xid["value"], new_edge.split('#')[0], new_edge.split('#')[1])

    def process_remove(self, record: Dict):
        """Add all of the result identities and then remove any deleted identities from atomic_id.

        Args:
            record (Dict): Remove record from GAM.
        """

        with tracer.start_as_current_span("process_remove"):
            all_identifiers = record["resultingGuestIdentifiers"]
            removed_identifiers = record["removedGuestIdentifiers"]
            # HACK: We don't need to iterate over the entire inner records, since a connection is bi-directional.
            for outer_new_identifier in all_identifiers:
                for inner_new_identifier in all_identifiers:
                    # Do not create any self connected nodes.
                    if inner_new_identifier["type"] == outer_new_identifier["type"] and inner_new_identifier["value"] == outer_new_identifier["value"]:
                        continue
                    self.lookup.link_identity(inner_new_identifier["type"], inner_new_identifier["value"], outer_new_identifier["type"], outer_new_identifier["value"])

            for removed_identifier in removed_identifiers:
                self.lookup.unlink_identity(removed_identifier["type"], removed_identifier["value"])

def _split_xids_from_other_identifiers(identifiers):
    with tracer.start_as_current_span("split_xids_from_other_identifiers"):
        xids = list(filter(lambda identifier: identifier['type'] == 'xid', identifiers))
        identifiers = list(filter(lambda identifier: identifier['type'] != 'xid', identifiers))
        return xids, identifiers

def _get_new_edges(existing_edges, merge_record_edges):
    existing_edges_transformed = {existing_edge.target_node for existing_edge in existing_edges}
    merge_record_edges_transformed = {f"{merge_record_edge['type']}#{merge_record_edge['value']}" for merge_record_edge in merge_record_edges}
    
    new_edges = merge_record_edges_transformed - existing_edges_transformed
    new_edges = list(map(lambda new_edge: new_edge, new_edges))
    return new_edges
