from datetime import datetime
import requests
import xmltodict


# Return XML data
BASE_URL = 'https://efa.vrr.de/standard/XML_DM_REQUEST'

def xml_to_dict(xml_response):
    full_response = xmltodict.parse(xml_response.content)
    departures = {}
    trains = []
    current_time = datetime.now()
    format_date = "%Y-%m-%d %H:%M:%S"

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

        train['date_time'] = year + '-' + month.zfill(2) + '-' + day.zfill(2) + ' ' + hour.zfill(2) + ':' + minute.zfill(2) + ':' + second.zfill(2)
        arrival_time = datetime.strptime(train['date_time'], format_date)
        time_delta = (arrival_time - current_time).total_seconds()/60
        train['arrival'] = str(round(time_delta)) + ' min.'

        train['line'] = departure['itdServingLine'][u'@number']
        train['direction_to'] = departure['itdServingLine'][u'@direction']
        train['direction_from'] = departure['itdServingLine'][u'@directionFrom']
        # train['route_description'] = departure['itdServingLine']['itdRouteDescText']
        # train['route_description'] = 'description'

        trains.append(train)

    departures['trains'] = trains

    return departures


def get_departures(stop, direction):
    payload = {'sessionID': '0', 'language': 'de',
               'typeInfo_dm': 'stopID',
               'nameInfo_dm': stop,
               'useRealtime': '1',
               'mode': 'direct',
               'line': direction,
               'limit': 8
               }

    response = requests.get(BASE_URL, params=payload)
    
    if response.status_code == 200:
        return xml_to_dict(response)
    else:
        return {}


if __name__ == '__main__':
    id = 2
    if id == 1:
        # Home
        stop = '20018107'
        direction = 'RBG:71707: :H'
    elif id ==2:
        # Airport
        stop = '20018249'
        # tuple
        direction = 'RBG:70072: :R','RBG:70071: :R','DDB:92E11: :R'
        # list
        direction = ['RBG:70072: :R','RBG:70071: :R','DDB:92E11: :R']

    dict_content = get_departures(stop=stop, direction=direction)
    print(dict_content)
    print(f'direction is type {type(direction)} and has value {direction}')
