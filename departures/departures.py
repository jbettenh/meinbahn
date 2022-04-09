from calendar import day_abbr
from datetime import date, time, datetime
from operator import index
import re
from unittest import registerResult
from pyparsing import Combine
import requests
import xmltodict


# Return XML data
BASE_URL = 'https://efa.vrr.de/standard/XML_DM_REQUEST'

def xml_helper(xml_response):
    departures_dict = xmltodict.parse(xml_response)

    return departures_dict


def get_departures(stop='20018249', direction='RBG:71707: :H'):

    payload = {'sessionID': '0', 'language': 'de',
               'typeInfo_dm': 'stopID',
               'nameInfo_dm': stop,
               'useRealtime': '1',
               'mode': 'direct',
               'line': direction
               }

    response = requests.get(BASE_URL, params=payload)
    return response



if __name__ == '__main__':
    xml_content = get_departures(stop='20018107', direction='RBG:71707: :H')
    result = xmltodict.parse(xml_content.content)
    for index, departure in enumerate(result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture']):
        stop_id = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index][u'@stopID']
        stop_name = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index][u'@nameWO']
        platform = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index][u'@platform']

        day = int(result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdDate'][u'@day'])
        month = int(result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdDate'][u'@month'])
        year = int(result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdDate'][u'@year'])
        hour = int(result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdTime'][u'@hour'])
        minute = int(result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdTime'][u'@minute'])
        second = int(result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdTime'][u'@second'])
        line = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdServingLine'][u'@number']
        direction_to = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdServingLine'][u'@direction']
        direction_from = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdServingLine'][u'@directionFrom']
        route_description = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdServingLine']['itdRouteDescText']
        dt = date(year, month, day)
        tm = time(hour, minute, second)
        combined = datetime.combine(dt, tm)
        # print(f'Departing from {stop_name}')
        # print(f'Next {line} train from {direction_from} heading to {direction_to}')
        print(f'Next train at {combined} on platform: {platform}')
        #print(f'{route_description}')

