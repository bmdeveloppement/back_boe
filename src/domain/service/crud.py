# -*- coding: utf-8 -*-

import logging
from lib.database_utils import SqlAlchemyConnector
from lib.item_utils import copy_items

logger = logging.getLogger(__name__)


class CrudService(object):

    def __init__(self):
        """Init"""
        # Import model path from model_name
        from_path = 'domain.model.%s' % self.model_name
        magic_import = __import__(from_path, fromlist=[self.model_name])

        # Generate the CamelCase model classname
        model_class_name = ''
        for model_class_name_split in self.model_name.split('_'):
            model_class_name += model_class_name_split.capitalize()

        # Import model from generated classname
        self.__model__ = getattr(magic_import, model_class_name)
        self.__type__ = self.__model__

        # List of parameters used on models
        self.model_parameters = ['order_by', 'limit', 'offset']

    def get_columns(self):
        """Get columns of the current table"""
        columns = [str(column).replace(self.model_name + '.', '')
                   for column in self.__model__.__table__.columns]
        columns.remove('id')
        return columns

    def get_relationships(self):
        """Get relationships of the current table, from forein keys"""
        relationships = [str(foreign_key.parent.name).replace('_id', '')
                         for foreign_key in self.__model__.__table__.foreign_keys]
        return relationships

    @SqlAlchemyConnector.provide_session
    def get(self, resource_id, session=None):
        """Get an instance"""
        model_instance = session.query(self.__model__).get(resource_id)
        return model_instance

    @SqlAlchemyConnector.provide_session
    def get_full(self, resource_id, session=None):
        """Get an instance with loading subinstances"""
        model_instance = session.query(self.__model__).get(resource_id)
        if model_instance:
            result = model_instance.dump()
            try:
                for relationship in self.get_relationships():
                    result[relationship] = getattr(model_instance, relationship).dump()
                return result
            except Exception as e:
                logging.error(repr(e))
                return False
        else:
            return None

    @SqlAlchemyConnector.provide_session
    def list(self, request=None, session=None):
        """List instances"""
        session_query = session.query(self.__model__)
        for param in self.model_parameters:
            if param in request:
                session_query = getattr(session_query, param)(request[param])
        return session_query.all()

    @SqlAlchemyConnector.provide_session
    def list_field(self, field_name, request=None, session=None):
        """List instances by field"""
        session_query = session.query(self.__model__.id,
                                      getattr(self.__model__, field_name))
        for param in self.model_parameters:
            if param in request:
                session_query = getattr(session_query, param)(request[param])
        return session_query.all()

    @SqlAlchemyConnector.provide_session
    def create(self, request, session=None):
        """Create new instance"""
        try:
            model_instance = self.__model__()
            copy_items(request, model_instance, self.get_columns())
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
            copy_items(request, model_instance, self.get_columns())
            session.commit()
            return model_instance.id
        except Exception as e:
            session.rollback()
            logging.error(repr(e))
            return False
