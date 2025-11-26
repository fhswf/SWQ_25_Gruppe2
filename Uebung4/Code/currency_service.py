"""
Implementierung: Currency-API Service
=====================================

TODO: Team B - Implementiert get_exchange_rate_assessment() hier!

Die Funktion soll:
1. Currency-API aufrufen (in Tests gemockt)
2. Wechselkurs extrahieren
3. Bewertung zurückgeben

Hinweise:
- Nutzt requests.get() für API-Aufrufe
- API-URL: https://api.exchangerate.com/convert?from={from_currency}&to={to_currency}
- Response-Format: {"rate": 1.05}
- Startet mit minimalster Implementierung!
"""

#implementiert von [LNBT]
from __future__ import annotations
import requests


def get_exchange_rate_assessment(from_currency: str, to_currency: str) -> str:
    """
    Ruft Currency-API auf und gibt Bewertung des Wechselkurses zurück
    
    Args:
        from_currency: Ausgangswährung (z.B. "EUR")
        to_currency: Zielwährung (z.B. "USD")
        
    Returns:
        Bewertung als String:
        - "sehr ungünstig" (< 0.90)
        - "ungünstig" (0.90-0.99)
        - "fair" (1.00-1.09)
        - "günstig" (1.10-1.19)
        - "sehr günstig" (≥ 1.20)
    """

API_URL_TEMPLATE = "https://api.exchangerate.com/convert?from={from_currency}&to={to_currency}"


def _fetch_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Kapselt den API-Aufruf, um ihn getrennt testen/mocken zu können.
    """
    url = API_URL_TEMPLATE.format(from_currency=from_currency, to_currency=to_currency)
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

    rate = data.get("rate")
    if rate is None:
        raise ValueError("API response does not contain 'rate'")
    if not isinstance(rate, (int, float)):
        raise TypeError("'rate' must be numeric")

    return float(rate)


def _assess_rate(rate: float) -> str:
    """
    Bewertungslogik getrennt von IO.
    """
    if rate < 0.90:
        return "sehr unguenstig"
    if rate < 1.00:
        return "unguenstig"
    if rate < 1.10:
        return "fair"
    if rate < 1.20:
        return "guenstig"
    return "sehr guenstig"


def get_exchange_rate_assessment(from_currency: str, to_currency: str) -> str:
    """
    Ruft Currency-API auf und gibt Bewertung des Wechselkurses zurück.
    """
    rate = _fetch_exchange_rate(from_currency, to_currency)
    return _assess_rate(rate)

