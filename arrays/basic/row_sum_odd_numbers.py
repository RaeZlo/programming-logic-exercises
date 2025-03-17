"""
You are given a triangle of consecutive odd numbers arranged as follows:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29

Each row contains consecutive odd numbers. Your task is to calculate the sum of the numbers in the 
nth row of this triangle (starting at row index 1).
For example:
Input: 1 → Output: 1
Input: 2 → Output: 3 + 5 = 8
Input: 3 → Output: 7 + 9 + 11 = 27

URL: https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
"""





def row_sum_odd_numbers(n:int) -> int:
    """
    Calcula la suma de los números en la fila `n` del triángulo de impares.

    Args:
        n (int): Índice de la fila en el triángulo (comenzando en 1).

    Returns:
        int: La suma de los números en la fila `n`.
    """
    return n ** 3

def row_sum_odd_numbers_alt(n: int) -> int:
    start = n * (n - 1) + 1  # Primer número impar de la fila `n`
    return sum(start + 2 * i for i in range(n))  # Sumar `n` impares consecutivos

print(row_sum_odd_numbers(1))  # Esperado: 1
print(row_sum_odd_numbers(2))  # Esperado: 8 (3 + 5)
print(row_sum_odd_numbers(3))  # Esperado: 27 (7 + 9 + 11)
print(row_sum_odd_numbers(4))  # Esperado: 64 (13 + 15 + 17 + 19)
print(row_sum_odd_numbers_alt(5))  # Esperado: 125 (21 + 23 + 25 + 27 + 29)
print(row_sum_odd_numbers_alt(10))  # Esperado: 1000
