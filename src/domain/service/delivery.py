# -*- coding: utf-8 -*-
import json
from lib.database_utils import SqlAlchemyConnector
from domain.service.crud import CrudService
from domain.model.delivery import Delivery


class DeliveryService(CrudService):

    model_name = 'delivery'

    def __init__(self):
        self.__type__ = Delivery


    @SqlAlchemyConnector.provide_session
    def get_full(self, resource_id, session=None):
        """Get an instance"""
        model_instance = session.query(Delivery).get(resource_id)
        print model_instance.client_id
        print model_instance.client.company_name
        print model_instance.dump()
        #print json.loads(model_instance)
        return json.dumps(model_instance.dump())