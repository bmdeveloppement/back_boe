# -*- coding: utf-8 -*-

import logging
from lib.database_utils import SqlAlchemyConnector
from lib.item_utils import copy_items
from domain.model.client import Client

logger = logging.getLogger(__name__)

class ClientService(object):

    def __init__(self, model_name):
        """Init"""
        from_path = 'domain.model.client'
        magic_import = __import__(from_path, fromlist=['client'])
        self.model = magic_import.Client
        self.__type__ = self.model

    @SqlAlchemyConnector.provide_session
    def list(self, session=None):
        """List instances"""
        model_instances = session.query(self.model).all()
        return model_instances

    @SqlAlchemyConnector.provide_session
    def get(self, id, session=None):
        """Get an instance"""
        model_instance = session.query(self.model).get(id)
        return model_instance

    @SqlAlchemyConnector.provide_session
    def create(self, request, session=None):
        """Create new instance"""
        try:
            model_instance = self.model()
            copy_items(request, model_instance, model_instance.attribute_list)
            session.add(model_instance)
            session.commit()
            return model_instance.id
        except Exception as e:
            session.rollback()
            logging.error(repr(e))
            return False

    @SqlAlchemyConnector.provide_session
    def edit(self, id, request, session=None):
        """Edit an instance"""
        try:
            model_instance = session.query(self.model).get(id)
            copy_items(request, model_instance, model_instance.attribute_list)
            session.commit()
            return model_instance.id
        except Exception as e:
            session.rollback()
            logging.error(repr(e))
            return False
