#!/usr/bin/env python3
"""Session authentication with expiration module for the API.
"""
import os
from flask import request
from datetime import datetime, timedelta

from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Session authentication class with expiration.
    """

    def __init__(self) -> None:
        """Initializes a new SessionExpAuth instance.

        Reads the session duration from environment variables.
        """
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', '0'))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None) -> str:
        """Creates a session id for the user.

        Args:
            user_id (str): The user id for which the session is created.

        Returns:
            str: The session id created for the user.
        """
        session_id = super().create_session(user_id)
        if isinstance(session_id, str):
            self.user_id_by_session_id[session_id] = {
                'user_id': user_id,
                'created_at': datetime.now(),
            }
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None) -> str:
        """Retrieves the user id associated with a given session id.

        Args:
            session_id (str): The session id.

        Returns:
            str: The user id associated with the session id,
            or None if not found or expired.
        """
        if session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict['user_id']
            if 'created_at' in session_dict:
                cur_time = datetime.now()
                time_span = timedelta(seconds=self.session_duration)
                exp_time = session_dict['created_at'] + time_span
                if exp_time >= cur_time:
                    return session_dict['user_id']
        return None
