# -*- coding: utf-8 -*-

from __future__ import absolute_import  # allows importing built-in json module
import uuid
import datetime
from json import dumps
from functools import wraps
from decimal import Decimal

try:
    from bson.objectid import ObjectId
except ImportError:
    ObjectId = None


def default_handler(obj):
    """JSON handler for default query formatting"""
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    if hasattr(obj, 'dump'):
        return obj.dump()
    if hasattr(obj, 'next'):
        return [i for i in obj]
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if isinstance(obj, set):
        return list(obj)
    if isinstance(obj, frozenset):
        return list(obj)
    if isinstance(obj, Decimal):
        return float(obj)
    if ObjectId is not None and isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, datetime.timedelta):
        return str(obj)
    raise TypeError("Object of type %s with value of %s "
                    "is not JSON serializable" % (type(obj), repr(obj)))


def json_format(fn=None, cls=None):
    @wraps(fn)
    def inner(*args, **kwargs):
        return jsonify(fn(*args, **kwargs))
    return inner


def jsonify(obj):
    """Creates a :class:`~flask.Response` with the JSON representation of
    the given arguments with an `application/json` mimetype.  The arguments
    to this function are the same as to the :class:`dict` constructor.

    Example usage::

        @app.route('/_get_current_user')cd ..
        def get_current_user():
            return jsonify(username=g.user.username,
                           email=g.user.email,
                           id=g.user.id)

    This will send a JSON response like this to the browser::

        {
            "username": "admin",
            "email": "admin@localhost",
            "id": 42
        }

    This requires Python 2.6 or an installed version of simplejson.  For
    security reasons only objects are supported toplevel.  For more
    information about this, have a look at :ref:`json-security`.

    .. versionadded:: 0.2
    """
    from flask import current_app

    return current_app.response_class(dumps(obj,
        indent=None, default=default_handler),
        mimetype='application/json')