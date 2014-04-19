#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os
import traceback

from os import path
from flask import make_response, g, session
from lib.configurator import Configurator
from lib.database_utils import SqlAlchemyConnector
from lib.boe_app import BoeFlaskApplication

sys.path.append(path.dirname(__file__))
Configurator(os.path.dirname(__file__))
application = BoeFlaskApplication(__name__)


def import_blueprints():
    """Import BPs"""
    from action.client import client_bp
    from action.dashboard import dashboard_bp
    from action.deliverer import deliverer_bp
    from action.delivery import delivery_bp
    from action.distribution_round_archive import distribution_round_archive_bp
    from action.distribution_round import distribution_round_bp
    from action.point_of_sale import point_of_sale_bp
    from action.point_of_sale_distribution_round import point_of_sale_distribution_round_bp
    from action.newspaper import newspaper_bp
    from action.order import order_bp
    from action.press_title import press_title_bp
    from action.supplier import supplier_bp
    from action.supplier_price import supplier_price_bp

    application.register_blueprint(client_bp)
    application.register_blueprint(dashboard_bp)
    application.register_blueprint(deliverer_bp)
    application.register_blueprint(delivery_bp)
    application.register_blueprint(distribution_round_bp)
    application.register_blueprint(distribution_round_archive_bp)
    application.register_blueprint(point_of_sale_bp)
    application.register_blueprint(point_of_sale_distribution_round_bp)
    application.register_blueprint(newspaper_bp)
    application.register_blueprint(order_bp)
    application.register_blueprint(press_title_bp)
    application.register_blueprint(supplier_bp)
    application.register_blueprint(supplier_price_bp)


@application.before_request
def authentify():
    """Authentify request before treatment"""
    pass


def set_logging():
    """Loggin sqlalchemy infos"""
    import logging
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def set_http_handlers():
    @application.errorhandler(Exception)
    def silent_death(error=None):
        """Forbidden handler"""
        print traceback.print_exc()
        resp = make_response('')
        resp.status_code = 200
        return resp

    @application.errorhandler(403)
    def forbidden(error=None):
        """Forbidden handler"""
        resp = make_response('Forbidden Access')
        resp.status_code = 403
        return resp

    @application.after_request
    def after_request(response):
        """Executed after every request"""
        # Set a custom header
        try:
            response.headers['X-Boe-Header'] = Configurator().boe_header
        except:
            pass

        # Disconnect from DB
        SqlAlchemyConnector().close_session()

        return response

set_http_handlers()
db = SqlAlchemyConnector().get_db()
import_blueprints()
# set_logging()
