"""
Given an array of integers, return a new array with each value doubled.

URL: https://www.codewars.com/kata/57f781872e3d8ca2a000007e
"""





def maps(nums: list[int]) -> list[int]:
    """
    En esta función, tomamos un arreglo de enteros y devolvemos un nuevo arreglo con cada valor duplicado.
    
    Args:
        nums (list[int]): Una lista de enteros.
        
    Returns:
        list[int]: Una lista de enteros con cada valor duplicado.
    """
    # Multiplicar cada número por 2 y devolver la nueva lista
    return [num * 2 for num in nums]

# Pruebas de la función
test1 = maps([1, 2, 3])
print(test1)  # Esperado: [2, 4, 6]

test2 = maps([0, -1, -2])
print(test2)  # Esperado: [0, -2, -4]
