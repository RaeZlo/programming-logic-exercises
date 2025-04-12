"""
Complete the function power_of_two that takes a non-negative integer and returns True if the number is a power of 2, or False if it's not.
A number is a power of 2 if it can be written as 2ⁿ, where n is an integer (for example: 1, 2, 4, 8, 16, 32, ...).

URL: https://www.codewars.com/kata/534d0a229345375d520006a0
"""





def power_of_two(number: int) -> bool:
    """
    Verifica si un número es una potencia de 2 usando división sucesiva.

    Args:
        number (int): Número entero no negativo.

    Returns:
        bool: True si es una potencia de 2, False si no lo es.
    """
    # Mientras el número sea mayor que 1 y divisible por 2,
    # seguimos dividiendo entre 2.
    while number > 1 and number % 2 == 0:
        number = number // 2

    # Al final, si el número es exactamente 1, entonces sí era potencia de 2.
    return number == 1


def power_of_two_alt(number: int) -> bool:
    """
    Verifica si un número es potencia de 2 usando su representación binaria.

    Args:
        number (int): Número entero no negativo.

    Returns:
        bool: True si es una potencia de 2, False si no lo es.
    """
    # Una potencia de 2 tiene exactamente un único '1' en su forma binaria.
    # Por ejemplo:
    #   1  -> 0b1        (una sola vez el bit 1)
    #   2  -> 0b10
    #   4  -> 0b100
    #   8  -> 0b1000
    # Entonces contamos los bits '1' y verificamos que solo haya uno.
    return number > 0 and bin(number).count("1") == 1


print(power_of_two(1))     # True (2^0)
print(power_of_two(2))     # True (2^1)
print(power_of_two(3))     # False
print(power_of_two(16))    # True (2^4)
print(power_of_two(18))    # False

print(power_of_two_alt(1))     # True
print(power_of_two_alt(8))     # True
print(power_of_two_alt(10))    # False
