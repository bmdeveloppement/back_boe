# -*- coding: utf-8 -*-
from flask import Blueprint, request

from lib.json_utils import json_format
from domain.service.dashboard import DashboardService

current_action = 'dashboard'
dashboard_bp = Blueprint(current_action, __name__,
                         url_prefix='/%s' % current_action)


@dashboard_bp.route('/', methods=['POST'])
@json_format
def get_by_date():
    """Get dashboard global statistics between two dates"""
    date_begin = request.form['date_begin']
    date_end = request.form['date_end']

    # Build result
    result = {}
    result['global_metrics'] = \
        DashboardService().get_global_statistics(date_begin, date_end)

    result['date_metrics'] = \
        DashboardService().get_date_statistics(date_begin, date_end)

    return result
