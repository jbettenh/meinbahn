from django.urls import path

from routes.views import Routes

app_name = "routes"
urlpatterns = [
    path("", Routes.as_view(), name="routes"),
]
