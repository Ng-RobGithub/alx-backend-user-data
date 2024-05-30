#!/usr/bin/env python3
"""
filtered_logger.py
Contains the filter_datum function to obfuscate PII in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message obfuscated.

    Arguments:
    fields: List of strings representing all fields to obfuscate
    redaction: String representing by what the field will be obfuscated
    message: String representing the log line
    separator: String representing by which character is separating all fields
    in the log line (message)

    Returns:
    The obfuscated log message.
    """
    for field in fields:
        message = re.sub(
            rf"{field}=[^{}]*".format(separator), f"{field}={redaction}",
            message)
    return message
