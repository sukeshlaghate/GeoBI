import importlib
import os
import sys

from GeoBI.settings import DEBUG
from connections.iconnection import IConnection
from patterns.singleton import Singleton


class UnknownConnectorTypeException(Exception):
    """Raised when an unknown connector type is encountered"""


class ConnectionManager(object,metaclass=Singleton):

    connector_classes = {}

    def __init__(self, path=None, connection_init_args={}):

        self.con_modules_dir = list()

        # add the path where we are located as core connectors are located in this path
        self.con_modules_dir.append(os.path.dirname(__file__))

        if path and path not in self.con_modules_dir:
            self.con_modules_dir.append(path)

        self._load_connectors()
        self._register_connectors(**connection_init_args)

    def _load_connectors(self):

        if self.con_modules_dir not in sys.path:
            sys.path.extend(self.con_modules_dir)

        # iterate over our paths to find and load modules
        for module_dir in self.con_modules_dir:
            connector_files = [file_name for file_name in os.listdir(module_dir)
                               if file_name.endswith('_connector.py')]

            connector_modules = [module.split('.')[0] for module in connector_files]
            for module in connector_modules:
                m = importlib.import_module(module, module_dir)
                if DEBUG:
                    print(m.__name__)
                    print('importing module', m)

    def _register_connectors(self, **connection_init_args):

        # since we know that all connectors will be subclass of IConnection abstract base class we call
        # short cut method __subclasses__() :)
        for subklas in IConnection.__subclasses__():
            self.connector_classes[subklas.__name__] = subklas
            if DEBUG:
                print('In ', __file__, '_register_connectors', type(subklas))
                print(subklas)
                print(subklas(None,None,None).__dict__)
                print('registry now contains', self.connector_classes)

    def get_connector_instance(self, connection_type, *args, **kwargs):
        """
        Determine the appropriate connector for the connection type,
        create a connection object to hold the connection parameters.

        :return: The connection object.
        """
        try:
            connection_cls = self.connection_registry[connection_type]
        except KeyError:
            raise UnknownConnectorTypeException(connection_type)

        conn_cls = connection_cls(*args,**kwargs)

        return conn_cls

    def get_registered_connectors(self):
        return list(self.connector_classes.keys())


# connection_manager = ConnectionManager()
