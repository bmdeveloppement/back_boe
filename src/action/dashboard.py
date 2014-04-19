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
    result['newspaper_global_metrics'] = \
        DashboardService().get_newspaper_global_statistics(date_begin, date_end)

    result['newspaper_date_metrics'] = \
        DashboardService().get_newspaper_date_statistics(date_begin, date_end)

    result['delivery_global_metrics'] = \
        DashboardService().get_delivery_global_statistics(date_begin, date_end)

    result['delivery_date_metrics'] = \
        DashboardService().get_delivery_date_statistics(date_begin, date_end)

    result['distribution_round_global_metrics'] = \
        DashboardService().get_distribution_round_global_statistics(date_begin, date_end)

    result['distribution_round_date_metrics'] = \
        DashboardService().get_distribution_round_date_statistics(date_begin, date_end)

    return result
