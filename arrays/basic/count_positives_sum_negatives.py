"""
Given an array of integers.
Return an array, where the first element is the count of positives numbers and the second 
element is sum of negative numbers. 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array.

URL: https://www.codewars.com/kata/576bb71bbbcf0951d5000044
"""





def count_positives_sum_negatives(numbers: list[int]) -> list[int]:
    """
    Esta función recibe una lista de enteros y retorna una lista donde:
    - El primer elemento es la cantidad de números positivos.
    - El segundo elemento es la suma de los números negativos.
    Si la lista está vacía o es nula, retorna una lista vacía.
    
    Args:
        numbers (list[int]): Una lista con enteros.
        
    Returns:
        list[int]: Una lista con dos elementos: la cantidad de números positivos y la suma de los negativos.
    """
    count_positives = sum(1 for num in numbers if num > 0)
    sum_negatives = sum(num for num in numbers if num < 0)

    return [count_positives, sum_negatives] if numbers else []

# Ejemplos de pruebas
print(count_positives_sum_negatives([1, 2, 3, -4, -5]))  # Esperado: [3, -9] (3 positivos, suma de negativos = -9)
print(count_positives_sum_negatives([0, 0, 0]))            # Esperado: [0, 0] (ningún número positivo, ningún negativo)
print(count_positives_sum_negatives([5, -3, -7, 2]))       # Esperado: [2, -10] (2 positivos, suma de negativos = -10)
print(count_positives_sum_negatives([]))                   # Esperado: [] (lista vacía)
