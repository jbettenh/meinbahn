from datetime import datetime

import requests
import xmltodict

# Return XML data
BASE_URL = "https://efa.vrr.de/standard/XML_DM_REQUEST"


def xml_to_dict(xml_response):
    full_response = xmltodict.parse(xml_response.content)
    departures = {}
    trains = []
    current_time = datetime.now()
    format_date = "%Y-%m-%d %H:%M:%S"

    for index, departure in enumerate(
        full_response["itdRequest"]["itdDepartureMonitorRequest"][
            "itdDepartureList"
        ]["itdDeparture"]
    ):
        train = {}
        train["train_id"] = index
        train["stop_id"] = departure["@stopID"]
        train["stop_name"] = departure["@nameWO"]
        train["platform"] = departure["@platform"]

        day = departure["itdDateTime"]["itdDate"]["@day"]
        month = departure["itdDateTime"]["itdDate"]["@month"]
        year = departure["itdDateTime"]["itdDate"]["@year"]
        hour = departure["itdDateTime"]["itdTime"]["@hour"]
        minute = departure["itdDateTime"]["itdTime"]["@minute"]
        second = departure["itdDateTime"]["itdTime"]["@second"]

        train["date_time"] = (
            year
            + "-"  # noqa: W503
            + month.zfill(2)  # noqa: W503
            + "-"  # noqa: W503
            + day.zfill(2)  # noqa: W503
            + " "  # noqa: W503
            + hour.zfill(2)  # noqa: W503
            + ":"  # noqa: W503
            + minute.zfill(2)  # noqa: W503
            + ":"  # noqa: W503
            + second.zfill(2)  # noqa: W503
        )
        arrival_time = datetime.strptime(train["date_time"], format_date)
        time_delta = (arrival_time - current_time).total_seconds() / 60
        train["arrival"] = str(round(time_delta)) + " min."

        train["line"] = departure["itdServingLine"]["@number"]
        train["direction_to"] = departure["itdServingLine"]["@direction"]
        train["direction_from"] = departure["itdServingLine"]["@directionFrom"]
        """
        train['route_description'] = departure['itdServingLine']
        ['itdRouteDescText']
        train['route_description'] = 'description'
        """
        trains.append(train)

    departures["trains"] = trains

    return departures


def get_departures(stop, direction):
    payload = {
        "sessionID": "0",
        "language": "de",
        "typeInfo_dm": "stopID",
        "nameInfo_dm": stop,
        "useRealtime": "1",
        "mode": "direct",
        "line": direction,
        "limit": 8,
    }
    print(f"the direction was {direction}")
    response = requests.get(BASE_URL, params=payload)

    if response.status_code == 200:
        return xml_to_dict(response)
    else:
        return {}
