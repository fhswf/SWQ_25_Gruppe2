"""
TDD-Template für Weather-API Service
====================================

TODO: Team A - Implementiert get_weather_category() testgetrieben!

Aufgabe:
- Funktion ruft Weather-API auf (mocken!)
- Extrahiert Temperatur aus JSON
- Gibt Kategorie zurück basierend auf Temperatur

Temperatur-Kategorien:
- < 0°C:      "frostgefahr"
- 0-10°C:     "kalt"
- 11-15°C:    "kühl"
- 16-24°C:    "angenehm"
- 25-30°C:    "warm"
- > 30°C:     "heiß"

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Dokumentiert eure Autorschaft: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest
from unittest.mock import patch
from Uebung4.Code.weather_service import get_weather_category


class TestWeatherService:
    """
    Tests für Weather-API Service

    TDD-Vorgehen:
    1. Test schreiben (RED)
    2. Minimale Implementierung (GREEN)
    3. Refactoring
    """

    """
    def test_placeholder(self):
        
        Placeholder - ersetzt durch echte Tests!

        Beispiel-Tests:
        - Temperatur 20°C → "angenehm"
        - Temperatur -5°C → "frostgefahr"
        - Temperatur 5°C → "kalt"
        - Temperatur 13°C → "kühl"
        - Temperatur 28°C → "warm"
        - Temperatur 35°C → "heiß"
       
        assert True, "TODO: Durch echte Tests ersetzen"
     """

    # TDD-Zyklus 1: RED von [PRSE]
    def test_angenehm(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 20}
            result = get_weather_category("Berlin")
            assert result == "angenehm"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5
            )

    # TDD-Zyklus 2: RED von [PRSE]
    def test_frostgefahr(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": -5}
            result = get_weather_category("Berlin")
            assert result == "frostgefahr"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5
            )

    # TDD-Zyklus 3: RED von [HAHR]
    def test_kalt(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 5}
            result = get_weather_category("Berlin")
            assert result == "kalt"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5
            )

    # TDD-Zyklus 4: RED von [HAHR]
    def test_kuehl(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 13}
            result = get_weather_category("Berlin")
            assert result == "kuehl"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5
            )

    # TDD-Zyklus 5: RED von [PRSE]
    def test_warm(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 28}
            result = get_weather_category("Berlin")
            assert result == "warm"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5
            )

    # TDD-Zyklus 6: RED von [HAHR]
    def test_heiss(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 35}
            result = get_weather_category("Berlin")
            assert result == "heiss"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5
            )

    # TDD-Zyklus 6: RED von [PRSE]
    def test_angenehm_Hamburg(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 20}
            result = get_weather_category("Hamburg")
            assert result == "angenehm"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Hamburg",
                timeout=5
            )

    # TDD-Zyklus 6: RED von [PRSE]
    def test_warm_Hamburg(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 29}
            result = get_weather_category("Hamburg")
            assert result == "warm"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Hamburg",
                timeout=5
            )

    # TDD-Zyklus 6: RED von [PRSE]
    def test_angenehm_andere_Temperatur(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 21}
            result = get_weather_category("Berlin")
            assert result == "angenehm"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5
            )