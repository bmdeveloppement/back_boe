# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.deliverer import DelivererService
from action.crud import crud_actions

current_action = 'deliverer'
deliverer_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=deliverer_bp,
             resource_name=current_action,
             resource_service=DelivererService)