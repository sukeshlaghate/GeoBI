from django.apps import AppConfig
from connections.connectionmanager import ConnectionManager


class ConnectionsConfig(AppConfig):
    name = 'connections'

    # startup code goes in here. Code is called once when django starts up
    def ready(self):
        # calling connection manager will initialize and register all our connectors
        print('ready called')
        ConnectionManager()
