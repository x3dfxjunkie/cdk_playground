"""
unit test Source S3
"""
import logging
import sys
import os
import tempfile
import boto3
from moto import mock_s3

from app.src.load_testing.app.sources.s3_source import S3Source

sample_data = """
                {"correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219","eventType":"IA_SYNC","item":{"entitlement":{"ttl_time":1627045200,"activities":[{"activity_date_time":"2021-06-22T11:11:24.664323","activityReason":"VIP","activityStatus":"BOOKED","activityUser":"expdev123","correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219"}],"booking_guest_id":"AAAAC6OCPMCU2JMHM46IJPRHO4","booking_id":"5cef301c-3571-47e8-90d6-a8aadbb42a86","createUserId":"expdev123","createdDate":"2021-06-22T11:11:24.664329","dasPrimaryIndicator":false,"entitlementKey":"NONINVENTORY-00000044-66d1-4764-b7f7-79743cbbe686","enttlEndDate":"2021-06-23T06:00:00","enttl_id":"00000044-66d1-4764-b7f7-79743cbbe686","enttlStartDate":"2021-06-22T06:00:00","experienceList":[{"experienceId":"353303","experienceType":"Attraction","locationList":[{"locationId":"353303","locationType":"Attraction"}],"parkId":"336894","remainingCount":1,"usesAllowed":1}],"guestId":"AAAAC6OCPMCU4JN6TSBZZUWOIA","operational_date-park_id":"1624345200-336894","productType":"NON","reason":"VIP","remainingCount":1,"status":"BOOKED","type":"NONINVENTORY","updateUserId":"expdev123","updatedDate":"2021-06-22T11:11:24.664329","usesAllowed":1,"windowOverride":false},"eventName":"INSERT"}}
                {"correlation_id":"f9b19be7-27fe-44f6-82a5-d3f9e7178b91","eventType":"IA_SYNC","item":{"entitlement":{"ttl_time":1627045200,"activities":[{"activity_date_time":"2021-06-22T11:11:24.664323","activityReason":"VIP","activityStatus":"BOOKED","activityUser":"expdev123","correlation_id":"c9cba394-2ad4-492b-b59f-b29e3cb8e219"},{"activity_date_time":"2021-06-22T11:11:27.449655","activityReason":"STD","activityStatus":"REDEEMED","activityUser":"DAP","correlation_id":"f9b19be7-27fe-44f6-82a5-d3f9e7178b91","redemptionDateTime":"2021-06-22T11:11:27.449661","redemptionExperienceId":"353303","redemptionLocationId":"353303","redemptionTouchDeviceId":"Mobile"}],"booking_guest_id":"AAAAC6OCPMCU2JMHM46IJPRHO4","booking_id":"5cef301c-3571-47e8-90d6-a8aadbb42a86","createUserId":"expdev123","createdDate":"2021-06-22T11:11:24.664329","dasPrimaryIndicator":false,"entitlementKey":"NONINVENTORY-00000044-66d1-4764-b7f7-79743cbbe686","enttlEndDate":"2021-06-23T06:00:00","enttl_id":"00000044-66d1-4764-b7f7-79743cbbe686","enttlStartDate":"2021-06-22T06:00:00","experienceList":[{"experienceId":"353303","experienceType":"Attraction","locationList":[{"locationId":"353303","locationType":"Attraction"}],"parkId":"336894","remainingCount":0,"usesAllowed":1}],"guestId":"AAAAC6OCPMCU4JN6TSBZZUWOIA","operational_date-park_id":"1624345200-336894","productType":"NON","reason":"VIP","remainingCount":0,"status":"REDEEMED","type":"NONINVENTORY","updateUserId":"DAP","updatedDate":"2021-06-22T11:11:27.449665","usesAllowed":1,"windowOverride":false},"eventName":"MODIFY"}}
            """

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


@mock_s3
def test_get_files_name_without_data():
    bucket_name = "bucket_test"
    bucket_path = "/"

    client = boto3.client("s3")
    client.create_bucket(Bucket="bucket_test")
    s3_source = S3Source(bucket_name, bucket_path)
    files_names = s3_source.get_file_names()
    assert len(files_names) == 0


@mock_s3
def test_get_files_name_with_data():
    bucket_name = "bucket_test"
    bucket_path = "orion_ea_normal/"

    client = boto3.client("s3")
    client.create_bucket(Bucket=bucket_name)

    client.put_object(
        Bucket=bucket_name, Body=bytes(sample_data, encoding="utf-8"), Key="orion_ea_normal/test_file.txt"
    )
    s3_source = S3Source(bucket_name, bucket_path)
    files_names = s3_source.get_file_names()

    hist_sample_data = s3_source.get_sample_data()

    assert len(files_names) == 1
    assert len(hist_sample_data) == 2


@mock_s3
def test_download_file():
    bucket_name = "bucket_test"
    bucket_path = "orion_ea_normal/"
    file_key = "test_file.txt"
    file_path = os.path.join(bucket_path, file_key)
    client = boto3.client("s3")
    client.create_bucket(Bucket=bucket_name)
    client.put_object(Bucket=bucket_name, Body=bytes(sample_data, encoding="utf-8"), Key=file_path)
    s3_source = S3Source(bucket_name, bucket_path)
    temp_folder = tempfile.gettempdir()
    original_cwd = os.getcwd()
    os.chdir(temp_folder)

    try:
        s3_source.download_file([file_path], local_folder_path=temp_folder)
        local_file_path = os.path.join(temp_folder, file_path)
        assert os.path.isfile(local_file_path), f"{local_file_path} does not exist"
        with open(local_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        assert content.strip() == sample_data.strip(), "File content does not match"
    finally:
        os.chdir(original_cwd)
