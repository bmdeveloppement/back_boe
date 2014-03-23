# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from domain.service.crud import CrudService
from domain.model.distribution_round import DistributionRound


class DistributionRoundService(CrudService):

    model_name = 'distribution_round'

    def __init__(self):
        """Init"""
        self.__model__ = DistributionRound
        self.__type__ = DistributionRound

    @SqlAlchemyConnector.provide_session
    def get_full(self, resource_id, session=None):
        """Get an instance"""
        model_instance = session.query(DistributionRound).get(resource_id)
        if model_instance:
            result = model_instance.dump()
            result['deliverer'] = model_instance.deliverer.dump()
            return result
        else:
            return None
