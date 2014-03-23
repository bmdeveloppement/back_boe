# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.press_title import PressTitleService
from action.crud import crud_actions

current_action = 'press_title'
press_title_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=press_title_bp,
             resource_name=current_action,
             resource_service=PressTitleService)
