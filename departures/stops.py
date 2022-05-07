import requests


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
                'itdTimeHour': '08',
                'itdTimeMinute': '30',
                'outputFormat': 'JSON'}

    response = requests.get(BASE_URL, params=payload)
    response.encoding = 'ISO-8859-1'
    print(response.encoding)
    print(response.text)
    return response


if __name__ == '__main__':
    full_response = get_stops('Bilk (Düsseldorf)', 'Kronprinzenstrasse')
    lines = full_response['servingLines']['lines']
    print(lines)
    with open('line_data.txt', 'w') as outfile:
        outfile.write(full_response.text)
         
    for line in lines:
        print(line['mode']['number'] + ' ' + line['mode']['destID'] + ' ' + line['mode']['destination'])