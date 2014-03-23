# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.client import Client
#from domain.model.DistributionRound import DistributionRound

class Delivery(db.Model, Model):
    """Model"""
    __tablename__ = 'delivery'
    __attribute_list__ = ['client_id']

    id = db.Column(db.Integer(10), primary_key=True)
    #distribution_round_id = db.Column(db.Integer,
    #                                  db.ForeignKey('distribution_round.id'),
    #                                  nullable=False)
    #point_of_sale_id = db.Column(db.Integer,
    #                            db.ForeignKey('point_of_sale.id'),
    #                            nullable=False)
    #date
    #price
    client_id = db.Column(db.Integer,
                          db.ForeignKey('client.id'),
                          nullable=False)

    client = db.relationship(Client, uselist=False)  # , lazy='joined'
