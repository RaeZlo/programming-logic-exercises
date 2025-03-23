"""
Given a 2D list of integers, return a single list with all the integers sorted in ascending order.

URL: https://www.codewars.com/kata/57ee99a16c8df7b02d00045f
"""





def flatten_and_sort(array: list[list[int]]) -> list[int]:
    """
    Aplana una lista 2D y la ordena en orden ascendente.

    Args:
        array (list[list[int]]): Lista de listas con números enteros.

    Returns:
        list[int]: Lista aplanada y ordenada.
    """
    return sorted([num for sublist in array for num in sublist])


def flatten_and_sort_alt(array: list[list[int]]) -> list[int]:
    """
    Alternativa: Aplana una lista 2D sumando las sublistas y la ordena en orden ascendente.

    Args:
        array (list[list[int]]): Lista de listas con números enteros.

    Returns:
        list[int]: Lista aplanada y ordenada.
    """
    return sorted(sum(array, []))

print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))  # Esperado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]))         # Esperado: [1, 2, 3, 4, 5, 6, 100]
print(flatten_and_sort([[]]))                                  # Esperado: []
