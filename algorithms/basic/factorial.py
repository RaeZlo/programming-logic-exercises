"""
Write a function that calculates the factorial of a non-negative integer. The factorial of a number n, denoted as 
n!, is the product of all positive integers less than or equal to n. For example, 5!=5×4×3×2×1=120. By convention, 0! is 1. 
If the input number is less than 0 or greater than 12, throw an exception or return a special error value.

URL: https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
"""





def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo, validando que esté en el rango [0, 12].

    Args:
        n (int): Número entero cuyo factorial se desea calcular.

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es menor que 0 o mayor que 12.
    """
    if n < 0 or n > 12:
        raise ValueError("Input must be between 0 and 12 inclusive.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def factorial_alt(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo utilizando recursión.

    Args:
        n (int): Número entero cuyo factorial se desea calcular.

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es menor que 0 o mayor que 12.
    """
    if n < 0 or n > 12:
        raise ValueError("Input must be between 0 and 12 inclusive.")
    return 1 if n <= 1 else n * factorial_alt(n - 1)


print(factorial(5))        # 120
print(factorial_alt(0))    # 1
print(factorial(12))       # 479001600
# print(factorial(13))     # ValueError
