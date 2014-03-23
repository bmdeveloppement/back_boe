# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.supplier_price import SupplierPriceService
from action.crud import crud_actions

current_action = 'supplier_price'
supplier_price_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=supplier_price_bp,
             resource_name=current_action,
             resource_service=SupplierPriceService)
