import json

# from collections import namedtuple


tests = [
    json.loads(
        """
        {
            "url": "http://myvalidateurl.disney.com",
            "scope_mapper_bucket": "bucket_test",
            "scope_mapper_key": "path/to/my/object_test"
        }
        """
    )
]
