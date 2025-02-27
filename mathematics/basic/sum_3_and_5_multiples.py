"""
Return the sum of all multiples of 3 or 5 below a given number. If the number is negative, return 0. 
If a number is a multiple of both 3 and 5, count it only once.

URL: https://www.codewars.com/kata/514b92a657cdc65150000006
"""





def sum_3_and_5_multiples(num: int) -> int:
    """
    En esta función, sumamos todos los múltiplos de 3 o 5 menores que un número dado. 
    Si el número es negativo, devolvemos 0. Si un número es múltiplo tanto de 3 como de 5, se cuenta solo una vez.
    
    Args:
        num (int): El número límite hasta el cual se buscan los múltiplos.
        
    Returns:
        int: La suma de todos los múltiplos de 3 o 5 menores que el número dado.
    """
    if num < 0:
        return 0
    return sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0)

# Ejemplo de prueba 1
test1 = sum_3_and_5_multiples(10)  
print(f"La suma de los múltiplos de 3 o 5 es: {test1}.")  # Esperado: 23

# Ejemplo de prueba 2
test2 = sum_3_and_5_multiples(20)  
print(f"La suma de los múltiplos de 3 o 5 es: {test2}.")  # Esperado: 78
