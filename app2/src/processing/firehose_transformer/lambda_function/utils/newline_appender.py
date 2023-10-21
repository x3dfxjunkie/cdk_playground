""" Function that simply transform base64 data and appends a new line
"""

import base64


def append_new_line(base64_data: str) -> str:
    return base64.b64encode((base64.b64decode(base64_data).decode("ascii") + "\n").encode("ascii")).decode("ascii")
