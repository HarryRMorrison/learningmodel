import json

def get_weather(city: str) -> str:
    """
    Get the weather for a city.

    Args:
        city: Name of the city
    """
    fake_weather = {
        "perth": {"temperature": 22, "condition": "sunny"},
        "sydney": {"temperature": 18, "condition": "rainy"},
    }

    result = fake_weather.get(
        city.lower(),
        {"error": "City not found"},
    )

    return json.dumps(result)


TOOLS = { get_weather: {   
                        "type": "function",
                        "function": {
                            "name": "get_weather",
                            "description": "Get the current weather for a city",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "city": {
                                        "type": "string",
                                        "description": "The city name"
                                    }
                                },
                                "required": ["city"]
                            }
                        }
                    },
}