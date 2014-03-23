# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.press_title import PressTitle
from domain.model.point_of_sale import PointOfSale

class Order(db.Model, Model):
    """Model"""
    __tablename__ = 'order'
    __attribute_list__ = ['press_title_id', 'point_of_sale_id', 'order_date',
                          'delivery_date', 'quantity']
    __relationships__ = ['press_title', 'point_of_sale']

    id = db.Column(db.Integer(10), primary_key=True)
    press_title_id = db.Column(db.Integer,
                               db.ForeignKey('press_title.id'),
                               nullable=False)
    point_of_sale_id = db.Column(db.Integer,
                                 db.ForeignKey('point_of_sale.id'),
                                 nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer(11), nullable=False)

    press_title = db.relationship(PressTitle, uselist=False)
    point_of_sale = db.relationship(PointOfSale, uselist=False)
