# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.distribution_round import DistributionRound
#from domain.model.point_of_sale import PointOfSale

class Delivery(db.Model, Model):
    """Model"""
    __tablename__ = 'delivery'
    __attribute_list__ = ['distribution_round_id', 'point_of_sale_id',
                          'date', 'price']

    id = db.Column(db.Integer(10), primary_key=True)
    distribution_round_id = db.Column(db.Integer,
                                      db.ForeignKey('distribution_round.id'),
                                      nullable=False)
    point_of_sale_id = db.Column(db.Integer(10), nullable=False)
    #point_of_sale_id = db.Column(db.Integer,
    #                             db.ForeignKey('point_of_sale.id'),
    #                             nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    distribution_round = db.relationship(DistributionRound, uselist=False)
    #point_of_sale = db.relationship(PointOfSale, uselist=False)
