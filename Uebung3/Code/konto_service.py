# CNSK, SNKM
"""
TODO: Implementieren Sie die KontoService-Klasse basierend auf dem KontoServiceInterface
"""

from decimal import Decimal
from typing import List, Dict
from .interfaces import KontoServiceInterface, KontoInterface


# TODO: Team B - Später ersetzt ihr diesen Import durch Team A's Implementation:
from .konto import Konto


class KontoService(KontoServiceInterface):
    """
    TODO: Implementieren Sie diese Klasse

    HINWEIS für Team B - Parallele Entwicklung:
    - Arbeiten Sie mit dem KontoInterface, nicht der konkreten Konto-Klasse
    - Nutzen Sie die _create_konto() Factory-Methode für Konto-Erstellung
    - So können Sie sofort anfangen, ohne auf Team A zu warten!

    Funktionalitäten:
    - Konten verwalten (als List[KontoInterface])
    - Validierung der Benutzereingaben
    - Neue KontoID: max KontoID + 1
    - Export-Funktionen
    - Berechnungen
    """

    def __init__(self):
        # Initialisiert die KontoService-Instanz und die interne Kontenliste
        super().__init__()
        self._konten: List[KontoInterface] = []
        

    def _create_konto(self, konto_id: int, saldo: Decimal) -> KontoInterface:
        # Factory-Methode zur Erstellung eines Konto-Objekts
        return Konto(konto_id, saldo)

    def konten_auflisten(self) -> List[Dict]:
        # Gibt eine Liste aller Konten als Dicts zurück
        konten_liste = []
        for konto in self._konten:
            konten_liste.append({
                'konto_id': konto.konto_id,
                'saldo': konto.saldo
            }) 
        return konten_liste

    def konto_erstellen(self, saldo: Decimal = Decimal('0.00')) -> int:
        # Erstellt ein neues Konto mit dem angegebenen Anfangssaldo und gibt die Konto-ID zurück
        konto_id = self.get_max_konto_id() + 1
        konto = self._create_konto(konto_id, saldo)
        self._konten.append(konto)
        return konto_id

    def ueberweisen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        # Saldo von von_konto_id um betrag verringern und Saldo von zu_konto_id um betrag erhöhen
        von_konto = next((k for k in self._konten if k.konto_id == von_konto_id), None)
        zu_konto = next((k for k in self._konten if k.konto_id == zu_konto_id), None)
        if von_konto is None or zu_konto is None:
            raise ValueError("Konto nicht gefunden")
        von_konto.auszahlen(betrag)
        zu_konto.einzahlen(betrag)

    def einziehen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        # verringert das Guthaben von zu_konto_id um betrag und erhöht das Guthaben von von_konto_id um betrag
        von_konto = next((k for k in self._konten if k.konto_id == von_konto_id), None)
        zu_konto = next((k for k in self._konten if k.konto_id == zu_konto_id), None)
        if von_konto is None or zu_konto is None:
            raise ValueError("Konto nicht gefunden")
        zu_konto.auszahlen(betrag)
        von_konto.einzahlen(betrag)

    def get_max_konto_id(self) -> int:
        # Gibt die maximale Konto-ID zurück
        max_id = 0
        for konto in self._konten:
            if konto.konto_id > max_id:
                max_id = konto.konto_id
        return max_id

    def gesamtsaldo_berechnen(self) -> Decimal:
        # Berechnet den Gesamtsaldo aller Konten
        gesamt = Decimal("0.00")
        for konto in self._konten:
            gesamt += konto.saldo
        return gesamt
