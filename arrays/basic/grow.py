"""
Given a non-empty array of integers, return the result of multiplying the values together in order. 

URL: https://www.codewars.com/kata/57f780909f7e8e3183000078
"""





def grow(numbers:list[int]) -> int:
    """
    Esta función recibe una lista de enteros no vacía y retorna el resultado de multiplicar todos 
    los valores de la lista en orden.
    
    Args:
        numbers (list[int]): Una lista de enteros no vacía.
        
    Returns:
        int: El resultado de multiplicar todos los elementos de la lista.
    """
    result = 1
    for num in numbers:
        result *= num
    return result

print(grow([1, 2, 3, 4]))    # Esperado: 24 (1 * 2 * 3 * 4 = 24)
print(grow([5, 2, 2]))       # Esperado: 20 (5 * 2 * 2 = 20)
print(grow([10, 0, 3]))      # Esperado: 0 (10 * 0 * 3 = 0)
print(grow([1]))             # Esperado: 1 (solo un número, el resultado es 1)
