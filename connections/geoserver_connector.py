"""Concrete implementation of the connection class
for Geoserver
"""

from uuid import uuid4

from connections.iconnection import IConnection


class GeoserverConnection(IConnection):

    connection_types = {'Geoserver-Connection'}

    def __init__(self, url, username, passwrd, **kwargs):
        super().__init__(url, username, passwrd, **kwargs)
        self.unique_id = uuid4()
        self.class_type = 'Spatial_Connector'

    def geturl(self):
        return super().geturl()

    def getusername(self):
        return super().getusername()

    def getpassword(self):
        return super().getpassword()

    def getproxy(self):
        pass

    def id(self):
        return self.unique_id

    def classtype(self):
        return self.class_type