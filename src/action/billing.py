# -*- coding: utf-8 -*-
from flask import Blueprint, request
from lib.json_utils import json_format
from domain.service.billing import BillingService

current_action = 'billing'
billing_bp = Blueprint(current_action, __name__,
                       url_prefix='/%s' % current_action)


@billing_bp.route('/client', methods=['POST'])
@json_format
def get_client_by_date():
    """Get billing informations between two dates"""
    date_begin = request.form['date_begin']
    date_end = request.form['date_end']

    # Build result
    result = {}
    result['client_newspaper'] = \
        BillingService().get_client_newspaper(date_begin, date_end)

    result['client_delivery'] = \
        BillingService().get_client_delivery(date_begin, date_end)

    return result


@billing_bp.route('/supplier', methods=['POST'])
@json_format
def get_supplier_by_date():
    """Get billing informations between two dates"""
    date_begin = request.form['date_begin']
    date_end = request.form['date_end']

    # Build result
    result = {}

    result['supplier'] = \
        BillingService().get_supplier(date_begin, date_end)

    return result


@billing_bp.route('/deliverer', methods=['POST'])
@json_format
def get_deliverer_by_date():
    """Get billing informations between two dates"""
    date_begin = request.form['date_begin']
    date_end = request.form['date_end']

    # Build result
    result = {}

    result['deliverer'] = \
        BillingService().get_deliverers(date_begin, date_end)

    return result
