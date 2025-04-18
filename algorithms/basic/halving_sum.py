"""
Given a positive integer n, calculate the following sum:

n + n/2 + n/4 + n/8 + ...
All elements of the sum are the results of integer division.

URL: https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d
"""





def halving_sum(n: int) -> int:
    """
    Calcula la suma n + n//2 + n//4 + ... hasta que n sea 0.

    Args:
        n (int): Entero positivo inicial.

    Returns:
        int: Resultado de la suma de divisiones sucesivas.
    """
    result = 0
    while n > 0:
        result += n
        n //= 2
    return result


print(halving_sum(25))  # 25 + 12 + 6 + 3 + 1 = 47
print(halving_sum(1))   # 1
print(halving_sum(2))   # 2 + 1 = 3
