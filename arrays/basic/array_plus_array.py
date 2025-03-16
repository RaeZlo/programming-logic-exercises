"""
Given two arrays of integers, return the sum of both arrays combined.

URL: https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
"""





def array_plus_array(arr1: list[int], arr2: list[int]) -> int:
    """
    Suma todos los elementos de dos listas y retorna el resultado.

    Args:
        arr1 (list[int]): Primera lista de números enteros.
        arr2 (list[int]): Segunda lista de números enteros.

    Returns:
        int: La suma total de los elementos de ambas listas.
    """
    return sum(arr1 + arr2)

print(array_plus_array([1, 2, 3], [4, 5, 6]))  # Esperado: 21 (1+2+3+4+5+6)
print(array_plus_array([-1, -2, -3], [-4, -5, -6]))  # Esperado: -21
print(array_plus_array([0, 0, 0], [0, 0, 0]))  # Esperado: 0
print(array_plus_array([100, 200, 300], [400, 500, 600]))  # Esperado: 2100
print(array_plus_array([], []))  # Esperado: 0 (caso borde con listas vacías)
