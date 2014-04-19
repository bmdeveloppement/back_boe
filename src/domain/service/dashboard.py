# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from sqlalchemy.sql import select


class DashboardService(object):

    @SqlAlchemyConnector.provide_session
    def get_newspaper_global_statistics(self,
                                        date_begin,
                                        date_end,
                                        session=None):
        """Get global statistics"""
        from domain.model.newspaper import Newspaper
        from sqlalchemy import func

        # Build fields
        count = func.count(Newspaper.id).label('count')
        price = func.sum(Newspaper.price).label('price')
        supplier_cost = func.sum(Newspaper.supplier_cost) \
            .label('supplier_cost')
        royalty_cost = func.sum(Newspaper.royalty_cost).label('royalty_cost')

        # Build query
        query = session.query(count, price, supplier_cost, royalty_cost) \
            .filter(Newspaper.date >= date_begin) \
            .filter(Newspaper.date <= date_end)

        # Format keyed tuples to dict
        query_result = query.all().pop(0)
        result = dict(zip(query_result._labels, query_result))

        return result

    @SqlAlchemyConnector.provide_session
    def get_newspaper_date_statistics(self,
                                      date_begin,
                                      date_end,
                                      session=None):
        """Get statistics by date"""
        from domain.model.newspaper import Newspaper
        from sqlalchemy import func

        # Build fields
        count = func.count(Newspaper.id).label('count')
        price = func.sum(Newspaper.price).label('price')
        supplier_cost = func.sum(Newspaper.supplier_cost) \
            .label('supplier_cost')
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
    def get_delivery_global_statistics(self,
                                       date_begin,
                                       date_end,
                                       session=None):
        """Get global statistics"""
        from domain.model.delivery import Delivery
        from sqlalchemy import func

        # Build fields
        count = func.count(Delivery.id).label('count')
        price = func.sum(Delivery.price).label('price')

        # Build query
        query = session.query(count, price) \
            .filter(Delivery.date >= date_begin) \
            .filter(Delivery.date <= date_end)

        # Format keyed tuples to dict
        query_result = query.all().pop(0)
        result = dict(zip(query_result._labels, query_result))

        return result

    @SqlAlchemyConnector.provide_session
    def get_delivery_date_statistics(self,
                                     date_begin,
                                     date_end,
                                     session=None):
        """Get statistics by date"""
        from domain.model.delivery import Delivery
        from sqlalchemy import func

        # Build fields
        count = func.count(Delivery.id).label('count')
        price = func.sum(Delivery.price).label('price')

        # Build query
        query = session.query(count, price, Delivery.date.label('date')) \
            .filter(Delivery.date >= date_begin) \
            .filter(Delivery.date <= date_end) \
            .group_by(Delivery.date).order_by(Delivery.date)

        # Format keyed tuples to dict
        result = []
        for item in query.all():
            result.append(dict(zip(item._labels, item)))

        return result

    @SqlAlchemyConnector.provide_session
    def get_distribution_round_global_statistics(self,
                                                 date_begin,
                                                 date_end,
                                                 session=None):
        """Get global statistics"""
        from domain.model.distribution_round_archive import \
            DistributionRoundArchive
        from sqlalchemy import func

        # Build fields
        count = func.count(DistributionRoundArchive.id).label('count')
        cost = func.sum(DistributionRoundArchive.cost).label('cost')

        # Build query
        query = session.query(count, cost) \
            .filter(DistributionRoundArchive.date >= date_begin) \
            .filter(DistributionRoundArchive.date <= date_end)

        # Format keyed tuples to dict
        query_result = query.all().pop(0)
        result = dict(zip(query_result._labels, query_result))

        return result

    @SqlAlchemyConnector.provide_session
    def get_distribution_round_date_statistics(self,
                                               date_begin,
                                               date_end,
                                               session=None):
        """Get statistics by date"""
        from domain.model.distribution_round_archive import \
            DistributionRoundArchive
        from sqlalchemy import func

        # Build fields
        count = func.count(DistributionRoundArchive.id).label('count')
        cost = func.sum(DistributionRoundArchive.cost).label('cost')

        # Build query
        query = session.query(count, cost, DistributionRoundArchive.date.label('date')) \
            .filter(DistributionRoundArchive.date >= date_begin) \
            .filter(DistributionRoundArchive.date <= date_end) \
            .group_by(DistributionRoundArchive.date) \
            .order_by(DistributionRoundArchive.date)

        # Format keyed tuples to dict
        result = []
        for item in query.all():
            result.append(dict(zip(item._labels, item)))

        return result