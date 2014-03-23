# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.supplier import SupplierService
from action.crud import crud_actions

current_action = 'supplier'
supplier_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=supplier_bp,
             resource_name=current_action,
             resource_service=SupplierService)
