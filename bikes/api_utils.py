import os
import json
import urllib.request

import pandas as pd

from weatherbit.api import Api
from datetime import datetime


apiKeyOPW = "ae0b8892c1c157c7a34956cb20307db7"
apiBaseOPW = "https://api.openweathermap.org/data/2.5/"
apiTypeOPW = "forecast?"
apiLocaleOPW = "q=Dublin,ie"
apiAuthOPW = "&APPID="

apiKeyWB = "a3e3e6c71bdd4d7586933ac1a57de143"
apiBaseWB = "https://api.weatherbit.io/v2.0/"
apiTypeWB = "forecast/3hourly?units=m"
apiLonWB = "&lon=-6.26181"
apiLangWB = "&lang=en"
apiPreWB = "&key="
apiLatWB = "&lat=53.3494146"

current_dir = os.path.dirname(os.path.realpath('__file__'))
station_file = current_dir + '/bikes/stationData.csv'
testRequest = {
    "departure_station": "PORTOBELLO_ROAD",
    "Year": 2019,
    "Month": 10,
    "Day": 26,
    "Hour": 17,
    "Minute": 20,
    "Second": 15,
    "arrival_station": "GRAND_CANAL_DOCK"
    }


def construct_request_OPW():
    """ Construct a five-day three-hourly OWM request """
    
    return apiBaseOPW + apiTypeOPW + apiLocaleOPW + apiAuthOPW + apiKeyOPW


def construct_request_WB():
    """ Construct a five-day three-hourly OWM request """
    
    return apiBaseWB + apiTypeWB + apiLonWB + apiLangWB + apiPreWB + apiKeyWB + apiLatWB


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


def find_timestamp_OPW(data, ye, mo, da, ho, mi, se):
    """ Find the data corresponding to the given time """

    epoch_time = int(to_epoch_time(ye, mo, da, ho, mi, se))
    forecasts = data["list"]
    
    for dictionary in forecasts:
        time = int(dictionary["dt"])
        if epoch_time >= time and epoch_time < (time + (3600 * 3)):
            return dictionary


def find_timestamp_WB(data, ye, mo, da, ho, mi, se):
    """ Find the data corresponding to the given time """

    epoch_time = int(to_epoch_time(ye, mo, da, ho, mi, se))
    forecasts = data["data"]
    
    for dictionary in forecasts:
        time = int(dictionary["ts"])
        if epoch_time >= time and epoch_time < (time + (3600 * 3)):
            return dictionary

        

def check_time(ye, mo, da, ho, mi, se):
    """ Make sure that the time is within the five-day bound """

    epoch_time = int(to_epoch_time(ye, mo, da, ho, mi, se))
    current_epoch = int(get_current_epoch())
    assertion = "Time must be no more than five days from now!"
    
    assert epoch_time < current_epoch + 3600 * 24 * 5, assertion


def kelvin_to_celsius(kelvin):
    """ Converts temperature to Ceslius """

    return kelvin - 273.15
    

def get_avg_temp_OPW(weather):
    """ Get average temperature for specific timestamp (C) """
    temp = weather["main"]["temp"]
    return kelvin_to_celsius(temp)


def get_min_temp_OPW(weather):
    """ Get minimum temperature for specific timestamp (C) """

    temp = weather["main"]["temp_min"]
    return kelvin_to_celsius(temp)


def get_max_temp_OPW(weather):
    """ Get maximum temperature for specific timestamp (C) """

    temp =  weather["main"]["temp_max"]
    return kelvin_to_celsius(temp)


def get_wind_speed_OPW(weather):
    """ Get wind speed for specific timestamp (m/s) """

    return weather["wind"]["speed"]


def get_sea_pressure_OPW(weather):
    """ Get sea-level pressure for specific timestamp (hPa) """

    return weather["main"]["sea_level"]


def get_precipitation_OPW(weather):
    """ Get precipitation for specific timestamp / 3 (mm) """

    if weather.get("rain") is None:
        return 0
    else:
        return weather["rain"]["3h"] / 3


def get_temperature_WB(weather):
    """ Get maximum temperature for specific timestamp (C) """
    
    return weather["app_temp"]


def get_precipitation_WB(weather):
    """ Get precipitation for specific timestamp (mm) """
    
    return weather["precip"]


def get_sea_pressure_WB(weather):
    """ Get sea-level pressure for specific timestamp (hPa) """
    
    return weather["pres"]


def get_wind_speed_WB(weather):
    """ Get wind speed for specific timestamp (m/s) """
    
    return weather["wind_spd"]


def get_humidity_WB(weather):
    """ Get relative humidity """
    
    return weather["rh"]


def get_dew_point_temperature(weather):
    """ Get dew point temperature (C) """

    return weather["dewpt"]



def get_data_WB(ye, mo, da, ho, mi, se):
    """ Get forecasted weather data for Dublin at given time """
    
    weather = get_weather(construct_request_WB())
    weather = find_timestamp_WB(weather, ye, mo, da, ho, mi, se)

    return {
        "Rainfall": get_precipitation_WB(weather),
        "Temperature": get_temperature_WB(weather),
        "Wet Bulb Temperature": 1,
        "Dew Point Temperature": get_dew_point_temperature(weather),
        "Vapour Pressure": 1,
        "Humidity": get_humidity_WB(weather),
        "Sea-level Pressure": get_sea_pressure_WB(weather),
        "Wind Speed": get_wind_speed_WB(weather),
        }


def get_station_data(station_name):
    """ Get information about the given station """

    csv = pd.read_csv(station_file)
    stations = list(csv["Station"])
    for num, station in enumerate(stations):
        if csv.loc[num, "Station"] == station_name:
            data = csv.iloc[[num]]

    if data is None:
        print("No station of this name found!")

    return data


def get_station_neighbours(station_data):
    """ Gets the closest statiosn to the given station """  
    
    return list(list(station_data.values)[0][-3:])


def get_station_behaviour(station_data):
    """ Get the average daily behaviour of given station """

    return list(list(station_data.values)[0][2:-3])


def get_station_capacity(station_data):
    """ Get the average daily behaviour of given station """

    return list(station_data.values)[0][1]


def get_station_info(station_name):
    """ Format station information nicely """

    data = get_station_data(station_name)
    
    return {
        "name": station_name,
        "capacity": get_station_capacity(data),
        "behaviour": get_station_behaviour(data),
        "neighbours": get_station_neighbours(data),
        }


def get_neighbours_info(station_info, prefix="N"):
    """ Gets the Information about the station's neighbours """

    return {prefix + "_{}".format(num + 1): get_station_info(neighbour)
            for num, neighbour in enumerate(station_info["neighbours"])}


def get_arrival_info(station_name):
    """ Get the info for all four stations """

    station_info = get_station_info(station_name)
    stations_info = get_neighbours_info(station_info, prefix="A")
    stations_info["A_0"] = station_info
    return stations_info


def get_departure_info(station_name):
    """ Get the info for all four stations """

    station_info = get_station_info(station_name)
    stations_info = get_neighbours_info(station_info, prefix="D")
    stations_info["D_0"] = station_info
    return stations_info


def get_all_infos(request):
    """ Get info for all stations """

    arrival_info = get_arrival_info(request["arrival_station"])
    departure_info = get_departure_info(request["departure_station"])
    arrival_info.update(departure_info)

    return arrival_info


def get_silly_estimate(station_info, hour, key):
    """ Build placeholder estimate for station occupancy """
    
    estimate = station_info["behaviour"][int(hour * 4)]
    
    return {key: {
        "name": station_info["name"], 
        "estimate": int(estimate),
        "capacity": station_info["capacity"],
    }}


def get_silly_estimates(request):
    """ Given a request, build silly estimates of occupancies """

    return_dict = {}
    hour = request["Hour"]
    infos = get_all_infos(request)
    for key in infos.keys():
        item = infos[key]
        item_dict = get_silly_estimate(item, hour, key)
        return_dict.update(item_dict)

    return return_dict
        
