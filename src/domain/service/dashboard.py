# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from sqlalchemy.sql import select


class DashboardService(object):

    @SqlAlchemyConnector.provide_session
    def get_newspaper_statistics(self, date_begin, date_end, session=None):
        """Get statistics by date"""
        from domain.model.newspaper import Newspaper
        model_instance = session.query(Newspaper).filter_by(Newspaper.date>date_begin).get(resource_id)

        if model_instance:
            result = model_instance.dump()
            result['newspaper'] = model_instance.newspaper.dump()
            return result
        else:
            return None

    @SqlAlchemyConnector.provide_session
    def get_delivery_statistics(self, date_begin, date_end, session=None):
        """Get statistics by date"""
        from domain.model.delivery import Delivery
        model_instance = session.query(Delivery).get(resource_id)
        return 'pipo'