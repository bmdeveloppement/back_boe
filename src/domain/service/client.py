from lib.database_utils import SqlAlchemyConnector
from domain.model.client import Client

class ClientService(object):

    def __init__(self):
        """Init"""
        self.__type__ = Client

    @SqlAlchemyConnector.provide_session
    def list(self, session=None):
        """List instances"""
        pass

    @SqlAlchemyConnector.provide_session
    def get(self, client_id, session=None):
        """Get an instance"""
        client = session.query(Client).get(client_id)
        return client

    @SqlAlchemyConnector.provide_session
    def create(self, request, session=None):
        """Create new instance"""
        pass

    @SqlAlchemyConnector.provide_session
    def edit(self, client_id, request, session=None):
        """Edit an instance"""
        pass
