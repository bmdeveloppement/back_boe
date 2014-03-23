# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.newspaper import NewspaperService
from action.crud import crud_actions

current_action = 'newspaper'
newspaper_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=newspaper_bp,
             resource_name=current_action,
             resource_service=NewspaperService)
