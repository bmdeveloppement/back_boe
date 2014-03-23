# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.supplier import Supplier

class PressTitle(db.Model, Model):
    """Model"""
    __tablename__ = 'press_title'
    __attribute_list__ = ['supplier_id', 'name', 'supplier_cost', 
                          'royalty_cost', 'paging']
    __relationships__ = ['supplier_id']

    id = db.Column(db.Integer(10), primary_key=True)
    supplier_id = db.Column(db.Integer,
                            db.ForeignKey('supplier.id'),
                            nullable=False)
    name = db.Column(db.String(50), nullable=False)
    supplier_cost = db.Column(db.Float(precision=2), nullable=False)
    royalty_cost = db.Column(db.Float(precision=2), nullable=False)
    paging = db.Column(db.Integer(10), nullable=False)

    supplier = db.relationship(Supplier, uselist=False)
