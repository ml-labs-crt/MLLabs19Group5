import json
import urllib.request

from datetime import datetime


apiKey = "ae0b8892c1c157c7a34956cb20307db7"
apiBase = "https://api.openweathermap.org/data/2.5/"
apiType = "forecast?"
apiLocale = "q=Dublin,ie"
apiAuth = "&APPID="


def construct_request():
    """ Construct a five-day three-hourly OWM request """
    
    return apiBase + apiType + apiLocale + apiAuth + apiKey


def send_request(request):
    """ Send request to OWM and retrieve resposne body """
    
    return urllib.request.urlopen(request).read()


def get_weather(request):
    """ Send request to OWM and return as a dictionary """
    
    body = send_request(request)
    return json.loads(body.decode("utf-8"))


def to_epoch_time(ye, mo, da, ho, mi, se):
    """ Converts human-readable time to epoch time """

    return datetime(ye, mo, da, ho, mi, se).strftime('%s')


def get_current_epoch():
    """ Gets the current GMT epoch time """

    time = datetime.now()
    return time.strftime('%s')


def find_timestamp(data, ye, mo, da, ho, mi, se):
    """ Find the data corresponding to the given time """

    epoch_time = int(to_epoch_time(ye, mo, da, ho, mi, se))
    forecasts = data["list"]
    
    for dictionary in forecasts:
        time = int(dictionary["dt"])
        if epoch_time >= time and epoch_time < (time + (3600 * 3)):
            return dictionary


def check_time(ye, mo, da, ho, mi, se):
    """ Make sure that the time is within the five-day bound """

    epoch_time = int(to_epoch_time(ye, mo, da, ho, mi, se))
    current_epoch = int(get_current_epoch())
    assertion = "Time must be no more than five days from now!"
    
    assert epoch_time < current_epoch + 3600 * 24 * 5, assertion


def kelvin_to_celsisu(kelvin):
    """ Converts temperature to Ceslius """

    return kelvin - 273.15
    

def get_avg_temp(weather):
    """ Get average temperature for specific timestamp (C) """
    temp = weather["main"]["temp"]
    return kelvin_to_celsius(temp)


def get_min_temp(weather):
    """ Get minimum temperature for specific timestamp (C) """

    temp = weather["main"]["temp_min"]
    return kelvin_to_celsius(temp)


def get_max_temp(weather):
    """ Get maximum temperature for specific timestamp (C) """

    temp =  weather["main"]["temp_max"]
    return kelvin_to_celsius(temp)


def get_wind_speed(weather):
    """ Get wind speed for specific timestamp (m/s) """

    return weather["wind"]["speed"]


def get_sea_pressure(weather):
    """ Get sea-level pressure for specific timestamp (hPa) """

    return weather["main"]["sea_level"]


def get_precipitation(weather):
    """ Get precipitation for specific timestamp / 3 (mm) """

    if weather.get("rain") is None:
        return 0
    else:
        return weather["rain"]["3h"] / 3

    


