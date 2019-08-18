import math
import time
from datetime import datetime
from datetime import timedelta
from functools import wraps

import numpy as np
import requests

# NASA's API and API key
API = "https://api.nasa.gov/planetary/earth/assets"

# This can go to some configuration file
API_KEY = "9Jz6tLIeJ0yY9vjbEUWaH9fsXA930J9hspPchut"

# Constants
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'

# Error Constants
INVALID_COORDINATES = 'ERROR_INVALID_COORDINATE'
INSUFFICIENT_DATA = 'ERROR_INSUFFICIENT_DATA_RECORDED'
UNHANDLED_RESPONSE = 'ERROR_UNHANDLED_RESPONSE'


class BaseException(Exception):
    """
    Base exception class
    """
    err_code = None
    err_str = None

    def to_dict(self):
        """
        return json object
        """
        return {
            'err_code': self.err_code,
            'err_str': self.err_str
        }


class UnhandledResponseError(BaseException):
    """
    Unhandled response
    """
    err_code = 1000
    err_str = UNHANDLED_RESPONSE


class InvalidCoordinateError(BaseException):
    """
    Invalid Coordinate exception
    """
    err_code = 1001
    err_str = INVALID_COORDINATES


class InsufficientDataError(BaseException):
    """
    Insufficient data recorded
    """
    err_code = 1002
    err_str = INSUFFICIENT_DATA


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2):
    """Retry calling the decorated function using an exponential backoff.

    :param ExceptionToCheck: the exception to check
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay each retry
    :type backoff: int
    """

    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry


@retry(UnhandledResponseError, tries=4)
def flyby(latitude, longitude):
    """
    get next time a photo will be taken by a satellite
    :param latitude:
    :param longitude:
    :return:
    """
    try:
        if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
            raise InvalidCoordinateError

        querystring = {"api_key": API_KEY, "lat": str(latitude),
                       "lon": str(longitude)}

        response = requests.request("GET", API, params=querystring)

        # if response.status_code == 403
        if response.status_code != 200:
            raise UnhandledResponseError

        json_response = response.json()
        total_records = json_response.get('count')
        results = json_response.get('results')

        if total_records < 2:
            raise InsufficientDataError

        avg_time_delta, last_date = \
            get_last_date_and_average_time_delta(results, total_records)

        sd = get_standard_deviation(results, total_records)
        print("latest : {}".format(last_date))
        print("average time delta : {}".format(avg_time_delta))

        dates_diff = datetime.today() - last_date
        if dates_diff.total_seconds() < 0:
            predicted = last_date
        else:
            dates_diff % avg_time_delta
            predicted = datetime.today() + (dates_diff % avg_time_delta)

        print("Next time: {}".format(predicted))
        print("Next time also can be between {} : {}".format(
            predicted - timedelta(seconds=sd),
            predicted + timedelta(seconds=sd)))
        print("-----------------------")
        return predicted

    except (InvalidCoordinateError, InsufficientDataError) as err:
        print(err.to_dict())
        print("-----------------------")
        return err.to_dict()


def get_last_date_and_average_time_delta(results, count):
    dates = map(lambda x: datetime.strptime(x['date'], DATE_FORMAT), results)
    dates_list = list(dates)

    oldest = min(dates_list)
    youngest = max(dates_list)

    # Average time taken is the duration between the youngest and oldest
    # recorded date, divided by the number of periods (n - 1)
    ave_time_delta = (youngest - oldest) / (count - 1)
    return ave_time_delta, youngest


def get_standard_deviation(results, count):
    str_dates = map(lambda x: x['date'], results)
    mean_date = (np.array(list(str_dates), dtype='datetime64[s]')
                 .view('i8')
                 .mean()
                 .astype('datetime64[s]'))
    dates = map(lambda x: datetime.strptime(x['date'], DATE_FORMAT), results)
    dates_list = list(dates)
    sd = 0.0
    for date in dates_list:
        date_diff = date - mean_date.astype(datetime)
        sd += date_diff.seconds ** 2
    sd = math.sqrt(sd / float(count - 1))
    return sd


if __name__ == "__main__":
    print("GULF OF GUINEA")
    result = flyby(0.000000, 0.000000)
    # assert result['err_str'] == INSUFFICIENT_DATA
    #
    # print("GRAND CANYON")
    # result = flyby(36.098592, -112.097796)
    # assert result is not None
    #
    # print("NIAGARA FALLS")
    # result = flyby(43.078154, -79.075891)
    # assert result is not None
    #
    # print("FOUR CORNERS")
    # result = flyby(36.998979, -109.045183)
    # assert result is not None
    #
    # print("DELPHIX")
    # result = flyby(37.7937007, -122.4039064)
    # assert result is not None
    #
    # print("Invalid Latitude Negative")
    # result = flyby(-90.000001, 0.000000, )
    # assert result['err_str'] == INVALID_COORDINATES
    # print("Minimum Latitude")
    # result = flyby(-90.000000, 0.000000)
    # assert result['err_str'] == INSUFFICIENT_DATA
    #
    # print("Invalid Latitude Positive")
    # result = flyby(90.000001, 0.000000, )
    # assert result['err_str'] == INVALID_COORDINATES
    # print("Maximum Latitude")
    # result = flyby(90.000000, 0.000000)
    # assert result['err_str'] == INSUFFICIENT_DATA
    #
    # print("Invalid Longitude Negative")
    # result = flyby(0.000000, -180.000001)
    # assert result['err_str'] == INVALID_COORDINATES
    # print("Minimum Longitude")
    # result = flyby(0.000000, -180.000000)
    # assert result['err_str'] == INSUFFICIENT_DATA
    #
    # print("Invalid Longitude Positive")
    # result = flyby(0.000000, 180.000001, )
    # assert result['err_str'] == INVALID_COORDINATES
    # print("Maximum Longitude")
    # result = flyby(0.000000, 180.000000, )
    # assert result['err_str'] == INSUFFICIENT_DATA
