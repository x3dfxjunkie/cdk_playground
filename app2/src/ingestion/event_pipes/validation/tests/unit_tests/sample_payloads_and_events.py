"""This module contains sample lambda events and data contract pipe information for the unit tests in `test_data_contract_validation_lambda.py`"""
import base64
import json

TABLE_PATH = "metadata.table-name"
EVENT_COMMON_METADATA = {
    "eventSource": "aws:kinesis",
    "eventID": "shardId-000000000000: 49640450530655783448641595467156077838773832572853026818",
    "eventVersion": "1.0",
    "eventSourceARN": "arn:aws:kinesis:us-east-1: 375056740518:stream/SampleStream",
    "eventName": "aws:kinesis:record",
    "invokeIdentityArn": "arn:aws:iam: : 375056740518:role/GAMAffiliationEventPipeStack-Role1ABCC5F0-RVXXJ07VA918",
    "awsRegion": "us-east-1",
    "kinesisSchemaVersion": "1.0",
}
PHONE_MESSAGE = "Phone Message"
INTERNET_EMAIL = "Internet Email"
TEST_SWID = "{8C79C430-3E7F-4DDC-9BCF-89902607A749}"
ELIGIBILITY_START_DATE = "2023-07-07T21:14:00Z"
END_DATE = "2023-08-04T06:59:00Z"
GAM_TABLE_PATH = "Header.Namespace"
TEST_TIMESTAMP = "2023-05-02T09:52:18.9736704Z"

EVENT_CME_RESERVATION = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test2",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": "eyJkYXRhIjogeyJpZCI6IDc0MDA3NDUzLCJyZXNfaWQiOiAiNDUwNjA2NDA3NzE0NjUzMTg0IiwiY29uZl9pZCI6ICI0NTA2MDY0MDc2OTc4NzU5NjgiLCJzd2lkIjogInsyNDkwQ0E0Ny1BQUFBLUJCQkItOTM5Ny04NEYzNDNCN0I3MjZ9Iiwid2FzX2ludl9vdmVycmlkZSI6IDAsImd1ZXN0X2ZpcnN0X25hbWUiOiAiR3Vlc3QiLCJndWVzdF9sYXN0X25hbWUiOiAiVGhyZWVTaXh0eSIsImd1ZXN0X2VtYWlsX2lkIjogIm5vdHJlYWxAeW9wbWFpbC5jb20iLCJpbnZfYnVja2V0X2lkIjogIldEV19NS19BUF9EQUlMWSIsImV4cF9kYXRlIjogIjIwMjMtMDQtMjEiLCJleHBfc2xvdCI6ICJEQUlMWSIsImV4cF9wYXJrIjogIldEV19NSyIsInByb2R1Y3RfaWQiOiAiV0RXX0FQIiwic2xvdF9zdGFydF9kdHMiOiAiMjAyMy0wNC0yMVQwMzowMDowMFoiLCJyZXNfc3RhdHVzIjogIkFMTE9DQVRFRCIsInRrdF92aXN1YWxfaWQiOiAiMjQxMzI5MDUwODIyMDAwMzIiLCJyZXNfdGlja2V0X3NrdSI6ICJOMUZDMyIsInJlc19vcmlnaW4iOiAiV0VCLVRJQ0tFVFMtUEFTU0VTIiwiY3JlYXRlZF91c3IiOiAiZi1jbWUtcmVzZXJ2YXRpb24iLCJjcmVhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMVoiLCJ1cGRhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMVoiLCJhZ2VfZ3JvdXAiOiAiQURVTFQiLCJzaG93X2xhc3RfZm91ciI6IDAsInN1cnZleV9zZW50IjogMCwiYXV0b191cGRhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMFoifSwibWV0YWRhdGEiOiB7InRpbWVzdGFtcCI6ICIyMDIzLTA0LTE3VDE3OjMzOjE3LjM4MTM4MloiLCJyZWNvcmQtdHlwZSI6ICJkYXRhIiwib3BlcmF0aW9uIjogImluc2VydCIsInBhcnRpdGlvbi1rZXktdHlwZSI6ICJzY2hlbWEtdGFibGUiLCJzY2hlbWEtbmFtZSI6ICJhd2FrZW5pbmciLCJ0YWJsZS1uYW1lIjogInJlc2VydmF0aW9uIiwidHJhbnNhY3Rpb24taWQiOiA4MDY3NDk0ODEyOTM1MTJ9fQ==",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    }
]

EVENT_CME_RESERVATION_CLOUDEVENT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test2",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": "eyAgICAic291cmNlIjogImFybjphd3M6a2luZXNpczp1cy1lYXN0LTE6NTQzMjc2OTA4NjkzOnN0cmVhbS9sc3QtdXNlMS1wci0yMDgwLWRsci1jbWUta2luZXNpcy1kbXotZG16IiwgICAgImlkIjogIjI5YzNlZjUyLTQxMDAtNGRhNC1hOGQ0LTExMzVlODExM2IwYSIsICAgICJ0eXBlIjogImFwcC5zcmMuZGF0YV9zdHJ1Y3R1cmVzLmRhdGFfY29udHJhY3RzLnNvdXJjZS5jbWUuZGxyLmNtZV9kbHJfcmVzZXJ2YXRpb25fc291cmNlX2RhdGFfY29udHJhY3QuQ01FRExSUmVzZXJ2YXRpb25Nb2RlbCIsICAgICJzcGVjdmVyc2lvbiI6ICIxLjAiLCAgICAidGltZSI6ICIyMDIzLTA2LTIxVDIwOjE2OjU1LjYwNDU4MyswMDowMCIsICAgICJzdWJqZWN0IjogbnVsbCwgICAgImRhdGFjb250ZW50dHlwZSI6ICJhcHBsaWNhdGlvbi9qc29uIiwgICAgImRhdGFzY2hlbWEiOiBudWxsLCAgICAicm91dGVyX2RhdGFiYXNlIjogImRibmFtZSIsICAgICJjaGVja19zdW0iOiAiYjMxN2IwM2E5YjVkN2QwYjg3ZDcwMjQyNTkwNjdmZWNiZDk5MzZiODBkNzBiOTU2ZDRlZjU1ZDE2NTBmMDE4YyIsICAgICJldmVudF9pZCI6ICJzaGFyZElkLTAwMDAwMDAwMDAwMDo0OTY0MTQyMjU3MjY4MzAwMTYxNjAzMTE4OTcxNjkzNjk0MDQ3NTcyMzU0NTgxNjU0NjE0ODM1NCIsICAgICJyb3V0ZXJfc2NoZW1hIjogInNjaGVtYSIsICAgICJyb3V0ZXJfdGFibGUiOiAidGFibGUiLCAgICAiZGF0YV9jb250cmFjdF92ZXJzaW9uIjogInYwLjEiLCAgICAidHJhY2VwYXJlbnQiOiAiMS02NDkzNWFiNS01NjgwOGQ5NjM5NTQ0NTU4NzA1MjAwOWIiLCAgICAicGFydGl0aW9uX2tleSI6ICJ0ZXN0NCIsICAgICJzdHJlYW0iOiAibHN0LXVzZTEtcHItMjA4MC1kbHItY21lLWtpbmVzaXMtZG16LWRteiIsICAgICJ0cmFjZXN0YXRlIjogIlJvb3Q9MS02NDkzNWFiNS01NjgwOGQ5NjM5NTQ0NTU4NzA1MjAwOWI7UGFyZW50PTI2YWVjYmQ0NzE4NjVjNjU7U2FtcGxlZD0xIiwgICAgInZhbGlkYXRlZCI6IHRydWUsICAgICJkYXRhIjogeyAgICAgICJkYXRhIjogeyAgICAgICAgImlkIjogNzQwMDc0NTMsICAgICAgICAicmVzX2lkIjogIjQ1MDYwNjQwNzcxNDY1MzE4NCIsICAgICAgICAiY29uZl9pZCI6ICI0NTA2MDY0MDc2OTc4NzU5NjgiLCAgICAgICAgInN3aWQiOiAiezI0OTBDQTQ3LUFBQUEtQkJCQi05Mzk3LTg0RjM0M0I3QjcyNn0iLCAgICAgICAgIndhc19pbnZfb3ZlcnJpZGUiOiAwLCAgICAgICAgImd1ZXN0X2ZpcnN0X25hbWUiOiAiR3Vlc3QiLCAgICAgICAgImd1ZXN0X2xhc3RfbmFtZSI6ICJUaHJlZVNpeHR5IiwgICAgICAgICJndWVzdF9lbWFpbF9pZCI6ICJub3RyZWFsQHlvcG1haWwuY29tIiwgICAgICAgICJpbnZfYnVja2V0X2lkIjogIldEV19NS19BUF9EQUlMWSIsICAgICAgICAiZXhwX2RhdGUiOiAiMjAyMy0wNC0yMSIsICAgICAgICAiZXhwX3Nsb3QiOiAiREFJTFkiLCAgICAgICAgImV4cF9wYXJrIjogIldEV19NSyIsICAgICAgICAicHJvZHVjdF9pZCI6ICJXRFdfQVAiLCAgICAgICAgInNsb3Rfc3RhcnRfZHRzIjogIjIwMjMtMDQtMjFUMDM6MDA6MDBaIiwgICAgICAgICJyZXNfc3RhdHVzIjogIkFMTE9DQVRFRCIsICAgICAgICAidGt0X3Zpc3VhbF9pZCI6ICIyNDEzMjkwNTA4MjIwMDAzMiIsICAgICAgICAicmVzX3RpY2tldF9za3UiOiAiTjFGQzMiLCAgICAgICAgInJlc19vcmlnaW4iOiAiV0VCLVRJQ0tFVFMtUEFTU0VTIiwgICAgICAgICJjcmVhdGVkX3VzciI6ICJmLWNtZS1yZXNlcnZhdGlvbiIsICAgICAgICAiY3JlYXRlZF9kdHMiOiAiMjAyMy0wNC0xN1QxMzozMzoxNS4yMzFaIiwgICAgICAgICJ1cGRhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMVoiLCAgICAgICAgImFnZV9ncm91cCI6ICJBRFVMVCIsICAgICAgICAic2hvd19sYXN0X2ZvdXIiOiAwLCAgICAgICAgInN1cnZleV9zZW50IjogMCwgICAgICAgICJhdXRvX3VwZGF0ZWRfZHRzIjogIjIwMjMtMDQtMTdUMTM6MzM6MTUuMjMwWiIgICAgICB9LCAgICAgICJtZXRhZGF0YSI6IHsgICAgICAgICJ0aW1lc3RhbXAiOiAiMjAyMy0wNC0xN1QxNzozMzoxNy4zODEzODJaIiwgICAgICAgICJyZWNvcmQtdHlwZSI6ICJkYXRhIiwgICAgICAgICJvcGVyYXRpb24iOiAiaW5zZXJ0IiwgICAgICAgICJwYXJ0aXRpb24ta2V5LXR5cGUiOiAic2NoZW1hLXRhYmxlIiwgICAgICAgICJzY2hlbWEtbmFtZSI6ICJhd2FrZW5pbmciLCAgICAgICAgInRhYmxlLW5hbWUiOiAicmVzZXJ2YXRpb24iLCAgICAgICAgInRyYW5zYWN0aW9uLWlkIjogODA2NzQ5NDgxMjkzNTEyICAgICAgfSAgICB9ICB9",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    }
]

EVENT_CME_DOUBLE = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": "eyJkYXRhIjp7ImlkIjoxNDQ5OCwiaW52X2J1Y2tldF9pZCI6IldEV19NS19BUF9EQUlMWSIsImludl9kYXRlIjoiMjAyMy0wNC0yMiIsInRpbWVfem9uZSI6IkFtZXJpY2EvTmV3X1lvcmsiLCJtYXhfaW52ZW50b3J5IjoxMzAwMCwic29mdF9pbnZlbnRvcnlfbGltaXQiOjEyOTIwLCJjdXJyX2ludmVudG9yeSI6OTk0OCwibGFzdF91cGRhdGVkIjoiMjAyMy0wNC0xN1QxMzozMzoxNVoiLCJ1cGRhdGVfdXNyIjoiRFVNTVkwMSIsImNyZWF0ZWRfb24iOiIyMDIyLTAxLTIwVDExOjQzOjMxWiIsImNyZWF0ZWRfdXNyIjoiRFVNTVkwMiIsImlzX2FjdGl2ZSI6MSwiaXNfcmVzZXJ2YWJsZSI6MX0sIm1ldGFkYXRhIjp7InRpbWVzdGFtcCI6IjIwMjMtMDQtMTdUMTc6MzM6MTcuNDI3NTYyWiIsInJlY29yZC10eXBlIjoiZGF0YSIsIm9wZXJhdGlvbiI6InVwZGF0ZSIsInBhcnRpdGlvbi1rZXktdHlwZSI6InNjaGVtYS10YWJsZSIsInNjaGVtYS1uYW1lIjoiYXdha2VuaW5nIiwidGFibGUtbmFtZSI6Imludl9idWNrZXRfZGF0ZV90aW1lIiwidHJhbnNhY3Rpb24taWQiOjgwNjc0OTQ4MTI5ODQwOX19Cg==",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    },
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test2",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": "eyJkYXRhIjogeyJpZCI6IDc0MDA3NDUzLCJyZXNfaWQiOiAiNDUwNjA2NDA3NzE0NjUzMTg0IiwiY29uZl9pZCI6ICI0NTA2MDY0MDc2OTc4NzU5NjgiLCJzd2lkIjogInsyNDkwQ0E0Ny1BQUFBLUJCQkItOTM5Ny04NEYzNDNCN0I3MjZ9Iiwid2FzX2ludl9vdmVycmlkZSI6IDAsImd1ZXN0X2ZpcnN0X25hbWUiOiAiR3Vlc3QiLCJndWVzdF9sYXN0X25hbWUiOiAiVGhyZWVTaXh0eSIsImd1ZXN0X2VtYWlsX2lkIjogIm5vdHJlYWxAeW9wbWFpbC5jb20iLCJpbnZfYnVja2V0X2lkIjogIldEV19NS19BUF9EQUlMWSIsImV4cF9kYXRlIjogIjIwMjMtMDQtMjEiLCJleHBfc2xvdCI6ICJEQUlMWSIsImV4cF9wYXJrIjogIldEV19NSyIsInByb2R1Y3RfaWQiOiAiV0RXX0FQIiwic2xvdF9zdGFydF9kdHMiOiAiMjAyMy0wNC0yMVQwMzowMDowMFoiLCJyZXNfc3RhdHVzIjogIkFMTE9DQVRFRCIsInRrdF92aXN1YWxfaWQiOiAiMjQxMzI5MDUwODIyMDAwMzIiLCJyZXNfdGlja2V0X3NrdSI6ICJOMUZDMyIsInJlc19vcmlnaW4iOiAiV0VCLVRJQ0tFVFMtUEFTU0VTIiwiY3JlYXRlZF91c3IiOiAiZi1jbWUtcmVzZXJ2YXRpb24iLCJjcmVhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMVoiLCJ1cGRhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMVoiLCJhZ2VfZ3JvdXAiOiAiQURVTFQiLCJzaG93X2xhc3RfZm91ciI6IDAsInN1cnZleV9zZW50IjogMCwiYXV0b191cGRhdGVkX2R0cyI6ICIyMDIzLTA0LTE3VDEzOjMzOjE1LjIzMFoifSwibWV0YWRhdGEiOiB7InRpbWVzdGFtcCI6ICIyMDIzLTA0LTE3VDE3OjMzOjE3LjM4MTM4MloiLCJyZWNvcmQtdHlwZSI6ICJkYXRhIiwib3BlcmF0aW9uIjogImluc2VydCIsInBhcnRpdGlvbi1rZXktdHlwZSI6ICJzY2hlbWEtdGFibGUiLCJzY2hlbWEtbmFtZSI6ICJhd2FrZW5pbmciLCJ0YWJsZS1uYW1lIjogInJlc2VydmF0aW9uIiwidHJhbnNhY3Rpb24taWQiOiA4MDY3NDk0ODEyOTM1MTJ9fQ==",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    },
]

EVENT_CME_INVBUCKETDATETIME = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": "eyJkYXRhIjoJeyJpZCI6CTE0NDk4LCJpbnZfYnVja2V0X2lkIjoJIldEV19NS19BUF9EQUlMWSIsImludl9kYXRlIjoJIjIwMjMtMDQtMjIiLCJ0aW1lX3pvbmUiOgkiQW1lcmljYS9OZXdfWW9yayIsIm1heF9pbnZlbnRvcnkiOgkxMzAwMCwic29mdF9pbnZlbnRvcnlfbGltaXQiOgkxMjkyMCwiY3Vycl9pbnZlbnRvcnkiOgk5OTQ4LCJsYXN0X3VwZGF0ZWQiOgkiMjAyMy0wNC0xN1QxMzozMzoxNVoiLCJ1cGRhdGVfdXNyIjoJIkhBUlZFMDE5IiwiY3JlYXRlZF9vbiI6CSIyMDIyLTAxLTIwVDExOjQzOjMxWiIsImNyZWF0ZWRfdXNyIjoJIkJBUktEMDA4IiwiaXNfYWN0aXZlIjoJMSwiaXNfcmVzZXJ2YWJsZSI6CTF9LCJtZXRhZGF0YSI6CXsidGltZXN0YW1wIjoJIjIwMjMtMDQtMTdUMTc6MzM6MTcuNDI3NTYyWiIsInJlY29yZC10eXBlIjoJImRhdGEiLCJvcGVyYXRpb24iOgkidXBkYXRlIiwicGFydGl0aW9uLWtleS10eXBlIjoJInNjaGVtYS10YWJsZSIsInNjaGVtYS1uYW1lIjoJImF3YWtlbmluZyIsInRhYmxlLW5hbWUiOgkiaW52X2J1Y2tldF9kYXRlX3RpbWUiLCJ0cmFuc2FjdGlvbi1pZCI6CTgwNjc0OTQ4MTI5ODQwOX19",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    }
]

EVENT_CME_VALIDATION_ERROR = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": "eyJkYXRhIjp7ImlkIjoiMTQ0OThhIiwiaW52X2J1Y2tldF9pZCI6IldEV19NS19BUF9EQUlMWSIsImludl9kYXRlIjoiMjAyMy0wNC0yMiIsInRpbWVfem9uZSI6IkFtZXJpY2EvTmV3X1lvcmsiLCJtYXhfaW52ZW50b3J5IjoxMzAwMCwic29mdF9pbnZlbnRvcnlfbGltaXQiOjEyOTIwLCJjdXJyX2ludmVudG9yeSI6OTk0OCwibGFzdF91cGRhdGVkIjoiMjAyMy0wNC0xN1QxMzozMzoxNVoiLCJ1cGRhdGVfdXNyIjoiRFVNTVkwMSIsImNyZWF0ZWRfb24iOiIyMDIyLTAxLTIwVDExOjQzOjMxWiIsImNyZWF0ZWRfdXNyIjoiRFVNTVkwMiIsImlzX2FjdGl2ZSI6MSwiaXNfcmVzZXJ2YWJsZSI6MX0sIm1ldGFkYXRhIjp7InRpbWVzdGFtcCI6IjIwMjMtMDQtMTdUMTc6MzM6MTcuNDI3NTYyWiIsInJlY29yZC10eXBlIjoiZGF0YSIsIm9wZXJhdGlvbiI6InVwZGF0ZSIsInBhcnRpdGlvbi1rZXktdHlwZSI6InNjaGVtYS10YWJsZSIsInNjaGVtYS1uYW1lIjoiYXdha2VuaW5nIiwidGFibGUtbmFtZSI6Imludl9idWNrZXRfZGF0ZV90aW1lIiwidHJhbnNhY3Rpb24taWQiOjgwNjc0OTQ4MTI5ODQwOX19Cg==",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    }
]

EVENT_DOES_NOT_MATCH_DATACONTRACT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test2",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": "eyJkYXRhIjp7ImlkIjoxNDQ5OCwiaW52X2J1Y2tldF9pZCI6IldEV19NS19BUF9EQUlMWSIsImludl9kYXRlIjoiMjAyMy0wNC0yMiIsInRpbWVfem9uZSI6IkFtZXJpY2EvTmV3X1lvcmsiLCJtYXhfaW52ZW50b3J5IjoxMzAwMCwic29mdF9pbnZlbnRvcnlfbGltaXQiOjEyOTIwLCJjdXJyX2ludmVudG9yeSI6OTk0OCwibGFzdF91cGRhdGVkIjoiMjAyMy0wNC0xN1QxMzozMzoxNVoiLCJ1cGRhdGVfdXNyIjoiRFVNTVlfVVNFUl8wMSIsImNyZWF0ZWRfb24iOiIyMDIyLTAxLTIwVDExOjQzOjMxWiIsImNyZWF0ZWRfdXNyIjoiRFVNTVlfVVNFUl8wMiIsImlzX2FjdGl2ZSI6MSwiaXNfcmVzZXJ2YWJsZSI6MX0sIm1ldGFkYXRhIjp7InRpbWVzdGFtcCI6IjIwMjMtMDQtMTdUMTc6MzM6MTcuNDI3NTYyWiIsInJlY29yZC10eXBlIjoiZGF0YSIsIm9wZXJhdGlvbiI6InVwZGF0ZSIsInBhcnRpdGlvbi1rZXktdHlwZSI6InNjaGVtYS10YWJsZSIsInNjaGVtYS1uYW1lIjoiYXdha2VuaW5nIiwidGFibGUtbmFtZSI6Imludl9idWNrZXRfZGF0ZV90aW1lX3Rlc3QiLCJ0cmFuc2FjdGlvbi1pZCI6ODA2NzQ5NDgxMjk4NDA5fX0K",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    }
]

EVENT_CME_RESERVATION_OPERATION_LOAD = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test3",  # pragma: allowlist secret
        "sequenceNumber": "49641422572683001616031189740483188664357679489248919554",
        "data": "eyJkYXRhIjp7ImlkIjozODQ2OSwicmVzX2lkIjoiMjAwMzcwMjQ0MDY1NTQ0OTYwIiwiY29uZl9pZCI6IjIwMDM3MDI0NDAyNzc5NjIyNCIsInN3aWQiOiJ7MDU3RTU1NEYtRTczNy00QUJFLUE4NjQtQjIwRUI4OEIxMDQ0fSIsIndhc19pbnZfb3ZlcnJpZGUiOjAsImd1ZXN0X2ZpcnN0X25hbWUiOiIqIiwiZ3Vlc3RfbGFzdF9uYW1lIjoiKiIsImd1ZXN0X2VtYWlsX2lkIjoibWlja2V5Lm1vdXNlQGRpc25leXRlc3QuY29tIiwiaW52X2J1Y2tldF9pZCI6IkRMUl9DQV9QSF9EQUlMWSIsImV4cF9kYXRlIjoiMjAyMi0xMS0xNCIsImV4cF9zbG90IjoiREFJTFkiLCJleHBfcGFyayI6IkRMUl9DQSIsInByb2R1Y3RfaWQiOiJETFJfUEgiLCJzbG90X3N0YXJ0X2R0cyI6IjIwMjItMTEtMTRUMDA6MDA6MDBaIiwicmVzX3N0YXR1cyI6Ik5FVyIsInRrdF92aXN1YWxfaWQiOiI2NjMxNTU1Njc0ODg4MDkzNTM1MzUzNSIsInJlc19vcmlnaW4iOiJVTklGSUVELUNIRUNLT1VUIiwiY3JlYXRlZF91c3IiOiJ0ZXN0LXVzZXIiLCJjcmVhdGVkX2R0cyI6IjIwMjItMTAtMDVUMTQ6NTk6NDguODg0WiIsInVwZGF0ZWRfdXNyIjoidGVzdC11c2VyIiwidXBkYXRlZF9kdHMiOiIyMDIyLTEwLTA1VDE1OjAxOjQzLjMwNloiLCJhZ2VfZ3JvdXAiOiJBRFVMVCIsInJlc190aWNrZXRfc2t1IjoiNjYzMjRQQUgiLCJzaG93X2xhc3RfZm91ciI6MSwic3VydmV5X3NlbnQiOjAsImF1dG9fdXBkYXRlZF9kdHMiOiIyMDIyLTEwLTA1VDE1OjAxOjQzLjMwNVoifSwibWV0YWRhdGEiOnsidGltZXN0YW1wIjoiMjAyMy0wNi0wNVQyMDoxMjo1NS44MzM2OThaIiwicmVjb3JkLXR5cGUiOiJkYXRhIiwib3BlcmF0aW9uIjoibG9hZCIsInBhcnRpdGlvbi1rZXktdHlwZSI6InByaW1hcnkta2V5Iiwic2NoZW1hLW5hbWUiOiJhd2FrZW5pbmciLCJ0YWJsZS1uYW1lIjoicmVzZXJ2YXRpb24ifX0K",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1685995975.842,
    }
]

EVENT_CME_INVBUCKETDATETIME_TRANSACTION_ID = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test4",  # pragma: allowlist secret
        "sequenceNumber": "49641422572683001616031189716936940475723545816546148354",
        "data": "ewoJImRhdGEiOgl7CgkJImlkIjoJMTAwODIsCgkJImludl9idWNrZXRfaWQiOgkiRExSX0RQX1BIX0RBSUxZIiwKCQkiaW52X2RhdGUiOgkiMjAyMS0wOS0yNiIsCgkJInRpbWVfem9uZSI6CSJBbWVyaWNhL0xvc19BbmdlbGVzIiwKCQkibWF4X2ludmVudG9yeSI6CTEwMDAsCgkJInNvZnRfaW52ZW50b3J5X2xpbWl0IjoJOTAwLAoJCSJjdXJyX2ludmVudG9yeSI6CTEsCgkJImxhc3RfdXBkYXRlZCI6CSIyMDIxLTA4LTE5VDExOjIwOjQ3WiIsCgkJInVwZGF0ZV91c3IiOgkidGVzdHVzZXIiLAoJCSJjcmVhdGVkX29uIjoJIjIwMjEtMDUtMjRUMTI6NTU6MDdaIiwKCQkiY3JlYXRlZF91c3IiOgkidGVzdHVzZXIiLAoJCSJpc19hY3RpdmUiOgkxLAoJCSJpc19yZXNlcnZhYmxlIjoJMQoJfSwKCSJtZXRhZGF0YSI6CXsKCQkidGltZXN0YW1wIjoJIjIwMjMtMDYtMDVUMjA6MTI6MzguMTYxMjY5WiIsCgkJInJlY29yZC10eXBlIjoJImRhdGEiLAoJCSJvcGVyYXRpb24iOgkibG9hZCIsCgkJInBhcnRpdGlvbi1rZXktdHlwZSI6CSJwcmltYXJ5LWtleSIsCgkJInNjaGVtYS1uYW1lIjoJImF3YWtlbmluZyIsCgkJInRhYmxlLW5hbWUiOgkiaW52X2J1Y2tldF9kYXRlX3RpbWUiCgl9Cn0=",  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1685995958.251,
    }
]


GAM_DLR_REG_GUEST_RECORD = {
    "type": "RegisteredGuest",
    "action": "CREATE",
    "nativeGuestIds": [{"type": "swid", "value": TEST_SWID}],
    "registeredGuest": {
        "swid": TEST_SWID,
        "name": {
            "title": "Mr.",
            "firstName": "Excellent",
            "lastName": "Kitchen",
            "middleName": "Full",
            "suffix": "Jr.",
        },
        "dateOfBirth": [1973, 1, 1],
        "gender": "NOT_SPECIFIED",
        "userName": "oneidtestFF_ExcellentKitchen637115",
        "email": "Kitchen66@mailinator.com",
        "countryCode": "US",
        "languageCode": "en-US",
        "status": "ACTIVE",
        "emailValidationStatus": "UNVALIDATED",
        "registrationDate": "2023-07-13T11:06:12.583Z",
        "testProfileFlag": "Y",
        "referenceId": TEST_SWID,
        "clientId": "TPR-WDW-LBJS.WEB-STAGE",
        "affiliateName": "disneyid",
        "ageBand": "ADULT",
        "addressList": [
            {
                "id": "259d6c1a-4ca6-46cd-900c-e9a9a15f12e9",
                "line1": "103 Montgomery St",
                "city": "San Francisco",
                "stateOrProvince": "CA",
                "country": "US",
                "postalCode": "94129",
                "type": "BILLING",
            }
        ],
        "phoneList": [
            {
                "id": "a40adeae-a5eb-44fd-9e80-c48ce39dc781",
                "number": "2065001234",
                "countryCode": "1",
                "type": "MOBILE",
            }
        ],
        "communicationPreferences": {"preferredLanguage": "en"},
        "messagingPreferences": {
            "messagingPreferencesForm": {
                "offers": {
                    "type": "select",
                    "required": False,
                    "multi": True,
                    "options": [
                        {"text": PHONE_MESSAGE, "value": "SMS", "checked": False},
                        {"text": INTERNET_EMAIL, "value": "EMAIL", "checked": False},
                    ],
                },
                "disneyFamilyOfBusinessNews": {
                    "type": "select",
                    "required": False,
                    "multi": True,
                    "options": [
                        {"text": PHONE_MESSAGE, "value": "SMS", "checked": False},
                        {"text": INTERNET_EMAIL, "value": "EMAIL", "checked": False},
                    ],
                },
                "itineraryReminders": {
                    "type": "select",
                    "required": False,
                    "multi": True,
                    "options": [
                        {"text": PHONE_MESSAGE, "value": "SMS", "checked": False},
                        {"text": INTERNET_EMAIL, "value": "EMAIL", "checked": False},
                    ],
                },
                "weeklyDisneyInsiderNewsletter": {
                    "type": "select",
                    "required": False,
                    "multi": True,
                    "options": [
                        {"text": PHONE_MESSAGE, "value": "SMS", "checked": False},
                        {"text": INTERNET_EMAIL, "value": "EMAIL", "checked": False},
                    ],
                },
                "mediaAlerts": {
                    "type": "select",
                    "required": False,
                    "multi": True,
                    "options": [
                        {"text": PHONE_MESSAGE, "value": "SMS", "checked": False},
                        {"text": INTERNET_EMAIL, "value": "EMAIL", "checked": False},
                    ],
                },
                "familyAndFriendsNotifications": {
                    "type": "select",
                    "required": False,
                    "multi": True,
                    "options": [
                        {"text": PHONE_MESSAGE, "value": "SMS", "checked": False},
                        {"text": INTERNET_EMAIL, "value": "EMAIL", "checked": False},
                    ],
                },
                "itineraryChanges": {
                    "type": "select",
                    "required": False,
                    "multi": True,
                    "options": [
                        {"text": PHONE_MESSAGE, "value": "SMS", "checked": False},
                        {"text": INTERNET_EMAIL, "value": "EMAIL", "checked": False},
                    ],
                },
            }
        },
        "preferences": {"favoriteCharacterId": "15655408", "avatarId": "15655408"},
    },
}

GAM_DLR_ADMISSION_RECORD = {
    "type": "ADMISSION",
    "action": "MODIFY",
    "nativeGuestIds": [{"type": "swid", "value": TEST_SWID}],
    "admissionEntitlement": {
        "visualId": "705670556016858874559",
        "name": "2-Day Park Hopper Ticket",
        "orderConfirmationNumber": "DD480047710433095680",  # pragma: allowlist secret
        "governmentIdLinked": False,
        "geniePlus": False,
        "sku": "70567PAH",
        "productInstanceId": "dlr-theme-park_2_C_P_0_RF_AF_SOF_progenstr",
        "status": "ACTIVE",
        "owner": {"profileId": TEST_SWID, "ownerType": "B2C"},
        "primaryGuest": TEST_SWID,
        "shared": False,
        "assignedGuest": {"nickname": "Lumbering Refrigerator", "firstName": "Lumbering", "lastName": "Refrigerator"},
        "productTypeId": "dlr-theme-park",
        "category": {"id": "ThemePark", "name": "Theme Park Tickets"},
        "featureIds": ["336894", "330339"],
        "voidable": False,
        "guestAgeGroup": "CHILD",
        "remainingUse": 2,
        "useCount": 0,
        "primaryGuestLinked": False,
        "renewable": False,
        "modifiable": True,
        "upgradeable": False,
        "skipRenewal": False,
        "parkHopper": True,
        "sourceLexvas": True,
        "packageEntitlement": False,
        "mainEntrancePass": False,
        "options": [
            {"optionType": "addOns", "optionValue": ["park-hopper"]},
            {"optionType": "numDays", "optionValue": ["2"]},
            {"optionType": "ageGroup", "optionValue": ["child"]},
        ],
        "startDateTime": "2023-07-17T09:18:00.000-07:00",
        "endDateTime": "2023-07-31T23:59:00.000-07:00",
    },
}


GAM_DLR_EVENT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test2",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": base64.b64encode(json.dumps(GAM_DLR_ADMISSION_RECORD).encode("utf-8")),  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    },
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test2",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": base64.b64encode(json.dumps(GAM_DLR_REG_GUEST_RECORD).encode("utf-8")),  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    },
]

GAM_DLR_LEVEL_N_ENTITLEMENT_RECORD = {
    "action": "MODIFY",
    "actualExpirationDateTime": None,
    "captureDate": None,
    "endDate": END_DATE,
    "endDateTime": END_DATE,
    "enterpriseProductID": "GeniePlus",
    "entitlementID": None,
    "entitlementType": "GeniePlus",
    "expirationDate": None,
    "externalReferences": {"ticket-visual-id": None},
    "guests": [
        {
            "externalIdentifiers": [{"id": None, "type": "ticket-visual-id"}],
            "fulfillmentStatus": [],
            "levelnLinkId": None,
            "relationship": ["OWNER", "PARTICIPANT"],
        }
    ],
    "issueType": "standard",
    "levelNProducts": [
        {
            "constraints": [],
            "features": [
                {
                    "constraints": [],
                    "eligibilityDates": [
                        {
                            "eligibilityEndDate": END_DATE,
                            "eligibilityStartDate": ELIGIBILITY_START_DATE,
                        }
                    ],
                    "type": "EXPERIENCE_ACCESS",
                },
                {
                    "constraints": [],
                    "eligibilityDates": [
                        {
                            "eligibilityEndDate": "2023-09-18T06:59:00Z",
                            "eligibilityStartDate": "2023-07-07T07:00:00Z",
                        }
                    ],
                    "type": "AUDIO_TOURS",
                },
                {
                    "constraints": [],
                    "eligibilityDates": [
                        {
                            "eligibilityEndDate": "2023-09-17T12:59:00Z",
                            "eligibilityStartDate": "2023-07-21T13:00:00Z",
                        }
                    ],
                    "type": "AUGMENTED_REALITY",
                },
                {
                    "constraints": [],
                    "eligibilityDates": [
                        {
                            "eligibilityEndDate": "2023-07-22T12:59:00Z",
                            "eligibilityStartDate": "2023-07-21T13:00:00Z",
                        },
                        {
                            "eligibilityEndDate": "2023-07-21T12:59:00Z",
                            "eligibilityStartDate": "2023-07-20T13:00:00Z",
                        },
                    ],
                    "type": "PHOTO_ACCESS",
                },
            ],
            "id": "dlr-theme-park_2_A_PGP_0_RF_AF_SOF_progenstr",
            "type": "GeniePlus",
        }
    ],
    "maximumQuantity": "1",
    "minimumQuantity": "1",
    "nativeGuestIds": [{"type": "leveln-link-id", "value": None}],
    "onlineEngagementDateTime": None,
    "overrideGuestCount": "",
    "plannedArrivalDate": None,
    "purchaseDateTime": "2023-07-21T04:00:00Z",
    "reason": "",
    "redemptionDate": None,
    "resortReservationEndDate": "2023-08-04T00:00:00Z",
    "resortReservationStartDate": "2023-07-07T00:00:00Z",
    "salesPrice": "0.00",
    "salesTax": "0.00",
    "settlementDate": None,
    "sites": ["DLR"],
    "source": "TMS",
    "startDate": ELIGIBILITY_START_DATE,
    "startDateTime": ELIGIBILITY_START_DATE,
    "status": "active",
    "timestamp": "2023-07-21T15:39:34.112Z",
    "type": "LevelN Entitlement",
}

GAM_DLR_BROKEN_EVENT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "1",
        "data": base64.b64encode(
            json.dumps(GAM_DLR_LEVEL_N_ENTITLEMENT_RECORD).encode("utf-8")
        ),  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    },
]


DATA_PIPE_INFO_GAM = {
    "metrics": {"error": {"namespace": "event_pipes_validation_errors", "value": 1, "unit": "Count"}},
    "table_path": "type",
    "schema_path": "temp",
    "data_mapper_type": "nested",
    "data_contracts": [
        {
            "data_contract": "app.src.data_structures.data_contracts.source.gam_dlr.v0.gam_dlr_registered_guest_source_data_contract",
            "class_name": "GAMDLRRegisteredGuestModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": "type", "value": "RegisteredGuest"}],
            "router_database": "dbname",
            "router_schema": "schema",
            "router_table": "REGISTERED_GUEST",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.gam_dlr.v0.gam_dlr_tickets_source_data_contract",
            "class_name": "GAMDLRTicketsModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": "type", "value": "ADMISSION"}],
            "router_database": "dbname",
            "router_schema": "schema",
            "router_table": "ADMISSION",
        },
    ],
}


DATA_PIPE_INFO = {
    "metrics": {"error": {"namespace": "event_pipes_validation_errors", "value": 1, "unit": "Count"}},
    "table_path": TABLE_PATH,
    "schema_path": "metadata.schema-name",
    "data_mapper_type": "nested",
    "data_contracts": [
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_reservation_source_data_contract",
            "class_name": "CMEDLRReservationModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": TABLE_PATH, "value": "reservation"}],
            "router_database": "dbname",
            "router_schema": "schema",
            "router_table": "table",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_inv_bucket_date_time_source_data_contract",
            "class_name": "CMEDLRInvBucketDateTimeModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": TABLE_PATH, "value": "inv_bucket_date_time"}],
            "router_database": "dbname2",
            "router_schema": "schema2",
            "router_table": "table2",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_res_summary_stats_source_data_contract",
            "class_name": "CMEDLRResSummaryStatsModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": TABLE_PATH, "value": "res_summary_stats"}],
            "router_database": "dbname3",
            "router_schema": "schema3",
            "router_table": "table3",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_res_by_dates_stats_source_data_contract",
            "class_name": "CMEDLRResByDatesStatsModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": "metadata.table-name", "value": "res_by_dates_stats"}],
            "router_database": "dbname4",
            "router_schema": "schema4",
            "router_table": "table4",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_wdw.v0.cme_wdw_res_guest_links_source_data_contract",
            "class_name": "CMEWDWResGuestLinksModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": TABLE_PATH, "value": "res_guest_links"}],
            "router_database": "dbname5",
            "router_schema": "schema5",
            "router_table": "table5",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_inventory_product_source_data_contract",
            "class_name": "CMEDLRInventoryProductModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": TABLE_PATH, "value": "inventory_product"}],
            "router_database": "dbname6",
            "router_schema": "schema6",
            "router_table": "table6",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_inv_bucket_source_data_contract",
            "class_name": "CMEDLRInventoryProductModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": TABLE_PATH, "value": "inv_bucket"}],
            "router_database": "dbname7",
            "router_schema": "schema7",
            "router_table": "table7",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_destination_source_data_contract",
            "class_name": "CMEDLRDestinationModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": TABLE_PATH, "value": "destination"}],
            "router_database": "dbname8",
            "router_schema": "schema8",
            "router_table": "table8",
        },
        {
            "data_contract": "app.src.data_structures.data_contracts.source.cme_dlr.v0.cme_dlr_park_source_data_contract",
            "class_name": "CMEDLRParkModel",
            "data_contract_version": "v0.1",
            "key_path": [{"name": TABLE_PATH, "value": "park"}],
            "router_database": "dbname9",
            "router_schema": "schema9",
            "router_table": "table9",
        },
    ],
}

PLAYAPP_PAYLOAD = {
    "playId": "test",
    "request": {
        "action": "GESTURE",
        "guestId": "test",
        "guestIdType": "xband-shortrange-public-id",
        "location": "test",
        "sourceId": "test",
        "type": "STATUE_QUEST",
    },
    "response": {"payload": {"message": "success", "taskId": "bb8"}},
    "swid": "test",
    "timestamp": "2023-08-03T17:51:42.000Z",
}

PLAYAPP_EVENT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "1",
        "data": base64.b64encode(json.dumps(PLAYAPP_PAYLOAD).encode("utf-8")),  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    },
]

DATA_PIPE_INFO_PLAYAPP = {
    "metrics": {"error": {"namespace": "event_pipes_validation_errors", "value": 1, "unit": "Count"}},
    "data_contracts": [
        {
            "data_contract": "app.src.data_structures.data_contracts.source.playapp.v0.playapp_quest_source_data_contract",
            "class_name": "PlayAppQuestModel",
            "data_contract_version": "v0.1",
            "router_database": "dbname",
            "router_schema": "schema",
            "router_table": "table",
        }
    ],
    "data_mapper_type": "singleton",
}

GALAXY_PAYLOAD = {
    "Header": {
        "Version": "0.2",
        "MessageID": "85e6c51a-bf24-44f4-8555-4aef4b6bb637",
        "MessageTimestamp": TEST_TIMESTAMP,
        "SourceSystemName": "GTS.Galaxy",
        "SourceSystemVersion": "0.2",
        "DispatchTimestamp": TEST_TIMESTAMP,
        "SourceEventDateTime": "2023-05-02T09:52:18.4530000+00:00",
        "DataID": "3960650f-f131-4a83-afd4-9836f0a1eead",
        "DataCommitTimestamp": "2023-05-02T16:52:18.4530000Z",
        "CorrelationID": None,
        "Namespace": "GTS.Galaxy.Pass.Created",
        "SchemaVersion": "0.2",
        "Suppressed": None,
        "Retransmit": None,
        "Operation": None,
        "EncryptedRandomSeed": None,
        "Breadcrumb": {"SystemName": "GTS.Galaxy", "timestamp": TEST_TIMESTAMP},
        "PayloadEncoding": "JSON",
    },
    "Payload": '{"pass":{"passAccount":"52200026638","openedDate":"2023-05-02T00:00:00","validDays":0,"passKindId":"6533","validFromDate":"2023-05-02T00:00:00","birthDate":"1955-01-01T00:00:00","price":1399,"tax":0,"useCount":0,"reissueCount":0,"status":0,"limitCount":0,"companyId":"1","categoryId":"809","subcategoryId":"19","taxFlags":"NNNNNNNN","accessCodeId":"80919","visualId":"809190052200026638","functionKeyFlags":"NNNNNNNN","functionKeyKind":0,"priorPassAccount":"","priorPassKindId":"0","noteId":"0","pictureId":"0","discountId":"0","productId":"80919N","maximumUses":0,"taxMethods":"00000000","nodeId":"522","transactionNumber":56855,"contactId":"67089678","adultQuantity":0,"childQuantity":0,"pendingPictureId":"0","customerId":"0","siteId":"0","orderId":"30901657","debitCardId":"0","purchaserContactId":"0","sendToType":0,"maximumPeople":0,"parentPassId":"0","purchaserPassId":"0","scannedVisualId":"809190052200026638","userDefinedFields":[{"index":1,"value":""},{"index":2,"value":""},{"index":3,"value":""},{"index":4,"value":""},{"index":5,"value":""},{"index":6,"value":"NO"},{"index":7,"value":"NO"},{"index":8,"value":""},{"index":9,"value":""},{"index":10,"value":""}],"contact":{"jobTitle":"","firstName":"ALEX","middleName":"","lastName":"CROSS","unformattedLastName":"CROSS","nameTitleId":"0","nameSuffixId":"0","salutation":"","identificationNumber":"","birthDate":"1955-01-01T00:00:00","contactType":7,"gender":1,"ageGroup":0,"phone":"7145551212","fax":"","cell":"","email":"ALEXCROSS@TEST.DISNEY.COM","unformattedPhone":"7145551212","externalId":"","isPrimaryContact":false,"canContactViaEmail":false,"hasSpecialNeeds":false,"isDeceased":false,"address":{"addressType":6,"street1":"132 HARBOR","street2":"","street3":"","city":"GLENDALE","state":"CA","postalCode":"91221","country":"US","wasAddressCorrected":false,"doesAllowMailings":false,"id":"50817313"},"id":"67089678"},"salesChannelId":0,"mustUseByState":0,"termStartDate":"2023-05-02T00:00:00","priorPassId":0,"id":"627286040"},"timestamp":"2023-05-02T09:52:18.453Z","userId":"5129","eventId":"3960650f-f131-4a83-afd4-9836f0a1eead","tags":["809190052200026638"]}',
}

GALAXY_EVENT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "1",
        "data": base64.b64encode(json.dumps(GALAXY_PAYLOAD).encode("utf-8")),  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    },
]

DATA_PIPE_INFO_GALAXY = {
    "metrics": {"error": {"namespace": "event_pipes_validation_errors", "value": 1, "unit": "Count"}},
    "table_path": GAM_TABLE_PATH,
    "default_schema": "TEST_GALAXY",
    "key_to_load": "Payload",
    "data_contracts": [],
    "data_mapper_type": "wrapped",
}

CE_WRAPPED_DINETIME_PAYLOAD = {
    "id": "89d3d5b3-2158-4d10-911f-4f2e1b346169",
    "source": "https://dine-sci-svc.wdprapps.disney.com",
    "subject": "experience.status.update",
    "type": "com.disney.wdpr.fnb.model.event.ExperienceStatusEvent",
    "data": '{"id":"bfb1660d-da98-4286-bf11-300dbc337458","facility":{"id":"90001865","destinationId":"WDW"},"experienceRef":{"id":"1523251234509","type":"DINING_RESERVATION"},"guestRef":{"id":"someSwid","type":"SWID"},"status":"VisitNotified","updatedAt":"2023-08-02T12:08:56.339958-04:00"}',
    "time": "2023-08-02T12:08:56.339958-04:00",
    "specversion": "1.0",
    "datacontenttype": "application/json",
}


DINETIME_EVENT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "1",
        "data": base64.b64encode(json.dumps(CE_WRAPPED_DINETIME_PAYLOAD).encode("utf-8")),  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    },
]
DATA_PIPE_INFO_DINETIME = {
    "metrics": {"error": {"namespace": "event_pipes_validation_errors", "value": 1, "unit": "Count"}},
    "table_path": "experienceRef.type",
    "default_schema": "TEST_DINETIME",
    "key_to_load": "data",
    "data_contracts": [],
    "data_mapper_type": "wrapped",
}

SNAPP_RECORD = {
    "Header": {
        "Breadcrumb": [{"SystemID": "SnApp", "Timestamp": "2023-08-15T22:12:15.813+0000"}],
        "CorrelationId": "Test",
        "DataCommitTimestamp": "2023-08-15T22:12:15.811+0000",
        "DataId": "Test",
        "DispatchTimestamp": "2023-08-15T22:12:15.833+0000",
        "EncryptedRandomSeed": None,
        "MessageId": "Test",
        "MessageTimestamp": "2023-08-15T22:12:15.854+0000",
        "Namespace": "SnApp.Entitlement.TicketSale",
        "Operation": "new",
        "PayloadEncoding": "JSON",
        "Recovery": False,
        "Retransmit": False,
        "SchemaVersion": "1",
        "SourceEventDateTime": "2023-08-15T22:12:15.830+0000",
        "SourceSystemName": "SnApp",
        "SourceSystemVersion": "8.10.1.0.6",
        "Suppressed": False,
        "Version": "1",
    },
    "Payload": {
        "Entitlement": {
            "Account": {
                "Code": "Test",
                "Demographics": {"FirstName": "Test", "OkToEmailOffers": "N"},
                "ExternalReference": [{"Type": "GUID", "Value": "Test"}],
                "Id": "B39FFDD2-F3E6-0041-67DA-0189FB41B1F1",
                "Status": 1,
            },
            "Order": {
                "ExternalReference": [{"Type": "Test", "Value": None}],
                "ReservationCode": "Test",
            },
            "Product": {
                "Code": "Test",
                "ExternallyPriced": True,
                "MetaData": {
                    "APSeasonClass": None,
                    "AnnualPassType": None,
                    "Consume": "T",
                    "MemoryMaker": None,
                    "ProductEntitlementType": "BASE",
                },
                "Name": "1DAY EC ONLY GATE AD",
                "Type": 1,
            },
            "Ticket": {
                "Barcode": "Test",
                "Code": "Test",
                "CreateDate": "Test",
                "Dssn": "Test",
                "ExpiredOnDateTime": "2023-08-19T00:00:00.000+0000",
                "FirstUsageDateTime": None,
                "GroupQuantity": 1,
                "Id": "Test",
                "LastUsageDateTime": None,
                "MagneticCode": " Test ",
                "NoCharge": False,
                "Price": 158.69,
                "PurchaseDate": "2023-08-15",
                "RedemptionPriorityOrder": 1,
                "RemainingValue": 149,
                "SerialNumber": "35163",
                "Site": "DTI",
                "Station": "0",
                "Status": 0,
                "Tax": 9.69,
                "TicketCode": "P:1241.0.230815.35163",
                "UsagesCount": 0,
                "ValidEndDate": "2023-08-19",
                "ValidStartDate": "2023-08-19",
            },
            "Transaction": {
                "Code": "Test",
                "CreateDate": "Test",
                "Dssn": "Test",
                "Id": "Test",
                "SerialNumber": "Test",
                "Site": "DTI",
                "Station": "1",
                "TransactionCode": "Test",
            },
        }
    },
}

SNAPP_EVENT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": base64.b64encode(json.dumps(SNAPP_RECORD).encode("utf-8")),  # pragma: allowlist secret
        "approximateArrivalTimestamp": 1683221732.016,
    }
]

DATA_PIPE_INFO_SNAPP = {
    "metrics": {"error": {"namespace": "event_pipes_validation_errors", "value": 1, "unit": "Count"}},
    "table_path": GAM_TABLE_PATH,
    "default_schema": "testing",
    "data_contracts": [
        {
            "data_contract": "app.src.data_structures.data_contracts.source.snapp.v0.snapp_entitlement_source_data_contract",
            "class_name": "SnAppEntitlementModel",
            "data_contract_version": "v0.1",
            "key_path": [
                {"name": GAM_TABLE_PATH, "value": "SnaApp.Entitlement.Update"},
                {"name": GAM_TABLE_PATH, "value": "SnApp.Entitlement.Redemption"},
                {"name": GAM_TABLE_PATH, "value": "SnApp.Entitlement.TicketSale"},
            ],
            "router_database": "dbname",
            "router_schema": "schema",
            "router_table": "table",
        }
    ],
    "data_mapper_type": "nested",
}


SHOPDISNEY_PAYLOAD = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><order xmlns="http://www.demandware.com/xml/impex/order/2006-10-31" order-no="5002401234"><order-date>2023-10-03T17:56:44.231Z</order-date></order>'


SHOPDISNEY_EVENT = [
    {
        **EVENT_COMMON_METADATA,
        "partitionKey": "test",
        "sequenceNumber": "49640450530655783448641595467156077838773832572853026818",
        "data": base64.b64encode(SHOPDISNEY_PAYLOAD.encode("utf-8")),
        "approximateArrivalTimestamp": 1683221732.016,
    }
]

DATA_PIPE_INFO_SHOPDISNEY = {
    "metrics": {"error": {"namespace": "event_pipes_validation_errors", "value": 1, "unit": "Count"}},
    "default_schema": "testing",
    "data_contracts": [],
    "data_mapper_type": "nested-xml",
}
