"""
Triangular numbers are numbers that can be represented as dots forming an equilateral triangle.

For example:
The first triangular number is 1.
The second triangular number is 3.
The third triangular number is 6.

Your task is to return the n-th triangular number. If the number is out of range (e.g., 0 or a negative number), return 0.

URL: https://www.codewars.com/kata/525e5a1cb735154b320002c8
"""





def triangular(n: int) -> int:
    """
    Calcula el número triangular n-ésimo.

    Args:
        n (int): Número entero positivo.

    Returns:
        int: El n-ésimo número triangular, o 0 si n <= 0.
    """
    return n * (n + 1) // 2 if n > 0 else 0


print(triangular(1))   # Esperado: 1
print(triangular(2))   # Esperado: 3
print(triangular(3))   # Esperado: 6
print(triangular(0))   # Esperado: 0
print(triangular(-5))  # Esperado: 0
