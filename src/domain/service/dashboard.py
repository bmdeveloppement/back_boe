# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from sqlalchemy.sql import select


class DashboardService(object):

    @SqlAlchemyConnector.provide_session
    def get_global_statistics(self,
                              date_begin,
                              date_end,
                              session=None):
        """Get global statistics"""

        result = {}

        # Newspaper
        result['newspaper'] = \
            self.get_newspaper_global_statistics(date_begin, date_end)

        # Delivery
        result['delivery'] = \
            self.get_delivery_global_statistics(date_begin, date_end)

        # Distribution round
        result['distribution_round'] = \
            self.get_distribution_round_global_statistics(date_begin, date_end)

        return result

    @SqlAlchemyConnector.provide_session
    def get_date_statistics(self,
                            date_begin,
                            date_end,
                            session=None):
        """Get statistics by date"""
        from datetime import datetime
        from collections import OrderedDict
        result = {}

        # Fetch newspaper statistics
        newspaper_statistics = \
            self.get_newspaper_date_statistics(date_begin, date_end)

        # Fetch delivery statistics
        delivery_statistics = \
            self.get_delivery_date_statistics(date_begin, date_end)

        # Fetch distribution round statistics
        distribution_round_statistics = \
            self.get_distribution_round_date_statistics(date_begin, date_end)

        # Merge fetched results
        result = self.build_date_result(result,
                                        newspaper_statistics,
                                        'newspaper')
        result = self.build_date_result(result,
                                        delivery_statistics,
                                        'delivery')
        result = self.build_date_result(result,
                                        distribution_round_statistics,
                                        'distribution_round')

        # Order by date
        result = sorted(result.items())

        return result

    def build_date_result(self, result, statistics, key):
        """Merge statistics by date"""
        import dateutil.parser

        # Append result for each date
        for statistic in statistics:
            date = dateutil.parser.parse(str(statistic['date']))
            date = date.strftime('%Y-%m-%d')
            if date not in result:
                result[date] = []
            result[date].append({key: statistic})

        return result

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
            .order_by(DistributionRoundArchive.date) \
            .order_by(DistributionRoundArchive.date)

        # Format keyed tuples to dict
        result = []
        for item in query.all():
            result.append(dict(zip(item._labels, item)))

        return result