# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from sqlalchemy.sql import select


class DashboardService(object):

    @SqlAlchemyConnector.provide_session
    def get_newspaper_statistics(self, date_begin, date_end, session=None):
        """Get statistics by date"""
        # Execute specific query
        rows = session.execute("""SELECT date, COUNT(id) AS newspaper_count,
            SUM(price) AS price,SUM(supplier_cost) AS supplier_cost,
            SUM(royalty_cost) AS royalty_cost
            FROM newspaper
            WHERE date >= :date_begin AND date <= :date_end
            GROUP BY date""",
            {'date_begin': date_begin, 'date_end': date_end})
        result = {}
        for row in rows:
            print row
            result[row['date']] = row

        return result

    @SqlAlchemyConnector.provide_session
    def get_delivery_statistics(self, date_begin, date_end, session=None):
        """Get statistics by date"""
        from domain.model.delivery import Delivery
        model_instance = session.query(Delivery).get(resource_id)
        return 'pipo'