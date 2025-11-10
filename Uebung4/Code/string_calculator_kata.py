#Implementiert von: Jan Hamer[JNHR] und Leon Borchardt[LNBT]

def add(numbers: str) -> int:    
    # Empty String Case
    if numbers == "":
        return 0

    number_list = format_string_to_int_list(numbers)

    sum_of_numbers = 0

    for number in number_list:
        if number < 0:
            raise ValueError("Negative Zahlen sind nicht Erlaubt!")
        elif number > 1000:
            continue
        sum_of_numbers += number

    return sum_of_numbers

def format_string_to_int_list(numbers: str) -> list:
    # Unify seperators
    numbers = numbers.replace("\n",",")

    # Split String in List
    string_list = numbers.split(",")

    # String -> Integer
    number_list = list(map(int, string_list))

    return number_list
    