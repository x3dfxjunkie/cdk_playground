import datetime as dt
from typing import Any, Dict, List

from aws_lambda_powertools import Logger
from opentelemetry import trace
from opentelemetry.metrics import get_meter
from pydantic import parse_obj_as

import app.src.data_structures.object_lookup.lookup as lookup
from app.src.data_structures.data_contracts.source.ea_dlr.v0.ea_dlr_lightning_lane_source_data_contract import (
    EADLRLightningLaneModel,
)
from app.src.data_structures.data_contracts.source.ea_wdw.v0.ea_wdw_lightning_lane_source_data_contract import (
    EAWDWLightningLaneModel,
)
from app.src.data_structures.events.attraction_ridden_event import AttractionRideHistory
from app.src.data_structures.events.lightning_lane_event import (
    Experience,
    Facility,
    LightningLaneEvent,
    LocationHierarchy,
)
from app.src.data_structures.object_lookup.metadata_lookup import AttractionMetadataLookup
from app.src.data_structures.profiles.profile import Profile
from app.src.processing.realtime.module.domains.stream_processor import StreamProcessor

logging = Logger(service=__name__)
trace.get_tracer_provider()
tracer = trace.get_tracer(__name__)

ll_event_meter = get_meter("processing.events.lightninglane")
ll_profile_meter = get_meter("processing.persistent.profile")
ll_event_records = ll_event_meter.create_counter("records")
ll_profile_records = ll_profile_meter.create_counter("records")


class LightningLaneEventGenerator(StreamProcessor):
    """
    Processor that processes lightning lane data from source stream and generates lightning lane data to an event table.
    """

    def __init__(
        self,
        dynamo_resource,
        kinesis_client,
        event_table_name: str,
        identity_table_name: str,
        identity_nodes_table_name: str,
        identity_edges_table_name: str,
        profile_table_name: str,
        identity_notification_stream_name: str,
        metadata_lookup: AttractionMetadataLookup = None,
        attraction: str = "DLR",
    ) -> None:
        with tracer.start_as_current_span("init LightningLaneGenerator"):
            super().__init__()
            self.event_table_name = event_table_name
            self.identity_table_name = identity_table_name
            self.identity_nodes_table_name = identity_nodes_table_name
            self.identity_edges_table_name = identity_edges_table_name
            self.profile_table_name = profile_table_name
            self.dynamo_resource = dynamo_resource
            self.kinesis_client = (kinesis_client,)
            self.identity_notification_stream_name = identity_notification_stream_name
            self.lookup = lookup.DynamoDBLookupFactory.get_dynamodb_lookup(
                dynamo_resource,
                kinesis_client,
                profile_table_name=profile_table_name,
                identity_table_name=identity_table_name,
                identity_nodes_table_name=identity_nodes_table_name,
                identity_edges_table_name=identity_edges_table_name,
                events_table_name=event_table_name,
                identity_notification_stream_name=identity_notification_stream_name,
            )
            self.metadata_lookup = metadata_lookup or AttractionMetadataLookup()
            self.attraction = attraction

    def process_records_batch(self, records: List[Dict[str, Any]]) -> None:
        """
        Process all records in a batch as a list of dictionary elements
        """
        dynamodb = self.dynamo_resource.Table(self.event_table_name)

        lightning_lane_events = []
        for record in records:
            try:
                with tracer.start_as_current_span("process_record"):
                    ll_event_records.add(1, attributes={"status": "started_processing"})
                    lightning_lane_events.append(self.process_record(record))
                    ll_event_records.add(1, attributes={"status": "completed"})
            except Exception as e:
                ll_event_records.add(1, attributes={"status": "errors"})
                logging.warning("Unable to process record: %s \nException: %s", record, e)

        for lightning_lane_event in lightning_lane_events:
            with tracer.start_as_current_span("check_for_duplicates_and_send"):
                if not self.event_functional_duplicate(lightning_lane_event):
                    self.update_profile(lightning_lane_event)
                    ll_event = {}
                    ll_event["atomic_id#event_name"] = lightning_lane_event.atomic_id + "#lightning_lane"
                    event_time_key = int(lightning_lane_event.last_modified.timestamp() * 1000)
                    ll_event["event_time"] = event_time_key
                    ll_event["class_name"] = lightning_lane_event.class_name
                    ll_event["event"] = lightning_lane_event.to_json()
                    dynamodb.put_item(Item=ll_event)
                else:
                    ll_event_records.add(1, attributes={"status": "duplicate"})

    def event_functional_duplicate(self, current_ll_event) -> bool:
        """Check the current event against a prior event of the same type

        Args:
            current_ll_event (LightningLaneEvent): The current LL event being evaluated

        Returns:
            bool: True if the current event is a functional duplicate of a prior event.
        """
        previous_event = self.get_previous_event(current_ll_event)
        if previous_event is None:
            return False
        if previous_event.event_status == current_ll_event.event_status:
            if (
                current_ll_event.event_status == "REDEEMED"
                and current_ll_event.event_type == "NONINVENTORY"
                and previous_event.remaining_count > current_ll_event.remaining_count
            ):
                return False
            return True
        return False

    def get_previous_event(self, current_ll_event):
        """Returns the previous event of the same type and ID as the current event.

        Args:
            current_ll_event (LightningLaneEvent): The current even being evaluated

        Returns:
            LightningLaneEvent: The previous LightningLaneEvent of the same type and ID as the current.
        """
        previous_events = self.lookup.get_events_from_profile(
            current_ll_event.atomic_id, dt.datetime(1970, 1, 1, 0, 10), dt.datetime(3000, 1, 1, 0, 0)
        )
        if previous_events is None:
            return None
        if len(previous_events) == 0:
            return None
        # Iterate through the past events and look for the same event key. The first encountered event is the latest of that key.
        for previous_event in previous_events:
            if previous_event.transaction_id == current_ll_event.transaction_id:
                return previous_event
        return None

    def process_record(self, record):
        """Processes a single record into a LightningLaneEvent object

        Args:
            record (Dict): The dictionary representation of a raw event.

        Returns:
            LightningLaneEvent: The curated LightningLaneEvent
        """
        ea_ll_record = None
        if self.attraction == "DLR":
            EADLRLightningLaneModel.update_forward_refs()
            ea_ll_record = parse_obj_as(EADLRLightningLaneModel, record)
        elif self.attraction == "WDW":
            EAWDWLightningLaneModel.update_forward_refs()
            ea_ll_record = parse_obj_as(EAWDWLightningLaneModel, record)

        if ea_ll_record is None:
            raise Exception("Invalid attraction.  Only WDW and DLR accepted.")

        ea_link_id = ea_ll_record.item.entitlement.guest_id
        event_type = ea_ll_record.item.entitlement.type
        transaction_id = ea_ll_record.item.event_id

        # So, order is important here. The first case is evaluated first, if it's none, it will try to find the experience in the list.
        # If the first case is none and there is also no experience_list, then an exception will be raised (None not subscriptable)
        experience_id = (
            ea_ll_record.item.entitlement.experience_id
            or ea_ll_record.item.entitlement.experience_list[0].experience_id
        )
        location_id = (
            ea_ll_record.item.entitlement.location_id
            or ea_ll_record.item.entitlement.experience_list[0].location_list[0].location_id
        )
        park_id = ea_ll_record.item.entitlement.park_id or ea_ll_record.item.entitlement.experience_list[0].park_id

        remaining_count = ea_ll_record.item.entitlement.remaining_count
        guest_id = ea_link_id
        event_status = ea_ll_record.item.entitlement.status

        # Various timestamps
        event_time = dt.datetime.now()
        created_time = ea_ll_record.item.entitlement.created_date
        last_modified = ea_ll_record.item.entitlement.updated_date
        experience_start = ea_ll_record.item.entitlement.enttl_start_date
        experience_end = ea_ll_record.item.entitlement.enttl_end_date

        # Lookup atomic_id
        atomic_id = self.lookup.fetch_or_create_atomic_id("ealinkid", ea_link_id)

        # Lookup experience
        experience = self.get_experience(experience_id, location_id, park_id)

        # Determine Curated Status
        curated_status, curated_confidence_score, curated_confidence_label = self.get_curated_status_and_confidence(
            event_status
        )

        lightning_lane_event = LightningLaneEvent(
            "lightning_lane",
            event_type,
            atomic_id,
            guest_id,
            transaction_id,
            experience,
            remaining_count,
            event_time,
            created_time,
            last_modified,
            experience_start,
            experience_end,
            event_status,
            curated_status,
            curated_confidence_score,
            curated_confidence_label,
        )
        return lightning_lane_event

    @tracer.start_as_current_span("update_profile")
    def update_profile(self, lightning_lane_event: LightningLaneEvent):
        profile = self.lookup.profile_lookup(
            atomic_id=lightning_lane_event.atomic_id,
        )

        if profile is None:
            profile = Profile(lightning_lane_event.atomic_id, [], [])

        attraction_history = profile.attraction_ride_histories
        is_new_attraction_for_guest = True
        if lightning_lane_event.event_status == "REDEEMED":
            ll_ride_count = 1
        else:
            ll_ride_count = 0
        for attraction in attraction_history:
            if attraction.attraction_id == lightning_lane_event.experience.experience_id:
                is_new_attraction_for_guest = False
                attraction.attraction_ride_count += ll_ride_count
                break

        if is_new_attraction_for_guest:
            attraction_ride_history_record = AttractionRideHistory(
                attraction_id=lightning_lane_event.experience.experience_id,
                attraction_name=lightning_lane_event.experience.experience_name,
                attraction_ride_count=ll_ride_count,
            )
            profile.attraction_ride_histories.append(attraction_ride_history_record)
            ll_profile_records.add(
                1,
                attributes={
                    "status": "attraction_ride_history_calc",
                    "ride": attraction_ride_history_record.attraction_name,
                },
            )

        # Persist updated profile:
        self.save_profile(profile)

    @tracer.start_as_current_span("save_profile")
    def save_profile(self, profile: Profile):
        dynamodb = self.dynamo_resource.Table(self.profile_table_name)
        dynamo_profile = {}
        dynamo_profile["atomic_id"] = profile.atomic_id
        dynamo_profile["profile"] = profile.to_json()
        dynamodb.put_item(Item=dynamo_profile)
        ll_profile_records.add(1, attributes={"status": "profile_updated"})

    def get_location_hierarchy(self, location_id):
        """Return a LocationHierachy object given a location id

        Args:
            location_id (str): The location id

        Returns:
            LocationHierachy: The location hierarchy mapping to the location id.
        """
        facility = Facility("Facility Id N/A", "Facility Name N/A")
        location_hierarchy = LocationHierarchy(facility, facility, facility, facility, facility)
        return location_hierarchy

    def get_curated_status_and_confidence(self, event_status):
        """Given an event status, return the curated status, confidence score, and confidence label

        Args:
            event_status (str): Raw event status

        Returns:
            curated_status, confidence_score, confidence_label: Curated status and confidence data.
        """
        if event_status == "BOOKED" or event_status == "INQUEUE":
            curated_status = "Booked"
            curated_confidence_score = 100
            curated_confidence_label = "High"
        elif event_status == "CANCELLED":
            curated_status = "Not Experienced"
            curated_confidence_score = 100
            curated_confidence_label = "High"
        elif event_status == "REDEEMED":
            curated_status = "Experienced"
            curated_confidence_score = 90
            curated_confidence_label = "High"
        else:
            curated_status = "Invalid"
            curated_confidence_score = 0
            curated_confidence_label = "Zero"

        return curated_status, curated_confidence_score, curated_confidence_label

    def get_experience(self, experience_id, location_id, park_id):
        """Given an experience_id and a location_id, get the experience object.

        Args:
            experience_id (str): The experience id from raw data
            location_id (str): The location id from raw data

        Returns:
            Experience: Object mapping to the experience
        """
        # Lookup facility
        location_hierarchy = self.get_location_hierarchy(location_id)
        # Lookup experience name
        attraction_name = self.metadata_lookup.get_attraction_by_id(
            attraction_id=experience_id,
            facility_id=park_id,
        ).get("name")

        if attraction_name is None:
            attraction_name = "N/A"

        experience = Experience(
            experience_id,
            "Experience Category N/A",
            attraction_name,
            location_id,
            "Location Name N/A",
            location_hierarchy=location_hierarchy,
        )
        return experience
