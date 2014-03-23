# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.press_title import PressTitle
from domain.model.client import Client

class SupplierPrice(db.Model, Model):
    """Model"""
    __tablename__ = 'supplier_price'
    __attribute_list__ = ['press_title_id', 'client_id', 'value']
    __relationships__ = ['press_title', 'client']

    id = db.Column(db.Integer(10), primary_key=True)
    press_title_id = db.Column(db.Integer,
                               db.ForeignKey('press_title.id'),
                               nullable=False)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('client.id'),
                          nullable=False)
    value = db.Column(db.Float(precision=2), nullable=False)

    press_title = db.relationship(PressTitle, uselist=False)
    client = db.relationship(Client, uselist=False)
