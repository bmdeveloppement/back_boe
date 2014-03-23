# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.point_of_sale import PointOfSaleService
from action.crud import crud_actions
from lib.json_utils import json_format

current_action = 'point_of_sale'
point_of_sale_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=point_of_sale_bp,
             resource_name=current_action,
             resource_service=PointOfSaleService)


@point_of_sale_bp.route('/get_full/<int:reference_id>', methods=['GET'])
@json_format
def get_full(reference_id):
    """Get full details"""
    return PointOfSaleService().get_full(reference_id)
