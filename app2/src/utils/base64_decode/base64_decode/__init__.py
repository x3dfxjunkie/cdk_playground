"""
base64 decode data or return string
"""

import base64
import binascii


def b64decode(data) -> str:
    """decode base64 data to string

    Args:
        data (bytes-like obj): bytes-like obj

    Returns:
        str: base64 decoded string
    """
    try:
        decoded_data = base64.b64decode(data, validate=True).decode()
    except binascii.Error:
        if isinstance(data, bytes):
            data = data.decode()
        decoded_data = data
    return decoded_data
