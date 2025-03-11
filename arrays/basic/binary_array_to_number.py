"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

URL: https://www.codewars.com/kata/578553c3a1b8d5c40300037c
"""





def binary_array_to_number(nums: list[int]) -> int:
    """
    En esta función, tomamos un arreglo de unos y ceros, y convertimos su valor binario equivalente en un número entero.
    
    Args:
        nums (list[int]): Una lista de enteros que representa un número binario.
        
    Returns:
        int: El número entero equivalente al valor binario dado.
    """
    # Unir los elementos del arreglo en una cadena y luego convertir esa cadena a un número entero en base 2
    return int("".join(str(num) for num in nums), 2)

test1 = binary_array_to_number([0, 0, 0, 1])
print(test1)  # Esperado: 1

test2 = binary_array_to_number([1, 0, 1, 1])
print(test2)  # Esperado: 11
