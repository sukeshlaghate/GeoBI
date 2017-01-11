"""Concrete implementation of the connection class
for ArcGIS Server
"""

from uuid import uuid4

from connections.iconnection import IConnection


class ArcGISServerConnection(IConnection):

    connection_types = {'ArcGISServer-Connection'}

    def __init__(self, url, username, passwrd, **kwargs):

        self.impersonate_user = kwargs.pop('impersonate', False)
        self.impersonate_user_name = kwargs.pop('impersonate_user','')
        self.impersonate_password = kwargs.pop('impersonate_password','')
        self.proxy = kwargs.pop('proxy','')
        self.unique_id = uuid4()
        self.class_type = 'Spatial_Connector'
        super().__init__(url, username, passwrd, **kwargs)

    def geturl(self):
        return super().geturl()

    def getusername(self):
        return super().getusername()

    def getpassword(self):
        return super().getpassword()

    def getproxy(self):
        return self.proxy;

    def id(self):
        return self.unique_id

    def classtype(self):
        return self.class_type