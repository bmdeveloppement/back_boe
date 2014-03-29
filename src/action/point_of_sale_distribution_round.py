# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.point_of_sale_distribution_round import PointOfSaleDistributionRoundService
from action.crud import crud_actions

current_action = 'point_of_sale_distribution_round'
point_of_sale_distribution_round_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=point_of_sale_distribution_round_bp,
             resource_name=current_action,
             resource_service=PointOfSaleDistributionRoundService)
