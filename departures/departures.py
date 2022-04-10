from calendar import day_abbr
from datetime import date, time, datetime
from operator import index
import re
from unittest import registerResult
from pyparsing import Combine
import requests
import xmltodict
import json
import pprint


# Return XML data
BASE_URL = 'https://efa.vrr.de/standard/XML_DM_REQUEST'

def xml_to_json(xml_response):
    full_response = xmltodict.parse(xml_response.content)
    departures = {}
    trains = []

    for index, departure in enumerate(full_response['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture']):
        train = {}
        train['train_id'] = index
        train['stop_id'] = departure[u'@stopID']
        train['stop_name'] = departure[u'@nameWO']
        train['platform'] = departure[u'@platform']

        day = departure['itdDateTime']['itdDate'][u'@day']
        month = departure['itdDateTime']['itdDate'][u'@month']
        year = departure['itdDateTime']['itdDate'][u'@year']
        hour = departure['itdDateTime']['itdTime'][u'@hour']
        minute = departure['itdDateTime']['itdTime'][u'@minute']
        second = departure['itdDateTime']['itdTime'][u'@second']
        train['date_time'] = day.zfill(2) + '/' + month.zfill(2) + '/' + year + ' ' + hour.zfill(2) + ':' + minute.zfill(2) + ':' + second.zfill(2)

        train['line'] = departure['itdServingLine'][u'@number']
        train['direction_to'] = departure['itdServingLine'][u'@direction']
        train['direction_from'] = departure['itdServingLine'][u'@directionFrom']
        train['route_description'] = departure['itdServingLine']['itdRouteDescText']

        trains.append(train)
   
    departures['trains'] = trains
    departures_list = json.dumps(departures)

    return departures_list

def xml_to_dict(xml_response):
    full_response = xmltodict.parse(xml_response.content)
    departures = {}
    trains = []

    for index, departure in enumerate(full_response['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture']):
        train = {}
        train['train_id'] = index
        train['stop_id'] = departure[u'@stopID']
        train['stop_name'] = departure[u'@nameWO']
        train['platform'] = departure[u'@platform']

        day = departure['itdDateTime']['itdDate'][u'@day']
        month = departure['itdDateTime']['itdDate'][u'@month']
        year = departure['itdDateTime']['itdDate'][u'@year']
        hour = departure['itdDateTime']['itdTime'][u'@hour']
        minute = departure['itdDateTime']['itdTime'][u'@minute']
        second = departure['itdDateTime']['itdTime'][u'@second']
        train['date_time'] = day.zfill(2) + '/' + month.zfill(2) + '/' + year + ' ' + hour.zfill(2) + ':' + minute.zfill(2) + ':' + second.zfill(2)

        train['line'] = departure['itdServingLine'][u'@number']
        train['direction_to'] = departure['itdServingLine'][u'@direction']
        train['direction_from'] = departure['itdServingLine'][u'@directionFrom']
        train['route_description'] = departure['itdServingLine']['itdRouteDescText']

        trains.append(train)
   
    departures['trains'] = trains

    return departures

def get_departures(stop='20018107', direction='RBG:71707: :H'):

    payload = {'sessionID': '0', 'language': 'de',
               'typeInfo_dm': 'stopID',
               'nameInfo_dm': stop,
               'useRealtime': '1',
               'mode': 'direct',
               'line': direction
               }

    response = requests.get(BASE_URL, params=payload)
    
    return xml_to_dict(response)


if __name__ == '__main__':
    json_content = get_departures(stop='20018107', direction='RBG:71707: :H')
    # with open('json_data.json', 'w') as outfile:
    #     outfile.write(json_content)
    # pprint.pprint(json_content, indent=4)
