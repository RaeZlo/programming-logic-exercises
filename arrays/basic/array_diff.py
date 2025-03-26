"""
Implement a function that computes the difference between two lists. The function should remove all occurrences 
of elements from the first list (a) that are present in the second list (b). The order of elements in the first 
list should be preserved in the result.

URL: https://www.codewars.com/kata/523f5d21c841566fde000009
"""





def array_diff(a: list[int], b: list[int]) -> list[int]:
    """
    Filtra la lista 'a' eliminando los elementos que aparecen en 'b'.

    Args:
        a (list[int]): Lista base de números enteros.
        b (list[int]): Lista de elementos a eliminar de 'a'.

    Returns:
        list[int]: Lista filtrada sin los elementos de 'b'.
    """
    # Usamos una comprensión de listas para construir una nueva lista 
    # que solo contenga los elementos de 'a' que NO estén en 'b'.
    return [num for num in a if num not in b]


def array_diff_alt(a: list[int], b: list[int]) -> list[int]:
    """
    Alternativa usando filter() y una función lambda.

    Args:
        a (list[int]): Lista base de números enteros.
        b (list[int]): Lista de elementos a eliminar de 'a'.

    Returns:
        list[int]: Lista filtrada sin los elementos de 'b'.
    """
    # La función filter() recorre 'a' y mantiene los elementos 
    # que cumplen la condición num not in b.
    # La función lambda num: num not in b es una función anónima que 
    # devuelve True si el número no está en 'b' (se conserva en la nueva lista).
    # Se convierte el resultado de filter() en una lista con list().
    return list(filter(lambda num: num not in b, a))


print(array_diff([1, 2, 3, 4, 5], [2, 4]))  # Esperado: [1, 3, 5]
print(array_diff([1, 1, 2, 3, 1], [1]))  # Esperado: [2, 3]
print(array_diff([1, 2, 3, 4, 5], []))  # Esperado: [1, 2, 3, 4, 5]
print(array_diff([], [1, 2, 3]))  # Esperado: []
print(array_diff([1, 2, 2, 2, 3], [2]))  # Esperado: [1, 3]
