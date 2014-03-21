# -*- coding: utf-8 -*-
"""
Module for handling database connection for the application.
"""
# MYSQL imports
import MySQLdb
from MySQLdb.cursors import DictCursor
from sqlalchemy import pool

from lib.configurator import Configurator
from lib.singleton import Singleton


class SqlAlchemyConnector(Singleton):
    """"""

    def __init__(self):
        self.db = None
        self.store = None

    def get_db(self):
        if(self.db is None):
            from main import application
            from flask.ext.sqlalchemy import SQLAlchemy

            db_config = Configurator().get_setting('databases')['auth']
            application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % (
                db_config['user'], db_config['password'], db_config['host'],
                db_config['database'])
            application.config['SQLALCHEMY_POOL_SIZE'] = db_config['pool_size']
            application.config['SQLALCHEMY_POOL_RECYCLE'] = 1800
            application.config['SQLALCHEMY_MAX_OVERFLOW'] = db_config['pool_size']
            application.config['SQLALCHEMY_POOL_TIMEOUT'] = 2
            self.db = SQLAlchemy(application)
        return self.db

    def get_session(self):
        session = self.get_db().session
        session.commit()
        return session

    def get_store(self):
        if(self.store is None):
            from main import store
            self.store = store
        return self.store

    def close_session(self):
        return self.get_session().close()

    @staticmethod
    def provide_session(fn):
        """
        Decorator function for wrapping MySQL call.
        Ensure that connection opened are closed.
        """
        from functools import wraps

        @wraps(fn)
        def wrapper(self, *args):
            """Wraps the function for providing a generated cursor,
            in order to clean close it at the end of the execution."""
            session = SqlAlchemyConnector().get_session()
            result = fn(self, *args, session=session)
            session.flush()
            return result
        return wrapper


class DbConnector(Singleton):
    """
    Class manipulating all databases connections. Centralize pooling policy.
    """

    def __init__(self):
        """DbConnector"""
        print 'Initializing DbConnector'
        self.settings = Configurator().get_setting('databases')
        self.pooled_databases = {}
        self.direct_databases = {}
        self.pool = {}
        self.discover_direct_links()
        self.listeners = {}
        self.create_pools()

    def create_pools(self):
        """Create all pools of connection and populate them"""
        if 'pool' in self.settings:
            for db_type in self.settings['pool']:
                for db_name in self.settings['pool'][db_type]:
                    {
                        'mysql': self.create_mysql_pool,
                        #'mongodb': self.create_mongo_pool,
                        'redis': self.create_redis_pool,
                    }[db_type](db_name)

    def discover_direct_links(self):
        """Discover all databases managed in direct links"""
        if 'direct' in self.settings:
            for db_type in self.settings['direct']:
                for db_name in self.settings['direct'][db_type]:
                    self.direct_databases[db_name] = db_type

    def create_mysql_pool(self, db_name):
        """Create MySQL connections pool

        db_name
          Name of the database to initialize"""

        db_yml = self.settings['pool']['mysql'][db_name]
        self.pooled_databases[db_name] = 'mysql'
        mysql_pool = pool.QueuePool(creator=MysqlConnectionCreator(db_yml),
            max_overflow=db_yml['pool_size'],
            pool_size=db_yml['pool_size'], recycle=1800,
            echo=True, timeout=2)
        self.pool[db_name] = mysql_pool

    def __del__(self):
        """
        Delete the database manager object. Should not happen in WSGI mode.
        """
        print "Deleting connection manager"
        self.close_connections()
        DbConnector.__instance = None

    def close_connections(self):
        """Close all connections"""
        for db in self.pool:
            if self.pool[db]['type'] == 'mysql':
                self.pool[db]['instance'].close()
            if self.pool[db]['type'] == 'mongodb':
                self.pool[db]['instance'].connection.disconnect()

    def get_connection(self, db_name):
        """Get an available connection to the given database.
        FIXME: KeyError to suppress

        db_name
          Database name to connect to
        """
        if db_name in self.pooled_databases:
            return {
                'redis': self.get_pooled_redis_connection,
                'mysql': self.get_pooled_mysql_connection,
            }[self.pooled_databases[db_name]](db_name)
        else:
            return None

    def get_pooled_mysql_connection(self, db_name):
        """Return a MySQL connection to the given database

        db_name
          Database connection to get"""
        return self.pool[db_name].connect()