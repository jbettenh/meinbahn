from django.urls import path

from . import views

app_name = 'departures'
urlpatterns = [
    path('', views.get_departures_list, name='index'),
]