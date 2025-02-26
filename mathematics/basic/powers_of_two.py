"""
Complete the function that takes a non-negative integer n as input, and returns a list 
of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

URL: https://www.codewars.com/kata/57a083a57cb1f31db7000028
"""





def powers_of_two(num: int) -> list:
    """
    En esta función, generamos una lista con las potencias de 2 cuyo exponente 
    va desde 0 hasta `num` (inclusive). Cada elemento de la lista es de la forma 
    2^i, donde `i` es el exponente.
    
    Args:
        num (int): El exponente máximo para el cual generar las potencias de 2.
        
    Returns:
        list: Una lista con las potencias de 2 desde 2^0 hasta 2^num.
    """
    return [2 ** i for i in range(0, num + 1)]

# Pruebas de la función
test1 = powers_of_two(3)
print(f"Las potencias de 2 son: {test1}")  # Esperado: [1, 2, 4, 8]

test2 = powers_of_two(5)
print(f"Las potencias de 2 son: {test2}")  # Esperado: [1, 2, 4, 8, 16, 32]
