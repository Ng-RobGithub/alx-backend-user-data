#!/usr/bin/env python3
"""
Password encryption module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the hashed password as bytes.
    
    Args:
    password (str): The password to be hashed.
    
    Returns:
    bytes: The salted, hashed password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
