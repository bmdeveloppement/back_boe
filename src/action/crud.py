# -*- coding: utf-8 -*-
import logging
from flask import abort, Blueprint, request
from flask.views import MethodView
from lib.json_utils import json_format

logger = logging.getLogger(__name__)


class CrudView(MethodView):
    """Base class for crud views.

    Register on initialization a service and a formatter. Request will be passed
    to the service through the CrudView.execute method and the result will be
    passed to the formatter.
    """
    decorators = [json_format]

    def __init__(self, resource_service):
        self.resource_service = resource_service()

    def execute(self, action, *args, **kwargs):
        """Will execute the method named **action** on the class defined
        **resource_service** and format the result through the also class
        defined **formatter**."""
        result = getattr(self.resource_service, action)(*args, **kwargs)
        return result


class CrudGetView(CrudView):

    def get(self, resource_id):
        return self.execute('get', resource_id)


class CrudGetFullView(CrudView):

    def get(self, resource_id):
        return self.execute('get_full', resource_id)


class CrudListView(CrudView):

    def post(self):
        return self.execute('list')


class CrudListFieldView(CrudView):

    def post(self, field_name):
        return self.execute('list_field', field_name)


class CrudCreateView(CrudView):

    def put(self):
        attrs = request.form
        return self.execute('create', attrs)


class CrudUpdateView(CrudView):

    def post(self, resource_id):
        attrs = request.form
        return self.execute('update', resource_id, attrs)


class CrudDeleteView(CrudView):

    def delete(self, resource_id):
        return self.execute('delete', resource_id)


def crud_actions(blueprint, resource_name, resource_service, formatter=None):
    # Get
    crud_get = CrudGetView.as_view(resource_name + '_get',
            resource_service=resource_service)
    blueprint.add_url_rule('/<resource_id>', view_func=crud_get, methods=['GET'])

    # Get Full
    crud_get_full = CrudGetFullView.as_view(resource_name + '_get_full',
            resource_service=resource_service)
    blueprint.add_url_rule('/get_full/<resource_id>', view_func=crud_get_full, methods=['GET'])

    # List
    crud_list = CrudListView.as_view(resource_name + '_list',
            resource_service=resource_service)
    blueprint.add_url_rule('/', view_func=crud_list, methods=['POST'])

    # List Field
    crud_list_field = CrudListFieldView.as_view(resource_name + '_list_field',
            resource_service=resource_service)
    blueprint.add_url_rule('/field_name/<field_name>', view_func=crud_list_field, methods=['POST'])

    # Create
    crud_create = CrudCreateView.as_view(resource_name + '_create',
            resource_service=resource_service)
    blueprint.add_url_rule('/', view_func=crud_create, methods=['PUT'])

    # Update
    crud_update = CrudUpdateView.as_view(resource_name + '_update',
            resource_service=resource_service)
    blueprint.add_url_rule('/<resource_id>', view_func=crud_update, methods=['POST'])

    # Delete
    crud_delete = CrudDeleteView.as_view(resource_name + '_delete',
            resource_service=resource_service)
    blueprint.add_url_rule('/<resource_id>', view_func=crud_delete, methods=['DELETE'])
