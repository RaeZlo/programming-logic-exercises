"""
Given an array of numbers, return a new array of length number containing the last even numbers from the 
original array (in the same order). The original array will be not empty and will contain at least "number" even numbers.

URL: https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c
"""





def even_numbers(numbers: list[int], occ: int) -> list[int]:
    """
    Extrae los últimos 'occ' números pares de una lista.

    Args:
        numbers (list[int]): Lista de números enteros.
        occ (int): Cantidad de números pares a devolver.

    Returns:
        list[int]: Lista con los últimos 'occ' números pares.
    """
    return [num for num in numbers if num % 2 == 0][-occ:]  # Filtra pares y toma los últimos 'occ'


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # Esperado: [4, 6, 8]
print(even_numbers([2, 4, 6, 8, 10], 2))  # Esperado: [8, 10]
print(even_numbers([5, 7, 9, 10, 12, 14, 16], 4))  # Esperado: [10, 12, 14, 16]
print(even_numbers([0, 1, 2, 3, 4, 5, 6], 1))  # Esperado: [6]
print(even_numbers([100, 200, 300, 400, 500], 5))  # Esperado: [100, 200, 300, 400, 500]
