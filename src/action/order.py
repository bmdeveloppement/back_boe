# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.order import OrderService
from action.crud import crud_actions

current_action = 'order'
order_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=order_bp,
             resource_name=current_action,
             resource_service=OrderService)
