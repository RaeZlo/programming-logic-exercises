"""
Write a function which takes a number as input and returns the sum of the absolute value of 
each of the number's decimal digits.
Let's assume that all numbers in the input will be integer values.


URL: https://www.codewars.com/kata/52f3149496de55aded000410
"""





def sum_digits(number):
    """
    Esta función recibe un número entero y retorna la suma de los valores absolutos de cada uno de sus dígitos.
    
    Args:
        number (int): El número del cual se calculará la suma de los dígitos.
        
    Returns:
        int: La suma de los dígitos del número, tomando en cuenta su valor absoluto.
    """
    return sum(int(digit) for digit in str(abs(number)))  

test1 = sum_digits(-22)
print(f"La suma de los dígitos es: {test1}")  # Esperado: 4 (2 + 2)

test2 = sum_digits(12345)
print(f"La suma de los dígitos es: {test2}")  # Esperado: 15 (1 + 2 + 3 + 4 + 5)
