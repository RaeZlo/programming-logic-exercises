"""
Write a function that takes in a positive parameter num and returns its multiplicative 
persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)

URL: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
"""





def persistence(num: int) -> int:
    """
    En esta función, calculamos la persistencia multiplicativa de un número, que es el número de veces que 
    debemos multiplicar sus dígitos hasta que se obtiene un solo dígito.
    
    Args:
        num (int): El número para calcular su persistencia multiplicativa.
        
    Returns:
        int: La cantidad de multiplicaciones necesarias para llegar a un solo dígito.
    """
    if num < 10:
        return 0  # Si el número es un solo dígito, la persistencia es 0
    
    product = 1
    for digit in str(num):
        product *= int(digit)  # Multiplicamos todos los dígitos

    return 1 + persistence(product)  # Sumamos 1 por la multiplicación actual y seguimos recursivamente

# Ejemplo de prueba 1
test1 = persistence(39)
print(f"La persistencia multiplicativa de 39 es: {test1}.")  # Esperado: 3

# Ejemplo de prueba 2
test2 = persistence(999)
print(f"La persistencia multiplicativa de 999 es: {test2}.")  # Esperado: 4
