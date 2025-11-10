# Implementiert von: [HAHR], [PRSE]

from decimal import Decimal
from .interfaces import KontoInterface

class Konto(KontoInterface):

    """
    Initialisierung der Konto-Klasse
    Regeln:
    - ID wird bei Erstellung mitgegeben (numerisch, darf nicht leer sein)
    - Konto darf nicht überzogen werden (Saldo < 0)
    - Fehler bei inkorrekter Nutzung werfen
    """
    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):
        if konto_id is None or not isinstance(konto_id, int) or konto_id <= 0:
            raise ValueError("Konto-ID muss eine gültige Zahl sein, darf nicht leer sein und größer 0 sein.")
        if saldo < Decimal('0.00'):
            raise ValueError("Startsaldo darf nicht negativ sein.")
        self._konto_id = konto_id
        self._saldo = saldo
    
    # Attribut für die Konto-ID
    @property
    def konto_id(self) -> int:
        return self._konto_id
    
    # Attribut für den Kontostand
    @property
    def saldo(self) -> Decimal:
        return self._saldo
    
    # Methode zum Einzahlen
    def einzahlen(self, betrag: Decimal) -> None:
        if betrag <= Decimal('0.00'):
            raise ValueError("Einzahlungsbetrag muss höher als 0 Euro sein.")
        self._saldo += betrag
    
    # Methode zum Auszahlen
    def auszahlen(self, betrag: Decimal) -> None:
        if self._saldo <= Decimal('0.00'):
            raise ValueError("Konto ist leer, eine Auszahlung ist nicht möglich.")
        if betrag <= Decimal('0.00'):
            raise ValueError("Auszahlungsbetrag muss positiv sein.")
        if self._saldo - betrag < Decimal('0.00'):
            raise ValueError("Konto darf nicht überzogen werden.")
        self._saldo -= betrag

    def __str__(self):
        return f"Konto(ID: {self._konto_id}, Saldo: {self._saldo:.2f})"
    
    def __eq__(self, other):
        if not isinstance(other, Konto):
            return False
        return (self.konto_id == other.konto_id) and (self.saldo == other.saldo)
