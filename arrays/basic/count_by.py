"""
Create a function with two arguments that will return an array of the first n multiples of x.
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array or list (depending on language).

URL: https://www.codewars.com/kata/5513795bd3fafb56c200049e
"""





def count_by(x: int, n: int) -> list[int]:
    """
    Esta función recibe dos argumentos: un número x y un valor n.
    Retorna una lista con los primeros n múltiplos de x.
    
    Args:
        x (int): El número cuyo múltiplo se debe generar.
        n (int): La cantidad de múltiplos a devolver.
        
    Returns:
        list[int]: Una lista con los primeros n múltiplos de x.
    """
    return [num * x for num in range(1, n + 1)]

print(count_by(2, 5))   # Esperado: [2, 4, 6, 8, 10] (primeros 5 múltiplos de 2)
print(count_by(3, 4))   # Esperado: [3, 6, 9, 12] (primeros 4 múltiplos de 3)
print(count_by(5, 3))   # Esperado: [5, 10, 15] (primeros 3 múltiplos de 5)
print(count_by(7, 6))   # Esperado: [7, 14, 21, 28, 35, 42] (primeros 6 múltiplos de 7)
