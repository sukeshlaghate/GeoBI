from django.conf.urls import url
from website.views import indexview

urlpatterns = [
    url(r'^$', indexview),
]
