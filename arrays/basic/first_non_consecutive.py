"""
You need to find the first element in an array that is not consecutive.

An element is "not consecutive" if it is not exactly 1 greater than the previous element. 
For example, in the array [1, 2, 3, 4, 6, 7, 8], the number 6 is the first non-consecutive number
because it comes after 4, skipping 5.

If all elements are consecutive, return null.

The array will always have at least two elements, all numbers will be unique, and the array will be 
sorted in ascending order. The first non-consecutive number could be positive or negative.

URL: https://www.codewars.com/kata/58f8a3a27a5c28d92e000144
"""





def first_non_consecutive(arr: list[int]) -> int | None:
    """
    Encuentra el primer número no consecutivo en una lista ordenada.

    Args:
        arr (list[int]): Lista de números enteros ordenados en orden ascendente.

    Returns:
        int | None: El primer número que rompe la secuencia consecutiva, o None si todos son consecutivos.
    """
    for key, num in enumerate(arr, start=arr[0]):  # Iteramos con enumerate empezando desde el primer número
        if key != num:  # Si el índice esperado no coincide con el número real, hay una interrupción en la secuencia
            return num
    return None  # Si no hay números no consecutivos, retornamos None

print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))  # Esperado: 6
print(first_non_consecutive([4, 5, 6, 8, 9]))        # Esperado: 8
print(first_non_consecutive([-3, -2, -1, 1, 2]))     # Esperado: 1
print(first_non_consecutive([10, 11, 12, 13]))       # Esperado: None (todos consecutivos)
print(first_non_consecutive([100, 102]))            # Esperado: 102
