import json
import re
from typing import Any, Dict, Optional

import requests
from requests.exceptions import JSONDecodeError, RequestException


def calculate(expression):
    # Remove any non-digit or non-operator characters from the expression
    expression = re.sub(r"[^0-9+\-*/().]", "", expression)

    try:
        # Evaluate the expression using the built-in eval() function
        result = eval(expression)
        return str(result)
    except (SyntaxError, ZeroDivisionError, NameError, TypeError, OverflowError):
        return "Error: Invalid expression"


def get_lat_long(place: str):
    url = "https://geocode.xyz"
    params = {"locate": place, "geoit": "JSON", "region": "US"}
    headers = {"User-Agent": "YourApp/1.0"}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        lat_long_dict = response.json()

        if lat_long_dict and "alt" in lat_long_dict and "loc" in lat_long_dict["alt"]:
            longt = lat_long_dict["alt"]["loc"]["longt"]
            latt = lat_long_dict["alt"]["loc"]["latt"]
            print(f"Place: {place}")
            print(f"Longitude: {longt}")
            print(f"Latitude: {latt}")
            return {"latitude": latt, "longitude": longt}
        else:
            print(f"No location data found for {place}")
            return None

    except RequestException as e:
        print(f"Request error: {e}")
        return None
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return None


def get_weather(latitude: str, longitude: str):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    return response.json()


tools = [
    {
        "name": "calculator",
        "description": "A simple calculator that performs basic arithmetic operations.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate (e.g., '2 + 3 * 4').",
                }
            },
            "required": ["expression"],
        },
    },
    {
        "name": "get_lat_long",
        "description": "Tool to retrieve latitude and longitude for a given place.",
        "input_schema": {
            "type": "object",
            "properties": {
                "place": {
                    "type": "string",
                    "description": "The place name to geocode and get coordinates for. (e.g., San Francisco)",
                }
            },
            "required": ["place"],
        },
    },
    {
        "name": "get_weather",
        "description": "Returns weather data for a given latitude and longitude.",
        "input_schema": {
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "string",
                    "description": "The latitude coordinate as a string",
                },
                "longitude": {
                    "type": "string",
                    "description": "The longitude coordinate as a string",
                },
            },
            "required": ["latitude", "longitude"],
        },
    },
]