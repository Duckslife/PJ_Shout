# -*- coding: utf-8 -*-

import falcon
import re

from sqlalchemy.orm.exc import NoResultFound

from app import log
from app.api.common import BaseResource
from app.utils.hooks import auth_required
from app.utils.auth import encrypt_token, hash_password, verify_password, uuid

from app.model import User

LOG = log.get_logger()

AUTH_ID_EMAIL = 'email:%s'
AUTH_ID_FACEBOOK = 'facebook:%s'


class Collection(BaseResource):
    """
    Handle for endpoint: /v1/users
    """
    def on_post(self, req, res):
        session = req.context['session']
        user_req = self.load_request(req, res)

        if user_req is not None:
            auth_id = AUTH_ID_EMAIL % user_req['email']
            user = User()
            user.username = user_req['username']
            user.email = user_req['email']
            user.password = hash_password(user_req['password']).decode('utf-8')
            user.lat = user_req['lat']
            user.lng = user_req['lng']
            user.phone = user_req['phone']
            user.auth_id = auth_id
            user.token = encrypt_token(auth_id + ':' + uuid()).decode('utf-8')
            user.attr = user_req['attr']
            session.add(user)
            res.status = falcon.HTTP_201
            res.body = self.to_json({
                'meta': {
                    'code': 201
                }
            })
        else:
            self.abort(falcon.HTTP_400, "Invalid Parameter")

    def on_get(self, req, res):
        session = req.context['session']
        users_db = session.query(User).all()
        res.status = falcon.HTTP_200
        res.body = self.from_db_to_json(users_db)


class Item(BaseResource):
    """
    Handle for endpoint: /v1/users/{user_id}
    """
    def on_get(self, req, res, user_id):
        pass


class Self(BaseResource):
    """
    Handle for endpoint: /v1/users/self
    """
    LOGIN = 'login'
    LOGOUT = 'logout'
    RESETPW = 'resetpw'

    def on_get(self, req, res):
        cmd = re.split('\\W+', req.path)[-1:][0]
        LOG.debug("cmd in Self: %s", cmd)
        if cmd == Self.LOGIN:
            self.process_login(req, res)
        elif cmd == Self.LOGOUT:
            self.process_logout(req, res)
        elif cmd == Self.RESETPW:
            self.process_resetpw(req, res)

    def process_login(self, req, res):
        email = req.params['email']
        print(email)
        password = req.params['password']
        LOG.info("login from %s", req.params['email'])
        session = req.context['session']
        try:
            user_db = session.query(User).filter(User.email == email).one()
            LOG.info("User from db:%s", user_db)
            if verify_password(password, user_db.password.encode('utf-8')):
                res.status = falcon.HTTP_200
                res.body = self.to_json(user_db.to_dict())
            else:
                res.status = falcon.HTTP_401
                res.body = self.to_json({
                    'meta': {
                        'code': 401,
                        'message': 'password not match'
                    }
                })
        except NoResultFound:
            res.status = falcon.HTTP_404
            res.body = self.to_json({
                'meta': {
                    'code': 404,
                    'message': 'user not exists'
                }
            })

    @falcon.before(auth_required)
    def process_logout(self, req, res):
        LOG.info("logout from %s", req.context['auth_user'])
        pass

    @falcon.before(auth_required)
    def process_resetpw(self, req, res):
        LOG.info("resetpw from %s", req.context['auth_user'])
        pass
