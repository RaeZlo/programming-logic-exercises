"""
Write a function that takes an array of integers and a target number. The function should find two different numbers in the 
array that sum up to the target value and return their indices as a tuple. There may be multiple valid answers, and any one 
of them is acceptable.

URL: https://www.codewars.com/kata/52c31f8e6605bcc646000082
"""





def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    """
    Encuentra dos números en la lista cuya suma sea igual al objetivo y devuelve sus índices.

    Args:
        numbers (list[int]): Lista de números enteros.
        target (int): Número objetivo.

    Returns:
        tuple[int, int]: Índices de los dos números cuya suma es igual al objetivo.
    """
    seen = {}  # Diccionario para almacenar los números vistos y sus índices
    for index, num in enumerate(numbers):
        complement = target - num  # Número necesario para alcanzar el objetivo
        if complement in seen:
            return seen[complement], index  # Se encontró una combinación válida
        seen[num] = index  # Guarda el número con su índice para futuras búsquedas


def two_sum_alt(nums: list[int], t: int) -> list[int]:
    """
    Alternativa usando una doble iteración (menos eficiente).

    Args:
        nums (list[int]): Lista de números enteros.
        t (int): Número objetivo.

    Returns:
        list[int]: Índices de los dos números cuya suma es igual al objetivo.
    """
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]  # Retorna la primera combinación encontrada
            

print(two_sum([2, 7, 11, 15], 9))  # (0, 1) → 2 + 7 = 9
print(two_sum([3, 2, 4], 6))  # (1, 2) → 2 + 4 = 6
print(two_sum([1, 3, 4, 2], 6))  # (2, 3) → 4 + 2 = 6
print(two_sum([5, 10, 15, 20], 25))  # (1, 2) → 10 + 15 = 25
print(two_sum([1, 2, 3, 4, 5], 8))  # (2, 4) → 3 + 5 = 8
