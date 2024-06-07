#!/usr/bin/env python3
"""Session authentication module for the API.
"""
from uuid import uuid4
from flask import request

from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session authentication class.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id for the user.

        Args:
            user_id (str): The user id.

        Returns:
            str: The session id created for the user.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the user id of the user associated with
        a given session id.

        Args:
            session_id (str): The session id.

        Returns:
            str: The user id associated with the session id.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """Retrieves the user associated with the request.

        Args:
            request: The current request.

        Returns:
            User: The user associated with the request.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Destroys an authenticated session.

        Args:
            request: The current request.

        Returns:
            bool: True if the session was successfully destroyed,
            False otherwise.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
            return True
        return False
