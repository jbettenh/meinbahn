from django.shortcuts import render
from .departures import get_departures

        
def get_departures_list(request):
    upcoming_trains = get_departures(stop='20018107', direction='RBG:71707: :H')
    return render(request, 'departures/index.html', {'departures_list': upcoming_trains['trains']})
