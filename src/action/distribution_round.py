# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.distribution_round import DistributionRoundService
from action.crud import crud_actions
from lib.json_utils import json_format

current_action = 'distribution_round'
distribution_round_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=distribution_round_bp,
             resource_name=current_action,
             resource_service=DistributionRoundService)


@distribution_round_bp.route('/get_full/<int:reference_id>', methods=['GET'])
@json_format
def get_full(reference_id):
    """Get full details"""
    return DistributionRoundService().get_full(reference_id)
