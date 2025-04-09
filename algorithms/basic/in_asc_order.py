"""
Write a function that checks if the numbers in an array are in ascending order. 
An array is in ascending order if there are no two adjacent numbers where the left number is 
greater than the right number. If the array has 0 or 1 element, it is automatically considered to be in ascending order.

URL: https://www.codewars.com/kata/56b7f2f3f18876033f000307
"""





def in_asc_order(arr:list[int]) -> bool:
    """
    Verifica si los elementos de la lista están en orden ascendente.

    Args:
        arr (list[int]): Lista de números enteros.

    Returns:
        bool: True si la lista está en orden ascendente o tiene 0/1 elemento, False en caso contrario.
    """
    return sorted(arr) == arr


def in_asc_order_alt(arr: list[int]) -> bool:
    """
    Versión alternativa: utiliza comparación directa entre lista original y lista ordenada.

    Args:
        arr (list[int]): Lista de números enteros.

    Returns:
        bool: True si la lista está en orden ascendente, False en caso contrario.
    """
    return arr == sorted(arr)


print(in_asc_order([1, 2, 3, 4]))    # True
print(in_asc_order([1, 3, 2]))       # False
print(in_asc_order([5]))            # True
print(in_asc_order([]))             # True
