# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from sqlalchemy.sql import select


class DashboardService(object):

    @SqlAlchemyConnector.provide_session
    def get_newspaper_global_statistics(self, date_begin, date_end, session=None):
        """Get statistics by date"""
        from domain.model.newspaper import Newspaper
        from sqlalchemy import func

        # Build fields
        count = func.count(Newspaper.id).label('count')
        price = func.sum(Newspaper.price).label('price')
        supplier_cost = func.sum(Newspaper.supplier_cost).label('supplier_cost')
        royalty_cost = func.sum(Newspaper.royalty_cost).label('royalty_cost')

        # Build query
        query = session.query(count, price, supplier_cost, royalty_cost) \
            .filter(Newspaper.date >= date_begin) \
            .filter(Newspaper.date <= date_end) \
            .order_by(Newspaper.date)

        # Format keyed tuples to dict
        query_result = query.all().pop(0)
        print query_result
        result = dict(zip(query_result._labels, query_result))

        return result

    @SqlAlchemyConnector.provide_session
    def get_newspaper_date_statistics(self, date_begin, date_end, session=None):
        """Get statistics by date"""
        from domain.model.newspaper import Newspaper
        from sqlalchemy import func

        # Build fields
        count = func.count(Newspaper.id).label('count')
        price = func.sum(Newspaper.price).label('price')
        supplier_cost = func.sum(Newspaper.supplier_cost).label('supplier_cost')
        royalty_cost = func.sum(Newspaper.royalty_cost).label('royalty_cost')

        # Build query
        query = session.query(count, price, supplier_cost, royalty_cost,
                              Newspaper.date.label('date')) \
            .filter(Newspaper.date >= date_begin) \
            .filter(Newspaper.date <= date_end) \
            .group_by(Newspaper.date).order_by(Newspaper.date)

        # Format keyed tuples to dict
        result = []
        for item in query.all():
            result.append(dict(zip(item._labels, item)))

        return result

    @SqlAlchemyConnector.provide_session
    def get_delivery_statistics(self, date_begin, date_end, session=None):
        """Get statistics by date"""
        from domain.model.delivery import Delivery
        model_instance = session.query(Delivery).get(resource_id)
        return 'pipo'