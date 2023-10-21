import base64
import json
from typing import Dict, List


def mock_event(stream_name: str, records: List[Dict]) -> Dict:
    """
    Utility function to create a mock event for the processing lambda
    Receives a Dict and embeds it within a Kinesis event data object (base64 encoded)

    Args:
        stream_name (str): The name of the stream
        records (List[Dict]): The records to embed in the event

    Returns:
        Dict: The mock event
    """
    return {
        "Records": [
            {
                "eventSourceARN": f"arn:aws:kinesis:us-east-1:000000000000:stream/{stream_name}",
                "kinesis": {
                    "data": base64.b64encode(json.dumps(record).encode("utf-8")).decode(
                        "utf-8"
                    )
                },
            }
            for record in records
        ]
    }
