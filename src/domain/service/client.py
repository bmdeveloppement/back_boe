# -*- coding: utf-8 -*-

import logging
from lib.database_utils import SqlAlchemyConnector
from lib.item_utils import copy_items
from domain.model.client import Client

logger = logging.getLogger(__name__)

class ClientService(object):

    def __init__(self):
        """Init"""
        self.__type__ = Client

    @SqlAlchemyConnector.provide_session
    def list(self, session=None):
        """List instances"""
        clients = session.query(Client).all()
        return clients

    @SqlAlchemyConnector.provide_session
    def get(self, id, session=None):
        """Get an instance"""
        client = session.query(Client).get(id)
        return client

    @SqlAlchemyConnector.provide_session
    def create(self, request, session=None):
        """Create new instance"""
        try:
            client = Client()
            copy_items(request, client, client.attribute_list)
            session.add(client)
            session.commit()
            return client.id
        except Exception as e:
            session.rollback()
            logging.error(repr(e))
            return False

    @SqlAlchemyConnector.provide_session
    def edit(self, id, request, session=None):
        """Edit an instance"""
        try:
            client = session.query(Client).get(id)
            copy_items(request, client, client.attribute_list)
            session.commit()
            return client.id
        except Exception as e:
            session.rollback()
            logging.error(repr(e))
            return False
