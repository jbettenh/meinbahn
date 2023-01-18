from django.urls import path

from . import views

app_name = "departures"
urlpatterns = [
    path("", views.get_departures_list, name="index"),
    path("home/", views.get_route_departures, name="home"),
    path("work/", views.get_route_departures, name="work"),
    path("airport/", views.get_route_departures, name="airport"),
]
