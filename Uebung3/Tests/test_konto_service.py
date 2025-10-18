# Implementiert von: SNKM

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
from ..Code.konto import Konto

class TestKontoServiceErstellung:

    def test_service_initialisierung(self):
        # Test Service ohne Parameter erstellen
        service = KontoService()
        assert service is not None

    def test_service_mit_initialen_konten(self):
        # Test Service mit initialen Konten erstellen
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal("100.00"))
        assert konto_id == 1

    def test_service_initialer_zustand(self):
        # Test Service-Zustand nach Erstellung prüfen
        service = KontoService()
        konten = service.konten_auflisten()
        assert len(konten) == 0



class TestKontoVerwaltung:

    def test_konto_erstellen_valid_saldo(self):
        # Test für konto_erstellen() mit gültigem Saldo
        service = KontoService()
        konto = service.konto_erstellen(Decimal("250.00"))
        assert konto == 1  # Erste KontoID sollte 1 sein

    def test_konto_erstellen_automatische_id_vergabe(self):
        # Test für automatische ID-Vergabe bei konto_erstellen()
        service = KontoService()
        id1 = service.konto_erstellen(Decimal("100.00"))
        id2 = service.konto_erstellen(Decimal("200.00"))
        assert id1 == 1
        assert id2 == 2

    def test_konto_erstellen_konto_in_liste(self):
        # Test, ob erstelltes Konto in interner Liste ist
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal("150.00"))
        konten = service.konten_auflisten()
        assert any(k['konto_id'] == konto_id for k in konten)

    def test_konto_erstellen_rueckgabe_id(self):
        # Test der Rückgabe der Konto-ID bei konto_erstellen()
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal("75.00"))
        assert konto_id == 1

    def test_konto_erstellen_invalid_saldo(self):
        # Test für konto_erstellen() mit ungültigem Saldo
        service = KontoService()
        with pytest.raises((ValueError, TypeError)):
            service.konto_erstellen("abc")
            service.konto_erstellen(None)

    def test_konten_auflisten_leer(self):
        # Test konten_auflisten() bei leerem Service
        service = KontoService()
        konten = service.konten_auflisten()
        assert konten == []

    def test_konten_auflisten_liste_nach_erstellung(self):
        # Test konten_auflisten() nach Konto-Erstellung
        service = KontoService()
        service.konto_erstellen(Decimal("100.00"))
        service.konto_erstellen(Decimal("200.00"))
        konten = service.konten_auflisten()
        assert len(konten) == 2
        assert konten[0]['saldo'] == Decimal("100.00")
        assert konten[1]['saldo'] == Decimal("200.00")

    def test_konten_auflisten_korrekte_anzahl_und_inhalte(self):
        # Test konten_auflisten() mit mehreren Konten
        service = KontoService()
        saldos = [Decimal("50.00"), Decimal("150.00"), Decimal("250.00")]
        for saldo in saldos:
            service.konto_erstellen(saldo)
        konten = service.konten_auflisten()
        assert len(konten) == 3
        for i, konto in enumerate(konten):
            assert konto['saldo'] == saldos[i]

class TestTransaktionen:

    def test_einzahlen_existing_konto(self):
        # Test Einzahlung auf existierendes Konto erfolgreich (direkt Konto-Methode verwenden, da KontoService keine einzahlen-Methode hat)
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal("100.00"))
        konto = service._konten[konto_id - 1]
        konto.einzahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("150.00")

    def test_einzahlen_non_existing_konto(self):
        # Test Einzahlung auf nicht-existierendes Konto wirft Exception
        service = KontoService()
        service.konto_erstellen(Decimal("100.00"))
        with pytest.raises(IndexError):
            konto = service._konten[2]
            konto.einzahlen(Decimal("50.00"))

    def test_einzahlen_invalid_betrag(self):
        # Test Einzahlung mit ungültigem Betrag wirft Exception
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal("100.00"))
        konto = service._konten[konto_id - 1]
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("-10.00"))

    def test_auszahlen_ausreichender_saldo(self):
        # Test Auszahlung bei ausreichendem Saldo
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal("200.00"))
        konto = service._konten[konto_id - 1]
        konto.auszahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("150.00")

    def test_auszahlen_unzureichender_saldo(self):
        # Test Auszahlung bei unzureichendem Saldo
        service = KontoService()
        konto_id = service.konto_erstellen(Decimal("100.00"))
        konto = service._konten[konto_id - 1]
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("150.00"))

    def test_auszahlen_nicht_existierendes_konto(self):
        # Test Auszahlung von nicht-existierendem Konto
        service = KontoService()
        service.konto_erstellen(Decimal("100.00"))
        with pytest.raises(IndexError):
            konto = service._konten[2]
            konto.auszahlen(Decimal("50.00"))

    def test_ueberweisen_existing_konten(self):
        # Test Überweisung zwischen existierenden Konten
        service = KontoService()
        konto_id_1 = service.konto_erstellen(Decimal("300.00"))
        konto_id_2 = service.konto_erstellen(Decimal("100.00"))
        service.ueberweisen(konto_id_1, konto_id_2, Decimal("50.00"))
        konten = service.konten_auflisten()
        saldo_1 = next(k['saldo'] for k in konten if k['konto_id'] == konto_id_1)
        saldo_2 = next(k['saldo'] for k in konten if k['konto_id'] == konto_id_2)
        assert saldo_1 == Decimal("250.00")
        assert saldo_2 == Decimal("150.00")

    def test_ueberweisen_unzureichender_saldo(self):
        # Test Überweisung bei unzureichendem Saldo
        service = KontoService()
        konto_id_1 = service.konto_erstellen(Decimal("50.00"))
        konto_id_2 = service.konto_erstellen(Decimal("100.00"))
        with pytest.raises(ValueError):
            service.ueberweisen(konto_id_1, konto_id_2, Decimal("100.00"))

    def test_ueberweisen_von_nicht_existierendem_konto(self):
        # Test Überweisung von nicht-existierendem Konto
        service = KontoService()
        konto_id_2 = service.konto_erstellen(Decimal("100.00"))
        with pytest.raises(ValueError):
            service.ueberweisen(999, konto_id_2, Decimal("50.00"))

    def test_ueberweisen_an_nicht_existierendes_konto(self):
        # Test Überweisung an nicht-existierendes Konto
        service = KontoService()
        konto_id_1 = service.konto_erstellen(Decimal("100.00"))
        with pytest.raises(ValueError):
            service.ueberweisen(konto_id_1, 999, Decimal("50.00"))


class TestSaldoFunktionen:

    def test_gesamtsaldo_leere_kontenliste(self):
        # Test Gesamtsaldo bei leerer Kontenliste
        service = KontoService()
        gesamt = service.gesamtsaldo_berechnen()
        assert gesamt == Decimal("0.00")

    def test_gesamtsaldo_ein_konto(self):
        # Test Gesamtsaldo mit einem Konto
        service = KontoService()
        service.konto_erstellen(Decimal("150.00"))
        gesamt = service.gesamtsaldo_berechnen()
        assert gesamt == Decimal("150.00")

    def test_gesamtsaldo_mehrere_konten(self):
        # Test Gesamtsaldo mit mehreren Konten
        service = KontoService()
        service.konto_erstellen(Decimal("100.00"))
        service.konto_erstellen(Decimal("200.00"))
        service.konto_erstellen(Decimal("50.00"))
        gesamt = service.gesamtsaldo_berechnen()
        assert gesamt == Decimal("350.00")


class TestUtilityFunktionen:

    def test_get_max_konto_id_first_id(self):
        # Test get_max_konto_id() erste ID ist 1
        service = KontoService()
        if service.konten_auflisten() == []:
            service.konto_erstellen(Decimal("100.00"))
        max_id = service.get_max_konto_id()
        assert max_id == 1

    def test_get_max_konto_id_continued_ids(self):
        # Test get_max_konto_id() mit fortlaufenden IDs
        service = KontoService()
        service.konto_erstellen(Decimal("100.00"))
        service.konto_erstellen(Decimal("200.00"))
        max_id = service.get_max_konto_id()
        assert max_id == 2

    def test_get_max_konto_id_no_duplicate_ids(self):
        # Test get_max_konto_id() keine doppelten IDs
        service = KontoService()
        ids = set()
        for _ in range(5):
            konto_id = service.konto_erstellen(Decimal("50.00"))
            assert konto_id not in ids
            ids.add(konto_id)
        max_id = service.get_max_konto_id()
        assert max_id == 5

class TestKontoServiceIntegration:

    def test_vollstaendiger_workflow(self):
        service = KontoService()
        konto_id_1 = service.konto_erstellen(Decimal("500.00"))
        konto_id_2 = service.konto_erstellen(Decimal("300.00"))
        konto1 = service._konten[konto_id_1 - 1]
        konto2 = service._konten[konto_id_2 - 1]
        konto1.auszahlen(Decimal("100.00"))
        konto2.einzahlen(Decimal("200.00"))
        gesamt = service.gesamtsaldo_berechnen()
        assert gesamt == Decimal("900.00")
        konten = service.konten_auflisten()
        saldo_1 = next(k['saldo'] for k in konten if k['konto_id'] == konto_id_1)
        saldo_2 = next(k['saldo'] for k in konten if k['konto_id'] == konto_id_2)
        assert saldo_1 == Decimal("400.00")
        assert saldo_2 == Decimal("500.00")
