# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.client import ClientService
from action.crud import crud_actions

current_action = 'client'
client_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=client_bp,
             resource_name=current_action,
             resource_service=ClientService)