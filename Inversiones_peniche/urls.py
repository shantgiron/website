from django.conf.urls import url
from . import views


app_name = 'inversiones_peniche'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

