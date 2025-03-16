"""
Given an array of integers as strings and numbers, return the sum 
of the array values as if all were numbers.
Return your answer as a number.

URL: https://www.codewars.com/kata/57eaeb9578748ff92a000009
"""





def sum_mix(arr: list[str | int]) -> int:
    """
    Convierte todos los elementos de la lista a enteros y retorna su suma.

    Args:
        arr (list[str | int]): Lista que contiene números como enteros y cadenas.

    Returns:
        int: La suma de todos los elementos convertidos a enteros.
    """
    return sum(int(num) for num in arr)

print(sum_mix([9, 3, "7", "3"]))  # Esperado: 22 (9 + 3 + 7 + 3)
print(sum_mix(["5", "0", 9, 3, 2, 1, "9", 6, 7]))  # Esperado: 42
print(sum_mix(["3", 6, 6, 0, "5", 8, 5, "6", 2,"0"]))  # Esperado: 41
print(sum_mix(["1", "2", "3", "4", "5"]))  # Esperado: 15
print(sum_mix([]))  # Esperado: 0 (caso borde con lista vacía)
