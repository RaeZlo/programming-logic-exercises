"""
Write a function that takes an array of three distinct numbers and returns the index of 
the number that lies between the other two.

For example:
gimme([2, 3, 1]) should return 0 because 2 is between 1 and 3, and its index is 0.
gimme([5, 10, 14]) should return 1 because 10 is between 5 and 14, and its index is 1.

URL: https://www.codewars.com/kata/545a4c5a61aa4c6916000755
"""






def gimme(numbers: list[int]) -> int:
    """
    Devuelve el índice del número intermedio en una lista de tres números distintos.

    Args:
        numbers (list[int]): Lista de tres números distintos.

    Returns:
        int: Índice del número que está entre los otros dos.
    """
    return numbers.index(sorted(numbers)[1])  # Encuentra el índice del número medio en la lista original

print(gimme([2, 3, 1]))  # Esperado: 0
print(gimme([5, 10, 14]))  # Esperado: 1
print(gimme([-5, -10, -14]))  # Esperado: 0
print(gimme([100, 200, 150]))  # Esperado: 2
