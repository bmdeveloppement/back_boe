# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.point_of_sale import PointOfSale
from domain.model.distribution_round import DistributionRound

class PointOfSaleDistributionRound(db.Model, Model):
    """Model"""
    __tablename__ = 'point_of_sale_distribution_round'

    id = db.Column(db.Integer(10), primary_key=True)
    point_of_sale_id = db.Column(db.Integer,
                            db.ForeignKey('point_of_sale.id'),
                            nullable=False)
    distribution_round_id = db.Column(db.Integer,
                            db.ForeignKey('distribution_round.id'),
                            nullable=False)

    point_of_sale = db.relationship(PointOfSale, uselist=False)
    distribution_round = db.relationship(DistributionRound, uselist=False)
