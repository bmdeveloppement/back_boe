# -*- coding: utf-8 -*-

import logging
from lib.database_utils import SqlAlchemyConnector
from lib.item_utils import copy_items

logger = logging.getLogger(__name__)

class CrudService(object):

    def __init__(self):
        """Init"""
        from_path = 'domain.model.%s' % self.model_name
        magic_import = __import__(from_path, fromlist=[self.model_name])
        self.__model__ = getattr(magic_import, self.model_name.capitalize())
        self.__type__ = self.__model__

    @SqlAlchemyConnector.provide_session
    def get(self, resource_id, session=None):
        """Get an instance"""
        model_instance = session.query(self.__model__).get(resource_id)
        return model_instance

    @SqlAlchemyConnector.provide_session
    def list(self, session=None):
        """List instances"""
        model_instances = session.query(self.__model__).all()
        return model_instances

    @SqlAlchemyConnector.provide_session
    def create(self, request, session=None):
        """Create new instance"""
        try:
            model_instance = self.__model__()
            copy_items(request, model_instance, model_instance.__attribute_list__)
            session.add(model_instance)
            session.commit()
            return model_instance.id
        except Exception as e:
            session.rollback()
            logging.error(repr(e))
            return False

    @SqlAlchemyConnector.provide_session
    def update(self, resource_id, request, session=None):
        """Edit an instance"""
        try:
            model_instance = session.query(self.__model__).get(resource_id)
            copy_items(request, model_instance, model_instance.__attribute_list__)
            session.commit()
            return model_instance.id
        except Exception as e:
            session.rollback()
            logging.error(repr(e))
            return False
