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

from ..Code.konto import Konto


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
        with pytest.raises(TypeError):
            Konto(1, "fünfzig")

    # Umsetzung von PRSE
    def test_kontoerstellung_id_none(self):
        """Test: Konto mit None als ID → Exception"""
        with pytest.raises(ValueError):
            Konto(None, Decimal("50.00"))

    # Umsetzung von PRSE
    def test_kontoerstellung_saldo_none(self):
        """Test: Konto mit None als Saldo → Exception"""
        with pytest.raises(TypeError):
            Konto(1, None)


class TestKontoEigenschaften:
    """
    Tests für Konto-Eigenschaften (Properties)
    """
    # Beispiel-Tests:
    # - konto.konto_id gibt korrekte ID zurück
    # - konto.saldo gibt korrekten Saldo zurück
    # - Properties sind read-only (falls gewünscht)

    # Umsetzung von HAHR
    def test_konto_id_read_only(self):
        """Test: konto_id Property ist read-only"""
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(AttributeError):
            konto.konto_id = 2

    # Umsetzung von HAHR
    def test_saldo_read_only(self):
        """Test: saldo Property ist read-only"""
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(AttributeError):
            konto.saldo = Decimal("200.00")

    # Umsetzung von HAHR
    def test_konto_id_type(self):
        """Test: konto_id Property gibt int zurück"""
        konto = Konto(1, Decimal("100.00"))
        assert isinstance(konto.konto_id, int)

    # Umsetzung von HAHR
    def test_saldo_type(self):
        """Test: saldo Property gibt Decimal zurück"""
        konto = Konto(1, Decimal("100.00"))
        assert isinstance(konto.saldo, Decimal)


class TestEinzahlung:
    """
    Tests für die Einzahlungs-Funktionalität
    """
    # Beispiel-Tests:
    # - Einzahlung von positivem Betrag
    # - Saldo wird korrekt erhöht
    # - Einzahlung von 0 → Exception?
    # - Einzahlung von negativem Betrag → Exception?
    # - Einzahlung von ungültigem Typ → Exception?

    # Umsetzung von HAHR
    def test_einzahlung_positiv(self):
        """Test: Einzahlung von positivem Betrag"""
        konto = Konto(1, Decimal("100.00"))
        konto.einzahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("150.00")

    # Umsetzung von HAHR
    def test_einzahlung_zero(self):
        """Test: Einzahlung von 0 → Exception"""
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("0.00"))

    # Umsetzung von HAHR
    def test_einzahlung_negativ(self):
        """Test: Einzahlung von negativem Betrag → Exception"""
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("-10.00"))

    # Umsetzung von HAHR
    def test_einzahlung_invalid_type(self):
        """Test: Einzahlung von ungültigem Typ → Exception"""
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(TypeError):
            konto.einzahlen("fünfzig")

    # Umsetzung von HAHR
    def test_erhoehung_saldo(self):
        """Test: Saldo wird korrekt erhöht nach Einzahlung"""
        konto = Konto(1, Decimal("200.00"))
        konto.einzahlen(Decimal("75.50"))
        assert konto.saldo == Decimal("275.50")


class TestAuszahlung:
    """
    Tests für die Auszahlungs-Funktionalität  
    """
    # Beispiel-Tests:
    # - Auszahlung bei ausreichendem Saldo
    # - Saldo wird korrekt reduziert
    # - Auszahlung bei unzureichendem Saldo → Exception?
    # - Auszahlung von 0 → Exception?
    # - Auszahlung von negativem Betrag → Exception?
    # - Überziehung vermeiden

    # Umsetzung von HAHR
    def test_auszahlung_ausreichend_saldo(self):
        """Test: Auszahlung bei ausreichendem Saldo"""
        konto = Konto(1, Decimal("100.00"))
        konto.auszahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("50.00")

    # Umsetzung von HAHR
    def test_auszahlung_unzureichend_saldo(self):
        """Test: Auszahlung bei unzureichendem Saldo → Exception"""
        konto = Konto(1, Decimal("30.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("50.00"))

    # Umsetzung von HAHR
    def test_auszahlung_zero(self):
        """Test: Auszahlung von 0 → Exception"""
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("0.00"))

    # Umsetzung von HAHR
    def test_auszahlung_negativ(self):
        """Test: Auszahlung von negativem Betrag → Exception"""
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("-20.00"))

    # Umsetzung von HAHR
    def test_saldo_nicht_negativ(self):
        """Test: Konto darf nicht überzogen werden"""
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("150.00"))

    # Umsetzung von HAHR
    def test_saldo_reduziert(self):
        """Test: Saldo wird korrekt reduziert nach Auszahlung"""
        konto = Konto(1, Decimal("200.00"))
        konto.auszahlen(Decimal("75.50"))
        assert konto.saldo == Decimal("124.50")


class TestKontoGrenzfaelle:
    """
    Tests für Grenzfälle und Besonderheiten
    """
    # Beispiel-Tests:
    # - Sehr große Beträge
    # - Sehr kleine Beträge (Cent-Bereich)
    # - Decimal-Präzision
    # - String-Repräsentation (__str__, __repr__)
    # - Gleichheit von Konten

    # Umsetzung von HAHR
    def test_einzahlung_grosser_betrag(self):
        """Test: Einzahlung eines sehr großen Betrags"""
        konto = Konto(1, Decimal("1000.00"))
        konto.einzahlen(Decimal("1000000.00"))
        assert konto.saldo == Decimal("1001000.00")

    # Umsetzung von HAHR
    def test_einzahlung_kleiner_betrag(self):
        """Test: Einzahlung eines sehr kleinen Betrags (Cent-Bereich)"""
        konto = Konto(1, Decimal("0.01"))
        konto.einzahlen(Decimal("0.02"))
        assert konto.saldo == Decimal("0.03")

    # Umsetzung von HAHR
    def test_decimal_praezision(self):
        """Test: Decimal-Präzision bei Einzahlungen und Auszahlungen"""
        konto = Konto(1, Decimal("0.10"))
        konto.einzahlen(Decimal("0.20"))
        konto.auszahlen(Decimal("0.15"))
        assert konto.saldo == Decimal("0.15")

    # Umsetzung von HAHR
    def test_string_repraesentation(self):
        """Test: String-Repräsentation des Kontos"""
        konto = Konto(1, Decimal("100.00"))
        assert str(konto) == "Konto(ID: 1, Saldo: 100.00)"

    # Umsetzung von HAHR
    def test_konto_gleichheit(self):
        """Test: Gleichheit von Konten basierend auf ID und Saldo"""
        konto1 = Konto(1, Decimal("100.00"))
        konto2 = Konto(1, Decimal("100.00"))
        konto3 = Konto(2, Decimal("100.00"))
        assert konto1 == konto2
        assert konto1 != konto3

