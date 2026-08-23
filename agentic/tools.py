import json
from pydantic import BaseModel, ConfigDict, Field

class GetWeatherArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    city: str = Field(
        min_length=1,
        description="Name of the city"
    )

class GetSurfForecastArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    city: str = Field(
        min_length=1,
        description="Name of the city"
    )

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

def get_surf_forecast(city: str) -> str:
    """
    Get the surf forecast for a city.

    Args:
        city: Name of the city
    """
    fake_surf_forecast = {
        "perth": {"wave_height": 1.5, "condition": "good"},
        "sydney": {"wave_height": 0.5, "condition": "poor"},
    }

    result = fake_surf_forecast.get(
        city.lower(),
        {"error": "City not found"},
    )

    return json.dumps(result)

TOOLS = {
    "get_weather": {
        "function": get_weather,
        "args_model": GetWeatherArgs,
        "description": "Get the current weather for a city.",
    },
    "get_surf_forecast": {
        "function": get_surf_forecast,
        "args_model": GetSurfForecastArgs,
        "description": "Get the surf forecast for a city.",
    }
}

def build_tool_schemas():
    schemas = []

    for name, tool in TOOLS.items():
        schemas.append({
            "type": "function",
            "function": {
                "name": name,
                "description": tool["description"],
                "parameters": tool["args_model"].model_json_schema(),
            },
        })

    return schemas