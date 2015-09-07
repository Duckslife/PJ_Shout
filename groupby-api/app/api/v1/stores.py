# -*- coding: utf-8 -*-

from app.api.common import BaseResource
import falcon
from app.model import Store, Menu, Crawling
from app.utils.auth import decrypt_token
from app.utils.pagination import *



class Collection(BaseResource):
    def on_get(self, req, res, page_id):
        session = req.context['session']
        store_db = session.query(Crawling)
        page = SqlalchemyOrmPage(store_db, page= page_id, items_per_page= 20)
        if(int(page_id)< page.last_page):
            rset = [dict(store_name=q.title, contents=q.contents)for q in page]
            rset.append({'next_url_id': int(page_id)+1})
            res.status = falcon.HTTP_200
            res.body = self.to_json(rset)

        elif(int(page_id)== page.last_page):
            rset = [dict(store_name=q.title, address=q.contents)for q in page]
            rset.append({'next_url_id': 'end of pages'})
            res.status = falcon.HTTP_200
            res.body = self.to_json(rset)

        else:
            res.status = falcon.HTTP_400
            res.body = self.to_json({
                'meta':{
                    'code': 401,
                    'message': 'out of range'
                }
            })




class Item(BaseResource):
    def on_get(self, req, res, store_id):
        session = req.context['session']
        token = req.get_header('auth')
        auth_token = decrypt_token(token)
        if auth_token is not None:
            menu_db = (session.query(Store).join(Menu).filter(Store.id == int(store_id)).values(Menu.menuname,
                                                                                                Menu.menu_set_option,
                                                                                                Menu.menu_size_option,
                                                                                                Store.name))
            resullist=[]
            for menuname, menu_set_option, menu_size_option, name in menu_db:
                resullist.append({'menuanme':menuname,
                                  'menu_set_option': menu_set_option,
                                  'menu_size_option': menu_size_option,
                                  'name': name})
            res.status = falcon.HTTP_200
            res.body = self.to_json(resullist)

        else:
            res.status = falcon.HTTP_400
            res.body = self.to_json({
                    'meta': {
                        'code': 401,
                        'message': 'password not match'
                    }
                })

class Place(BaseResource):
    def on_get(self, req, res):
        pass

    def on_post(self, req, res):
        pass
