"""
Write a function that returns the values from an array that are not odd (i.e., even numbers). 
All values in the array will be integers. Return the non-odd values in the same order as they appear in the input array.

URL: https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce
"""






def no_odds(values: list[int]) -> list[int]:
    """
    Filtra los valores pares de una lista.

    Args:
        values (list[int]): Lista de números enteros.

    Returns:
        list[int]: Lista con solo los números pares.
    """
    return [num for num in values if num % 2 == 0]  # Filtrar números pares


print(no_odds([1, 2, 3, 4, 5, 6]))  # Esperado: [2, 4, 6]
print(no_odds([7, 8, 10, 13, 17]))  # Esperado: [8, 10]
print(no_odds([1, 3, 5, 7]))  # Esperado: []
print(no_odds([2, 4, 6, 8]))  # Esperado: [2, 4, 6, 8]
print(no_odds([]))  # Esperado: []
