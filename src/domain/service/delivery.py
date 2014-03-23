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
        if model_instance:
            result = model_instance.dump()
            result['distribution_round'] = model_instance.distribution_round.dump()
            result['point_of_sale'] = model_instance.point_of_sale.dump()
            return result
        else:
            return None
