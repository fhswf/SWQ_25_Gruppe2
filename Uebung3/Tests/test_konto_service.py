#Implementiert von: Jan Hamer[JNHR] und Leon Borchardt[LNBT]
"""
Test-Template für die KontoService-Klasse (Test-After Approach)
===============================================================

TODO: Team B - Implementieren Sie hier Ihre Tests NACH der KontoService-Implementierung!

Arbeitsablauf:
1. Implementieren Sie zuerst die KontoService-Klasse in Code/konto_service.py
2. Schreiben Sie dann hier umfassende Tests für Ihren Service
3. Testen Sie alle Service-Methoden gründlich
4. Dokumentieren Sie Ihre Autorschaft in den Tests

Tipps für Service-Tests:
- Nutzen Sie pytest fixtures für Setup/Teardown
- Testen Sie Integration zwischen Service und Konto-Klasse
- Testen Sie sowohl normale als auch Grenzfälle
- Testen Sie Validierungslogik im Service
"""

import pytest
from decimal import Decimal

from ..Code.konto_service import KontoService

class TestKontoServiceErstellung:
    """
    Tests für KontoService-Erstellung und Setup
    """
    def test_service_initialisierung(self):
        """Test: KontoService erstellen"""
        service = KontoService()
        assert len(service.konten_auflisten()) == 0

    def test_service_mit_initialen_konten(self):
        """Test: KontoService mit initialem Konto erstellen"""
        service = KontoService()
        service.konto_erstellen(Decimal('100.00'))
        assert len(service.konten_auflisten()) == 1 

    


class TestKontoVerwaltung:
    """
    Tests für Konto-Erstellung und -Verwaltung
    """
    def test_konto_erstellen(self):
        """Test: Konto erstellen"""
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal('100.00'))
        assert konto_id is not None
        assert len(service.konten_auflisten()) == 1

    def test_konto_erstellen_ungültiger_saldo(self):
        """Test: Konto mit ungültigem Saldo erstellen"""
        service = KontoService()
        with pytest.raises(ValueError):
            service.konto_erstellen(Decimal('-50.00'))

    def test_konten_auflisten(self):
        """Test: Konten auflisten"""
        service = KontoService()
        service.konto_erstellen(Decimal('100.00'))
        konten = service.konten_auflisten()
        assert len(konten) == 1
        assert konten[0].saldo == Decimal('100.00')

class TestTransaktionen:
    """
    Tests für Transaktions-Funktionen
    """

    def test_einzahlen(self):
        """Test: Einzahlung von positivem Betrag"""
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal('100.00'))
        service.einzahlen(konto_id, Decimal('50.00'))
        assert service.konten_auflisten()[0].saldo == Decimal('150.00')

    def test_einzahlen_negativer_betrag(self):
        """Test: Einzahlung von negativem Betrag"""
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal('100.00'))
        with pytest.raises(ValueError):
            service.einzahlen(konto_id, Decimal("-50.00"))

    def test_einzahlen_nicht_existierendes_konto(self):
        """Test: Einzahlen auf nicht existierendes Konto"""
        service = KontoService()
        with pytest.raises(ValueError):
            service.einzahlen(999, Decimal('50.00'))

    def test_auszahlen(self):
        """Test: Auszahlen von passendem Betrag"""
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal('100.00'))
        service.auszahlen(konto_id, Decimal('50.00'))
        assert service.konten_auflisten()[0].saldo == Decimal('50.00')

    def test_auszahlen_negativer_betrag(self):
        """Test: Auszahlen eines negativen Betrags"""
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal('100.00'))
        with pytest.raises(ValueError):
            service.auszahlen(konto_id, Decimal('-50.00'))

    def test_auszahlen_unzureichender_saldo(self):
        """Test: Auszahlen eines zu hohen Betrags"""
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal('100.00'))
        with pytest.raises(ValueError):
            service.auszahlen(konto_id, Decimal('150.00'))

    def test_ueberweisen(self):
        """Test: Überweisen von passendem Betrag"""
        service = KontoService()
        konto_id1 = service.konto_erstellen(Decimal('100.00'))
        konto_id2 = service.konto_erstellen(Decimal('50.00'))
        service.ueberweisen(konto_id1, konto_id2, Decimal('50.00'))
        assert service.konten_auflisten()[0].saldo == Decimal('50.00')
        assert service.konten_auflisten()[1].saldo == Decimal('100.00')

    def test_ueberweisen_negativer_betrag(self):
        """Test: Überweisen eines negativen Betrags"""
        service = KontoService()
        konto_id1 = service.konto_erstellen(Decimal('100.00'))
        konto_id2 = service.konto_erstellen(Decimal('50.00'))
        with pytest.raises(ValueError):
            service.ueberweisen(konto_id1, konto_id2, Decimal('-50.00'))
    
    def test_ueberweisen_unzureichender_saldo(self):
        """Test: Überweisen bei unzureichendem Saldo"""
        service = KontoService()
        konto_id1 = service.konto_erstellen(Decimal('100.00'))
        konto_id2 = service.konto_erstellen(Decimal('50.00'))
        with pytest.raises(RuntimeError):
            service.ueberweisen(konto_id1, konto_id2, Decimal('200.00'))

    def test_einziehen(self):
        """Test: Enziehen eines passenden Betrags"""
        service = KontoService()
        konto_id1 = service.konto_erstellen(Decimal('100.00'))
        konto_id2 = service.konto_erstellen(Decimal('50.00'))
        service.einziehen(konto_id1, konto_id2, Decimal('50.00'))
        assert service.konten_auflisten()[0].saldo == Decimal('50.00')
        assert service.konten_auflisten()[1].saldo == Decimal('100.00')

    def test_einziehen_negativer_betrag(self):
        """Test: Einziehen eines negativen Betrags"""
        service = KontoService()
        konto_id1 = service.konto_erstellen(Decimal('100.00'))
        konto_id2 = service.konto_erstellen(Decimal('50.00'))
        with pytest.raises(ValueError):
            service.einziehen(konto_id1, konto_id2, Decimal('-50.00'))

    def test_einziehen_unzureichender_saldo(self):
        """Test: Einziehen bei unzureichendem Saldo"""
        service = KontoService()
        konto_id1 = service.konto_erstellen(Decimal('100.00'))
        konto_id2 = service.konto_erstellen(Decimal('50.00'))
        with pytest.raises(RuntimeError):
            service.ueberweisen(konto_id1, konto_id2, Decimal('200.00'))


class TestSaldoFunktionen:
    """
    Tests für Saldo-bezogene Funktionen
    """

    def test_gesamtsaldo(self):
        """Test: Gesamtsaldo berechnen"""
        service = KontoService()
        service.konto_erstellen(Decimal('100.00'))
        service.konto_erstellen(Decimal('200.00'))
        assert service.gesamtsaldo() == Decimal('300.00')


class TestUtilityFunktionen:
    """
    Tests für Hilfsfunktionen
    """

    def test_get_max_konto_id(self):
        """Test: KontoID Zuweisung"""
        service = KontoService()
        assert service.get_max_konto_id() == 0
        service.konto_erstellen(Decimal('100.00'))
        assert service.get_max_konto_id() == 1

class TestKontoServiceIntegration:
    """
    Integration-Tests zwischen Service und Konto-Klassen
    """

    def test_vollstaendiger_workflow(self):
        """Test: Vollständiger Workflow"""
        service = KontoService()
        konto_id1 = service.konto_erstellen(Decimal('100.00'))
        konto_id2 = service.konto_erstellen(Decimal('200.00'))
        service.einzahlen(konto_id1, Decimal('50.00'))
        service.ueberweisen(konto_id1, konto_id2, Decimal('100.00'))
        assert service.gesamtsaldo() == Decimal('350.00')
