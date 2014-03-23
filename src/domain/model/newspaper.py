# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.client import Client
from domain.model.press_title import PressTitle
from domain.model.delivery import Delivery
from domain.model.point_of_sale import PointOfSale

class Newspaper(db.Model, Model):
    """Model"""
    __tablename__ = 'newspaper'
    __attribute_list__ = ['client_id', 'press_title_id', 'delivery_id', 'point_of_sale_id',
                          'date', 'price', 'supplier_cost', 'royalty_cost', 'paging', 'unsold']
    __relationships__ = ['client', 'press_title', 'delivery', 'point_of_sale']

    id = db.Column(db.Integer(10), primary_key=True)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('client.id'),
                          nullable=False)
    press_title_id = db.Column(db.Integer,
                               db.ForeignKey('press_title.id'),
                               nullable=False)
    delivery_id = db.Column(db.Integer,
                            db.ForeignKey('delivery.id'),
                            nullable=False)
    point_of_sale_id = db.Column(db.Integer,
                                 db.ForeignKey('point_of_sale.id'),
                                 nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    supplier_cost = db.Column(db.Float(precision=2), nullable=False)
    royalty_cost = db.Column(db.Float(precision=2), nullable=False)
    paging = db.Column(db.Integer(11), nullable=False)
    unsold = db.Column(db.Boolean, nullable=False)

    client = db.relationship(Client, uselist=False)
    press_title = db.relationship(PressTitle, uselist=False)
    delivery = db.relationship(Delivery, uselist=False)
    point_of_sale = db.relationship(PointOfSale, uselist=False)
