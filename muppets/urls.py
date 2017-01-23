from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/(?P<id>[0-9]+)$', views.muppet, name='muppet'),
    url(r'^[/]{0,1}$', views.index, name='index'),
]