"""
The task is to create a function that calculates the sum of all integers between two given numbers, including both numbers. 
If the two numbers are equal, return either of them.

Rules:
If the two numbers are equal, return either of them.
If the numbers are not equal, sum all the integers between them and return the result.

URL: https://www.codewars.com/kata/55f2b110f61eb01779000053
"""





def get_sum(a: int, b: int) -> int:
    """
    Calcula la suma de todos los enteros entre 'a' y 'b' (inclusive).

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: Suma de los enteros entre 'a' y 'b' (incluidos).
    """
    return sum(range(min(a, b), max(a, b) + 1))


print(get_sum(1, 0))   # 1
print(get_sum(1, 2))   # 3
print(get_sum(0, 1))   # 1
print(get_sum(1, 1))   # 1
print(get_sum(-1, 0))  # -1
print(get_sum(-1, 2))  # 2
