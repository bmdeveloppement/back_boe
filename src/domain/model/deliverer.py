# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model


class Deliverer(db.Model, Model):
    """Model"""
    __tablename__ = 'deliverer'

    id = db.Column(db.Integer(10), primary_key=True)
    company_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(50), nullable=False)