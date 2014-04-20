# -*- coding: utf-8 -*-
from flask import Blueprint, request
from lib.json_utils import json_format
from domain.service.billing import BillingService

current_action = 'billing'
billing_bp = Blueprint(current_action, __name__,
                       url_prefix='/%s' % current_action)


@billing_bp.route('/', methods=['POST'])
@json_format
def get_by_date():
    """Get billing informations between two dates"""
    date_begin = request.form['date_begin']
    date_end = request.form['date_end']

    # Build result
    result = {}
    result['client_newspapers'] = \
        BillingService().get_client_newspaper(date_begin, date_end)

    result['client_deliveries'] = \
        BillingService().get_client_delivery(date_begin, date_end)

    result['suppliers'] = \
        BillingService().get_supplier(date_begin, date_end)

    result['deliverers'] = \
        BillingService().get_deliverers(date_begin, date_end)

    return result
