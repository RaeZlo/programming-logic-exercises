"""
Write a function that returns both the minimum and maximum number of the given list/array.

URL: https://www.codewars.com/kata/559590633066759614000063
"""





def min_max(numbers: list[int]) -> list[int]:
    """
    Esta función recibe una lista de números enteros y retorna una lista con el mínimo y el máximo.

    Args:
        numbers (list[int]): Lista de números enteros.

    Returns:
        list[int]: Una lista con dos elementos: el mínimo y el máximo de la lista original.
    """
    return [min(numbers), max(numbers)] 


def min_max_alt(numbers: list[int]) -> list[int]:
    """
    Alternativa que ordena la lista sin modificar la original.

    Args:
        numbers (list[int]): Lista de números enteros.

    Returns:
        list[int]: Lista con el mínimo y el máximo.
    """
    sorted_numbers = sorted(numbers) 
    return [sorted_numbers[0], sorted_numbers[-1]] 


print(min_max([1, 2, 3, 4, 5]))   # Esperado: [1, 5]
print(min_max_alt([233, 5, 7, 99]))   # Esperado: [5, 233]
print(min_max_alt([10, 10, 10]))      # Esperado: [10, 10] (caso borde con todos iguales)
print(min_max([42]))              # Esperado: [42, 42] (caso borde con un solo número)
