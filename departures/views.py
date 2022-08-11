from django.shortcuts import render
from django.views.generic import ListView
from .departures import get_departures
from routes.models import Route

        
def get_departures_list(request):
    upcoming_trains = get_departures(stop='20018107', direction='RBG:71707: :H')
    return render(request, 'departures/index.html', {'departures_list': upcoming_trains['trains']})


def get_route_departures(request):
    path = request.path[:request.path.rfind('/')].rsplit('/', 1)[-1]   
    route = Route.objects.get(name=path)
    upcoming_trains = get_departures(stop=route.stop_id, direction=route.direction)

    return render(request, 'departures/departures.html', {'departures_list': upcoming_trains['trains']})