"""
Given a 2D list of positive numbers, find the sum of the smallest numbers in each row.

URL: https://www.codewars.com/kata/5d5ee4c35162d9001af7d699
"""





def sum_of_minimums(numbers: list[list[int]]) -> int:
    """
    Calcula la suma de los valores mínimos de cada fila en una matriz 2D.

    Args:
        numbers (list[list[int]]): Lista de listas con números positivos.

    Returns:
        int: Suma de los valores mínimos de cada fila.
    """
    return sum(min(row) for row in numbers)


print(sum_of_minimums([
    [7, 9, 8, 6], 
    [5, 3, 2, 4], 
    [11, 15, 10, 12]
]))  # Esperado: 6 + 2 + 10 = 18

print(sum_of_minimums([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]))  # Esperado: 1 + 4 + 7 = 12

print(sum_of_minimums([
    [10, 20, 30], 
    [5, 15, 25], 
    [2, 12, 22]
]))  # Esperado: 10 + 5 + 2 = 17
