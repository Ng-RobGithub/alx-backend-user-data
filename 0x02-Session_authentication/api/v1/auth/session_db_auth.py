#!/usr/bin/env python3
"""Session authentication with expiration
and storage support module for the API.
"""
from flask import request
from datetime import datetime, timedelta
from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Session authentication class with expiration and storage support.
    """

    def create_session(self, user_id=None) -> str:
        """Creates and stores a session id for the user.

        Args:
            user_id (str): The user id for which the session is created.

        Returns:
            str: The session id created for the user.
        """
        session_id = super().create_session(user_id)
        if isinstance(session_id, str):
            user_session = UserSession(user_id=user_id, session_id=session_id)
            user_session.save()
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None):
        """Retrieves the user id associated with a given session id.

        Args:
            session_id (str): The session id.

        Returns:
            str: The user id associated with the session id, or None
            if not found or expired.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not sessions:
            return None
        session = sessions[0]
        if session.is_expired(self.session_duration):
            return None
        return session.user_id

    def destroy_session(self, request=None) -> bool:
        """Destroys an authenticated session.

        Args:
            request: The current request.

        Returns:
            bool: True if the session was successfully destroyed,
            False otherwise.
        """
        session_id = self.session_cookie(request)
        if session_id is None or not isinstance(session_id, str):
            return False
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if not sessions:
            return False
        sessions[0].remove()
        return True
