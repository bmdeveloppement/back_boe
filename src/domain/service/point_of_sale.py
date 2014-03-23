# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from domain.service.crud import CrudService
from domain.model.point_of_sale import PointOfSale


class PointOfSaleService(CrudService):

    model_name = 'point_of_sale'

    def __init__(self):
        """Init"""
        self.__model__ = PointOfSale
        self.__type__ = PointOfSale

    @SqlAlchemyConnector.provide_session
    def get_full(self, resource_id, session=None):
        """Get an instance"""
        model_instance = session.query(PointOfSale).get(resource_id)
        if model_instance:
            result = model_instance.dump()
            result['client'] = model_instance.client.dump()
            result['distribution_round'] = model_instance.distribution_round.dump()
            return result
        else:
            return None
