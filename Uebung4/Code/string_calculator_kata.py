# TODO: Implementiere den String Calculator mit TDD
# Hinweise: Beginne mit den Basisregeln ("" -> 0, "1" -> 1, "1,2" -> 3)
# Erweitere schrittweise mit Tests für \n, benutzerdefinierte Delimiter, etc.

def add(numbers: str) -> int:    
    # Empty String Case
    if numbers == "":
        return 0
    # Unify seperators
    numbers = numbers.replace("\n",",")

    # Split String in List
    stringList = numbers.split(",")

    # String -> Integer
    numberList = list(map(int, stringList))

    for number in numberList:
        if number < 0:
            raise ValueError("Negative Zahlen sind nicht Erlaubt!")

    sumOfNumbers = sum(numberList)

    for 
    return sumOfNumbers
    