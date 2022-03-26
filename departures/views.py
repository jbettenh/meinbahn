from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from .models import Departure

class IndexView(ListView):
    context_object_name = 'departures_list'
    template_name = 'departures/index.html'

    def get_queryset(self):
        return Departure.objects.all()
