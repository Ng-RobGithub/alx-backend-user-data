#!/usr/bin/env python3
""" Protecting PII """

from typing import List
import logging
import re
from mysql.connector import connection
from os import environ

PII_FIELDS = ('name', 'email', 'password', 'ssn', 'phone')


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Returns the log message obfuscated."""
    temp = message
    for field in fields:
        pattern = rf"{field}=[^;]*{separator}"
        replacement = f"{field}={redaction}{separator}"
        temp = re.sub(pattern, replacement, temp)
    return temp


def get_logger() -> logging.Logger:
    """Returns a logger object."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> connection.MySQLConnection:
    """Connect to MySQL server with environmental vars."""
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")

    if not db_name:
        raise ValueError("Database name is not specified in environment variables")

    try:
        connector = connection.MySQLConnection(
            user=username,
            password=password,
            host=db_host,
            database=db_name)
    except Exception as e:
        raise RuntimeError(f"Error connecting to database: {e}")
    return connector


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes the class instance."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records."""
        return filter_datum(
            self.fields, self.REDACTION, super(RedactingFormatter, self).format(record),
            self.SEPARATOR)


def main() -> None:
    """
    Obtain a database connection using get_db
    and retrieve all rows in the users table and display each row
    """
    try:
        db = get_db()
        cur = db.cursor()

        query = 'SELECT * FROM users;'
        cur.execute(query)
        fetch_data = cur.fetchall()

        logger = get_logger()

        for row in fetch_data:
            fields = 'name={}; email={}; phone={}; ssn={}; password={}; ip={}; '\
                     'last_login={}; user_agent={};'
            fields = fields.format(row[0], row[1], row[2], row[3],
                                   row[4], row[5], row[6], row[7])
            logger.info(fields)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    main()
