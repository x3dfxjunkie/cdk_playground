"""Module to store raw GAM events and scenarios
"""
import json

class GamRawScenarios:
    """Class to represent GAM raw event scenarios.

    Returns:
        _type_: _description_
    """

    @staticmethod
    def all_events():
        return [
            GamRawEvents.GAM_NEW_IDENTIFIER_EXISTING_GUEST,
            GamRawEvents.GAM_REMOVE_GUEST_IDENTIFIER,
            GamRawEvents.GAM_NEW_GUEST,
            GamRawEvents.GAM_MERGE_GUESTS_NON_SWID,
            GamRawEvents.GAM_MERGE_GUESTS_SWID,
            GamRawEvents.GAM_SNAPSHOT,
        ]

    @staticmethod
    def two_different_guests_add_events():
        event_1 = json.loads(GamRawEvents.GAM_NEW_IDENTIFIER_EXISTING_GUEST)
        event_2 = json.loads(GamRawEvents.GAM_NEW_IDENTIFIER_EXISTING_GUEST)

        event_1_previous_guest_identifiers = [
            {
                "type": "xid",
                "value": "xid_1"
            },
            {
                "type": "swid",
                "value": "swid_1"
            },
        ]
        event_2_previous_guest_identifiers = [
            {
                "type": "xid",
                "value": "xid_2"
            },
            {
                "type": "swid",
                "value": "swid_2"
            },
        ]

        event_1_added_guest_identifiers = [
            {
                "type" : "transactional-guest-id",
                "value" : "transactional-guest-id_1"
            }
        ]
        event_2_added_guest_identifiers = [
            {
                "type" : "transactional-guest-id",
                "value" : "transactional-guest-id_2"
            }
        ]

        event_1_resulting_guest_identifiers = event_1_previous_guest_identifiers + event_1_added_guest_identifiers
        event_2_resulting_guest_identifiers = event_2_previous_guest_identifiers + event_2_added_guest_identifiers

        event_1["previousGuestIdentifiers"] = event_1_previous_guest_identifiers
        event_2["previousGuestIdentifiers"] = event_2_previous_guest_identifiers

        event_1["addedGuestIdentifiers"] = event_1_added_guest_identifiers
        event_2["addedGuestIdentifiers"] = event_2_added_guest_identifiers

        event_1["resultingGuestIdentifiers"] = event_1_resulting_guest_identifiers
        event_2["resultingGuestIdentifiers"] = event_2_resulting_guest_identifiers

        return [event_1, event_2]

    @staticmethod
    def two_different_guests_add_events_and_merge():
        merge_event = json.loads(GamRawEvents.GAM_MERGE_GUESTS_NON_SWID)

        merge_event_previous_1 = [
            {
                "type": "xid",
                "value": "xid_1"
            },
            {
                "type": "swid",
                "value": "swid_1"
            },
        ]
        merge_event_previous_2 = [
            {
                "type": "xid",
                "value": "xid_2"
            },
            {
                "type": "swid",
                "value": "swid_2"
            },
        ]
        merge_event_resulting_guest_identifiers = [
            {
                "type": "xid",
                "value": "xid_1"
            },
            {
                "type": "swid",
                "value": "swid_1"
            },
            {
                "type": "swid",
                "value": "swid_2"
            },
        ]
        merge_event["previousGuestIdentifiers1"] = merge_event_previous_1
        merge_event["previousGuestIdentifiers2"] = merge_event_previous_2
        merge_event["resultingGuestIdentifiers"] = merge_event_resulting_guest_identifiers

        return GamRawScenarios.two_different_guests_add_events() + [merge_event]

    @staticmethod
    def two_different_guests_add_events_and_merge_then_removed():
        remove_event = json.loads(GamRawEvents.GAM_REMOVE_GUEST_IDENTIFIER)

        remove_event_previous = [
            {
                "type": "xid",
                "value": "xid_1"
            },
            {
                "type": "swid",
                "value": "swid_1"
            },
            {
                "type": "swid",
                "value": "swid_2"
            },
        ]

        remove_event_deleted = [
            {
                "type": "swid",
                "value": "swid_2"
            },
        ]

        remove_event_resulting_guest_identifiers = [
            {
                "type": "xid",
                "value": "xid_1"
            },
            {
                "type": "swid",
                "value": "swid_1"
            },
        ]
        remove_event["previousGuestIdentifiers"] = remove_event_previous
        remove_event["removedGuestIdentifiers"] = remove_event_deleted
        remove_event["resultingGuestIdentifiers"] = remove_event_resulting_guest_identifiers

        return GamRawScenarios.two_different_guests_add_events_and_merge() + [remove_event]

class GamRawEvents:
    """
    Class to store raw GAM events.
    """

    GAM_NEW_IDENTIFIER_EXISTING_GUEST = """
    {
        "type" : "GUEST_IDENTIFIER",
        "action" : "ADD",
        "timestamp" : "2017-09-22T08:25:42Z",
        "previousGuestIdentifiers" : [
            {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "admission-link-id",
                "value" : "07100927241300268"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }
        ],
        "addedGuestIdentifiers" : [
            {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }
        ],
        "resultingGuestIdentifiers" : [
            {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "admission-link-id",
                "value" : "07100927241300268"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }, {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }
        ]
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )

    GAM_REMOVE_GUEST_IDENTIFIER = """
    {
        "type" : "GUEST_IDENTIFIER",
        "action" : "REMOVE",
        "timestamp" : "2017-09-22T08:25:42Z",
        "previousGuestIdentifiers" : [
            {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "admission-link-id",
                "value" : "07100927241300268"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }, {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }
        ],
        "removedGuestIdentifiers" : [
            {
                "type" : "admission-link-id",
                "value" : "07100927241300268"
            }
        ],
        "resultingGuestIdentifiers" : [ {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }, {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }
        ]
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )

    GAM_NEW_GUEST = """
    {
        "type" : "GUEST_IDENTIFIER",
        "action" : "ADD",
        "timestamp" : "2017-09-22T08:25:42Z",
        "previousGuestIdentifiers" : [],
        "addedGuestIdentifiers" : [
            {
                "type" : "admission-link-id",
                "value" : "07604201081400029"
            }
        ],
        "resultingGuestIdentifiers" : [
            {
                "type" : "xid",
                "value" : "E7CBB8DF-E96D-4CBF-9912-4A5910303B25"
            },
            {
                "type" : "admission-link-id",
                "value" : "07604201081400029"
            }
        ]
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )

    GAM_MERGE_GUESTS_NON_SWID = """
    {
        "type" : "GUEST_IDENTIFIER",
        "action" : "MERGE",
        "timestamp" : "2017-09-22T08:25:42Z",
        "previousGuestIdentifiers1" : [
            {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }, {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }
        ],
        "previousGuestIdentifiers2" : [
            {
                "type" : "xid",
                "value" : "E7CBB8DF-E96D-4CBF-9912-4A5910303B25"
            }, {
                "type" : "admission-link-id",
                "value" : "07604201081400029"
            }
        ],
        "resultingGuestIdentifiers" : [
            {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }, {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }, {
                "type" : "admission-link-id",
                "value" : "07604201081400029"
            }
        ]
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )

    GAM_MERGE_GUESTS_SWID = """
    {
        "type" : "GUEST_IDENTIFIER",
        "action" : "MERGE",
        "timestamp" : "2017-09-22T08:25:42Z",
        "previousGuestIdentifiers1" : [
            {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }, {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }
        ],
        "previousGuestIdentifiers2" : [
            {
                "type" : "xid",
                "value" : "E7CBB8DF-E96D-4CBF-9912-4A5910303B25"
            }, {
                "type" : "admission-link-id",
                "value" : "07604201081400029"
            }, {
                "type" : "swid",
                "value" : "{51BBD5EA-2119-4AE5-899D-90D286833D8A}"
            }
        ],
        "resultingGuestIdentifiers" : [
            {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }, {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }, {
                "type" : "admission-link-id",
                "value" : "07604201081400029"
            }
        ]
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )

    GAM_SNAPSHOT = """
    {
        "type" : "GUEST_IDENTIFIER",
        "action" : "SNAPSHOT",
        "timestamp" : "2017-09-22T08:25:42Z",
        "previousGuestIdentifiers" : [],
        "addedGuestIdentifiers" : [],
        "resultingGuestIdentifiers" : [
            {
                "type" : "xid",
                "value" : "A2BC8A93-F026-4C1B-8F76-8EF475D92EDF"
            }, {
                "type" : "swid",
                "value" : "{0A1D9AC3-12E8-4682-9D9A-C312E8D682B8}"
            }, {
                "type" : "cast-link-id",
                "value" : "38055"
            }, {
                "type" : "transactional-guest-id",
                "value" : "236728560"
            }, {
                "type" : "admission-link-id",
                "value" : "07604201081400029"
            }
        ]
    }
    """.replace(
        " ", ""
    ).replace(
        "\n", ""
    )
