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

# TODO: Team A - Import nach erster Implementierung:
# from ..Code.fizzbuzz_kata import fizzbuzz
from Uebung4.Code.fizzbuzz_kata import fizzbuzz as fizzbuzz

class TestFizzBuzzTDD:
    """
    TODO: Team A - Entwickelt FizzBuzz mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    def test_placeholder_start_here(self):
        """
        TODO: Team A - Ersetzt diesen Placeholder durch euren ersten TDD-Test!

        Ideen für den ersten Test:
        - Was ist das einfachste Verhalten?
        - fizzbuzz(1) sollte was zurückgeben?

        TDD-Autor: [Name und Zeit]
        """
        # TODO: Euer erster TDD-Test hier
        #assert True, "Placeholder - startet hier mit TDD!"

        # Beispiel-Idee (entfernt nach eigenem Test):
        assert fizzbuzz(0) == "0"
        assert fizzbuzz(1) == "1"
        assert fizzbuzz(2) == "2"
        assert fizzbuzz(3) == "Fizz"
        assert fizzbuzz(5) == "Buzz"
        assert fizzbuzz(15) == "FizzBuzz"

    def test_returnString(Self):
        testArray = [0,1,2]
        
        for test in testArray:
            assert fizzbuzz(test) == str(test)

    def test_returnFizz(Self):
        testArray = [3,6,9]

        for test in testArray:
            assert fizzbuzz(test) == "Fizz"

    def test_returnBuzz(Self):
        testArray = [5,10,20]

        for test in testArray:
            assert fizzbuzz(test) == "Buzz"

    def test_returnFizzBuzz(Self):
        testArray = [15,30,45]

        for test in testArray:
            assert fizzbuzz(test) == "FizzBuzz"



class TestFizzBuzzErweitert:
    """
    TODO: Team A - Erweiterte Tests, wenn Basis funktioniert
    """

    def test_placeholder_extended_tests(self):
        """
        TODO: Team A - Entwickelt weitere Tests für FizzBuzz

        Ideen:
        - Mehrere Zahlen gleichzeitig testen
        - Parametrisierte Tests (@pytest.mark.parametrize)
        - Edge Cases (negative Zahlen, 0, große Zahlen)
        """
        # TODO: Erweiterte Tests hier
        # assert True, "TODO: Erweiterte FizzBuzz-Tests implementieren"

    def test_returnString(Self):
        testArray = [0,1,2]
        
        for test in testArray:
            assert fizzbuzz(test) == str(test)

    def test_returnFizz(Self):
        testArray = [3,6,9, -3]

        for test in testArray:
            assert fizzbuzz(test) == "Fizz"

    def test_returnBuzz(Self):
        testArray = [5,10,20, -5]

        for test in testArray:
            assert fizzbuzz(test) == "Buzz"

    def test_returnFizzBuzz(Self):
        testArray = [15,30,45, -15]

        for test in testArray:
            assert fizzbuzz(test) == "FizzBuzz"

    def test_negativeValues(Self):
        testArray = [-4,0,-256]

        for test in testArray:
            assert fizzbuzz(test) == str(test)

    def test_EdgeCases(Self):
        testArray = [-7,0,8096]

        for test in testArray:
            assert fizzbuzz(test) == str(test)

    def test_canonicallyAll(self):        
        testArray = [0,1,2,3,5,15, -3]
        for test in testArray:
            def fizzbuzzreturn (test):
                if((test % 3) and (test % 5)):
                    assert fizzbuzz(test) == "FizzBuzz"
                elif(test % 3):
                    assert fizzbuzz(test) == "Fizz"
                elif(test % 5):
                    assert fizzbuzz(test) == "Buzz"
                else:
                    assert fizzbuzz(test) == str(test)



# TODO: Team A - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: [Was getestet] - Autor: [Name] - Zeit: [Zeit]
Implementation 1: [Minimale Lösung] - Zeit: [Zeit]

Test 2: [Was getestet] - Autor: [Name] - Zeit: [Zeit]  
Refactoring: [Was geändert] - Zeit: [Zeit]

[Weiter dokumentieren...]

Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
"""
