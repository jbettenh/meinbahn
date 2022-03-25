import requests


def get_home():

    payload = {'sessionID': '0', 'language': 'de', 'itdLPxx_dmRefresh': '',
               'typeInfo_dm': 'stopID',
               'nameInfo_dm': '20018249',
               'useRealtime': '1',
               'mode': 'direct',
               'line': ['DDB:92E11::R', 'RBG:70071::R', 'RBG:70072::R']
               }

    #response = requests.get('https://efa.vrr.de/standard/XML_DM_REQUEST', params=payload)
    response = requests.get('https://efa.vrr.de/standard/XSLT_DM_REQUEST', params=payload)
    return response.text


if __name__ == '__main__':
    print(get_home())