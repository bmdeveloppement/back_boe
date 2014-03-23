# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.deliverer import Deliverer

class DistributionRound(db.Model, Model):
    """Model"""
    __tablename__ = 'distribution_round'
    __attribute_list__ = ['deliverer_id', 'name', 'cost', 'schedule']
    __relationships__ = ['deliverer']

    id = db.Column(db.Integer(10), primary_key=True)
    deliverer_id = db.Column(db.Integer,
                            db.ForeignKey('deliverer.id'),
                            nullable=False)
    name = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Float(precision=2), nullable=False)
    schedule = db.Column(db.String(500), nullable=False)

    deliverer = db.relationship(Deliverer, uselist=False)
