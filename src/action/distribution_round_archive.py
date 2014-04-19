# -*- coding: utf-8 -*-
from flask import Blueprint

from domain.service.distribution_round_archive import DistributionRoundArchiveService
from action.crud import crud_actions
from lib.json_utils import json_format

current_action = 'distribution_round_archive'
distribution_round_archive_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)
crud_actions(blueprint=distribution_round_archive_bp,
             resource_name=current_action,
             resource_service=DistributionRoundArchiveService)
