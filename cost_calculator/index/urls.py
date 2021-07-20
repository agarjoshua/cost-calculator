from django.contrib import admin
from . import views
from django.urls import path

app_name = 'index'

urlpatterns = [
    path('', views.result, name='result'),
    path('norates', views.index, name='index'),
    path('rates', views.rates, name='rates'),
]