"""
Write a program that finds the summation of every number from 1 to num. The number will always be a positive 
integer greater than 0. Your function only needs to return the result, what is shown between parentheses in 
the example below is how you reach that result and it's not part of it, see the sample tests.

URL: https://www.codewars.com/kata/55d24f55d7dd296eb9000030
"""





def summation(num: int) -> int:
    """
    Esta función recibe un número entero positivo como argumento y retorna 
    la suma de todos los números enteros desde 1 hasta el número dado (inclusive).
    
    Args:
        num (int): El número hasta el cual se calculará la suma.
        
    Returns:
        int: La suma de todos los números desde 1 hasta num.
    """
    return sum(range(1, num + 1))

test1 = summation(8)
print(f"La suma de los números desde 1 hasta 8 es {test1}.")  # Esperado: 36

test2 = summation(2)
print(f"La suma de los números desde 1 hasta 2 es {test2}.")  # Esperado: 3
