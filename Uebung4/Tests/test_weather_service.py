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

# TODO: Team A - Import nach erster Implementierung:
from Uebung4.Code.weather_service import get_weather_category as weather


class TestWeatherService:
    """
    Tests für Weather-API Service

    TDD-Vorgehen:
    1. Test schreiben (RED)
    2. Minimale Implementierung (GREEN)
    3. Refactoring
    """

    def test_placeholder(self):
        """
        Placeholder - ersetzt durch echte Tests!

        Beispiel-Tests:
        - Temperatur 20°C → "angenehm"
        - Temperatur -5°C → "frostgefahr"
        - Temperatur 5°C → "kalt"
        - Temperatur 13°C → "kühl"
        - Temperatur 28°C → "warm"
        - Temperatur 35°C → "heiß"
        """
        # assert True, "TODO: Durch echte Tests ersetzen"

    def test_angenehm(self):
        assert weather("Berlin") == "angenehm"

    def test_frostgefahr(self):
        assert weather("Warschau") == "frostgefahr"

    def test_kalt(self):
        assert weather("Kiew") == "kalt"

    def test_kühl(self):
        assert weather("Wien") == "kühl"

    def test_warm(self):
        assert weather("Rom") == "warm"

    def test_heiß(self):
        assert weather("Barcelona") == "heiß"

    # TODO: Team A - Beispiel für ersten echten Test:
    def test_angenehm_ext(self):
        """TDD-Zyklus 1: RED von [Name] um [Zeit]"""
        with patch('requests.get') as mock_get:
            # Simuliere API-Response
            mock_get.return_value.json.return_value = {"temperature": 20}

            assert weather("Berlin") == "angenehm"

            # Optional: Verifiziere API-Aufruf
            mock_get.assert_called_once()

    # TODO: Team A - Weitere Tests für alle Temperaturkategorien hinzufügen!
