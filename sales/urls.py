from django.conf.urls import url

from . import views

app_name = 'sales'
urlpatterns = [
    url(r'^list$', views.list, name='list'),
    url(r'^$', views.index, name='index'),
]
