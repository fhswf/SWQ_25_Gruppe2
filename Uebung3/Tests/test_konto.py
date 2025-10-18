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
from ..Code.konto import Konto

class TestKontoErstellung:

    def test_konto_erstellung_positive_saldo_valid_id(self):
        # Testen der Kontoerstellung mit positivem Saldo und gültiger ID
        konto = Konto(1, Decimal("100.00"))
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("100.00")

    def test_konto_erstellung_null_saldo_valid_id(self):
        # Testen der Kontoerstellung mit null Saldo
        konto = Konto(1)
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("0.00")

    def test_konto_erstellung_invalid_id(self):
        # Testen von ungültigen Konto-IDs
        with pytest.raises((ValueError)):
            Konto(-1)
        with pytest.raises((ValueError)):
            Konto(None)
        with pytest.raises((TypeError)):
            Konto("abc")

    def test_konto_erstellung_invalid_saldo(self):
        # Testen von ungültigen Salden
        with pytest.raises((ValueError)):
            Konto(1, Decimal("-100.00"))
        with pytest.raises((TypeError)):
            Konto(1, "abc")


class TestKontoEigenschaften:

    def test_eigenschaften(self):
        # Testen der Eigenschaften konto_id und saldo
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
        # Testen einer gültigen Einzahlung
        konto = Konto(1, Decimal("100.00"))
        konto.einzahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("150.00")

    def test_einzahlen_invalid_betrag(self):
        # Testen von ungültigen Beträgen
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("0.00"))

    def test_einzahlen_negative_betrag(self):
        # Testen von negativen Beträgen
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("-10.00"))

    def test_einzahlen_non_decimal(self):
        # Testen von nicht-Decimal Beträgen
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(TypeError):
            konto.einzahlen("abc")


class TestAuszahlung:

    def test_auszahlen_valid(self):
        # Testen einer gültigen Auszahlung
        konto = Konto(1, Decimal("100.00"))
        konto.auszahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("50.00")

    def test_auszahlen_insufficient_funds(self):
        # Testen von unzureichenden Mitteln
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("150.00"))

    def test_auszahlen_invalid_betrag(self):
        #
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("0.00"))

    def test_auszahlen_negative_betrag(self):
        # Testen von negativen Beträgen
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("-10.00"))

    def test_auszahlen_non_decimal(self):
        # Testen von nicht-Decimal Beträgen
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(TypeError):
            konto.auszahlen("abc")


class TestKontoGrenzfaelle:

    def test_decimal_precision(self):
        # Testen von Dezimalgenauigkeit
        konto = Konto(1, Decimal("100.05"))
        assert konto.saldo == Decimal("100.05")
        konto.einzahlen(Decimal("0.11"))
        assert konto.saldo == Decimal("100.16")

    def test_large_amounts(self):
        # Testen von sehr großen Beträgen
        konto = Konto(1, Decimal("1000000000.00"))
        konto.einzahlen(Decimal("500000000.00"))
        assert konto.saldo == Decimal("1500000000.00")

    def test_small_amounts(self):
        # Testen von sehr kleinen Beträgen
        konto = Konto(1, Decimal("0.01"))
        konto.einzahlen(Decimal("0.05"))
        assert konto.saldo == Decimal("0.06")

    def test_konto_equality(self):
        # Zwei Konten mit gleichen IDs und Salden sollten als gleich betrachtet werden
        konto1 = Konto(1, Decimal("100.00"))
        konto2 = Konto(1, Decimal("100.00"))
        konto3 = Konto(2, Decimal("100.00"))
        assert konto1.konto_id == konto2.konto_id
        assert konto1.saldo == konto2.saldo
        assert konto1.konto_id != konto3.konto_id

    def test_konto_string_representation(self):
        # Überprüfen der String- und Repräsentationsmethoden
        konto = Konto(1, Decimal("100.00"))
        assert str(konto) == f"Konto(ID: {konto.konto_id}, Saldo: {konto.saldo})"
        assert repr(konto) == f"Konto(konto_id={konto.konto_id}, saldo={konto.saldo})"
