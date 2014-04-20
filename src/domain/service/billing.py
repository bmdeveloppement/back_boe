# -*- coding: utf-8 -*-
from lib.database_utils import SqlAlchemyConnector
from sqlalchemy.sql import select


class BillingService(object):

    @SqlAlchemyConnector.provide_session
    def get_client_newspaper(self, date_begin, date_end, session=None):
        """Get client newspaper billing"""
        from domain.model.newspaper import Newspaper
        from domain.model.press_title import PressTitle
        from domain.model.client import Client
        from sqlalchemy import func

        # Build fields
        count = func.count(Newspaper.id).label('count')
        name = PressTitle.name.label('name')
        price = func.sum(Newspaper.price).label('price')
        supplier_cost = func.sum(Newspaper.supplier_cost) \
            .label('supplier_cost')
        royalty_cost = func.sum(Newspaper.royalty_cost).label('royalty_cost')
        unsold = func.sum(Newspaper.unsold).label('unsold')
        client_id = Client.id.label('client_id')
        client_company_name = Client.company_name.label('client_company_name')

        # Build query
        query = session.query(count, name, price, supplier_cost,
                              royalty_cost, unsold,
                              client_id, client_company_name) \
            .join(Client, Newspaper.client_id == Client.id) \
            .join(PressTitle, Newspaper.press_title_id == PressTitle.id) \
            .filter(Newspaper.date >= date_begin) \
            .filter(Newspaper.date <= date_end) \
            .group_by(Client.id, PressTitle.id)

        # Format keyed tuples to dict
        result = []
        for item in query.all():
            result.append(dict(zip(item._labels, item)))

        return result

    @SqlAlchemyConnector.provide_session
    def get_client_delivery(self, date_begin, date_end, session=None):
        """Get client delivery billing"""
        from domain.model.delivery import Delivery
        from domain.model.point_of_sale import PointOfSale
        from domain.model.client import Client
        from sqlalchemy import func

        # Build fields
        count = func.count(Delivery.id).label('count')
        price = func.sum(Delivery.price).label('price')
        client_id = Client.id.label('client_id')
        client_company_name = Client.company_name.label('client_company_name')

        # Build query
        query = session.query(count, price,
                              client_id, client_company_name) \
            .join(PointOfSale, Delivery.point_of_sale_id == PointOfSale.id) \
            .join(Client, PointOfSale.client_id == Client.id) \
            .filter(Delivery.date >= date_begin) \
            .filter(Delivery.date <= date_end) \
            .group_by(Client.id)

        # Format keyed tuples to dict
        result = []
        for item in query.all():
            result.append(dict(zip(item._labels, item)))

        return result

    @SqlAlchemyConnector.provide_session
    def get_supplier(self, date_begin, date_end, session=None):
        """Get supplier billing"""
        from domain.model.newspaper import Newspaper
        from domain.model.press_title import PressTitle
        from domain.model.supplier import Supplier
        from sqlalchemy import func

        # Build fields
        count = func.count(Newspaper.id).label('count')
        supplier_cost = func.sum(Newspaper.supplier_cost) \
            .label('supplier_cost')
        royalty_cost = func.sum(Newspaper.royalty_cost).label('royalty_cost')
        unsold = func.sum(Newspaper.unsold).label('unsold')
        supplier_id = Supplier.id.label('provider_id')
        supplier_company_name = Supplier.company_name \
            .label('provider_company_name')

        # Build query
        query = session.query(count, supplier_cost,
                              royalty_cost, unsold,
                              supplier_id, supplier_company_name) \
            .join(PressTitle, Newspaper.press_title_id == PressTitle.id) \
            .join(Supplier, PressTitle.supplier_id == Supplier.id) \
            .filter(Newspaper.date >= date_begin) \
            .filter(Newspaper.date <= date_end) \
            .group_by(Supplier.id)

        # Format keyed tuples to dict
        result = []
        for item in query.all():
            result.append(dict(zip(item._labels, item)))

        return result

    @SqlAlchemyConnector.provide_session
    def get_deliverers(self, date_begin, date_end, session=None):
        """Get deliverer billing"""
        from domain.model.distribution_round \
            import DistributionRound
        from domain.model.distribution_round_archive \
            import DistributionRoundArchive
        from domain.model.deliverer import Deliverer
        from sqlalchemy import func

        # Build fields
        count = func.count(DistributionRoundArchive.id).label('count')
        cost = func.sum(DistributionRoundArchive.cost) \
            .label('cost')
        deliverer_id = Deliverer.id.label('deliverer_id')
        deliverer_company_name = Deliverer.company_name \
            .label('deliverer_company_name')

        # Build query
        query = session.query(count, cost,
                              deliverer_id, deliverer_company_name) \
            .join(DistributionRound, DistributionRoundArchive.distribution_round_id == DistributionRound.id) \
            .join(Deliverer, DistributionRound.deliverer_id == Deliverer.id) \
            .filter(DistributionRoundArchive.date >= date_begin) \
            .filter(DistributionRoundArchive.date <= date_end) \
            .group_by(Deliverer.id)

        # Format keyed tuples to dict
        result = []
        for item in query.all():
            result.append(dict(zip(item._labels, item)))

        return result