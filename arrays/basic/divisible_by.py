"""
Complete the function which takes two arguments and returns all numbers which are divisible 
by the given divisor. First argument is an array of numbers and the second is the divisor.

URL: https://www.codewars.com/kata/55edaba99da3a9c84000003b
"""





def divisible_by(numbers: list[int], divisor: int) -> list[int]:
    """
    Filtra los números divisibles por un divisor dado.

    Args:
        numbers (list[int]): Lista de números enteros.
        divisor (int): Número entero por el cual deben ser divisibles.

    Returns:
        list[int]: Lista con los números que son divisibles por el divisor.
    """
    return [num for num in numbers if num % divisor == 0]

print(divisible_by([1, 2, 3, 4, 5, 6], 2))  # Esperado: [2, 4, 6]
print(divisible_by([10, 20, 33, 40, 50], 10))  # Esperado: [10, 20, 40, 50]
print(divisible_by([7, 14, 21, 28], 7))  # Esperado: [7, 14, 21, 28]
print(divisible_by([3, 5, 9, 11], 4))  # Esperado: [] (ninguno es divisible)
print(divisible_by([], 3))  # Esperado: [] (caso borde con lista vacía)
