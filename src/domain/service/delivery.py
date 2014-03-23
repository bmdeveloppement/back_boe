# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from domain.service.crud import CrudService
from domain.model.delivery import Delivery


class DeliveryService(CrudService):

    model_name = 'delivery'

    def __init__(self):
        """Init"""
        self.__model__ = Delivery
        self.__type__ = Delivery

    @SqlAlchemyConnector.provide_session
    def get_full(self, resource_id, session=None):
        """Get an instance"""
        model_instance = session.query(Delivery).get(resource_id)
        result = model_instance.dump()
        result['client'] = model_instance.client.dump()
        return result
