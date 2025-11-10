"""
TDD Kata: FizzBuzz
Implementieren Sie die FizzBuzz-Funktion mit Test-Driven Development

Regeln:
1. Schreiben Sie zuerst einen Test (der fehlschlägt)
2. Schreiben Sie minimal nötigen Code, um den Test zu bestehen
3. Refactoring (Code verbessern ohne Funktionalität zu ändern)
4. Wiederholen Sie 1-3

FizzBuzz Regeln:
- Zahl durch 3 teilbar -> "Fizz"
- Zahl durch 5 teilbar -> "Buzz"  
- Zahl durch 3 UND 5 teilbar -> "FizzBuzz"
- Sonst -> Zahl als String
"""

# TDD-Zyklus 1,2,3,7: GREEN von [HAHR & PRSE]
def fizzbuzz(n: int) -> str:
    if n == 0:
        return "0"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
