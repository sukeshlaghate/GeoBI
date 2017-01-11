from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from connections.api import views as api_views

#router = DefaultRouter()
#router.register(r'connectors/$', api_views.ConnectionTypeView.as_view({'get': 'list'}))

urlpatterns = [
        url(r'^api/connectors/$', api_views.ConnectionTypeView.as_view(actions={'get':'list'})),
]
