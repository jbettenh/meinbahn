from operator import index
import re
from unittest import registerResult
import requests
import xmltodict


# Return XML data
BASE_URL = 'https://efa.vrr.de/standard/XML_DM_REQUEST'

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
    result = xmltodict.parse(xml_content.content, process_namespaces=False)
    index = 0
    for departure in result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture']:
        index += 1
        stop_id = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index][u'@stopID']
        stop_name = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index][u'@nameWO']
        platform = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index][u'@platform']
    
        next_train_hour = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdTime'][u'@hour']
        next_train_minute = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdTime'][u'@minute']
        next_train_second = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdDateTime']['itdTime'][u'@second']
        line = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdServingLine'][u'@number']
        direction_to = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdServingLine'][u'@direction']
        direction_from = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdServingLine'][u'@directionFrom']
        route_description = result['itdRequest']['itdDepartureMonitorRequest']['itdDepartureList']['itdDeparture'][index]['itdServingLine']['itdRouteDescText']
        # print(f'Departing from {stop_name}')
        # print(f'Next {line} train from {direction_from} heading to {direction_to}')
        print(f'Next train at {next_train_hour}:{next_train_minute}:{next_train_second} on platform: {platform}')
        #print(f'{route_description}')

