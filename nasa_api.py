import requests
from datetime import datetime

# NASA's API and API key
API = "https://api.nasa.gov/planetary/earth/assets"
API_KEY = "9Jz6tLIeJ0yY9vjbEUWaH9fsXA930J9hspPchute"

# Constants
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'

# Error Constants
INVALID_COORDINATES = 'Invalid coordinate!'
INSUFFICIENT_DATA = 'Insufficient data recorded'


def latest_average_time_delta(results, count):
    dates = map(lambda x: datetime.strptime(x['date'], DATE_FORMAT), results)
    dates_list = list(dates)
    # print(dates_list)
    oldest = min(dates_list)
    youngest = max(dates_list)

    # Average time taken is the duration between the youngest and oldest
    # recorded date, divided by the number of periods (n - 1)
    ave_time_delta = (youngest - oldest) / (count - 1)
    return ave_time_delta, youngest


def flyby(latitude, longitude, place='unspecified'):
    print("place ", place)
    # if invalid coordinate print invalid
    if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
        return INVALID_COORDINATES

    url = API

    querystring = {"api_key": API_KEY, "lat": str(latitude),
                   "lon": str(longitude)}

    response = requests.request("GET", url, params=querystring)

    if response.status_code != 200:
        return response.text

    json_response = response.json()
    count = json_response.get('count')
    results = json_response.get('results')

    # if count < 2, print insufficient
    if count < 2:
        print(INSUFFICIENT_DATA)
        return INSUFFICIENT_DATA

    ave_time_delta, latest = latest_average_time_delta(results, count)
    print("latest : {}".format(latest))
    print("ave_time_delta : {}".format(ave_time_delta))

    dates_diff = datetime.today() - latest
    if dates_diff.total_seconds() < 0:
        predicted = latest
    else:
        dates_diff % ave_time_delta
        predicted = datetime.today() + (dates_diff % ave_time_delta)

    # predicted = latest
    # while predicted <= datetime.today():
    #     predicted = predicted + ave_time_delta

    print(predicted)
    print("Next time: {}".format(predicted))


lat = 36.998979
lon = -109.045183

flyby(lat, lon)

flyby(0.000000, 0.000000, "GULF OF GUINEA")
flyby(36.098592, -112.097796, "GRAND CANYON")
flyby(43.078154, -79.075891, "NIAGARA FALLS")
flyby(36.998979, -109.045183, "FOUR CORNERS")
flyby(37.7937007, -122.4039064, "DELPHIX")

# BOUNDARY/EDGE

# MINIMUM LATITUDE
flyby(-90.000001, 0.000000, "MIN LAT 1")
flyby(-90.000000, 0.000000, "MIN LAT 2")
flyby(-89.999999, 0.000000, "MIN LAT 3")

# MAXIMUM LATITUDE
flyby(89.999999, 0.000000, "MAX LAT 1")
flyby(90.000000, 0.000000, "MAX LAT 2")
flyby(90.000001, 0.000000, "MAX LAT 3")

# MINIMUM LONGITUDE
flyby(0.000000, -180.000001, "MIN LON 1")
flyby(0.000000, -180.000000, "MIN LON 2")
flyby(0.000000, -179.999999, "MIN LON 3")

# MAXIMUM LONGITUDE
flyby(0.000000, 179.999999, "MAX LON 1")
flyby(0.000000, 180.000000, "MAX LON 2")
flyby(0.000000, 180.000001, "MAX LON 3")

# EDGES COMBINATION
flyby(-90.000000, -180.000000, "MIN LAT, MIN LON")
flyby(-90.000000, 180.000000, "MIN LAT, MAX LON")
flyby(90.000000, -180.000000, "MAX LAT, MIN LON")
flyby(90.000000, 180.000000, "MAX LAT, MAX LON")
