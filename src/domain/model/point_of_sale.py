# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.client import Client
from domain.model.distribution_round import DistributionRound

class PointOfSale(db.Model, Model):
    """Model"""
    __tablename__ = 'point_of_sale'

    id = db.Column(db.Integer(10), primary_key=True)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('client.id'),
                          nullable=False)
    distribution_round_id = db.Column(db.Integer,
                                      db.ForeignKey('distribution_round.id'),
                                      nullable=False)
    delivery_price = db.Column(db.Float(precision=2), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.Integer(11), nullable=False)
    additional_data = db.Column(db.String(100), nullable=True)

    client = db.relationship(Client, uselist=False)
    distribution_round = db.relationship(DistributionRound, uselist=False)
