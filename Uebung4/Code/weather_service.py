"""
Implementierung: Weather-API Service
====================================

TODO: Team A - Implementiert get_weather_category() hier!

Die Funktion soll:
1. Weather-API aufrufen (in Tests gemockt)
2. Temperatur extrahieren
3. Kategorie zurückgeben

Hinweise:
- Nutzt requests.get() für API-Aufrufe
- API-URL: https://api.weather.com/current?city={city}
- Response-Format: {"temperature": 20}
- Startet mit minimalster Implementierung!
"""

import requests


def get_weather_category(city: str) -> str:
    """
    Ruft Weather-API auf und gibt Temperatur-Kategorie zurück

    Args:
        city: Stadt, für die das Wetter abgefragt wird

    Returns:
        Temperatur-Kategorie als String:
        - "frostgefahr" (< 0°C)
        - "kalt" (0-10°C)
        - "kühl" (11-15°C)
        - "angenehm" (16-24°C)
        - "warm" (25-30°C)
        - "heiß" (> 30°C)
    """
    # Tipp: Startet mit einfachstem Fall (z.B. nur "angenehm" zurückgeben)
    # Erweitert schrittweise basierend auf Tests!
    # API-Call-Code:
    url = f"https://api.weather.com/current?city={city}"

    # TDD-Zyklus 1-6: REFACTOR von [HAHR] - Exception Handling ausgebessert
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"network error when calling weather API: {e}") from e
    except ValueError as e:
        raise RuntimeError(f"invalid response from weather API: {e}") from e
    
    if not isinstance(data, dict):
        raise RuntimeError("unexpected response format from weather API")

    temperature = data.get("temperature")

    if temperature is None:
        raise RuntimeError("missing or invalid temperature in weather API response")
    try:
        temperature = float(temperature)
    except (TypeError, ValueError) as e:
        raise RuntimeError("missing or invalid temperature in weather API response") from e

    # TDD-Zyklus 1-6: GREEN von [HAHR & PRSE]
    if temperature < 0:
        return "frostgefahr"
    elif 0 <= temperature <= 10:
        return "kalt"
    elif 11 <= temperature <= 15:
        return "kuehl"
    elif 16 <= temperature <= 24:
        return "angenehm"
    elif 25 <= temperature <= 30:
        return "warm"
    else:
        return "heiss"
