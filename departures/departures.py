from calendar import day_abbr
from datetime import date, time, datetime
from operator import index
import re
from unittest import registerResult
from pyparsing import Combine
import requests
import xmltodict
import json


# Return XML data
BASE_URL = 'https://efa.vrr.de/standard/XML_DM_REQUEST'

def xml_to_json(xml_response):
    full_response = xmltodict.parse(xml_response.content)
    departures = {}

    for index, departure in enumerate(full_response['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture']):
        departures[index] = {}
        departures[index]['stop_id'] = departure[u'@stopID']
        departures[index]['stop_name'] = departure[u'@nameWO']
        departures[index]['platform'] = departure[u'@platform']

        day = departure['itdDateTime']['itdDate'][u'@day']
        month = departure['itdDateTime']['itdDate'][u'@month']
        year = departure['itdDateTime']['itdDate'][u'@year']
        hour = departure['itdDateTime']['itdTime'][u'@hour']
        minute = departure['itdDateTime']['itdTime'][u'@minute']
        second = departure['itdDateTime']['itdTime'][u'@second']
        departures[index]['date_time'] = day + '/' + month + '/' + year + ' ' + hour + ':' + minute + ':' + second

        departures[index]['line'] = departure['itdServingLine'][u'@number']
        departures[index]['direction_to'] = departure['itdServingLine'][u'@direction']
        departures[index]['direction_from'] = departure['itdServingLine'][u'@directionFrom']
        departures[index]['route_description'] = departure['itdServingLine']['itdRouteDescText']

    print(departures)
    departures_list = json.dumps(departures)

    return departures_list


def get_departures(stop='20018107', direction='RBG:71707: :H'):

    payload = {'sessionID': '0', 'language': 'de',
               'typeInfo_dm': 'stopID',
               'nameInfo_dm': stop,
               'useRealtime': '1',
               'mode': 'direct',
               'line': direction
               }

    response = requests.get(BASE_URL, params=payload)
    
    return xml_to_json(response)


if __name__ == '__main__':
    
    json_content = get_departures(stop='20018107', direction='RBG:71707: :H')
    print(json_content)

        


