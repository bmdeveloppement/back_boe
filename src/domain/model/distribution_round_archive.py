# -*- coding: utf-8 *-*
from main import db
from domain.model.model import Model
from domain.model.distribution_round import DistributionRound


class DistributionRoundArchive(db.Model, Model):
    """Model"""
    __tablename__ = 'distribution_round_archive'

    id = db.Column(db.Integer(10), primary_key=True)
    distribution_round_id = db.Column(db.Integer,
                                      db.ForeignKey('distribution_round.id'),
                                      nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    cost = db.Column(db.Float(precision=2), nullable=False)

    distribution_round = db.relationship(DistributionRound, uselist=False)
