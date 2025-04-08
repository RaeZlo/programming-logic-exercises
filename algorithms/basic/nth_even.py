"""
Given a positive integer N, you need to return the N-th even number. Even numbers are those that are divisible by 2, 
starting from 0 (i.e., 0, 2, 4, 6, 8, etc.).

URL: https://www.codewars.com/kata/5933a1f8552bc2750a0000ed
"""





def nth_even(n: int) -> int:
    """
    Retorna el enésimo número par, empezando desde 0.

    Args:
        n (int): Posición del número par a retornar (1-indexado).

    Returns:
        int: El n-ésimo número par.
    """
    return 2 * (n - 1)


print(nth_even(1))  # 0
print(nth_even(2))  # 2
print(nth_even(3))  # 4
print(nth_even(100))  # 198
