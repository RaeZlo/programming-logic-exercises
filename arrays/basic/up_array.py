"""
Given an array of integers, the task is to return an array that represents the number formed 
by the integers in the list with 1 added to that number.

If the array is invalid (empty, contains negative integers, or contains integers with more than one digit), 
return None.

URL: https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
"""






def up_array(a: list[int]) -> list[int] | None:
    """
    Recibe una lista de dígitos y suma 1 al número que representan.

    Args:
        a (list[int]): Lista de dígitos.

    Returns:
        list[int] | None: Lista con el número aumentado en 1 o None si es inválida.
    """
    # Verificar si el array es inválido
    if not a or any(not 0 <= x < 10 for x in a):
        return None

    # Sumar 1 al número representado por la lista
    for i in range(1, len(a) + 1):
        a[-i] = (a[-i] + 1) % 10  # Incrementa el dígito y maneja el acarreo
        if a[-i]:  # Si no hay acarreo, terminamos
            break
    else:
        a.insert(0, 1)  # Si hubo un acarreo total (999 → 1000), agregamos 1 al inicio

    return a



print(up_array([2, 3, 9]))      # [2, 4, 0]
print(up_array([4, 3, 2, 5]))   # [4, 3, 2, 6]
print(up_array([9, 9, 9]))      # [1, 0, 0, 0]
print(up_array([0]))            # [1]
print(up_array([]))             # None (lista vacía)
print(up_array([-1, 2, 3]))     # None (contiene número negativo)
print(up_array([1, 20, 3]))     # None (contiene número con más de un dígito)
