"""
Given a list of numbers, find the mean (average). To do this:
Add all the numbers together.
Divide the sum by the total number of values in the list.
Example: For the list [1, 3, 5, 7], the sum is 16, and there are 4 numbers, so the mean is 16 / 4 = 4.

URL: https://www.codewars.com/kata/55d277882e139d0b6000005d
"""





def find_average(nums: list[int]) -> int:
    """
    Calcula el promedio entero de una lista de números.

    Args:
        nums (list[int]): Lista de números enteros.

    Returns:
        int: Promedio de los números en la lista (división entera).
             Retorna 0 si la lista está vacía.
    """
    return sum(nums) // len(nums) if nums else 0


print(find_average([1, 3, 5, 7]))  # Esperado: 4
print(find_average([10, 20, 30]))   # Esperado: 20
print(find_average([5]))            # Esperado: 5
print(find_average([]))             # Esperado: 0
