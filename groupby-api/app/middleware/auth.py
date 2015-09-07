# -*- coding: utf-8 -*-

from app import log
from app.utils.auth import decrypt_token

LOG = log.get_logger()


class AuthHandler(object):

    def process_request(self, req, res):
        LOG.debug("process_request() - Authorization: %s", req.auth)
        if req.auth is not None:
            token = decrypt_token(req.auth)
            # req.auth is like 'gAAAAABVwMgBhGf2xwfp4U3LuRUu7zToGxrrUZeWpRQxBPCPV-IZ2gZGtHBRQCqpP-16_ICFdgzE3YdKphQYcZ_PYYIdNGjhGFsxppag_B7yvmgQ6WceWF7lv3v8anr5o-m5-sOVtF1HdFm5zUxH1vW4vjgWsf4o6g=='
            # the decrypted token is like 'auth_type:id(email|facebook id):secret'
            # ex) 'email:interpolar.test1@gmail.com:CEfYjjxFWVh4aLUrAe9BMNaV'
            req.context['auth_user'] = token.decode('utf-8') if token else None
        else:
            req.context['auth_user'] = None
