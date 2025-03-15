"""
Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
If there are multiple elements with the same value, remove the one with the lowest index. 
If you get an empty array/list, return an empty array/list.
Don't change the order of the elements that are left.

URL: https://www.codewars.com/kata/563cf89eb4747c5fb100001b
"""





def remove_smallest(numbers: list[int]) -> list[int]:
    """
    Esta función recibe una lista de números enteros y retorna una nueva lista sin el menor valor.
    No modifica la lista original y mantiene el orden de los elementos restantes.

    Args:
        numbers (list[int]): Lista de números enteros.

    Returns:
        list[int]: Una nueva lista sin el menor número original.
    """
    if not numbers:
        return []  # Si la lista está vacía, devolvemos una lista vacía.

    min_index = numbers.index(min(numbers))  # Encontramos el índice del menor valor.
    return numbers[:min_index] + numbers[min_index + 1:]  # Retornamos una copia sin ese elemento.

def remove_smallest_alt(numbers: list[int]) -> list[int]:
    if not numbers:
        return []
    return numbers.remove(min(numbers))

print(remove_smallest([1, 2, 3, 4, 5]))   # Esperado: [2, 3, 4, 5]
print(remove_smallest_alt([5, 3, 2, 1, 4]))   # Esperado: [5, 3, 2, 4] (elimina el primer 1)
print(remove_smallest_alt([2, 2, 1, 2, 1]))   # Esperado: [2, 2, 2, 1] (elimina el primer 1)
print(remove_smallest([10]))              # Esperado: [] (caso borde, lista con un solo elemento)
print(remove_smallest([]))                # Esperado: [] (caso borde, lista vacía)
