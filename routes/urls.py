from django.urls import path

from routes.views import MyView

app_name = 'routes'
urlpatterns = [
    path('', MyView.as_view(), name='routes'),
]