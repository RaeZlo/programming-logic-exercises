"""
You are given an array of integers. Your task is to find an index N where the sum of the numbers to 
the left of N is equal to the sum of the numbers to the right of N. If no such index exists, return -1.
If there are multiple possible answers, return the smallest index.

Example 1: Input: [1, 2, 3, 4, 3, 2, 1]
Output: 3
Explanation: The sum of numbers to the left of index 3 is [1, 2, 3] = 6, and the sum to the right is [3, 2, 1] = 6.

URL: https://www.codewars.com/kata/5679aa472b8f57fb8c000047
"""





def find_even_index(numbers:list[int]) -> int:
    """
    Encuentra el índice donde la suma de los elementos a la izquierda es igual a la suma de los elementos a la derecha.

    Args:
        numbers (list[int]): Lista de números enteros.

    Returns:
        int: Índice encontrado o -1 si no existe.
    """
    for i in range(len(numbers)):  # Recorremos todos los índices posibles
        left_sum = sum(numbers[:i])    # Sumamos los elementos a la izquierda del índice i
        right_sum = sum(numbers[i+1:]) # Sumamos los elementos a la derecha del índice i
        
        if left_sum == right_sum:  # Si las sumas son iguales, hemos encontrado el índice
            return i
    
    return -1  # Si no encontramos ningún índice válido, devolvemos -1



print(find_even_index([1, 2, 3, 4, 3, 2, 1]))  # 3
print(find_even_index([1, 100, 50, -51, 1, 1]))  # 1
print(find_even_index([20, 10, -80, 10, 10, 15, 35]))  # 0
print(find_even_index([1, 2, 3, 4, 5]))  # -1
print(find_even_index([10, -10, 10, -10, 10, -10, 10]))  # 3
