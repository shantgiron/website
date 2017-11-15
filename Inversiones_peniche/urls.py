from django.conf.urls import url, include

from .views import ClienteUpdate
from . import views


app_name = 'inversiones_peniche'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^.*\.html', views.gentella_html, name='gentella'),
    url(r'nuevo/$', views.ClienteCreate.as_view(), name='cliente-add'),
    url(r'editar/(?P<pk>[0-9]+)/$', ClienteUpdate.as_view(), name='cliente-update')
]

