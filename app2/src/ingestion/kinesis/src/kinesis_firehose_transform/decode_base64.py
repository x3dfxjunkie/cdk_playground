import base64
import json


def lambda_handler(event, context) -> dict:
    """    Lambda Function to base64 decode the messages. This is part of the Kinesis Firehose resource
    to write the messages being received on the Kinesis Data Stream to the Raw S3 layer.

    Args:
        event (_type_): incoming events
        context (_type_): context

    Returns:
        dict: returns json (dict) payload which is base64 decoded
    """

    try:
        output = []
        for record in event['records']:

            # print("recordId: %s" % record['recordId'])
            payload = base64.b64decode(record['data'])

            # Do custom processing on the payload here

            # 'recordId': record['recordId'],
            output_record = {
                'result': 'Ok',
                'data': payload
            }
            output.append(output_record)

        print('Successfully processed {} records.'.format(
            len(event['records'])))

        return {'records': output}
    except:
        raise
