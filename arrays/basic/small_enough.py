"""
You will be given an array and a limit value. You must check that all values in the array 
are below or equal to the limit value. If they are, return true. Else, return false.
You can assume all values in the array are numbers.

URL: https://www.codewars.com/kata/57cc981a58da9e302a000214
"""





def small_enough(array: list[int], limit: int) -> bool:
    """
    Verifica si todos los elementos de la lista son menores o iguales al límite proporcionado.

    Args:
        array (list[int]): Lista de números a verificar.
        limit (int): Valor límite que no debe ser excedido por los elementos de la lista.

    Returns:
        bool: Devuelve True si todos los elementos son menores o iguales al límite, False en caso contrario.
    """
    return max(array) <= limit  # Si el valor máximo de la lista es menor o igual al límite, entonces todos los valores lo son

print(small_enough([66, 101], 200))  # Esperado: True
print(small_enough([78, 117, 115, 104, 45, 85, 112, 115], 120))  # Esperado: True
print(small_enough([101, 45, 75, 105, 104, 45, 85, 112, 115], 100))  # Esperado: False
