# Implementiert von: SNKM
"""
Test-Template für die Konto-Klasse (Test-After Approach)
========================================================

TODO: Team A - Implementieren Sie hier Ihre Tests NACH der Konto-Implementierung!

Arbeitsablauf:
1. Implementieren Sie zuerst die Konto-Klasse in Code/konto.py
2. Schreiben Sie dann hier umfassende Tests für Ihren Code
3. Testen Sie normale Fälle UND Grenzfälle
4. Dokumentieren Sie Ihre Autorschaft in den Tests

Tipps für gute Tests:
- Verwenden Sie aussagekräftige Test-Namen
- Testen Sie eine Sache pro Test
- Nutzen Sie pytest.raises() für Exception-Tests
- Denken Sie an Grenzwerte (0, negative Zahlen)
"""

import pytest
from decimal import Decimal

# TODO: Team A - Entkommentiert nach eurer Implementierung:
from ..Code.konto import Konto

class TestKontoErstellung:
    """
    Tests für die Konto-Erstellung
    TODO: Team A - Implementieren Sie Tests für den Konstruktor
    """

    def test_konto_erstellung_positive_saldo_valid_id(self):
        konto = Konto(1, Decimal("100.00"))
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("100.00")

    def test_konto_erstellung_null_saldo_valid_id(self):
        konto = Konto(1)
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("0.00")

    def test_konto_erstellung_invalid_id(self):
        with pytest.raises(ValueError):
            Konto(-1)
        with pytest.raises(ValueError):
            Konto(None)
        with pytest.raises(ValueError):
            Konto("abc")

    def test_konto_erstellung_invalid_saldo(self):
        with pytest.raises(ValueError):
            Konto(1, Decimal("-100.00"))
        with pytest.raises(ValueError):
            Konto(1, "abc")


class TestKontoEigenschaften:

    def test_eigenschaften(self):
        konto = Konto(1, Decimal("50.00"))
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("50.00")

    def test_eigenschaften_immutable(self):
        konto = Konto(1, Decimal("50.00"))
        # Versuchen, Properties zu setzen (sollte fehlschlagen)
        with pytest.raises(AttributeError):
            konto.konto_id = 2
        with pytest.raises(AttributeError):
            konto.saldo = Decimal("100.00")


class TestEinzahlung:

    def test_einzahlen(self):
        konto = Konto(1, Decimal("100.00"))
        konto.einzahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("150.00")

    def test_einzahlen_invalid_betrag(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("0.00"))

    def test_einzahlen_negative_betrag(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("-10.00"))

    def test_einzahlen_non_decimal(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen("abc")


class TestAuszahlung:

    def test_auszahlen_valid(self):
        konto = Konto(1, Decimal("100.00"))
        konto.auszahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("50.00")

    def test_auszahlen_insufficient_funds(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("150.00"))

    def test_auszahlen_invalid_betrag(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("0.00"))

    def test_auszahlen_negative_betrag(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("-10.00"))

    def test_auszahlen_non_decimal(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen("abc")


class TestKontoGrenzfaelle:
    """
    Tests für Grenzfälle und Besonderheiten
    TODO: Team A - Testet Edge Cases und besondere Situationen
    """

    def test_placeholder_grenzfaelle(self):
        """TODO: Team A - Tests für Grenzfälle"""
        # Beispiel-Tests:
        # - Sehr große Beträge
        # - Sehr kleine Beträge (Cent-Bereich)
        # - Decimal-Präzision
        # - String-Repräsentation (__str__, __repr__)
        # - Gleichheit von Konten
        assert True, "TODO: Tests für Grenzfälle implementieren"

    def test_placeholder_decimal_precision(self):
        konto = Konto(1, Decimal("100.05"))
        assert konto.saldo == Decimal("100.05")
        konto.einzahlen(Decimal("0.11"))
        assert konto.saldo == Decimal("100.16")

    def test_placeholder_large_amounts(self):
        konto = Konto(1, Decimal("1000000000.00"))
        konto.einzahlen(Decimal("500000000.00"))
        assert konto.saldo == Decimal("1500000000.00")

    def test_placeholder_small_amounts(self):
        konto = Konto(1, Decimal("0.01"))
        konto.auszahlen(Decimal("0.05"))
        assert konto.saldo == Decimal("0.05")

    def test_konto_equality(self):
        konto1 = Konto(1, Decimal("100.00"))
        konto2 = Konto(1, Decimal("100.00"))
        konto3 = Konto(2, Decimal("100.00"))
        assert konto1 == konto2
        assert konto1 != konto3

    def test_konto_string_representation(self):
        konto = Konto(1, Decimal("100.00"))
        assert str(konto) == "Konto(ID: 1, Saldo: 100.00)"
        assert repr(konto) == "Konto(konto_id=1, saldo=Decimal('100.00'))"


# TODO: Team A - Erweitern Sie diese Klassen oder fügen Sie neue hinzu!
# Weitere mögliche Test-Klassen:
# - TestKontoStringRepresentation
# - TestKontoEquality
# - TestKontoValidation
