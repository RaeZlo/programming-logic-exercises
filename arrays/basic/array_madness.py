"""
Given two integer arrays a and b (both of length >= 1), determine if the sum of the squares of the elements in a is 
strictly greater than the sum of the cubes of the elements in b.

URL: https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1
"""






def array_madness(a: list[int], b: list[int]) -> bool:
    """
    Compara la suma de los cuadrados de 'a' con la suma de los cubos de 'b'.

    Args:
        a (list[int]): Lista de enteros.
        b (list[int]): Lista de enteros.

    Returns:
        bool: True si la suma de los cuadrados de 'a' es mayor que la suma de los cubos de 'b', False en caso contrario.
    """
    return sum(num ** 2 for num in a) > sum(num ** 3 for num in b)


print(array_madness([4, 5, 6], [1, 2, 3]))  # Esperado: True (16+25+36 > 1+8+27)
print(array_madness([1, 2, 3], [4, 5, 6]))  # Esperado: False (1+4+9 < 64+125+216)
print(array_madness([10, 20, 30], [2, 3, 4]))  # Esperado: True (100+400+900 > 8+27+64)
print(array_madness([0], [0]))  # Esperado: False (0 > 0 es falso)
print(array_madness([2, 2, 2], [2, 2, 2]))  # Esperado: False (4+4+4 < 8+8+8)
