import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Route

class Routes(ListView):
    context_object_name = 'route_list'
    template_name = 'routes/routes.html'
    
    def get_queryset(self):
        return Route.objects.all()
