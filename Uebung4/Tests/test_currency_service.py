"""
TDD-Template für Currency-API Service
=====================================

Team B - Tests für get_exchange_rate_assessment().

Aufgabe:
- Funktion ruft Currency-API auf (mocken!)
- Extrahiert Wechselkurs aus JSON
- Gibt Bewertung zurück basierend auf Kurs

Wechselkurs-Bewertungen (Beispiel: EUR → USD):
- < 0.90:     "sehr unguenstig"
- 0.90-0.99:  "unguenstig"
- 1.00-1.09:  "fair"
- 1.10-1.19:  "guenstig"
- ≥ 1.20:     "sehr guenstig"

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!
"""

#implementiert von [LNBT]

import pytest
from unittest.mock import patch

# Import nach eurer Struktur:
from Uebung4.Code.currency_service import get_exchange_rate_assessment


class TestCurrencyService:
    """
    Basis-Tests für Currency-API Service.
    """

    def test_fair_rate(self):
        """TDD-Zyklus 1: RED/ GREEN – Kurs 1.05 -> fair"""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 1.05}

            result = get_exchange_rate_assessment("EUR", "USD")

            assert result == "fair"
            mock_get.assert_called_once()

    @pytest.mark.parametrize(
        "rate, expected",
        [
            (0.85, "sehr unguenstig"),
            (0.90, "unguenstig"),
            (0.95, "unguenstig"),
            (1.00, "fair"),
            (1.08, "fair"),
            (1.10, "guenstig"),
            (1.15, "guenstig"),
            (1.20, "sehr guenstig"),
            (1.35, "sehr guenstig"),
        ],
    )
    def test_all_rate_ranges(self, rate, expected):
        """Testet alle Bewertungsbereiche via Mock."""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": rate}

            result = get_exchange_rate_assessment("EUR", "USD")

            assert result == expected

    def test_api_called_with_correct_url(self):
        """Optional: prüft URL-Building."""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 1.05}

            get_exchange_rate_assessment("EUR", "USD")

            called_url = mock_get.call_args[0][0]
            assert "from=EUR" in called_url
            assert "to=USD" in called_url

    def test_missing_rate_raises_value_error(self):
        """Robustheit: fehlender rate-Field."""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"foo": 1.05}

            with pytest.raises(ValueError):
                get_exchange_rate_assessment("EUR", "USD")

    def test_non_numeric_rate_raises_type_error(self):
        """Robustheit: rate ist nicht numerisch."""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": "1.05"}

            with pytest.raises(TypeError):
                get_exchange_rate_assessment("EUR", "USD")


class TestCurrencyServiceAdditional:
    """
    Erweiterte Tests:
    - Grenzwerte
    - Dynamische Mocks für verschiedene Währungspaare
    - Robustheit bei int-Rates
    """

    @pytest.mark.parametrize(
        "rate, expected",
        [
            (0.8999, "sehr unguenstig"),  # knapp unter 0.90
            (0.9000, "unguenstig"),       # genau 0.90
            (0.9999, "unguenstig"),       # knapp unter 1.00
            (1.0000, "fair"),             # genau 1.00
            (1.0999, "fair"),             # knapp unter 1.10
            (1.1000, "guenstig"),         # genau 1.10
            (1.1999, "guenstig"),         # knapp unter 1.20
            (1.2000, "sehr guenstig"),    # genau 1.20
        ],
    )
    def test_boundary_values(self, rate, expected):
        """Testet die exakten Grenzwerte der Kategorien."""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": rate}

            assert get_exchange_rate_assessment("EUR", "USD") == expected

    def test_different_currency_pairs_dynamic_mock(self):
        """
        Dynamisches Mocking abhängig von URL:
        Prüft, dass unterschiedliche Währungspaare unterschiedliche Bewertungen liefern
        UND dass die URL-Parameter genutzt werden.
        """
        def mock_json_for_url():
            url = mock_get.call_args[0][0]

            if "from=EUR" in url and "to=USD" in url:
                return {"rate": 1.05}  # fair
            if "from=EUR" in url and "to=GBP" in url:
                return {"rate": 0.85}  # sehr unguenstig
            if "from=USD" in url and "to=EUR" in url:
                return {"rate": 1.15}  # guenstig

            return {"rate": 1.25}      # Default sehr guenstig

        with patch("requests.get") as mock_get:
            mock_get.return_value.json.side_effect = mock_json_for_url

            assert get_exchange_rate_assessment("EUR", "USD") == "fair"
            assert get_exchange_rate_assessment("EUR", "GBP") == "sehr unguenstig"
            assert get_exchange_rate_assessment("USD", "EUR") == "guenstig"
            assert mock_get.call_count == 3

    def test_rate_is_int_is_accepted(self):
        """Optional: API liefert int statt float."""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"rate": 1}  # int

            assert get_exchange_rate_assessment("EUR", "USD") == "fair"
