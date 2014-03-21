# -*- coding: utf-8 -*-
import logging
from flask import abort, Blueprint
from lib.json_utils import json_format
from domain.service.client import ClientService

logger = logging.getLogger(__name__)
client_bp = Blueprint('client', __name__, url_prefix='/client')


@client_bp.route('/<client_id>', methods=['GET'])
@json_format
def get(client_id):
    try:
        client = ClientService().get(client_id)
        print client
    except:
        logger.exception('An error occured when fecthing client')
        abort(404)
    if not client:
        abort(404)
    return client


@client_bp.route('/list', methods=['GET'])
@json_format
def list():
    try:
        clients = ClientService().list()
    except:
        logger.exception('An error occured when fecthing client')
        abort(404)
    if not clients:
        abort(404)
    return [client.to_dict() for client in clients]


@client_bp.route('', methods=['PUT'])
@json_format
def create():
    """Create new client"""
    from flask import request
    try:
        client = ClientService().create(request.form)
    except:
        logger.exception('An error occured when creating client')
        abort(409)
    if client is None:
        abort(409)
    elif not client:
        abort(500)
    return client.to_dict()


@client_bp.route('/<client_id>', methods=['POST'])
@json_format
def edit(client_id):
    """Update client by id, login is not editable"""
    from flask import request
    client = ClientService().edit(client_id, request.form)
    if client is None:
        abort(404)
    return client.to_dict()


@client_bp.route('/<id>', methods=['DELETE'])
@json_format
def delete(id):
    """Delete client by id"""
    abort(501)
