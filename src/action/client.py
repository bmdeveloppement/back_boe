# -*- coding: utf-8 -*-
import logging
from flask import abort, Blueprint
from lib.json_utils import json_format
from domain.service.client import ClientService

current_action = 'client'
logger = logging.getLogger(__name__)
client_bp = Blueprint(current_action, __name__, url_prefix='/%s' % current_action)


@client_bp.route('/<id>', methods=['GET'])
@json_format
def get(id):
    """Get item by id"""
    try:
        item = ClientService().get(id)
    except:
        logger.exception('An error occured when fecthing %s' % current_action)
        abort(404)
    if not item:
        abort(404)
    return item


@client_bp.route('', methods=['GET'])
@json_format
def list():
    """Create items"""
    try:
        items = ClientService().list()
    except:
        logger.exception('An error occured when fecthing %s' % current_action)
        abort(404)
    if not items:
        abort(404)
    return items


@client_bp.route('', methods=['PUT'])
@json_format
def create():
    """Create new item"""
    from flask import request
    try:
        item = ClientService().create(request.form)
    except:
        logger.exception('An error occured when creating %s' % current_action)
        abort(409)
    if item is None:
        abort(409)
    elif not item:
        abort(500)
    return item


@client_bp.route('/<id>', methods=['POST'])
@json_format
def edit(id):
    """Update item by id"""
    from flask import request
    item = ClientService().edit(id, request.form)
    if not item:
        abort(404)
    return item


@client_bp.route('/<id>', methods=['DELETE'])
@json_format
def delete(id):
    """Delete item by id"""
    abort(501)
