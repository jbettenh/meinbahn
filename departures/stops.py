import re
from urllib import response
import requests
import xmltodict
import pprint

# Return XML data
BASE_URL = 'https://efa.vrr.de/standard/XML_DM_REQUEST'

def get_stops(city, search):
    payload = {'sessionID': '0',
                'requestID': '0',
                'language': 'de',
                'selectAssignedStops': '1',
                'place_dm': city,
                'placeState_dm': 'empty',
                'type_dm': 'stop',
                'name_dm': search,
                'nameState_dm': 'empty',
                'itdTimeHour': '22',
                'itdTimeMinute': '04',
                'outputFormat': 'JSON'}

    response = requests.get(BASE_URL, params=payload)

    return response


if __name__ == '__main__':
    # full_response = xmltodict.parse(get_stops('Bilk (Düsseldorf)', 'Kronprinzenstrasse').content)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(get_stops('Bilk (Düsseldorf)', 'Kronprinzenstrasse').content)