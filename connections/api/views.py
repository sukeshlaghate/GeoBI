from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from connections.api.serializers import ConnectionSerializer
import json
from connections.connectionmanager import ConnectionManager


"""
Class used to list, retrieve, create, update, partial update and destroy connection objects.
 Connection objects are created for mapservice based on the connectors available.
"""


class ConnectionsView(viewsets.GenericViewSet):

    serializer_class = ConnectionSerializer


"""
Class used to list, retrieve, connector classes.
 Connector classes are used to create connection objects for mapservice.
"""


class ConnectionTypeView(viewsets.ViewSet):
    connectors = json.dumps(ConnectionManager().get_registered_connectors())  # '{ "data" :'++'}'
    print((ConnectionManager().get_registered_connectors())[0])

    @detail_route(methods=['get'])
    def list(self,request):
        print(self.connectors)
        return Response(self.connectors)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        return Response(self.connectors)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

