"""
TDD-Template für FizzBuzz Kata
==============================

TODO: Team A - Entwickelt FizzBuzz mit TDD!

FizzBuzz-Regeln:
- Zahl durch 3 teilbar → "Fizz"  
- Zahl durch 5 teilbar → "Buzz"
- Zahl durch 3 UND 5 teilbar → "FizzBuzz"
- Sonst → Zahl als String

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest

from Uebung4.Code.fizzbuzz_kata import fizzbuzz

# TODO: Team A - Import nach erster Implementierung:
# from ..Code.fizzbuzz_kata import fizzbuzz


class TestFizzBuzzTDD:
    """
    TODO: Team A - Entwickelt FizzBuzz mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    # TDD-Zyklus 1: RED von [PRSE]
    def test_non_divisible(self):
        assert fizzbuzz(1) == "1"
        assert fizzbuzz(2) != "1"

    # TDD-Zyklus 2: RED von [HAHR]
    def test_divisible_by_three(self):
        assert fizzbuzz(3) == "Fizz"

    # TDD-Zyklus 3: RED von [PRSE]
    def test_divisible_by_five(self):
        assert fizzbuzz(5) == "Buzz"

    # TDD-Zyklus 4: RED von [HAHR]
    def test_divisible_by_three_and_five(self):
        assert fizzbuzz(15) == "FizzBuzz"
        assert fizzbuzz(20) == "Buzz"
        assert fizzbuzz(21) == "Fizz"


class TestFizzBuzzErweitert:
    """
    TODO: Team A - Erweiterte Tests, wenn Basis funktioniert
    TODO: Team A - Entwickelt weitere Tests für FizzBuzz

    Ideen:
    - Mehrere Zahlen gleichzeitig testen
    - Parametrisierte Tests (@pytest.mark.parametrize)
    - Edge Cases (negative Zahlen, 0, große Zahlen)
    """

    # TDD-Zyklus 5: RED von [HAHR]
    def test_divisible_by_zero(self):
        assert fizzbuzz(0) == "0"

    # TDD-Zyklus 6: RED von [HAHR]
    def test_non_divisible_by_negative(self):
        assert fizzbuzz(-1) == "-1"
        assert fizzbuzz(-2) != "-1"

    # TDD-Zyklus 6: RED von [PRSE]
    def test_divisible_by_negative_three(self):
        assert fizzbuzz(-3) == "Fizz"

    # TDD-Zyklus 6: RED von [PRSE]
    def test_divisible_by_negative_five(self):
        assert fizzbuzz(-5) == "Buzz"
        
    # TDD-Zyklus 6: RED von [PRSE]
    def test_divisible_by_negative_three_and_five(self):
        assert fizzbuzz(-15) == "FizzBuzz"
        assert fizzbuzz(-20) == "Buzz"
        assert fizzbuzz(-21) == "Fizz"    
    
    # TDD-Zyklus 7: RED von [HAHR]
    def test_multiple_input_numbers(self):
        numbers = [0,1,3,5,15]
        assert fizzbuzz(numbers)
