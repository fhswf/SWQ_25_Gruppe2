#Implementiert von: Jan Hamer[JNHR]

import pytest

# TODO: Team B - Import nach erster Implementierung:
# from ..Code.string_calculator_kata import add
from ..Code.string_calculator_kata import add


class TestStringCalculatorTDD:
    # Basistests

    def test_empty_string(self):
        # Test eines leeren Strings
        assert add("") == 0

    def test_single_number(self):
        # Test einer einzelnen Zahl
        assert add("1") == 1

    def test_adding_two_numbers(self):
        # Test einer simplen Addition
        assert add("3,4") == 7

    def test_multiple_numbers(self):
        # Test mehrerer Additionen
        assert add("1,3,5,7") == 16


class TestStringCalculatorErweitert:
    # Erweiterte Tests nach Basis

    def test_newline_seperator(self):
        # Test mit Newline als Trennzeichen
        assert add("2\n6") == 8

    def test_mixed_seperators(self):
        # Test mit Newline und Comma als Trennzeichen
        assert add("1\n2,3") == 6

    def test_negative_number(self):
        # Test mit einer negativen Zahl
        with pytest.raises(ValueError):
            add("-1\n3")

    def test_huge_number(self):
        # Test einer zu großen Zahl
        assert add("23,10\n1002") == 33



# TODO: Team B - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: Basisfälle getestet - Autor: JNHR - Zeit: 5min
Implementation 1: add() Funktion erstellt - Zeit: 6min

Test 2: Erweiterte Tests hinzugefügt (Newline Seperator) - Autor: JNHR - Zeit: 3min
Refactoring: Ersetzen der Trennzeichen zum Vereinheitlichen - Zeit: 5min

Test 3: Negative Zahlen Test hinzugefügt - Autor: JNHR - Zeit: 2min
Refactoring: Schleife die jede Zahl prüft - Autor: JNHR - Zeit: 3min

Test 4: Zahlen über 1000 sollen ignoriert werden - Autor: JNHR - Zeit: 2min
Refactoring: Sum Funktion in Schleife integriert - Autor: JNHR - Zeit: 8min

[Weiter dokumentieren...]

Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
    - Am Anfang sum() genutzt, später durch for ersetzt, um einzelne zahlen zu prüfen
- Welche Tests brachten neue Herausforderungen?
    - Überlegen wie mit seperator umgegangen wird -> vereinheitlichung vor dem split
- Unterschiede zu FizzBuzz?
"""
