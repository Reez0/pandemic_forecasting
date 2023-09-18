from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('retrieve-forecast', views.get_forecast, name='retrieve_forecast')
]
