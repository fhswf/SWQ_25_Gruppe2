# Implementiert von: SNKM
"""
Hier sollen Sie Ihre Implementierung der Konto-Klasse erstellen.

TODO: Implementieren Sie die Konto-Klasse basierend auf dem KontoInterface
"""

from decimal import Decimal
from .interfaces import KontoInterface

class Konto(KontoInterface):
    """    
    Regeln:
    - ID wird bei Erstellung mitgegeben (numerisch, darf nicht leer sein)
    - Konto darf nicht überzogen werden (Saldo < 0)
    - Fehler bei inkorrekter Nutzung werfen
    """

    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):
        if konto_id is None or konto_id < 0:
            raise ValueError("Konto-ID muss eine positive Zahl sein")
        if saldo < 0:
            raise ValueError("Anfangssaldo darf nicht negativ sein")
        self._konto_id = konto_id
        self._saldo = saldo

    def __repr__(self) -> str:
        return f"Konto(konto_id={self.konto_id}, saldo={self.saldo})"

    def __str__(self) -> str:
        return f"Konto(ID: {self.konto_id}, Saldo: {self.saldo})"

    @property
    def konto_id(self) -> int:
        return self._konto_id

    @property
    def saldo(self) -> Decimal:
        return self._saldo

    def einzahlen(self, betrag: Decimal) -> None:
        if betrag <= 0:
            raise ValueError("Einzahlungsbetrag muss positiv sein")
        self._saldo += betrag

    def auszahlen(self, betrag: Decimal) -> None:
        if betrag <= 0:
            raise ValueError("Auszahlungsbetrag muss positiv sein")
        if self._saldo - betrag < 0:
            raise ValueError("Konto darf nicht überzogen werden")
        self._saldo -= betrag
