# -*- coding: utf-8 -*-

import sqlalchemy.orm.scoping as scoping
from sqlalchemy.exc import SQLAlchemyError


from app import log

LOG = log.get_logger()


class DatabaseSessionManager(object):
    def __init__(self, session_factory, auto_commit=False):
        self._session_factory = session_factory
        self._scoped = isinstance(session_factory, scoping.ScopedSession)
        self._auto_commit = auto_commit

    def process_request(self, req, res, resource=None):
        """
        Handle post-processing of the response (after routing).
        """
        LOG.debug('process_request()..')
        req.context['session'] = self._session_factory()

    def process_response(self, req, res, resource=None):
        """
        Handle post-processing of the response (after routing).
        """
        LOG.debug('process_response()..')
        session = req.context['session']

        if self._auto_commit:
            try:
                session.commit()
            except SQLAlchemyError:
                session.rollback()

        if self._scoped:
            session.rollback()
        else:
            session.close()
