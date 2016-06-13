from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^increase/', views.increase_quantity, name='increase_quantity'),
    url(r'^decrease/', views.decrease_quantity, name='decrease_quantity'),
    url(r'^$', views.index, name='index'),
]
