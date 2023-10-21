import json
import uuid
import copy
from datetime import datetime, timedelta


class LightningLaneScenarios:
    @staticmethod
    def all_ll_events() -> list():
        events = [
            json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01),
            json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_02),
            json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_03),
        ]
        return events

    @staticmethod
    def duplicate_ll_event() -> list():
        events = [
            json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01),
            json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01),
        ]
        return events

    @staticmethod
    def ll_events_no_status_change(status="BOOKED") -> list():
        event_1 = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01)
        event_1["item"]["entitlement"]["updatedDate"] = "2022-10-12T12:27:27.199502532"
        event_1["item"]["entitlement"]["status"] = status

        event_2 = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01)
        event_2["item"]["entitlement"]["updatedDate"] = "2022-10-12T12:28:27.199502532"
        event_2["item"]["entitlement"]["status"] = status

        events = [event_1, event_2]
        return events

    @staticmethod
    def ll_events_noninventory_redemptions() -> list():
        event_1 = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_NONINVENTORY_REDEMPTION)
        event_1["item"]["entitlement"]["updatedDate"] = "2022-10-12T12:27:27.199502532"
        event_1["item"]["entitlement"]["remainingCount"] = 2

        event_2 = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_NONINVENTORY_REDEMPTION)
        event_2["item"]["entitlement"]["updatedDate"] = "2022-10-12T12:28:27.199502532"
        event_2["item"]["entitlement"]["remainingCount"] = 1

        events = [event_1, event_2]
        return events

    @staticmethod
    def ll_cancelled() -> list():
        events = []
        base_event = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01)
        base_event["item"]["entitlement"]["status"] = "CANCELLED"
        events.append(base_event)
        return events

    @staticmethod
    def ll_redeemed() -> list():
        events = []
        base_event = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01)
        base_event["item"]["entitlement"]["status"] = "REDEEMED"
        events.append(base_event)
        return events

    @staticmethod
    def ll_bad() -> list():
        events = []
        base_event = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_01)
        base_event["item"]["entitlement"]["status"] = "BAD"
        events.append(base_event)
        return events

    @staticmethod
    def ll_events_bulk_different_event_ids(number_of_events: int, ll_status: str = "BOOKED") -> list():
        base_event = json.loads(LightningLaneRawEvents.LIGHTNING_LANE_RAW_EVENT_NONINVENTORY_REDEMPTION)
        events = []
        for num in range(0, number_of_events):
            new_event = copy.deepcopy(base_event)
            new_event_key = str(uuid.uuid1())
            updatedDate = datetime.strptime(
                new_event["item"]["entitlement"]["updatedDate"][:-4], "%Y-%m-%dT%H:%M:%S.%f"
            )
            updatedDate = updatedDate + timedelta(minutes=num)
            new_event["key"] = new_event_key
            new_event["item"]["entitlement"]["status"] = ll_status
            new_event["item"]["eventID"] = new_event_key
            new_event["item"]["entitlement"]["updatedDate"] = (
                datetime.strftime(updatedDate, "%Y-%m-%dT%H:%M:%S.%f") + "000"
            )
            events.append(new_event)
        return events


class LightningLaneRawEvents:
    LIGHTNING_LANE_RAW_EVENT_01 = """{
        "eventType": "IA_SYNC",
        "key": "f0be3034472a5bf4ed0741e3ed0ff40f",
        "item": {
            "eventID": "f0be3034472a5bf4ed0741e3ed0ff40f",
            "eventName": "INSERT",
            "entitlement": {
                "bookingGuestId": "AAAADA6M4LV52JPUBGU33JT77A",
                "operationalDate": "2022-10-12",
                "reason": "DAS",
                "createUserId": "HARIS014",
                "windowOverride": false,
                "entitlementKey": "NONINVENTORY-ae675891-94ac-4756-91da-6e7344922a26",
                "dasParentEntitlementId": "NONINVENTORY_AAAADA6M4LV52JPUBGU33JT77A_ae675891-94ac-4756-91da-6e7344922a26",
                "updatedDate": "2022-10-12T12:28:27.199502532",
                "type": "NONINVENTORY",
                "enttlEndDate": "2022-10-13T02:00:00",
                "remainingCount": 1,
                "operational_date-product_type-experience_id-guest_range": "1665558000-DAS-353305-A-L",
                "operational_date-park_id": "1665558000-330339",
                "guestId": "AAAADA6M4LV52JPUBGU33JT77A",
                "productType": "DAS",
                "TTL_TIME": 1668247200,
                "experienceList": [
                    {
                        "experienceId": "353305",
                        "locationList": [
                            {
                                "locationId": "353305",
                                "locationType": "Attraction"
                            }
                        ],
                        "experienceType": "Attraction",
                        "usesAllowed": 1,
                        "remainingCount": 1,
                        "parkId": "330339"
                    }
                ],
                "enttlStartDate": "2022-10-12T12:33:00",
                "updateUserId": "HARIS014",
                "operational_date-park_id-product_type-status": "1665558000-330339-DAS-BOOKED",
                "dasPrimaryIndicator": true,
                "usesAllowed": 1,
                "bookingId": "74e188bc-a1e3-49be-992c-19cb30ef67f9",
                "createdDate": "2022-10-12T12:28:27.199501888",
                "activities": [
                    {
                        "activityReason": "DAS",
                        "activityStatus": "BOOKED",
                        "correlationId": "7c0e6ec0-47fb-4f8a-9eb2-1f63894b263f",
                        "activityDateTime": "2022-10-12T12:28:27.199480942",
                        "activityUser": "HARIS014"
                    }
                ],
                "enttlId": "ae675891-94ac-4756-91da-6e7344922a26",
                "status": "BOOKED"
            }
        },
        "correlationId": "7c0e6ec0-47fb-4f8a-9eb2-1f63894b263f"
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )

    LIGHTNING_LANE_RAW_EVENT_02 = """
    {
        "eventType": "IA_SYNC",
        "key": "2f91f3aebee0d7a93c6e862b0c7b36c7",
        "item": {
            "eventID": "2f91f3aebee0d7a93c6e862b0c7b36c7",
            "eventName": "INSERT",
            "entitlement": {
                "bookingGuestId": "AAAADA6NZABAQJNQ2RBEMOCMLQ",
                "reason": "DVC",
                "createUserId": "XTQ165",
                "windowOverride": false,
                "entitlementKey": "NONINVENTORY-6a703d10-327b-4683-80a1-d2faa8406598",
                "updatedDate": "2022-10-12T12:59:40.659776684",
                "type": "NONINVENTORY",
                "enttlEndDate": "2022-10-13T05:00:00",
                "remainingCount": 1,
                "operational_date-product_type-experience_id-guest_range": "1665558000-NON-353303-M-Z",
                "operational_date-park_id": "1665558000-336894",
                "guestId": "AAAADA6NZABAQJNQ2RBEMOCMLQ",
                "productType": "NON",
                "TTL_TIME": 1668258000,
                "experienceList": [
                    {
                        "experienceId": "353303",
                        "locationList": [
                            {
                                "locationId": "353303",
                                "locationType": "Attraction"
                            }
                        ],
                        "experienceType": "Attraction",
                        "usesAllowed": 1,
                        "remainingCount": 1,
                        "parkId": "336894"
                    }
                ],
                "enttlStartDate": "2022-10-12T06:00:00",
                "updateUserId": "XTQ165",
                "operational_date-park_id-product_type-status": "1665558000-336894-NON-BOOKED",
                "dasPrimaryIndicator": false,
                "usesAllowed": 1,
                "bookingId": "7a7f96ac-7082-48cc-b01a-b6f45ca9da7e",
                "createdDate": "2022-10-12T12:59:40.659776533",
                "activities": [
                    {
                        "activityReason": "DVC",
                        "activityStatus": "BOOKED",
                        "correlationId": "dd7e4cff-3c47-4570-a5cc-3277cc6105ed",
                        "activityDateTime": "2022-10-12T12:59:40.659772715",
                        "activityUser": "XTQ165"
                    }
                ],
                "enttlId": "6a703d10-327b-4683-80a1-d2faa8406598",
                "status": "BOOKED"
            }
        },
        "correlationId": "dd7e4cff-3c47-4570-a5cc-3277cc6105ed"
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )

    LIGHTNING_LANE_RAW_EVENT_03 = """
    {
        "eventType": "IA_SYNC",
        "key": "c452b87f27e0771f00afbe5783250a81",
        "item": {
            "eventID": "c452b87f27e0771f00afbe5783250a81",
            "eventName": "INSERT",
            "entitlement": {
                "bookingGuestId": "AAAADBAFXT3DSKPKQEPMO2UAOU",
                "operationalDate": "2022-10-23",
                "reason": "PUR",
                "createUserId": "SYSTEM",
                "orderId": "1fa345f6-3d34-51a5-bb28-a8aa959c90e0",
                "windowOverride": false,
                "entitlementKey": "INVENTORY-2022-10-23-68d5218d-655a-4646-ae9a-aced303da1e6",
                "locationType": "Attraction",
                "experienceType": "Attraction",
                "updatedDate": "2022-10-23T09:49:24.625511769",
                "type": "INVENTORY",
                "enttlEndDate": "2022-10-23T10:50:00",
                "parkId": "330339",
                "remainingCount": 1,
                "experienceId": "19193461",
                "locationId": "19193461",
                "operational_date-park_id": "1666508400-330339",
                "guestId": "AAAADBAFXT3DUKPPBVYMYNGW5E",
                "productType": "EXT",
                "TTL_TIME": 1698083400,
                "enttlStartDate": "2022-10-23T09:50:00",
                "productId": "DL19193461EXARA12811",
                "updateUserId": "SYSTEM",
                "operational_date-park_id-product_type-status": "1666508400-330339-EXT-BOOKED",
                "sectorName": "EXTRA",
                "usesAllowed": 1,
                "bookingId": "ae662b32-c9c8-4efe-a4cc-c093ddec92cf",
                "itemId": "1f655871-00b7-5fef-af93-4c71eeec30b1",
                "createdDate": "2022-10-23T09:49:24.625511568",
                "productContentId": "DSEPV1_DSETV1",
                "passengerIdType": "ticket-visual-id",
                "activities": [
                    {
                        "activityReason": "PUR",
                        "activityStatus": "BOOKED",
                        "correlationId": "ee41a2e6-608d-4a1d-ae41-0e4d8629a619",
                        "activityDateTime": "2022-10-23T09:49:24.625502063",
                        "activityUser": "SYSTEM"
                    }
                ],
                "inventoryId": "EXTRA-19193461-19193461-20221023-1666543800-1666547400",
                "offerId": "AAAADBAFXT3DSKPKQEPMO2UAOU_75eb0302-cae6-4f31-bae6-e5a3b081dcf8_EXTRA-19193461-19193461-20221023_1666543800-1666547400",
                "passengerId": "705900556047562783592",
                "enttlId": "68d5218d-655a-4646-ae9a-aced303da1e6",
                "status": "BOOKED"
            }
        },
        "correlationId": "ee41a2e6-608d-4a1d-ae41-0e4d8629a619"
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )

    LIGHTNING_LANE_RAW_EVENT_NONINVENTORY_REDEMPTION = """{
            "eventType": "IA_SYNC",
            "key": "f0be3034472a5bf4ed0741e3ed0ff40f",
            "item": {
                "eventID": "f0be3034472a5bf4ed0741e3ed0ff40f",
                "eventName": "INSERT",
                "entitlement": {
                    "bookingGuestId": "AAAADA6M4LV52JPUBGU33JT77A",
                    "operationalDate": "2022-10-12",
                    "reason": "DAS",
                    "createUserId": "HARIS014",
                    "windowOverride": false,
                    "entitlementKey": "NONINVENTORY-ae675891-94ac-4756-91da-6e7344922a26",
                    "dasParentEntitlementId": "NONINVENTORY_AAAADA6M4LV52JPUBGU33JT77A_ae675891-94ac-4756-91da-6e7344922a26",
                    "updatedDate": "2022-10-12T12:28:27.199502532",
                    "type": "NONINVENTORY",
                    "enttlEndDate": "2022-10-13T02:00:00",
                    "remainingCount": 1,
                    "operational_date-product_type-experience_id-guest_range": "1665558000-DAS-353305-A-L",
                    "operational_date-park_id": "1665558000-330339",
                    "guestId": "AAAADA6M4LV52JPUBGU33JT77A",
                    "productType": "DAS",
                    "TTL_TIME": 1668247200,
                    "experienceList": [
                        {
                            "experienceId": "353305",
                            "locationList": [
                                {
                                    "locationId": "353305",
                                    "locationType": "Attraction"
                                }
                            ],
                            "experienceType": "Attraction",
                            "usesAllowed": 1,
                            "remainingCount": 1,
                            "parkId": "330339"
                        }
                    ],
                    "enttlStartDate": "2022-10-12T12:33:00",
                    "updateUserId": "HARIS014",
                    "operational_date-park_id-product_type-status": "1665558000-330339-DAS-REDEEMED",
                    "dasPrimaryIndicator": true,
                    "usesAllowed": 1,
                    "bookingId": "74e188bc-a1e3-49be-992c-19cb30ef67f9",
                    "createdDate": "2022-10-12T12:28:27.199501888",
                    "activities": [
                        {
                            "activityReason": "DAS",
                            "activityStatus": "REDEEMED",
                            "correlationId": "7c0e6ec0-47fb-4f8a-9eb2-1f63894b263f",
                            "activityDateTime": "2022-10-12T12:28:27.199480942",
                            "activityUser": "HARIS014"
                        }
                    ],
                    "enttlId": "ae675891-94ac-4756-91da-6e7344922a26",
                    "status": "REDEEMED"
                }
            },
            "correlationId": "7c0e6ec0-47fb-4f8a-9eb2-1f63894b263f"
        }
        """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )
