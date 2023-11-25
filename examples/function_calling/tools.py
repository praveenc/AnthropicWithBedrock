import openmeteo_requests
import requests
import requests_cache
from loguru import logger
from retry_requests import retry


def get_weather_condition(code):
    """
    Lookup the weather condition based on the WMO Weather interpretation codes.

    Args:
    code (int): The weather code for which the condition needs to be found.

    Returns:
    str: A description of the weather condition.
    """

    # Dictionary mapping weather codes to their descriptions.
    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog and depositing rime fog",
        48: "Fog and depositing rime fog",
        51: "Drizzle: Light",
        53: "Drizzle: Moderate",
        55: "Drizzle: Dense intensity",
        56: "Freezing Drizzle: Light",
        57: "Freezing Drizzle: Dense intensity",
        61: "Rain: Slight",
        63: "Rain: Moderate",
        65: "Rain: Heavy intensity",
        66: "Freezing Rain: Light",
        67: "Freezing Rain: Heavy intensity",
        71: "Snow fall: Slight",
        73: "Snow fall: Moderate",
        75: "Snow fall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Slight",
        81: "Rain showers: Moderate",
        82: "Rain showers: Violent",
        85: "Snow showers slight",
        86: "Snow showers heavy",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }

    # Return the description if the code is found, otherwise return an error message.
    return weather_conditions.get(code, "Code not found.")


def get_weather(latitude: str, longitude: str, units: str = "F"):
    # url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    # response = requests.get(url)
    cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"

    # convert string values to float
    lat_float = float(latitude.replace("'", "").replace('"', ""))
    long_float = float(longitude.replace("'", "").replace('"', ""))

    params = {
        "latitude": lat_float,
        "longitude": long_float,
        "current": ["temperature_2m", "weather_code"],
    }

    if units == "F":
        params["temperature_unit"] = "fahrenheit"
    # logger.info(params)
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]

    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_weather_code = current.Variables(1).Value()
    conditions = get_weather_condition(current_weather_code)

    weather_dict = {
        "temperature": current_temperature_2m,
        "conditions": conditions,
    }
    # logger.info(weather_dict)

    return weather_dict


get_weather_description = """<function>
<function_name>get_weather</function_name>
<function_description>Returns weather data for a given latitude and longitude.</function_description>
<required_argument>latitude (str): Latitude coordinates for the Name of the city or Airport code</required_argument>
<required_argument>longitude (str): Longitude coordinates for the Name of the city or Airport code</required_argument>
<optional_argument>units (str): Temperature units, either "F" for Fahrenheit or "C" for Celsius, default "F"</optional_argument>
<returns> temperature (float): Current temperature in Fahrenheit - Conditions (str): Short text description of weather conditions</returns>
<example_call>get_weather(latitude="52.52", longitude="-122.419998", units="F")</example_call>
</function>
"""


def get_lat_long(place: str):
    if len(place.strip()) < 3:
        raise ValueError

    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place, "format": "json", "limit": 1}
    response = requests.get(url, params=params).json()

    if response:
        lat = response[0]["lat"]
        lon = response[0]["lon"]
        return {"latitude": lat, "longitude": lon}
    else:
        return None


get_lat_long_description = """<function>
<function_name>get_lat_long</function_name>
<function_description>Returns the latitude and longitude for a given place name.</function_description>
<required_argument>place (str): Name of the city or Airport code to geocode and get coordinates for.</required_argument>
<returns>latitude (str): Latitude coordinates of the place - longitude (str): Longitude coordinates of the place</returns>
<raises>ValueError: If invalid location provided</raises>
<example_call>get_lat_long(place="Seattle")</example_call>
</function>
"""

list_of_function_specs = [get_weather_description, get_lat_long_description]
