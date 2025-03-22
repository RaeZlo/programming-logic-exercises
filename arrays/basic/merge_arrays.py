"""
Merge two sorted arrays into one array that is:
- Sorted in ascending order.
- Contains no duplicate values (each number appears only once).
- If both arrays are empty, return an empty array.

URL: https://www.codewars.com/kata/5899642f6e1b25935d000161
"""





def merge_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Fusiona dos listas ordenadas en una única lista sin duplicados y ordenada de menor a mayor.

    Args:
        arr1 (list[int]): Primera lista de números enteros ordenada.
        arr2 (list[int]): Segunda lista de números enteros ordenada.

    Returns:
        list[int]: Lista fusionada, ordenada y sin duplicados.
    """
    return sorted(set(arr1 + arr2))  # Combina las listas, elimina duplicados y ordena

print(merge_arrays([1, 3, 5], [2, 4, 6]))  # Esperado: [1, 2, 3, 4, 5, 6]
print(merge_arrays([1, 2, 2, 3], [2, 3, 4, 5]))  # Esperado: [1, 2, 3, 4, 5]
print(merge_arrays([], [2, 2, 3]))  # Esperado: [2, 3]
print(merge_arrays([], []))  # Esperado: []
