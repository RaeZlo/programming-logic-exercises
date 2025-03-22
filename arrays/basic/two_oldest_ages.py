"""
Write a function that takes an array of numbers and returns the two highest numbers. 
The result should be an array in the format [second highest, highest]. 
If there are multiple highest numbers, return both of them in the array.

URL: https://www.codewars.com/kata/511f11d355fe575d2c000001
"""





def two_oldest_ages(ages: list[int]) -> list[int]:
    """
    Retorna los dos números más altos de la lista en formato [segundo más alto, más alto].

    Args:
        ages (list[int]): Lista de números.

    Returns:
        list[int]: Lista con los dos números más altos en orden ascendente.
    """
    return sorted(ages)[-2:]  # Ordena la lista y devuelve los últimos dos elementos

print(two_oldest_ages([1, 2, 10, 8]))  # Esperado: [8, 10]
print(two_oldest_ages([5, 1, 5, 3]))  # Esperado: [5, 5]
print(two_oldest_ages([12, 45, 32, 45]))  # Esperado: [45, 45]
print(two_oldest_ages([99, 100, 100, 100]))  # Esperado: [100, 100]
