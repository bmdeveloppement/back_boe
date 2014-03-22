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
        self.model = getattr(magic_import, self.model_name.capitalize())
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
