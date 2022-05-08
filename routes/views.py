import imp
from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

class MyView(ListView):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World')
