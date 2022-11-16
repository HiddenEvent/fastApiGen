from typing import List
from sqlalchemy.orm import Session


class SessionControl:
    def __init__(self):
        self._session = None
        self._schema = None

    def initialize(self, sess, schema):
        if not sess or not schema:
            raise Exception("No Session")
        self._session = sess
        self._schema = schema

    @property
    def get_session(self):
        return self._session


session = SessionControl()
