from functools import wraps
from flask.globals import current_app
from .json_utils import default_handler
import json


def jsonify(method=None, cls=None):
    @wraps(method)
    def inner(*args, **kwargs):
        return current_app.response_class(json.dumps(method(*args, **kwargs), indent=None, default=default_handler), mimetype='application/json')

    return inner
