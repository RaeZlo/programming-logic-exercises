"""
Create a function that takes an integer n > 1 and returns an array with all of the integer's divisors 
(except for 1 and the number itself), from smallest to largest. If the number is prime, return the 
string (integer) is prime.

URL: https://www.codewars.com/kata/544aed4c4a30184e960010f4
"""





def divisors(num: int) -> list:
    """
    En esta función, encontramos todos los divisores de un número entero `num` (excepto 1 y el número en sí).
    Si el número es primo, devolvemos una cadena indicando que el número es primo.
    
    Args:
        num (int): El número del que se desean encontrar los divisores.
        
    Returns:
        list: Una lista con los divisores del número, de menor a mayor.
        str: Si el número es primo, devuelve una cadena indicando que el número es primo.
    """
    result = [divisor for divisor in range(2, num) if num % divisor == 0]
    return result if result else f"{num} es primo."

test1 = divisors(12)
print(f"Los divisores son: {test1}")  # Esperado: [2, 3, 4, 6]

test2 = divisors(13)
print(f"Los divisores son: {test2}")  # Esperado: "13 es primo."
