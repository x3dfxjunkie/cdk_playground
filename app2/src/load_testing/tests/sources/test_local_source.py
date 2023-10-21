"""
unit test Source S3
"""
import os
import shutil

import pytest

from app.src.load_testing.app.sources.local_source import LocalSource

sample_data = """{"correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219","eventType":"IA_SYNC","item":{"entitlement":{"ttl_time":1627045200,"activities":[{"activity_date_time":"2021-06-22T11:11:24.664323","activityReason":"VIP","activityStatus":"BOOKED","activityUser":"expdev123","correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219"}],"booking_guest_id":"AAAAC6OCPMCU2JMHM46IJPRHO4","booking_id":"5cef301c-3571-47e8-90d6-a8aadbb42a86","createUserId":"expdev123","createdDate":"2021-06-22T11:11:24.664329","dasPrimaryIndicator":false,"entitlementKey":"NONINVENTORY-00000044-66d1-4764-b7f7-79743cbbe686","enttlEndDate":"2021-06-23T06:00:00","enttl_id":"00000044-66d1-4764-b7f7-79743cbbe686","enttlStartDate":"2021-06-22T06:00:00","experienceList":[{"experienceId":"353303","experienceType":"Attraction","locationList":[{"locationId":"353303","locationType":"Attraction"}],"parkId":"336894","remainingCount":1,"usesAllowed":1}],"guestId":"AAAAC6OCPMCU4JN6TSBZZUWOIA","operational_date-park_id":"1624345200-336894","productType":"NON","reason":"VIP","remainingCount":1,"status":"BOOKED","type":"NONINVENTORY","updateUserId":"expdev123","updatedDate":"2021-06-22T11:11:24.664329","usesAllowed":1,"windowOverride":false},"eventName":"INSERT"}}
                {"correlation_id":"f9b19be7-27fe-44f6-82a5-d3f9e7178b91","eventType":"IA_SYNC","item":{"entitlement":{"ttl_time":1627045200,"activities":[{"activity_date_time":"2021-06-22T11:11:24.664323","activityReason":"VIP","activityStatus":"BOOKED","activityUser":"expdev123","correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219"},{"activity_date_time":"2021-06-22T11:11:27.449655","activityReason":"STD","activityStatus":"REDEEMED","activityUser":"DAP","correlation_id":"f9b19be7-27fe-44f6-82a5-d3f9e7178b91","redemptionDateTime":"2021-06-22T11:11:27.449661","redemptionExperienceId":"353303","redemptionLocationId":"353303","redemptionTouchDeviceId":"Mobile"}],"booking_guest_id":"AAAAC6OCPMCU2JMHM46IJPRHO4","booking_id":"5cef301c-3571-47e8-90d6-a8aadbb42a86","createUserId":"expdev123","createdDate":"2021-06-22T11:11:24.664329","dasPrimaryIndicator":false,"entitlementKey":"NONINVENTORY-00000044-66d1-4764-b7f7-79743cbbe686","enttlEndDate":"2021-06-23T06:00:00","enttl_id":"00000044-66d1-4764-b7f7-79743cbbe686","enttlStartDate":"2021-06-22T06:00:00","experienceList":[{"experienceId":"353303","experienceType":"Attraction","locationList":[{"locationId":"353303","locationType":"Attraction"}],"parkId":"336894","remainingCount":0,"usesAllowed":1}],"guestId":"AAAAC6OCPMCU4JN6TSBZZUWOIA","operational_date-park_id":"1624345200-336894","productType":"NON","reason":"VIP","remainingCount":0,"status":"REDEEMED","type":"NONINVENTORY","updateUserId":"DAP","updatedDate":"2021-06-22T11:11:27.449665","usesAllowed":1,"windowOverride":false},"eventName":"MODIFY"}}
                {"correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219","eventType":"IA_SYNC","item":{"entitlement":{"ttl_time":1627045200,"activities":[{"activity_date_time":"2021-06-22T11:11:24.664323","activityReason":"VIP","activityStatus":"BOOKED","activityUser":"expdev123","correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219"}],"booking_guest_id":"AAAAC6OCPMCU2JMHM46IJPRHO4","booking_id":"5cef301c-3571-47e8-90d6-a8aadbb42a86","createUserId":"expdev123","createdDate":"2021-06-22T11:11:24.664329","dasPrimaryIndicator":false,"entitlementKey":"NONINVENTORY-00000044-66d1-4764-b7f7-79743cbbe686","enttlEndDate":"2021-06-23T06:00:00","enttl_id":"00000044-66d1-4764-b7f7-79743cbbe686","enttlStartDate":"2021-06-22T06:00:00","experienceList":[{"experienceId":"353303","experienceType":"Attraction","locationList":[{"locationId":"353303","locationType":"Attraction"}],"parkId":"336894","remainingCount":1,"usesAllowed":1}],"guestId":"AAAAC6OCPMCU4JN6TSBZZUWOIA","operational_date-park_id":"1624345200-336894","productType":"NON","reason":"VIP","remainingCount":1,"status":"BOOKED","type":"NONINVENTORY","updateUserId":"expdev123","updatedDate":"2021-06-22T11:11:24.664329","usesAllowed":1,"windowOverride":false},"eventName":"INSERT"}}
                {"correlation_id":"f9b19be7-27fe-44f6-82a5-d3f9e7178b91","eventType":"IA_SYNC","item":{"entitlement":{"ttl_time":1627045200,"activities":[{"activity_date_time":"2021-06-22T11:11:24.664323","activityReason":"VIP","activityStatus":"BOOKED","activityUser":"expdev123","correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219"},{"activity_date_time":"2021-06-22T11:11:27.449655","activityReason":"STD","activityStatus":"REDEEMED","activityUser":"DAP","correlation_id":"f9b19be7-27fe-44f6-82a5-d3f9e7178b91","redemptionDateTime":"2021-06-22T11:11:27.449661","redemptionExperienceId":"353303","redemptionLocationId":"353303","redemptionTouchDeviceId":"Mobile"}],"booking_guest_id":"AAAAC6OCPMCU2JMHM46IJPRHO4","booking_id":"5cef301c-3571-47e8-90d6-a8aadbb42a86","createUserId":"expdev123","createdDate":"2021-06-22T11:11:24.664329","dasPrimaryIndicator":false,"entitlementKey":"NONINVENTORY-00000044-66d1-4764-b7f7-79743cbbe686","enttlEndDate":"2021-06-23T06:00:00","enttl_id":"00000044-66d1-4764-b7f7-79743cbbe686","enttlStartDate":"2021-06-22T06:00:00","experienceList":[{"experienceId":"353303","experienceType":"Attraction","locationList":[{"locationId":"353303","locationType":"Attraction"}],"parkId":"336894","remainingCount":0,"usesAllowed":1}],"guestId":"AAAAC6OCPMCU4JN6TSBZZUWOIA","operational_date-park_id":"1624345200-336894","productType":"NON","reason":"VIP","remainingCount":0,"status":"REDEEMED","type":"NONINVENTORY","updateUserId":"DAP","updatedDate":"2021-06-22T11:11:27.449665","usesAllowed":1,"windowOverride":false},"eventName":"MODIFY"}}"""


# pylint: disable=C0325,W0621
@pytest.fixture
def local_setup():
    dir_name = "test_data"
    os.mkdir(dir_name)
    with open(os.path.join(dir_name, "test_file_a.json"), "w", encoding="utf8") as file_obj:
        file_obj.write(sample_data)
    with open(os.path.join(dir_name, "test_file_b.json"), "w", encoding="utf8") as file_obj:
        file_obj.write(sample_data)
    yield (dir_name)
    shutil.rmtree(dir_name)


def test_num_sample_files(local_setup):
    local_source = LocalSource(local_setup)
    files_names = local_source.get_file_names()
    assert len(files_names) == 2


def test_num_samples(local_setup):
    local_source = LocalSource(local_setup)
    samples = local_source.get_sample_data()
    assert len(samples) == 8
