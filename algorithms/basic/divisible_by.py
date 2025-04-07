"""
Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. 
First argument is an array of numbers and the second is the divisor.

URL: https://www.codewars.com/kata/55edaba99da3a9c84000003b
"""





def divisible_by(numbers: list[int], divisor: int) -> list[int]:
    """
    Retorna una lista con los números divisibles por `divisor`.

    Args:
        numbers (list[int]): Lista de enteros.
        divisor (int): Número por el cual verificar divisibilidad.

    Returns:
        list[int]: Lista de números divisibles por `divisor`.
    """
    return [num for num in numbers if num % divisor == 0]


print(divisible_by([1, 2, 3, 4, 5, 6], 2))  # [2, 4, 6]
print(divisible_by([10, 15, 20, 25], 5))    # [10, 15, 20, 25]
print(divisible_by([3, 5, 8, 10], 3))       # [3]
