"""
Define a function that takes an integer argument and returns a logical value true or false depending
on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive 
divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).

URL: https://www.codewars.com/kata/5262119038c0985a5b00029f
"""






def is_prime(num):
    """
    En esta función, verificamos si un número es primo o no. Un número primo es mayor que 1 
    y no tiene divisores positivos diferentes de 1 y sí mismo.
    
    Args:
        num (int): El número a verificar.
        
    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    # Si el número es menor de 2 no es primo
    if num < 2:
        return False
    # Verificamos si tiene divisores distintos de 1 y él mismo
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    # En caso de no encontrar divisores el número es primo
    return True

test1 = is_prime(73)
print(f"El resultado es: {test1}") # Esperado: True

test2 = is_prime(6)
print(f"El resultado es: {test2}") # Esperado: False

test3 = is_prime(-5)
print(f"El resultado es: {test3}")  # Esperado: False (números negativos no son primos)
