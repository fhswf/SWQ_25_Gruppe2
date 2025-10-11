# Implementiert von: [HAHR], [PRSE]

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

from Uebung3.Code.konto import Konto


class TestKontoErstellung:
    """
    Tests für die Konto-Erstellung
    """
    # Umsetzung von HAHR
    def test_kontoerstellung_validId_positivSaldo(self):
        """Test: Konto mit gültiger ID und positivem Saldo erstellen"""
        konto = Konto(1, Decimal("100.00"))
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("100.00")

    # Umsetzung von HAHR
    def test_kontoerstellung_validId_zeroSaldo(self):
        """Test: Konto mit gültiger ID und Saldo 0 erstellen"""
        konto = Konto(2, Decimal("0.00"))
        assert konto.konto_id == 2
        assert konto.saldo == Decimal("0.00")

    # Umsetzung von HAHR
    def test_kontoerstellung_validId_negativSaldo(self):
        """Test: Konto mit gültiger ID und negativem Saldo → Exception"""
        with pytest.raises(ValueError):
            Konto(3, Decimal("-50.00"))
    
    # Umsetzung von HAHR
    def test_kontoerstellung_invalidId_negative(self):
        """Test: Konto mit ungültiger ID (negativ) → Exception"""
        with pytest.raises(ValueError):
            Konto(-1, Decimal("50.00"))

    # Umsetzung von PRSE
    def test_kontoerstellung_invalidId_zero(self):
        """Test: Konto mit ungültiger ID (0) → Exception"""
        with pytest.raises(ValueError):
            Konto(0, Decimal("50.00"))

    # Umsetzung von PRSE
    def test_kontoerstellung_invalidId_string(self):
        """Test: Konto mit ungültiger ID (String) → Exception"""
        with pytest.raises(ValueError):
            Konto("abc", Decimal("50.00"))

    # Umsetzung von PRSE
    def test_kontoerstellung_invalidSaldo_negative(self):
        """Test: Konto mit ungültigem Saldo (negativ) → Exception"""
        with pytest.raises(ValueError):
            Konto(1, Decimal("-10.00"))

    # Umsetzung von PRSE
    def test_kontoerstellung_invalidSaldo_string(self):
        """Test: Konto mit ungültigem Saldo, welches als string übergeben wird und zur Exception führt"""
        with pytest.raises(ValueError):
            Konto(1, "fünfzig")

    # Umsetzung von PRSE
    def test_kontoerstellung_id_none(self):
        """Test: Konto mit None als ID → Exception"""
        with pytest.raises(ValueError):
            Konto(None, Decimal("50.00"))

    # Umsetzung von PRSE
    def test_kontoerstellung_saldo_none(self):
        """Test: Konto mit None als Saldo → Exception"""
        with pytest.raises(ValueError):
            Konto(1, None)


class TestKontoEigenschaften:
    """
    Tests für Konto-Eigenschaften (Properties)
    TODO: Team A - Testet konto_id und saldo Properties
    """

    def test_placeholder_eigenschaften(self):
        """TODO: Team A - Tests für Properties"""
        # Beispiel-Tests:
        # - konto.konto_id gibt korrekte ID zurück
        # - konto.saldo gibt korrekten Saldo zurück
        # - Properties sind read-only (falls gewünscht)
        assert True, "TODO: Tests für Eigenschaften implementieren"


class TestEinzahlung:
    """
    Tests für die Einzahlungs-Funktionalität
    TODO: Team A - Testet alle Einzahlungs-Szenarien
    """

    def test_placeholder_einzahlung(self):
        """TODO: Team A - Tests für einzahlen() Methode"""
        # Beispiel-Tests:
        # - Einzahlung von positivem Betrag
        # - Saldo wird korrekt erhöht
        # - Einzahlung von 0 → Exception?
        # - Einzahlung von negativem Betrag → Exception?
        # - Einzahlung von ungültigem Typ → Exception?
        assert True, "TODO: Tests für Einzahlung implementieren"


class TestAuszahlung:
    """
    Tests für die Auszahlungs-Funktionalität  
    TODO: Team A - Testet alle Auszahlungs-Szenarien
    """

    def test_placeholder_auszahlung(self):
        """TODO: Team A - Tests für auszahlen() Methode"""
        # Beispiel-Tests:
        # - Auszahlung bei ausreichendem Saldo
        # - Saldo wird korrekt reduziert
        # - Auszahlung bei unzureichendem Saldo → Exception?
        # - Auszahlung von 0 → Exception?
        # - Auszahlung von negativem Betrag → Exception?
        # - Überziehung vermeiden
        assert True, "TODO: Tests für Auszahlung implementieren"


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


# TODO: Team A - Erweitern Sie diese Klassen oder fügen Sie neue hinzu!
# Weitere mögliche Test-Klassen:
# - TestKontoStringRepresentation
# - TestKontoEquality
# - TestKontoValidation