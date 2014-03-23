# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.client import Client
from domain.model.press_title import PressTitle
from domain.model.delivery import Delivery
from domain.model.point_of_sale import PointOfSale

class Supplier(db.Model, Model):
    """Model"""
    __tablename__ = 'supplier'
    __attribute_list__ = ['company_name', 'email_address', 'report', 'reporting_hour']
    __relationships__ = []

    id = db.Column(db.Integer(10), primary_key=True)
    company_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(50), nullable=False)
    report = db.Column(db.Boolean, nullable=False)
    reporting_hour = db.Column(db.DateTime, nullable=True)
